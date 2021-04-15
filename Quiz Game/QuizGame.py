def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again... \nYour answer:- ")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is",answer)
    
score = 0
print("\nQuiz Game on Inventor\n")
guess1 = input("Question 1:- Who is the Inventor of Python?\nAnswer 1:- ")
check_guess(guess1, "Guido van Rossum")
guess2 = input("\nQuestion 2:- Who is the Inventor of JavaScript?\nAnswer 2:- ")
check_guess(guess2, "Brendan Eich")
guess3 = input("\nQuestion 3:- Who is the Inventor of C++?\nAnswer 3:- ")
check_guess(guess3, "Bjarne Stroustrup")
print("\nYour Score is "+ str(score))