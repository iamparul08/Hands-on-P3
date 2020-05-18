userlist_ADID = []
stream_ADID = []
#userlist_ADID
for i in range(0,5):
    name = input("Enter Linux user names")
    userlist_ADID.append(name)
print(userlist_ADID)

#stream_ADID
for i in range(0,5):
    name = input("Enter CIS stream names")
    stream_ADID.append(name)
print(stream_ADID)

print("Original key list is : " + str(userlist_ADID))
print("Original value list is : "+ str(stream_ADID))

print("Dictionary is")
userdict_ADID = {}
for key in userlist_ADID:
    for value in stream_ADID:
        userdict_ADID[key] = value
        stream_ADID.remove(value)
        break

    # Printing resultant dictionary
print("Resultant dictionary is : " + str(userdict_ADID))