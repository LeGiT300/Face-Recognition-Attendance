import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

# Initialize Firebase


cred = credentials.Certificate("AccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://attendancerealtime-d1465-default-rtdb.firebaseio.com/'
})


# Create a new tkinter window
window = tk.Tk()

# Set the window title
window.title("Firebase Upload")

# Create the form labels
name_label = tk.Label(window, text="Name:")
matricule_label = tk.Label(window, text="Matricule:")
school_label = tk.Label(window, text="School:")
department_label = tk.Label(window, text="Department:")
program_label = tk.Label(window, text="Program:")


# Create the form fields
name_entry = tk.Entry(window)
matricule_entry = tk.Entry(window)
school_entry = tk.Entry(window)
department_entry = tk.Entry(window)
program_entry = tk.Entry(window)


#  = tk.Entry(window)
#  = tk.Text(window)

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=lambda: submit_form())

# Define the submit button click handler
def submit_form():
 
    name = name_entry.get()
    matricule = matricule_entry.get()
    school = school_entry.get()
    deparment = department_entry.get()
    program = program_entry.get()
    now = datetime.now()
    newT = now.strftime('%Y-%m-%d %H:%M:%S')
    # stringTime = json.dumps({'last_attendance': now.isoformat()})
    total_attendance = 0
    
    data = {
        matricule: {
           "name": name,
            "school": school,
            "department": deparment,
            "program": program,
            'last_attendance': newT,
            'total_attendance': total_attendance
        }
    }
    ref = db.reference("Student Data")
    
    for key, val in data.items():
        ref.child(key).set(val)
    # Display a success message to the user
    
    success_label = tk.Label(window, text="Form submitted successfully!")
    success_label.grid(row=9, column=1)
    

# Add the form elements to the window

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
matricule_label.grid(row=1, column=0)
matricule_entry.grid(row=1, column=1)
school_label.grid(row=2, column=0)
school_entry.grid(row=2, column=1)
department_label.grid(row=3, column=0)
department_entry.grid(row=3, column=1)
program_label.grid(row=4, column=0)
program_entry.grid(row=4, column=1)
submit_button.grid(row=8, column=1)

# Start the tkinter event loop




window.mainloop()