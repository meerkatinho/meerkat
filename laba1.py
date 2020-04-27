wrong_answer_counter=0
flag= True
while flag:
    num_1=int(input("first: "))
    num_2=int(input("second: "))
    command=input('input command: ')
    if command=='+':
        print(num_1 + num_2)
    elif command=='-':
        print(num_1 - num_2)
    elif command=='/':
        print(num_1 / num_2)
    elif command=='*':
        print(num_1 * num_2)
    else:
        print('error')
    while True:
        command=input('Continue? yes/no ')
        if command=="no":
            flag=False
            break
        elif command=="yes":
            break
        else:
            print("error")
            wrong_answer_counter+=1
            if wrong_answer_counter==3:
                flag=False
                print('too much error!')
                break

