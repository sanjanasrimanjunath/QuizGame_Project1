print("****************************")
print("Welcome to the Quiz Game!!!!")

def show_guidelines():
    print("QUIZ GAME GUIDELINES")
    print("-------------------------")
    print("1. Each question has 4 options (A, B, C, D).")
    print("2. Only ONE option is correct.")
    print("3. Correct Answer = +4 marks.")
    print("4. Wrong Answer   = -1 mark.")
    print("5. No skipping allowed.")
    print("6. Final score will be shown at the end.\n")

choice = input("Do you want to continue? (yes/no): ").strip().lower()

if choice == "yes":
    print("\nGreat! Let's start the quiz 🎯\n")
    show_guidelines()
    
else:
    print("\n👋 Thanks for visiting! Exiting the game...")
    exit()


question_bank=[
    {
        "question": "Which data structure uses LIFO (Last In, First Out) ordering?",
        "options": ["Queue", "Stack", "Heap", "Graph"],
        "answer": "Stack"
    },
    {
        "question": "In SQL, which command is used to remove a table and its schema?",
        "options": ["DELETE TABLE", "DROP TABLE", "TRUNCATE TABLE", "REMOVE TABLE"],
        "answer": "DROP TABLE"
    },
    {
        "question": "Which of these algorithms is NOT a comparison-based sorting algorithm?",
        "options": ["Merge Sort", "Quick Sort", "Counting Sort", "Heap Sort"],
        "answer": "Counting Sort"
    },
    {
        "question": "Which HTTP status code means 'OK'?",
        "options": ["200", "201", "301", "404"],
        "answer": "200"
    },
    {
        "question": "In Python, what does the 'len' function return for a list?",
        "options": ["The last index", "The last value", "The number of elements", "The sum of elements"],
        "answer": "The number of elements"
    },
    {
        "question": "Which of the following is NOT a property of ACID in databases?",
        "options": ["Atomicity", "Consistency", "Isolation", "Scalability"],
        "answer": "Scalability"
    },
    {
        "question": "Which Python collection is unordered and contains unique elements?",
        "options": ["list", "tuple", "set", "dict"],
        "answer": "set"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Central Programming Unit", "Core Processing Utility", "Compute Power Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which of the following traversals is depth-first?",
        "options": ["BFS", "Level-order", "DFS", "Dijkstra"],
        "answer": "DFS"
    },
    {
        "question": "Git command to create a new branch and switch to it is:",
        "options": ["git checkout -b <name>", "git branch -m <name>", "git switch -c <name>", "git new <name>"],
        "answer": "git checkout -b <name>"
    }
]

# Show the first question
#enumerate gives both index and value
score = 0
for i, q in enumerate(question_bank, start=1):
    print(f"\nQ{i}. {q['question']}")
    for j, option in enumerate(q["options"], start=1):
        print(f"{j}. {option}")

    choice = int(input("Enter your choice (1-4): "))

    if q["options"][choice - 1] == q["answer"]:
        print("✅ Correct!")
        score += 4
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}.")
        score-=1

print("\n🎉 Quiz Finished!")
print(f"Your final score: {score}/{len(question_bank)}")
