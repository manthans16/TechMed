from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "vipul"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        moblie = request.form['moblie']
        arrivals = request.form['arrivals']
        city = request.form['city']
        address = request.form['address']

        # Establish the database connection
        con = mysql.connector.connect(**db_config)
        cursor = con.cursor()

        # Insert data into the 'clinic' table using a prepared statement
        sql = "INSERT INTO clinic (fname, lname, email, moblie, arrivals, city, address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (fname, lname, email, moblie, arrivals, city, address)

        try:
            cursor.execute(sql, data)
            con.commit()
            return "Record Inserted.."
        except Exception as e:
            con.rollback()
            return "Error: " + str(e)
        finally:
            cursor.close()
            con.close()

    return render_template('form.html')

if __name__ == '__main__':
    app.run()
