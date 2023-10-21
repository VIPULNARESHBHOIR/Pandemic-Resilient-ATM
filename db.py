
import mysql.connector as msc

con = None
cursor = None

# Function to establish the database connection
def establish_connection():
    global con, cursor
    try:
        con = msc.connect(
            host="localhost",
            user="root",
            passwd="vipul",
            database="bank"
        )
        cursor = con.cursor()
    except Exception as e:
        print(e)

# Define the Update and Read functions 

def Update(query):
    try:

        cursor.execute(query) 
        con.commit()

        if cursor.rowcount>0:
            print ("Data Updated Successfully...") 
        else: 
            print ("No DataFound")
    except Exception as e:
        print(e)

def Read(query):
    try:
        cursor.execute(query) 
        ans=cursor.fetchall()
        cursor.close()
        con.close()
        if ans:
            return ans
        else: 
            return 11
    except Exception as e:
        print(e)
