import pyrebase

config = {
  'apiKey': "AIzaSyBLCdqXHMYP-Hm0maNclOpiWK-UsiQ-Eto",
  'authDomain' : "medify-37830.firebaseapp.com",
  'databaseURL': "https://medify-37830-default-rtdb.firebaseio.com",
  'projectId' : "medify-37830",
  'storageBucket' : "medify-37830.appspot.com",
  'messagingSenderId' : "882712357939",
  'appId' : "1:882712357939:web:f924a4b3f753079639c746",
  'measurementId' : "G-5H0GB0Z7WQ"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()
auth = firebase.auth()


def login(email, password):
    id_token = None

    try:
        id_token = auth.sign_in_with_email_and_password(email, password)["idToken"]
    except:
        print("Invalid credentials")

    return id_token is not None


def create_acct(email, password):
    try:
        auth.create_user_with_email_and_password(email, password)
    except:
        print("Acct. creation failed")


def verify_emt(ems_id):
    emt_list = database.child("emts").get().val()
    return ems_id in emt_list


def update_patient_info(info):
    patients = database.child("patients").get().val()
    if info["dlid"] in patients:
        for key in info:
            database.child("patients").child(info["dlid"]).update({key: info[key]})
    else:
        database.child("patients").set({info["dlid"] : info})


def get_patient_info(dlid):
    patient_info = database.child("patients").child(dlid).get().val()
    return patient_info

# Unit Test: User Login

# Unit Test: User Login --> Passed
print(verify_emt("101010"))
print(login("bun@njit.edu", "abcdefg"))

# Unit Test: Create Acct --> Passed
# create_acct("jt123@njit.edu", "abcdefgh")

# Unit Test: Verify EMS
print(verify_emt("10100"))

# Unit Test: Update Patient Info --> Passed
info = {  "name" : "Jonas",
          "age" : "15",
          "weight" : "145",
          "height" : "5'10",
          "blood type" : "A",
          "dlid" : "122441",
          "medical conditions" : "Autism",
          "allergies" : "Sound",
          "medication" : "Crack"
}
update_patient_info(info)

# Unit Test: Get Patient Info --> Passed
print(get_patient_info("12312441"))

