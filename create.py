from firebase import firebase
firebase = firebase.FirebaseApplication(
        "https://workshop-a32ad-default-rtdb.asia-southeast1.firebasedatabase.app/",None
)

mydata = {
        'id_smoothie':'1',
        'name_smoothie':'Lychee Smoothie',
        'taste':'normal',
        'cost':'24'
}

result = firebase.post('https://workshop-a32ad-default-rtdb.asia-southeast1.firebasedatabase.app/',mydata)
print(result)