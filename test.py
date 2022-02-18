from search import find_naive, find_boyer
from random import randint

# function call for checking both algoritms on random strings
def test_random():
    end_text = ""
    end_string = ""
    for i in range(0,10):
        value  = str(randint(0,2))
        end_text = end_text + value
    for i in range(0,2):
        example  = str(randint(0,2))
        end_string = end_string + example
    print("TEXT:" + end_text)
    print("STRING:" + end_string)
    print("Naive    "+ str(find_naive(end_string,end_text)))
    print("BM    "+ str(find_boyer(end_string,end_text)))

#function to check algorithm 
def do_tests_for(function_name, function):
    print(function_name)
    print("text empty")
    text = ""
    string = "AISDI"
    print(function(string, text))

    print("string empty")
    text = "AISDI"
    string = ""
    print(function(string, text))

    print("both empty")
    text = ""
    string = ""
    print(function(string, text))

    print("string longer than text")
    text = "AISDI"
    string = "AlaMaKotaŁaciatego"
    print(function(string, text))

    print("string not in text")
    text = "AISDI"
    string = "SesjaTużTuż"
    print(function(string, text))

    print("text empty")
    text = ""
    string = "AISDI"
    print(function(string, text))

    print("string equal to text")
    text = "łżą"
    string = "łżą"
    print(function(string, text))
    print("################################################################################")


do_tests_for("Algorytm naiwny", find_naive)
do_tests_for("Algorytm Boyera-Moore’a", find_boyer)

test_random()
test_random()
test_random()
test_random()

