from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from website.models.dbinteraction import DBInteraction
from flask_login import login_user, login_required, logout_user, current_user

admin = Blueprint('admin', __name__)

@admin.route('/login', methods=['GET', 'POST'])
def login():
    checkDB()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        dbinteraction = DBInteraction()           
        user = dbinteraction.QueryUser(email)
        if user:
            if dbinteraction.CheckPasswordHash(user, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('admin.adminhome'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("adminlogin.html", user=current_user)


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))


@admin.route('/subcategories')
@login_required
def adminsubcategories():
    query = ''' 
    SELECT subcat.id, cat.category, cat.description, subcat.subcategory, subcat.subdescription, cat.id as catid
    FROM subcategories as subcat 
    JOIN categories as cat 
	ON cat.id = subcat.catid
    '''
    dbinteraction = DBInteraction()
    categories = dbinteraction.ExecuteQuery(query)
    return render_template("admincategories.html", user=current_user, categories=categories)


@admin.route('/admin')
@login_required
def adminhome():
    query = '''
        SELECT category, count(category) as category_count FROM search_transactions
        GROUP BY category
        HAVING count(category)>1
        ORDER BY count(category) desc
    '''
    dbinteraction = DBInteraction()
    categories = dbinteraction.ExecuteQuery(query)
    return render_template("adminhome.html", user=current_user, categories=categories)


@admin.route("/add_category",methods=["POST","GET"])
@login_required
def add_category():
    if request.method == 'POST':
        txtcategory = (request.form['txtcategory']).strip()
        txtdescription = (request.form['txtdescription']).strip()
        txtsubcategory = (request.form['txtsubcategory']).strip()
        txtsubdescription = (request.form['txtsubdescription']).strip()
        if txtcategory == '':
            msg = 'Error: Please input category'  
            return jsonify(msg)
        elif txtdescription == '':
            msg = 'Error: Please input category description'
            return jsonify(msg)
        elif txtsubcategory == '':
            msg = 'Error: Please input subcategory' 
            return jsonify(msg)
        elif txtsubdescription == '':
            msg = 'Error: Please input subcategory description'
            return jsonify(msg)
        username = current_user
        dbinteraction = DBInteraction()
        category = dbinteraction.QueryCategory(txtcategory)
        if category is None:
            dbinteraction.AddCategory(txtcategory, txtdescription, username.first_name)
            category = dbinteraction.QueryCategory(txtcategory)
            dbinteraction.AddSubcategory(txtsubcategory, txtsubdescription, category.id, username.first_name)
            msg = 'Success: New category and subcategory created successfully.'   
        else:
            subcategory = dbinteraction.QuerySubcategory(txtsubcategory)
            if subcategory is None:
                category = dbinteraction.QueryCategory(txtcategory)
                dbinteraction.AddSubcategory(txtsubcategory, txtsubdescription, category.id, username.first_name)
                msg = 'Success: New subcategory created successfully.'
            else: 
                msg = 'Error: Category and Subcategory already exists.'
    return jsonify(msg)


@admin.route("/delete_category",methods=["POST","GET"])
@login_required
def delete_category():
    if request.method == 'POST':
        getid = request.form['string']
        if getid == '':
            msg = 'Error: Invalid subcategory id'  
            return jsonify(msg)
        dbinteraction = DBInteraction()
        subcategory = dbinteraction.QuerySubcategoryByID(getid)
        if not subcategory is None:
            catid = subcategory.catid
            dbinteraction.DeleteSubcategory(getid)
            subcategory = dbinteraction.QuerySubcategoryByCatID(catid)
            if subcategory is None:
                dbinteraction.DeleteCategory(catid)
            msg = 'Success: Record deleted successfully'   
        else:
            msg = 'Error: Failed to retrieve subcategory id from database.'  
    return jsonify(msg)


@admin.route("/update_category",methods=["POST","GET"])
@login_required
def update_category():
    if request.method == 'POST':
        getid = request.form['string']
        txtdescription = (request.form['txtdescription']).strip()
        txtsubdescription = (request.form['txtsubdescription']).strip()
        username = current_user
        dbinteraction = DBInteraction()
        subcategory = dbinteraction.QuerySubcategoryByID(getid)
        if not subcategory is None:
            catid = subcategory.catid
            dbinteraction.UpdateSubcategory(getid, txtsubdescription, username.first_name)
            dbinteraction.UpdateCategory(catid, txtdescription, username.first_name)
        else:
            msg = 'Error: Failed to retrieve subcategory id from database.'
        msg = 'Record successfully Updated'   
    return jsonify(msg) 


def checkDB():
    dbinteraction = DBInteraction()
    users = dbinteraction.QueryAllUsers()
    if not users:
        dbinteraction.AddUser('admin@gmail.com','admin','admin','admin')

