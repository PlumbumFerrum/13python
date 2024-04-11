import requests
import json 

User_Info = []

def New_User():
    User_Name = input('Name:')
    
    return User_Name

def save_users():
    Save_User = open('User_Info.json', 'w') 
    json.dump(User_Info, Save_User , indent = 4)

def load_users():
    try:
        f = open('User_Info.json', 'r')
        return json.loads(f.read())
    except:
        open('User_Info.json', 'w').write(json.dumps([]))
        return []

New_UserName = New_User()
User_Info = load_users()
User_Info.append(New_UserName)
save_users()

#print(User_Info)


#early response code
'''
def get_catagories():
    Catagories = open('Catagories.json', 'w')
    file = open('Catagories.json', 'r')
    Catagories = file.read()
    Catres = requests.get('https://opentdb.com/api_category.php')
    Catresponse = json.loads(Catres.text)
    Catagories = open('Catagories.json', 'w')
    Catagories.write(json.dumps(Catresponse['trivia_categories'], ensure_ascii=False, indent = 4))
   
get_catagories()
'''


def Get_Bounds():
    file = open('Catagories.json', 'r')
    Catagories =  json.loads(file.read())
    Amount = 50
    Difficulty_Options = ['easy','medium','hard']
    Type_Options = ['multiple','boolean']
    
    
    
    for x , i in enumerate(Catagories, start = 1):
        print( str(x) + ' ' + i['name'])
    Catagory = int(input('What catagory would you like:'))
    Catagory += 8 
    Catagory_URL = (f"&category={Catagory}")
    print(Catagory_URL)
    
    Difficulty = int(input('What difficultty Questions would you like?\n1: Easy\n2: Medium\n3: Hard'))
    Difficulty -= 1
    Difficulty_URL = (f"&difficulty={Difficulty_Options[Difficulty]}")
    
    Type = int(input('What Questions would you like to have:\n1: Multiple choice \n2: True/False '))
    Type -= 1
    Type_URL = (f"&type={Type_Options[Type]}")
    
    return Amount, Catagory_URL, Difficulty_URL, Type_URL

Amount, Catagory_URL, Difficulty_URL, Type_URL = Get_Bounds()


def NewQuestion(Amount, Catagory_URL, Difficulty_URL, Type_URL):
    
    
    

    URL_res = requests.get(f'https://opentdb.com/api.php?amount={str(Amount)}{Catagory_URL}{Difficulty_URL}{Type_URL}')
    response = json.loads(URL_res.text)
    
    questions = open('questions.json', 'w') 
    json.dump(response, questions, indent = 4)

    '''
    with open('questions.json', 'w') as questions:
        json.dump(response, questions, indent = 4)
    
    with open('questions.json', 'w') as f:
        questions.write(json.dumps(f,response))

    with open('questions.json', 'w') as f:
        response = json.dump(response, f, indent=4, sort_keys=True)
 
'''
NewQuestion(Amount, Catagory_URL, Difficulty_URL, Type_URL)

#early display funtion
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
        print('No questions found')        
'''


exiting = input('Press Any Key To Exit')

def exit(exiting):
    try:
        if exiting == '':
            quit()
    except:
        quit()