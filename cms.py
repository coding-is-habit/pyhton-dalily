#customer managment system
#to add user
def cs_add(id,name,age ):
    if id not in cs_id:
        cs_id.append(id)
        cs_name.append(name)
        cs_age.append(age)
        print(cs_id,cs_age,cs_name)
    else:
        print("user already exist")


#to search user using id of user
def search_user(searchi):
            if searchi in cs_id:
                user_index=cs_id.index(searchi)
                display_user(user_index)
            else:
                print("user not found")


#to delete user using id
def user_delete(user_d):
    if user_d in cs_id :
        temp=cs_id.index(user_d)
        cs_id.pop(temp)
        cs_name.pop(temp)
        cs_age.pop(temp)


#to update name age of user by id
def user_modify(user_m):
    display_user(cs_id.index(user_m))
    cs_name[cs_id.index(user_m)]=input('enter correct name')
    cs_age[cs_id.index(user_m)]=input('enter correct age')


#to display user using index
def display_user(index):

        print('User ID : ',cs_id[index])
        print('User Name: ',cs_name[index])
        print('User Age: ',cs_age[index])


#to display all user in system
def display_all():
    print('Sr. No\t User Id\tUser Name\tUser Age')
    for i in range(len(cs_id)):
        print(i+1,'\t\t',cs_id[i],'\t\t',cs_name[i],'\t',cs_age[i])

cs_id = []
cs_age = []
cs_name = []

while ( 1 ) :
    print('''    enter 1 to add customer
    enter 2 to search customer
    enter 3 to delete customer
    enter 4 to modify customer
    enter 5 to display all customers
    enter 6 to exit
    ''')

    ch=int(input('enter choice 1 to 6'))

#choice for add
    if ch == 1 :
        id = input('enter customer id:')
        name = input('enter customer name')
        age = input('enter age')
        confirm = input("enter yes to confirm or no to cancel ")
        if confirm == 'yes'and'Yes':
            cs_add(id, name, age)
            print("User Added Successfully")
        else:
            print('Thank You')


#choice for search
    elif ch ==2:
        searchi=input("Please enter id")
        search_user(searchi)


    elif ch == 3:
        user_d = input("Enter Id of User")
        if cs_id.count(user_d) != 0:
            user_delete(user_d)
            print("user deleted successfully")
        else:
            print("User Not Found")

#choice for modify
    elif ch == 4:
        user_m=input("Enter Id of User")
        if user_m in cs_id:
            user_modify(user_m)
            print("user modified")

        else:
            print('User Not Found')

#choice for display
    elif ch == 5:
        display_all()
        print("All User Are listed above")


#to stop loop
    elif ch == 6:
        break