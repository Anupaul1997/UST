import json
from functools import reduce
from flask import (Flask, jsonify, redirect, render_template, request, session,
                   url_for)
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "abc"  

client = MongoClient('localhost', 27017)
db=client['FoodAppDB']
collection_user=db['userdetailsdb']
collection_table=db['tabledetailsdb']
collection_menu=db['itemsdetails']
collection_logs=db['FullLogs']
    
# end points using app.routes
@app.route('/')
def show():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html",table_details=get_table_details())

@app.route('/admindashboard')
def admin_dashboard():
    return render_template("admindashboard.html",table_details=get_table_details())

@app.route('/menu')
def menu_items():
    return render_template("menuitems.html",menulist=get_menu_details())

@app.route('/viewrating')
def view_rating():
    
    all_doc=collection_logs.find({'full_logs.rating':{"$exists":True}},{"_id":0,"full_logs.rating":1})
    rating_list={1:0,2:0,3:0,4:0,5:0}
    for item in all_doc:
        rating_list[int(item['full_logs']["rating"])]+=1
    return render_template("viewrating.html",ratings=rating_list)

@app.route('/addmenu',methods=["GET","POST"])
def add_items():
    if request.method=="POST":
        item=request.form['item']
        rate=request.form['rate']
        record=collection_menu.find_one({'item':item},{"_id":1})
        if record:
            collection_menu.update_one({'_id':record['_id']},{'$set':{"price":rate}})
        else:
            collection_menu.insert_one({"item":item,"price":rate})
        return redirect("/menu")
    else:
        return render_template("addmenu.html")

@app.route('/register',methods=["GET","POST"])
def create_user():
    if request.method=="POST":
        _id=request.form['phone']
        name=request.form['name']
        password=request.form['password']
        new_user={"_id":_id,"name":name,"password":password}
        try :
            collection_user.insert_one(new_user)
        except:
            message="Phone Number is already registered!!!!use another ....."
            return render_template("register.html",message=message)
        return render_template("index.html")
    else:
        return render_template("register.html")


@app.route('/login',methods=["GET","POST"])
def get_user():   
    if request.method=="POST":
        phone=request.form['phone']
        password=request.form['password']
        if phone=="admin" and password=="admin@123":
            return redirect("/admindashboard")
        
        input_dict={"_id":phone,"password":password}
        records_fetched = collection_user.find({'_id':phone},{"_id":1,"name":1,"password":1})
        get_data_dict={}
        for i in records_fetched:
            get_data_dict=i


        if get_data_dict=={}:
            message="Not a Valid Member! Please register with your phone number ..."
            return render_template("index.html",message=message)
        elif input_dict["_id"]==get_data_dict["_id"] and input_dict["password"]==get_data_dict["password"]:
            session["username"]=get_data_dict["name"]
            session["_id"]=get_data_dict["_id"]
            return render_template("dashboard.html",table_details=get_table_details())
        else:
            message="Invalid Credential! Please provide your currect password..."
            return render_template("index.html",message=message)
    else:
        return render_template("index.html")


def get_table_details():
    records_fetched = collection_table.find({})
    get_table_dict=[]
    for i in records_fetched:
        get_table_dict.append(i)
    return  get_table_dict

def get_menu_details():
    records_fetched = collection_menu.find({})
    get_menu_dict=[]
    for i in records_fetched:
        get_menu_dict.append(i)
    return  get_menu_dict    
    
@app.route('/placeorder/<int:_id>',methods=["GET","POST"])
def place_order(_id):
    if request.method=="POST":
        try:
            orderlist=request.form['orderlist']       
            orderlist=orderlist.replace("\'","\"")
            orderlist=json.loads(orderlist)
            
            total=0
            for i in orderlist:
                for j in i.keys():
                    total+=(i[j][0]*i[j][1]['price'])

            collection_table.update_one({"_id":_id},{'$set':{'status':"true",'name':session["username"],"orderlist":orderlist,'total_amonut':total,"phone":session["_id"]}})
        except:
            return render_template("order.html",menulist=get_menu_details(),table_detail=table_detail)
        finally:
            return render_template("dashboard.html",table_details=get_table_details())
    
    get_table_detail=collection_table.find({"_id":_id})
    for i in get_table_detail:
        table_detail=i
    if "orderlist" in table_detail.keys():
        return render_template("order.html",menulist=get_menu_details(),orderlist=table_detail["orderlist"],table_detail=table_detail) 
    else:
        return render_template("order.html",menulist=get_menu_details(),table_detail=table_detail)

@app.route('/response/<int:_id>', methods=['POST'])
def response(_id):
    if request.method=="POST":

        item = request.form["item"]
        quant = int(request.form["quant"])
        rate=collection_menu.find_one({"item":item},{"_id":0,"price":1})
        if request.form["orderlist"]:
            orderlist=request.form["orderlist"]
            orderlist=orderlist.replace("\'","\"")
            orderlist=json.loads(orderlist)
            orderlist.append({item:[quant,rate]})
        else:
            orderlist=[{item:[quant,rate]}]

        get_table_detail=collection_table.find({"_id":_id})
        for i in get_table_detail:
            table_detail=i
        print(table_detail)
        return render_template("order.html",orderlist=orderlist,menulist=get_menu_details(),table_detail=table_detail)


@app.route('/remove/<int:_id>&&<string:item>&&<int:quant>', methods=['POST'])
def remove(_id,item,quant):
    if request.method=="POST":

        rate=collection_menu.find_one({"item":item},{"_id":0,"price":1})
        orderlist=request.form["orderlist"]
        orderlist=orderlist.replace("\'","\"")
        orderlist=json.loads(orderlist)

        orderlist.remove({item:[quant,rate]})
        
        get_table_detail=collection_table.find({"_id":_id})
        for i in get_table_detail:
            table_detail=i
        print(table_detail)
        return render_template("order.html",orderlist=orderlist,menulist=get_menu_details(),table_detail=table_detail)

@app.route('/resolve/<int:_id>',methods=["GET","POST"])
def resolve_order(_id):
    fetched=collection_table.find_one({"_id":_id})
    print(fetched)
    if request.method=="POST":
        if request.form['rating']:
            rating=request.form['rating']
            fetched["rating"]=rating
        collection_logs.insert_one({"full_logs":fetched})
        collection_table.update_one({"_id":_id},{'$set':{'status':"false"},'$unset':{'name':1,'orderlist':1,"total_amonut":1,"phone":1}})
        return redirect("/dashboard")
    else:
        collection_logs.insert_one({"full_logs":fetched})
        collection_table.update_one({"_id":_id},{'$set':{'status':"false"},'$unset':{'name':1,'orderlist':1,"total_amonut":1,"phone":1}})
        return redirect("/dashboard")


@app.route('/editpassword',methods=["GET","POST"])
def change_password():   
    if request.method=="POST":
        password=request.form['password']
        newpassword=request.form['password1']
        input_dict={"_id":session["_id"],"password":password}
        records_fetched = collection_user.find({'_id':session["_id"]},{"_id":1,"name":1,"password":1})
        get_data_dict={}
        for i in records_fetched:
            get_data_dict=i

        if input_dict["password"]==get_data_dict["password"]:
            collection_user.update_one({"_id":session["_id"]},{'$set':{'password':newpassword}})
            message="Password changed successfully ..."
            return render_template("dashboard.html",table_details=get_table_details(),message=message)
        else:
            message="Current Password is not matching! Please provide a valid one..."
            return render_template("editpassword.html",message=message)
    else:
        return render_template("editpassword.html")

@app.route('/editprofile',methods=["GET","POST"])
def change_profile():   
    if request.method=="POST":
        phone=request.form['phone']
        name=request.form['name']
        collection_table.update_many({"phone":session["_id"]},{'$set':{"name":name,'phone':phone}})
        records_fetched = collection_user.find({'_id':session["_id"]},{"_id":1,"name":1,"password":1})
        get_data_dict={}
        for i in records_fetched:
            get_data_dict=i
        collection_user.delete_one({"_id":session["_id"]})
        collection_user.insert_one({'_id':phone,"name":name,"password":get_data_dict['password']})
        session["_id"]=phone
        session["username"]=name
        return redirect("/viewprofile")
    else:
        return render_template("editprofile.html")

@app.route('/viewprofile')
def view_profile(): 
    return render_template("view_profile.html")

@app.route('/myorderlist')
def view_myorder(): 
    return render_template("myorder.html",table_details=get_table_details())

@app.route('/logout')
def logout(): 
    session.pop("_id",None)
    session.pop("username",None)
    return render_template("index.html")

if __name__ == "__main__":
    
    app.run(debug=True,port=8000)


"""
2.	Bring My Food, Kitchen
Description:
Create a RESTful Flask API. Create a login page. Ask new user to Register Yourself.
Go to next page that shows all tables already booked status and add a new Table with a create Button.
This will take new request Show a new Dashboard page showing request/orders from different table numbers with 
resolve button one food is delivered user can press resolve. 
[Additional Task: Give rating to the waiter who is delivering it]
"""