def show_menu():
    print("---------")
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
        
# below line explained:        
#f.read reads the file and returns a string. strings can be split, therefore, we can split this returned string. .split returns a list. you can add this onto lists -> [:].

        questions = f.read().split("\n")[:-1]
        
        score = 0
        
        
        for q in questions:
            question, answer = q.split('|')
            guess = input(question)
            print(guess)

            if guess == answer:
                score += 1
        
        print("you scored {0}".format(score))
    





        # another way to split the questions above:
        # for q in questions:
        #     x = q.split('|')
        #     print(x[0]) 
        #     print(x[1])

       
    



def add_a_question():
    question = input("Enter a question: ")
    answer = input("ok then tell me, " + question + ": ")
    
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
