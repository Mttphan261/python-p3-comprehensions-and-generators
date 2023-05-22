#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [int for int in num_list if int % 2 == 0]
    return even_list
    pass

def make_exclamation(sentence_list):
    exclamation_list = [f'{n}!' for n in sentence_list ]
    return exclamation_list
    pass