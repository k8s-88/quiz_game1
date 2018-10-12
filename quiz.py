def show_menu():
    print("Quiz Game")
    print("---------")
    print()
    print("1. Run Quiz")
    print("2. Enter a Question")
    print("3. Exit")
    print()
    
    option = input("Enter option: ")
    return option
    
    
def ask_questions():
    with open("questions.txt") as f:
        questions = f.read().split("\n")[:-1]
        
    score = 0
    total = len(questions)
    
    for q in questions:
        question, answer = q.split('|')
        guess = input(question)
        
        
        
        #point of comparsisson:
        if guess.casefold() == answer.casefold():
            score += 1
        
    print("You scored {0} out of {1}".format(score, total))
        
        

def add_a_question():
    question = input("Enter a question: ")
    answer = input("Ok then tell me, " + question + ": ")
    
    with open("questions.txt", "a") as f:
        line = question + "|" + answer + "\n"
        f.write(line)
    


while True:
    option = show_menu()
    
    if option == "1":
        ask_questions()

    if option == "2":
        add_a_question()
    
    if option == "3":
       break