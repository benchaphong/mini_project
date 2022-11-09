from firebase import firebase
firebase = firebase.FirebaseApplication(
        "https://workshop-a32ad-default-rtdb.asia-southeast1.firebasedatabase.app/",None
)

firebase.delete('https://workshop-a32ad-default-rtdb.asia-southeast1.firebasedatabase.app/')
print('recorde deleted')