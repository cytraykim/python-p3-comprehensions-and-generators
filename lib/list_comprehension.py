#!/usr/bin/env python3
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def return_evens(num_list):
    num_list = [num for num in num_list if num % 2 == 0]
    return num_list

sentence_list = ["Hello", "I'm doing great", "Python is fun"]
def make_exclamation(sentence_list):
    exclamation_list = [sentence + "!" for sentence in sentence_list]
    return exclamation_list