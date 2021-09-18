def minion_game(string):
    # your code goes herei
    kevin = 0
    stuart = 0
    string = list(string)
    for i in range (len(string)):
        if (string[i] in ('A', 'E', 'I', 'O', 'U')):
            kevin += (len(string))-i
        else :
            stuart += (len(string))-i
    if(kevin > stuart):
        print("Kevin",kevin)
    elif(stuart > kevin):
        print("Stuart",stuart)
    elif(stuart == kevin):
        print("Draw")
    else:
        print("Draw")
