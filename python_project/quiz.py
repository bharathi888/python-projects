print("welcome to quiz game:")
player=input("if you want play with me[yes,no]?:")
if player.lower()!="yes":
    quit()
print("lets start the game:")
question=input("What is the capital of India?")
score=0
if question.lower()=="new delhi":
    print("correct answer")
    score+=1
else:
    print("incorrect answer")
question=input("Who is known as the Father of the Nation in India?")

if question.lower()=="mahatma gandhi":
    print("correct answer")
    score+=1
else:
    print("incorrect answer")
question=input("Which planet is known as the Red Planet?")

if question.lower()=="mars":
    print("correct answer")
    score+=1
else:
    print("incorrect answer")
question=input("What is the national animal of India?")

if question.lower()==" bengal tiger":
    print("correct answer")
    score+=1
else:
    print("incorrect answer")
question=input("Who invented the telephone?")

if question.lower()=="alexander graham bell":
    print("correct answer")
    score+=1
else:
    print("incorrect answer")
question=input("Which is the largest ocean in the world?")

if question.lower()==" pacific ocean":
    print("correct answer")
    score+=1
else:
    print("incorrect answer")
question=input("What is the currency of Japan?")

if question.lower()=="yen":
    print("correct answer")
    score+=1
else:
    print("incorrect answer")
question=input("Who wrote the national anthem of India?")
if question.lower()=="rabindranath tagore":
    print("correct answer")
    score+=1
else:
    print("incorrect answer")
question=input("Which gas do plants absorb from the atmosphere?")

if question.lower()==" carbon dioxide":
    print("correct answer")
    score+=1
else:
    print("incorrect answer")
    question=input("What is the tallest mountain in the world?")

if question.lower()==" mount everest":
    print("correct answer")
    score+=1
else:
    print("incorrect answer")
print("your score: "+ str(score))



