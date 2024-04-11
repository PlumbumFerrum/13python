import requests
import json 
import os
import html
import random
from playsound import playsound

## final version ##


User_Info = []
def clear():
    os.system('cls')

def error_correct_input(bounds, input_question):
    while True:
        try:
            inputnumber = int(input(input_question))
            if inputnumber < bounds:
                return inputnumber
        except:
            print(f'Please Select a number between 1 and {bounds}\n')
def New_User():
    clear()
    User_Name = input('Name:')
    return User_Name


def save_users():
    Save_User = open('User_Info2.json', 'w') 
    json.dump(User_Info, Save_User , indent = 4)


def load_users():
    try:
        f = open('User_Info.json', 'r')
        return json.loads(f.read())
    except:
        open('User_Info.json', 'w').write(json.dumps([]))
        return []

def get_catagories():
    Catagories = open('Catagories.json', 'w')
    file = open('Catagories.json', 'r')
    Catagories = file.read()
    Catres = requests.get('https://opentdb.com/api_category.php')
    Catresponse = json.loads(Catres.text)
    Catagories = open('Catagories.json', 'w')
    Catagories.write(json.dumps(Catresponse['trivia_categories'], ensure_ascii=False, indent = 4))

def Get_Bounds():
    file = open('Catagories.json', 'r')
    Catagories =  json.loads(file.read()) 
        
    Difficulty_Options = ['easy','medium','hard']
    
    Type_Options = ['multiple','boolean']
    
    amount_users = error_correct_input(4, 'how many users would you like (1-4)')
    
    amount = error_correct_input(50, 'how many Questions would you like? (1-50)')

    clear()
    
    for x , i in enumerate(Catagories, start = 1):
        print( str(x) + ' ' + i['name'])
    
    Catagory = error_correct_input( 24, '\nWhat catagory would you like:')
    Catagory += 8 
    Catagory_URL = (f"&category={Catagory}")


    
    clear()
    difficulty = error_correct_input( 3, 'What diificulty questing would you like \n1: Easy\n2: Medium\n3: Hard')
    difficulty -= 1
    difficulty_URL = (f"&difficulty={Difficulty_Options[difficulty]}")
    clear()
    Type = error_correct_input( 2, 'What Questions would you like to have:\n1: Multiple choice \n2: True/False \n')
    Type -= 1
    Type_URL = (f"&type={Type_Options[Type]}")
    
    return amount, Catagory_URL, difficulty_URL, Type_URL, amount_users

def NewQuestion(amount, Catagory_URL, difficulty_URL, Type_URL):

    URL_res = requests.get(f'https://opentdb.com/api.php?amount={str(amount)}{Catagory_URL}{difficulty_URL}{Type_URL}')
    response = json.loads(URL_res.text)
    
    questions = open('questions.json', 'w') 
    json.dump(response, questions, indent = 4)
    questions.close()


    question = open('questions.json', 'r')
    data = json.load(question)

    #test sending to file
    
    return data

def Quiz_main(data, amount_users):
    clear()
    amount_users_repeater = 1
    
    while amount_users_repeater <= amount_users:
        
        
        for questions in data:
            clear()
            if amount_users_repeater == 1:        
                temap_array = questions['incorrect_answers']
                temap_array.append(questions['correct_answer'])
            
            print(html.unescape(questions['question']))
            #print('1 '+ questions['correct_answer'])
            random.shuffle(temap_array)
        
            for w , e in enumerate(temap_array, start = 1 ):
                print( html.unescape(str(w) +" "+ e))
            
            
            answer = int(error_correct_input(4, ''))
            answer-=1
            
            if temap_array[answer] == questions['correct_answer']:
                print('correct')
                #playsound("SoundBites\medieval-fanfare.mp3")
                
            else:    
                print('incorrect')
                #playsound("SoundBites\Wrong.mp3")
            input('press any key to continue')
        amount_users_repeater + 1

def exit(exiting):
    try:
        if exiting == '':
            clear()
            quit()
    except:
        clear()
        quit()


New_UserName = New_User()

User_Info = load_users()

User_Info.append(New_UserName)
save_users()

#early response code


   
get_catagories()



amount, Catagory_URL, difficulty_URL, Type_URL, amount_users = Get_Bounds()



data = NewQuestion(amount, Catagory_URL, difficulty_URL, Type_URL)
data = data['results']


Quiz_main(data, amount_users)



clear()
exiting = input('Press Any Key To Exit')
exit()




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

    with open('questions.json', 'w') as questions:
        json.dump(response, questions, indent = 4)
    
    with open('questions.json', 'w') as f:
        questions.write(json.dumps(f,response))

    with open('questions.json', 'w') as f:
        response = json.dump(response, f, indent=4, sort_keys=True)
        '''
