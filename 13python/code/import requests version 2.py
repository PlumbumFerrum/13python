import requests
import json 

User_Info = []

def New_User():
    User_Name = input("Name:")
    User_Info.append(User_Name)

def save_users():
    open('User_Info.json', 'w').write(json.dumps(User_Info))

def load_users():
    try:
        f = open('User_Info.json', 'r')
        return json.loads(f.read())
    except:
        open('User_Info.json', 'w').write(json.dumps([]))
        return []
#User_Info.append(Get_User_info())




#
#def request_Specific_Thingy():


User_Info = load_users()

New_User()

save_users()

print(User_Info)

def get_catagories():
    
    with open("Catagories.json", "w") as f:
        Catagories = json.dump("", f, indent=4, sort_keys=True)
    Catres = requests.get("https://opentdb.com/api_catagory.php")
    Catresponse = json.loads(Catres.text)
    Catagories = open('Catagories.json', 'w')
    Catagories.write(json.dumps(Catresponse, ensure_ascii=False, indent = 4))
    

def Get_Bounds():
    Amount = 50
    Catagory = input("What catagory would you like")
    return Amount, Catagory, Difficulty, Type

Amount, Catagory, Difficulty, Type = Get_Bounds()



def NewQuestion(Amount, Catagory, Difficulty, Type):
    
    
    with open("questions.json", "w") as f:
        questions = json.dump("", f, indent=4, sort_keys=True)
    res = requests.get('https://opentdb.com/api.php?amount'+str(Amount)+Catagory+Difficulty+Type)
    response = json.loads(res.text)
    questions = open('questions.json', 'w')
    questions.write(json.dumps(response, ensure_ascii=False, indent = 4))   

    question = open('questions.json', 'r')
    data = json.load(question)
    input('What difficulty question would you like?\n1: Easy\n2: Medium \n3: Hard\n\n\n',)
    
NewQuestion()

'''

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


exit = input("Press Any Key To Exit")
try:
     if exit == '':
          quit()
except:
     quit()