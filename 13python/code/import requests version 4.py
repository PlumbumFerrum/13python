import requests
import json 
import os
import html
import random

User_Info = []
def clear():
    os.system('cls')
def New_User():
    clear()
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

#early response code

def get_catagories():
    Catagories = open('Catagories.json', 'w')
    file = open('Catagories.json', 'r')
    Catagories = file.read()
    Catres = requests.get('https://opentdb.com/api_category.php')
    Catresponse = json.loads(Catres.text)
    Catagories = open('Catagories.json', 'w')
    Catagories.write(json.dumps(Catresponse['trivia_categories'], ensure_ascii=False, indent = 4))
   
get_catagories()

def Get_Bounds():
    file = open('Catagories.json', 'r')
    Catagories =  json.loads(file.read()) 
    amount = int(input('how many Questions would you like? (1-50)'))
    Difficulty_Options = ['easy','medium','hard']
    Type_Options = ['multiple','boolean']
    
    clear()
    for x , i in enumerate(Catagories, start = 1):
        print( str(x) + ' ' + i['name'])
    
    Catagory = int(input('\nWhat catagory would you like:'))
    Catagory += 8 
    Catagory_URL = (f"&category={Catagory}")
    
    clear()
    Difficulty = int(input('What difficultty Questions would you like?\n1: Easy\n2: Medium\n3: Hard'))
    Difficulty -= 1
    Difficulty_URL = (f"&difficulty={Difficulty_Options[Difficulty]}")
    clear()
    Type = int(input('What Questions would you like to have:\n1: Multiple choice \n2: True/False \n'))
    Type -= 1
    Type_URL = (f"&type={Type_Options[Type]}")
    
    return amount, Catagory_URL, Difficulty_URL, Type_URL

amount, Catagory_URL, Difficulty_URL, Type_URL, = Get_Bounds()


def NewQuestion(amount, Catagory_URL, Difficulty_URL, Type_URL):

    URL_res = requests.get(f'https://opentdb.com/api.php?amount={str(amount)}{Catagory_URL}{Difficulty_URL}{Type_URL}')
    response = json.loads(URL_res.text)
    
    questions = open('questions.json', 'w') 
    json.dump(response, questions, indent = 4)
    questions.close()


    question = open('questions.json', 'r')
    data = json.load(question)

    #test sending to file
    
    return data
 

data = NewQuestion(amount, Catagory_URL, Difficulty_URL, Type_URL)
data = data['results']


#print(data)
def Quiz_main(data):
    clear()
    repeater = 0
    
    while repeater < amount:
        
        clear()
        
        for questions in data:
            
            temap_array = questions['incorrect_answers']
            temap_array.append(questions['correct_answer'])
            print(html.unescape(questions['question']))
            #print('1 '+ questions['correct_answer'])
            random.shuffle(temap_array)
           
            for w , e in enumerate(temap_array, start = 1 ):
                print( html.unescape(str(w) +" "+ e))
            answer = int(input(""))
            answer-=1
            
        
            if temap_array[answer] == questions['correct_answer']:
                print('correct')
                input('')
            else:    
                print('incorrect')
                input('')
            clear()
         
        repeater += 1 


Quiz_main(data)
#early display funtion

exiting = input('Press Any Key To Exit')

def exit(exiting):
    try:
        if exiting == '':
            clear()
            quit()
    except:
        clear()
        quit()















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
'''
    with open('questions.json', 'w') as questions:
        json.dump(response, questions, indent = 4)
    
    with open('questions.json', 'w') as f:
        questions.write(json.dumps(f,response))

    with open('questions.json', 'w') as f:
        response = json.dump(response, f, indent=4, sort_keys=True)
        '''