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
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Establish the database connection
        con = mysql.connector.connect(**db_config)
        cursor = con.cursor()

        # Insert data into the 'contact' table using a prepared statement
        sql = "INSERT INTO contact (name, email, subject, message) VALUES (%s, %s, %s, %s)"
        data = (name, email, subject, message)

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
