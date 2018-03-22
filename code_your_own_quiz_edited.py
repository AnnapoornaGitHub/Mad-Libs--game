def scoring_details(correct_answer,incorrect_answer):
    '''Calulates 5 marks for each correct answer and displays number of correct and incorrect answers
    input keywords:
    correct_answer -- count of correct answers
    incorrect_answer -- count of incorrect answers
    output keywords:
    score -- score value
    '''
    print "Correct Answers: "+str(correct_answer)
    print "Incorrect Answers: "+str(incorrect_answer)
    score=int(correct_answer)*5
    return "Your Score is: "+str(score)

def qn_ans(option,attempt):
    '''Displays the questions according to the level chosen by the user.
    input keywords:
    option  -- levels(easy, medium,hard)
    attempt -- number of retry attempts
    output keywords:
    Goes to appropriate level
    attempt                -- retry attempts
    easy_qn & easy_ans     -- Display the questions and compare with the answer when level is easy
    medium_qn & medium_ans -- Display the questions and compare with the answer when level is medium
    hard_qn & hard_ans     -- Display the questions and compare with the answer when level is hard
    '''
    easy_qn=["___ is the capital of INDIA","Rose is a ___","I am ___ intelligent person","There are ___ continents in the world"]
    easy_ans=["DELHI","FLOWER","AN","SEVEN"]
    medium_qn=["___ is the King of the Forest","Peacock is the national ___ of India","Old id ___","Rain ___ go away","United States ___ America"]
    medium_ans=["LION","BIRD","GOLD","RAIN","OF"]
    hard_qn=["10 rupees contain ___ 1 rupee","IT is Information ___","Time and ___ wait for none","___ is a night bird"]
    hard_ans=["TEN","TECHNOLOGY","TIDE","OWL"]
    if option==1:
        return level(attempt,easy_qn,easy_ans)
    elif option==2:
        return level(attempt,medium_qn,medium_ans)
    elif option==3:
        return level(attempt,hard_qn,hard_ans)

def validate_answer(itr,usr_attempt,answ,qn,ans):
    '''If the answer is correct, it will replace the dash with correct answer from the question and prompt the next question
    input keywords:
    itr         -- iterator
    usr_attempt -- checks before prompting next question
    answ        -- count of correct/incorrect answers
    qn          -- current question according to iterator
    ans         -- appropriate answer
    output keywords:
    answ -- count of correct/incorrect answers
    attempt -- reset to user attempt for next question
    '''
    print qn[itr].replace("___",ans[itr])
    answ+=1
    attempt=usr_attempt    
    return (answ,attempt)

def level(attempt,qn,ans):
    '''Make the user play in the selected level with their chosen retry attempts
    input keywords:
    attempt -- retry attempts
    qn      -- questions according to levels (easy,medium,hard)
    ans     -- answers according to levels.
    output keywords:
    checks the answer in the validate_answer function and return the count of correct and incorrect answers
    itr             -- iterator variable
    usr_attempt     -- temp var to store attempts
    correct_answer  -- count of correct_answer
    qn              -- question
    ans             -- corresponding answer
    initiates scoring_details function to display scoring details
    correct_answer   -- count of correct answer
    incorrect_answer -- count of incorrect answer
    '''
    itr=initial_attempt=correct_answer=incorrect_answer=score=answ=0
    usr_attempt = attempt
    while itr<len(qn):    
        answer=raw_input(qn[itr]+"\n")
        if answer==ans[itr]:
            correct_answer,attempt,=validate_answer(itr,usr_attempt,correct_answer,qn,ans)            
            itr+=1
        else:
            if initial_attempt<attempt:
                print "Your answer is Incorrect.you can try "+str(attempt)+" times."
                attempt-=1
            else:
                print "You have crossed your retry attempts."
                incorrect_answer,attempt,=validate_answer(itr,usr_attempt,incorrect_answer,qn,ans)                
                itr+=1
    print "You have finished this level."
    print scoring_details(correct_answer,incorrect_answer)
    

print "Enter the answers in capital letters."
print "Scoring Details"
print "Correct ans=5Marks, Incorrect ans=0Marks"
attempt=int(raw_input("Enter the number of times you want to retry."))
#User can choose their retry attempts

while True:
    #checks the option that user opts is within the given levels.
    
    try:
        print "Choose the difficulty level"
        print "1.Easy 2.Medium 3.Hard"
        level_option=[1,2,3]
        option=int(raw_input("Enter the number:"))
    except ValueError:
        print "Enter only number"
        continue
    if option<level_option[0] or option>len(level_option):
        print "Enter the valid number(1 or 2 or 3)"
        continue
    else:
        break
if option in level_option:
    qn_ans(option,attempt)







