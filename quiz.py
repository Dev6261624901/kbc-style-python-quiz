questions = [
    ["What is the correct file extension for Python files?", ".pt", ".python", ".py", ".pyt", 3],
    ["Which of the following is a valid variable name in Python?", "1variable", "my-variable", "my_variable", "my variable", 3],
    ["What data type is the result of: type(5.0)?", "int", "float", "str", "complex", 2],
    ["What will 'Hello'[1] return?", "H", "e", "l", "o", 2],
    ["What is the output of len([1, [2, 3], 4])?", "2", "3", "4", "5", 2],
    ["Which of these is NOT a valid dictionary key type?", "'string'", "42", "('a', 'b')", "['list']", 4],
    ["What does a function return if there is no return statement?", "0", "Undefined", "None", "Empty string", 3],
    ["Which of these is the correct syntax for a 'for' loop?", "for(i=0; i<10; i++)", "foreach i in range(10)", "for i in range(10):", "loop i in range(10)", 3],
    ["What keyword is used to handle exceptions?", "catch", "try", "handle", "except", 2],
    ["In a class method, what does 'self' refer to?", "A variable", "The class itself", "The object instance", "Nothing special", 3],
    ["What is a Python decorator used for?", "Error handling", "Looping", "Adding comments", "Modifying functions", 4],
    ["Which function can convert a string to a number?", "str()", "int()", "chr()", "ord()", 2],
    ["What will print(type([])) return?", "<class 'list'>", "<list>", "list()", "<type 'list'>", 1],
    ["What is the output of print(2 ** 3)?", "5", "6", "8", "9", 3],
    ["Which of the following is used to define a block of code in Python?", "Braces {}", "Brackets []", "Indentation", "Parentheses ()", 3],
]

prize = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,120000,130000,140000,150000,70000000]

i = 0
for question in questions:
    print(f"\nQuestion for ₹{prize[i]}:")
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    
    try:
        a = int(input("Enter your option (1 for a, 2 for b, 3 for c, 4 for d): "))
        if a == question[5]:
            print("Correct answer!")
            print(f"You won ₹{prize[i]}")
        else:
            print(f"Wrong answer. The correct answer was option {question[5]}")
            print("Better luck next time!")
            break
    except:
        print("Invalid input. Please enter a number between 1 and 4.")
        break

    i += 1
else:
    print("Congratulations! You have answered all questions correctly and won ₹70,000,000!")