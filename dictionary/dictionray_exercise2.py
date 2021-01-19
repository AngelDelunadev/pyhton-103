ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
print (f"Ramit's email is {ramit['email']} " )
print (f"Ramit's first interests is {ramit['interests'][0]}")
print (f"""Jasmin's email is  {ramit["friends"][0]['email']}""")
print (f"""Jan's secound interest is {ramit["friends"][1]["interests"][1]}""")

def countFriends(dictionary):
    dictionary["friends_count"] =len(dictionary["friends"])
    return dictionary

countFriends(ramit)
print(ramit["friends_count"])