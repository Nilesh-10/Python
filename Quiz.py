
userName=""
password=""
def registration():
    global userName,password
    print("Enter user name:");
    print(type(userName))
    userName=str(input());
    print("Enter Password:");
    password = str(input());
    print(userName);
    print(password);

def login():
    print("Enter username:");
    LuserName = str(input())
    print("Enter Password:")
    Lpassword = str(input())
    if(userName == LuserName and password == Lpassword):
        print("Login successfull")
    else:
        print("Invalid user or password...")

        
def pythonQuiz():
    if(userName):
        question=list()
        answer = list()
        userAns =list()
        score =0
        grade=1
        question.append("1.In which year python was developed? \n A.1995 \n B.1972 \n C.1981 \n D.1989")
        print(question[0])
        answer.append("d")
        userAns.append(str(input()))
        question.append("2.Who developed the python language \n A.Zim Den \n B.Guido van Rossum \n C.Niene Strom \n D.Wick van Rosssum")
        print(question[1])
        answer.append("b")
        userAns.append(str(input()))
        question.append("3.How many keywords are there in python 3.7 \n A.32 \n B.33 \n C.31 \n D.30")
        print(question[2])
        answer.append("b")
        userAns.append(str(input()))
        question.append("4.In which year was the python 3.0 version developed? \nA.2005 \n B.2000 \n C.2010 \nD.2008")
        print(question[3])
        answer.append("d")
        userAns.append(str(input()))
        question.append("Which character is used in Python to make a single line comment? \nA./ \nB.// \nC.# \nD.?")
        print(question[4])
        answer.append("c")
        userAns.append(str(input()))
        for i in range(len(answer)):
            if(userAns[i] == answer[i]):
                score=score+1
        grade=(score*100)//5
        print("Your score:" + str(grade))
        if(grade>80):
            print("Excellent" + "  " + userName)

        elif(grade>70 and grade<80):
            print("Good" + "  " + userName)
        else:
            print("Try again" + "  " + userName)       
    else:
        print("Please Login")


def javaQuiz():
    if(userName):
        question=list()
        answer = list()
        userAns =list()
        score =0
        grade=1
        question.append("1.Which of the following is not a java features? \nA.Dynamic \nB.Architecture Neutral \nC.Use of pointer \nD.Object-oriented")
        print(question[0])
        answer.append("c")
        userAns.append(str(input()))
        question.append("2.Who invented java programming? \nA.Guido Van Rossum \nB.James Gosling \nC.Dennis Ritchie \nD.Bjarne Stroustrup")
        print(question[1])
        answer.append("b")
        userAns.append(str(input()))
        question.append("3.Which of these cannot be used for a variable name in java \nA.Identifiers & Keywords \nB.Identifiers \nC.Keywords \nD.none of the mentioned")
        print(question[2])
        answer.append("c")
        userAns.append(str(input()))
        question.append("4.What is the extension of java code file \nA.js\nB.txt\nC.class\nD.java")
        print(question[3])
        answer.append("d")
        userAns.append(str(input()))
        question.append("5.Which of the following is not an OOP concept in java\nA.Polymorphism \nB.Inheritance \nC.Compilation \nD.Encapsulation")
        print(question[4])
        answer.append("c")
        userAns.append(str(input()))
        for i in range(len(answer)):
            if(userAns[i] == answer[i]):
                score=score+1
        grade=(score*100)//5
        print("Your score:" + str(grade))
        if(grade>80):
            print("Excellent" + "  " + userName)

        elif(grade>70 and grade<80):
            print("Good" + "  " +userName)
        else:
            print("Try again" +"  " + userName)          
    else:
        print("Please Login")


while(1):
    print("1.Registration")
    print("2.Login")
    print("3.Python quiz")
    print("4.Java quiz")
    print("5.Exit")

    n=(input())
    if(n == '1'):
        registration()

    if(n == '2'):
        login()

    if(n == '3'):
        pythonQuiz()

    if(n == '4'):
        javaQuiz()
    if(n=='5'):
        exit(0)    
