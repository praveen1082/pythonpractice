customer = {
    "name": "praveen panta",
    "age": 30,
    "age_verified": True
}
#each key should be unique in a dictionary
print(customer['name'])
#if passed key if it does not exist the key error occurs and the matching name cases should also be same
print(customer.get("birthdata", "1998-08-04"))
customer["hello"] = "hello world"
print(customer)

