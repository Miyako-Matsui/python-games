def quiz():
  questions = [
      {"question": "What is the capital of France?", "answer": "Paris"},
      {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},

      ]

  score = 0 
  for question in questions:
    print(question["question"])
    answer = input("what is your answer : ").lower() 
    if answer == question["answer"].lower():
      score += 1 
      print("correct :) ") 
      
      
    else:
      print("wrong :( " )
  print ("Your score is " + str(score))

quiz()