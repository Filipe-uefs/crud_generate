# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 18:55:47 2022

@author: filipepds
"""
from model.Entity import Entity
from typing import List


class Generator:
    def __init__(self, entities: List[Entity] = []):
        self.entities = entities

    def create_file(self, name_file: str, content_file: str):
        print("Arquivo test.py foi criado")
        with open(f'{name_file}.py', 'w') as file:
            file.write(content_file)

    def run(self):
        print("In run")
