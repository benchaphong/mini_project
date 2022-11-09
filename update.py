#update
from firebase import firebase
firebase = firebase.FirebaseApplication(
        "https://workshop-a32ad-default-rtdb.asia-southeast1.firebasedatabase.app/",None
)

firebase.put('https://workshop-a32ad-default-rtdb.asia-southeast1.firebasedatabase.app/','name','Dragon Fruit Smoothie','taste','so sweet')
print('recorde update')