from data import question_data
from question_model import Question

list1=[]

for value in question_data:
    question=value["text"]
    answer=value["answer"]
    obj=Question(question,answer)
    list1.append(obj)

print(list1[0].answer)