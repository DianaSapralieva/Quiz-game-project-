from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

list1=[]

for value in question_data:
    question=value["text"]
    answer=value["answer"]
    obj=Question(question,answer)
    list1.append(obj)

# print(list1[0].question)
# print(list1[0].answer)

obj= QuizBrain(list1)


while obj.still_has_questions():
    next_question = obj.next_question()

print("Final score:", obj.score, "/", len(obj.question_list))    
