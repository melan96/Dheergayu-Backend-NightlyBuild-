######################################################


# Dheergayu Application Backend NightlyBuild Script #


#####################################################

from firebase import firebase
import firebase_admin
from firebase_admin import credentials, firestore
import requests
import random as rand
import json
import datetime

FIREBASE_CONFIGURATIONS_LOCATION = "/Users/melandias/Downloads/creds.json"
GLOBAL_USERID = "Q6b7CzQDg7avBqDgFJdmkwo87192"
APPLICATION_BACKEND_RUNTIME = ""
SERVICE_HOST_URL = "http://3.16.163.12:"
SLEEP_COMPONENT_SERVICE_ENDPOINT = "5010/api/models/sleep"
HRV_COMPONENT_SERVICE_ENDPOINT = "5020/api/model/hrv"
STATIC_FACE_COMPONENT_SERVICE_ENDPOINT = ""
DYNAMIC_FACE_COMPONENT_SERVICE_ENDPOINT = ""


def connectFireabseDatabase():
    print("Loaded Configuration File from : " + FIREBASE_CONFIGURATIONS_LOCATION)

    # Onetime run codeblock
    # Firebase Credentials

    # TODO: Cred.json should import on runtime
    databaseURL = {
        'databaseURL': "https://dheergayuappclient.firebaseio.com"
    }
    cred = credentials.Certificate(FIREBASE_CONFIGURATIONS_LOCATION)
    firebase_admin.initialize_app(cred, databaseURL)
    global database_fs
    database_fs = firestore.client()


# End of Onetime run code-block


def executionForSleepContext():
    # Read SLEEP Data for Firebase Readers

    print("\n"
          "\n"

          "*************************[[DEPRESSIVE-SLEEP-COMPONENT EXECUTION STARTED]]**********************************"

          "\n"
          "\n"
          )

    doc = database_fs.collection('sleep-data-comps').document(GLOBAL_USERID).get()
    if doc.exists:
        TST = doc.to_dict()['TST']
        SE = doc.to_dict()['SE']
        S1 = doc.to_dict()['S1']
        S2 = doc.to_dict()['S2']
        S3 = doc.to_dict()['S3']
        W = doc.to_dict()['W']
        TIB = doc.to_dict()['TIB']
        REM_Density = doc.to_dict()['REM_Density']
        REM = doc.to_dict()['REM']

        print(f' [READ - SLEEP_COMP] Document data: {doc.to_dict()}')

        print('[INVOKE-ENDPOINT]  ACCESSING ENDPOINT SERVICE /SLEEP')

        sleep_payload = {

            'TST': str(TST),
            'SE': str(SE),
            'S1': str(S1),
            'S2': str(S2),
            'S3': str(S3),
            'W': str(W),
            'TIB': str(TIB),
            'REM_Density': str(REM_Density),
            'REM': str(REM)

        }

        response_set = requests.post(SERVICE_HOST_URL + SLEEP_COMPONENT_SERVICE_ENDPOINT, data=json.dumps(sleep_payload))
        print('\n'
              '\n'
              '[INVOKE-ENDPOINT]  ACCESSING ENDPOINT SERVICE --- RESPONSE  /SLEEP')
        print("[INVOKE-ENDPOINT]  CAPTURED RESPONSE STATUS (200 - OK) --- >>  " + str(response_set))
        print("[INVOKE-ENDPOINT]  CAPTURED RESPONSE --- >>  " + str(response_set.text))
        dict = response_set.json()
        print('\n'
              '\n'
              '[INVOKE-ENDPOINT]  ACCESSING ENDPOINT SERVICE --- RESPONSE  /SLEEP')
        print('[INVOKE-ENDPOINT]  TERMINATE ENDPOINT SERVICE /SLEEP')

        global sleepuuid
        if dict == "[1]":
            sleepuuid = rand.randint(160,450)

        elif dict == "[2]":
            sleepuuid = rand.randint(451, 770)

        elif dict == "[3]":
            sleepuuid = rand.randint(771, 880)

        sleepuuid = sleepuuid/10
        print(sleepuuid)

        # Update firebase Value for the invoked paramaters
        doc_ref = database_fs.collection(u'report').document(u'' + GLOBAL_USERID + '')
        doc_ref.set({
            u'sleep_comp': u'' + str(sleepuuid) + '',
        })

    else:
        print(u' [ERROR] No such document!')
    print("\n"

          "*************************[[DEPRESSIVE_SLEEP-COMPONENT EXECUTION ENDED]]**********************************"
          "\n"

          "\n"
          )

def executionForHRVContext():
    # Read HRV Data for Firebase Readers
    doc = database_fs.collection('hrv-data-comps').document(GLOBAL_USERID).get()
    if doc.exists:
        maximum_heart_rate_achieved = doc.to_dict()['maximum_heart_rate_achieved']
        resting_blood_pressure = doc.to_dict()['resting_blood_pressure']
        age = doc.to_dict()['age']
        sex = '1'

        print("\n"
              "\n"

              "*************************[[HRV-COMPONENT EXECUTION STARTED]]**********************************"

              "\n"
              "\n"
              )
        print(f' [READ - HRV_COMP] Document data: {doc.to_dict()}')

        print('[INVOKE-ENDPOINT]  ACCESSING ENDPOINT SERVICE /HRV')

        hrv_payload = {

            'maximum_heart_rate_achieved': str(maximum_heart_rate_achieved),
            'resting_blood_pressure': str(resting_blood_pressure), 'age': str(age), 'sex': str(sex)

        }
        response_set = requests.post(SERVICE_HOST_URL + HRV_COMPONENT_SERVICE_ENDPOINT, data=json.dumps(hrv_payload))
        print('\n'
              '\n'
              '[INVOKE-ENDPOINT]  ACCESSING ENDPOINT SERVICE --- RESPONSE  /HRV')
        print("[INVOKE-ENDPOINT]  CAPTURED RESPONSE STATUS (200 - OK) --- >>  " + str(response_set))
        print("[INVOKE-ENDPOINT]  CAPTURED RESPONSE --- >>  " + str(response_set.text))
        dict = response_set.json()

        print('\n'
              '\n'
              '[INVOKE-ENDPOINT]  ACCESSING ENDPOINT SERVICE --- RESPONSE  /HRV')
        print('[INVOKE-ENDPOINT]  TERMINATE ENDPOINT SERVICE /HRV')

        global hrvuuid
        if dict == "[1]":
            hrvuuid = rand.randint(160,450)

        elif dict == "[2]":
            hrvuuid = rand.randint(451, 770)

        elif dict == "[3]":
            hrvuuid = rand.randint(771, 880)

        hrvuuid=hrvuuid/10
        print(hrvuuid)

        # Update firebase Value for the invoked paramaters
        doc_ref = database_fs.collection(u'report').document(u'' + GLOBAL_USERID + '')
        doc_ref.update({
            u'hrv_comp': u'' + str(hrvuuid) + '',
        })




    else:
        print(u' [ERROR] No such document!')


    print("\n"

          "*************************[[HRV-COMPONENT EXECUTION ENDED]]**********************************"
          "\n"

          "\n"
          )

# def executeForStaticFaceContext():
#  #   TODO : CREATE PKL FILE FROM MODEL
#  #   TODO : MODEL PKL INTIALIZATION




def updateDateTime():
    datetimenow = datetime.datetime
    print(datetimenow.today().strftime('%Y-%m-%d').__str__())
    database_fs.collection('report').document(GLOBAL_USERID).update({
        'date':datetimenow.today().strftime('%Y-%m-%d').__str__()
    })

def setOrUpdateDynamicComponent():
    database_fs.collection('report').document(GLOBAL_USERID).update({
        'dynamic_comp':'0',
        'dynamic_blink':'0',
        'dynamic_emotion':'0'
    })

def executeStaticComponent():




def main():

    connectFireabseDatabase()

    executionForSleepContext()
    executionForHRVContext()
    setOrUpdateDynamicComponent()
    updateDateTime()


if __name__ == "__main__":
    main()
