import json
import pandas as pd
import numpy as np
import pymongo

def mongoimport(csv_path):
    hr_df=pd.read_csv(csv_path)
    payload=json.loads(hr_df.to_json(orient="records"))
    collection.delete_many({})

    collection.insert_many(payload)

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db=client['HRdatabase1']
    collection=db['EmpCollection']
    mongoimport("C:/Users/anu/Documents/python programs/Data/HR-Employee-Attrition.csv")
    

    
    #1.find frequency of employee working in different departments
    print("\n\n1.find frequency of employee working in different departments ?\n")
    countdepartment=collection.aggregate([{ '$group' :{'_id' : '$Department', 'countDept':{'$count' : {}}}},
    {'$sort':{'countDept':-1}}])

    for item in countdepartment:
        print(item)


    #2.	Top hired employee is working in which department
    print("\n\n2.Top hired employee is working in which department ?\n")
    countedu=collection.aggregate([{ '$group' :{'_id' : '$EducationField', 'countedu':{'$count' : {}}}},
                                        {'$sort':{'countedu':-1}},{'$limit':1}])
    for item in countedu:
        print(item)

    #3.	Find the max and min salaried employee
    print("\n\n3.Find the max and min salaried employee?\n")
    max_min_income=collection.aggregate([{ '$group' :{'_id' : '$null', 'maxSalary':{'$max' : '$MonthlyIncome'},'minSalary':{'$min' : '$MonthlyIncome'}}}
                                        ,{ '$project' : { '_id' : 0 ,}}])
    for item in max_min_income:
        print(item)

    # maxincome=collection.find({},{'$EmployeeID':{'$eq':{'$max':'$Income'}}})
    # for item in maxincome:
    #     print(item)
    
    #4.	Find the AVG Monthly Income of overall employee
    print("\n\n4.Find the AVG Monthly Income of overall employee?\n")
    avg_income=collection.aggregate([{ '$group' :{'_id' : '$null', 'Avg_Salary':{'$avg' : '$MonthlyIncome'}}}
                                        ,{ '$project' : { '_id' : 0 ,}}])
    for item in avg_income:
        print(np.round(item['Avg_Salary'],2))
        
    #5. Find the AVG PercentSalaryHike of graduate employee .
    print("\n\n5. Find the AVG PercentSalaryHike of employee?.\n")
    avg_PercentSalaryHike=collection.aggregate([{ '$group' :{'_id' : 'null', 'Avg_PercentSalaryHike':{'$avg' : '$PercentSalaryHike'}}},{ '$project' : { '_id' : 0 ,}}])
    for item in avg_PercentSalaryHike:
        print(np.round(item['Avg_PercentSalaryHike'],2))
    
     
    #6. Find the AVG PercentSalaryHike of employee who have left the company (Attrition = 'Yes').
    print("\n\n6. Find the AVG PercentSalaryHike of employee who have left the company (Attrition = 'Yes').\n")
    Empl_PercentSalaryHike=collection.aggregate([{'$match':{'Attrition':'Yes'}},
                                                { '$group' :{'_id' : '$null', 'Avg_PercentSalaryHike':{'$avg' : '$PercentSalaryHike'}}},
                                                { '$project' : { '_id' : 0 ,}}])
    for item in Empl_PercentSalaryHike:
        print(np.round(item['Avg_PercentSalaryHike'],2))
    
    #7. Highest attrition is in which department.
    print("\n\n7. Highest attrition is in which department.\n")
    countdepartment=collection.aggregate([{'$match':{'Attrition':'Yes'}},
                                          { '$group' :{'_id' : '$Department', 'countDept':{'$count' : {}}}},
                                          {'$sort':{'countDept':-1}},
                                          {'$limit':1}])

    for item in countdepartment:
        print(item['_id']," :",item['countDept'])
    
    
    #8.Find the employee gualification recieving salary<=avg.salary of all employee.
    print("\n\n8.Find the employee gualification recieving salary<=avg.salary of all employee.\n")
    income_less_than_avg=collection.aggregate([{ '$match': {'EducationField':{'$lte':'avg_Salary'}}},
                                               { '$group' :{'_id' : '$EducationField', 'avg_Salary':{'$avg' : '$MonthlyIncome'}}}
                                               ])
    for item in income_less_than_avg:
        print(item['_id']," : ",item['avg_Salary'])

    income_less_than_avg=collection.aggregate([{ '$match': {'EducationField':{'$lte':'avg_Salary'}}},
                                               { '$group' :{'_id' : '$null', 'avg_Salary':{'$avg' : '$MonthlyIncome'}}}
                                               ])
    for item in income_less_than_avg:
        print(item['_id']," : ",item['avg_Salary'])

    count=collection.count_documents({})
    print(count)
    median=collection.find({}).sort('MonthlyIncome',1).skip(count//2-1).limit(1)

    for item in median:
        print(item)