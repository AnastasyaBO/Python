import redis

red = redis.Redis(
    host='',
    port=,
    password=''
)

cont = True
while cont:
    do = input("What do you want: ")
    if do == 'write':
        name = input("Name: ")
        phone = input("Phone: ")
        red.set(name, phone)

    elif do == 'read':
        name = input('Name: ')
        phone = red.get(name)
        if phone:
            print(f"{name}\'s phone is {str(phone)}")

    elif do == 'delete':
        name = input('Name: ')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is delete")
        else:
            print(f"Not found {name}")
    elif do == 'stop':
        break

