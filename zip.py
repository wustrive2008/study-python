#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 zip的使用
'''

actions = ['Up','Left','Down','Right','Restart','Exit']

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

print(zip(letter_codes, actions * 2))

actions_dict = dict(zip(letter_codes, actions * 2))

print(actions_dict)

#输出：
#[(87, 'Up'), (65, 'Left'), (83, 'Down'), (68, 'Right'), (82, 'Restart'), (81, 'Exit'), (119, 'Up'), (97, 'Left'), (115, 'Down'), (100, 'Right'), (114, 'Restart'), (113, 'Exit')]
#{65: 'Left', 115: 'Down', 68: 'Right', 97: 'Left', 119: 'Up', 114: 'Restart', 81: 'Exit', 82: 'Restart', 83: 'Down', 113: 'Exit', 87: 'Up', 100: 'Right'}
