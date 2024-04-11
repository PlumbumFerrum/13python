import requests
import json 




def NewQuestion():
    res = requests.get('https://opentdb.com/api.php?amount=50')
    response = json.loads(res.text)
    questions = open('questions.json', 'w')
    questions.write(json.dumps(response, ensure_ascii=False, indent = 4))   

    question = open('questions.json', 'r')
    data = json.load(question)
    print(data)
    try:
        for i in data['results']:        
            print(i['type'])
            print(i['difficulty'])
            print(i['category'])
            print(i['question'])
            print(i['correct_answer'])
            for answer in i['incorrect_answers']:
                print(answer)
    except:
        print("No questions found")        

'''
NewQuestion()
'''
User_Info = []


def Get_User_info():
    try:
        Users = open('Users.json', 'r')
        User_Info = json.load(Users)
    except:
        pass  
    
    User_Info = open('User_Info.json', 'w')
    User_Name = input("Name:")
    User_Info = json.dumps(User_Name)
    return User_Info       


User_Info.append(Get_User_info())
print(User_Info)
