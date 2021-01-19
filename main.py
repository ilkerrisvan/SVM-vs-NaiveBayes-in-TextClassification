import naivebayesian_question_based as nb_qb
import naivebayesian_answer_based as nb_ab
import svm_answer_based as svm_ab
import svm_question_based as svm_qb
import sys
import time

data_path = sys.argv[1]  ## location of texts
train_path = sys.argv[2]  ## location of texts
test_path = sys.argv[3]
svm_answer_based_path = sys.argv[4]
svm_question_based_path = sys.argv[5]

print("Use data.json, train_data.json, test_data.json for Naive Bayes\nUse svm_answer_based.json and test_data.json for SVM")

time.sleep(2)
method = int(input("(0) Question Based Naive Bayes\n(1) Answer Based Naive Bayes\n(2) Question Based SVM \n(3) Answer Based SVM\n(4) All\n")) #input from player
time.sleep(2)

if method == 0:
    nb_qb.run(data_path,train_path,test_path)
    sys.exit("Check the result,bye.")
if method == 1:
    nb_ab.run(data_path,train_path,test_path)
    sys.exit("Check the result,bye.")
if method == 2:
    svm_qb.run(svm_question_based_path,test_path)
    sys.exit("Check the result,bye.")
if method == 3:
    svm_ab.run(svm_answer_based_path, test_path)
    sys.exit("Check the result,bye.")
if method == 4:
    nb_qb.run(data_path, train_path, test_path)
    nb_ab.run(data_path, train_path, test_path)
    svm_qb.run(svm_question_based_path, test_path)
    svm_ab.run(svm_answer_based_path, test_path)
    sys.exit("Check the result,bye.")
else:
    sys.exit("There is no option about your input.")
