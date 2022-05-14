def expertSystem():
    print("Welcome to Employee performance expert system.")

    questions=["Are you satisfiedwith your job","how likely are you to recommend this as a good workplace","Did you make professional connections here?","Were you treated fairly in the office?"]
    sum=0
    for i in questions:
        print(i,"\n")
        print("1. Not at all\t2. less likely\t3. Neutral\t4. Slightly\t5. Absoluitely\n")
        rating = int(input("Enter your choice: "))
        sum+=rating
    
    if sum<=((len(questions)*5)/4):
        print("Not at all satisfied")
    elif sum<=((len(questions)*5)/2):
        print("Not satisfied")
    elif sum<=((len(questions)*5)*3/4):
        print("Satisfied")
    elif sum<=((len(questions)*5)):
        print("More than Satisfied")


    print("Thank you.")


expertSystem()