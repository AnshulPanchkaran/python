
from Question import Question 
question_prompts = [
"what color are apple?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
"what color are bananas?\n(a) Teal\n(b) Magnite \n(c) Yellow\n\n",
"what color are apple?\n(a) Yellow \n(b) Red\n(c) Blue\n\n",
]
questions = [
  Question(question_prompts[0],"a"),
  Question(question_prompts[1],"c"),
  Question(question_prompts[2],"b"),
 ]

def run_test(questions):
   score = 0
   for question in questions:
      answer = input(question.prompt)
      if answer == question.answer:
         score += 1
   print("you got" + str(score) + "/" + str(len(questions))+ "corect")
run_test(questions)
 