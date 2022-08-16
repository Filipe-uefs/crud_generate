# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:22:56 2022

@author: Usuario
"""

from model.Column import Column
from typing import List


class Entity:
    def __init__(self, name: str = "entity", columns: List[Column] = []):

        self.name = name
        self.columns = columns

    def add_column(self, column: Column):

        print(f"Column {column.name} was add in {self.name}")
        if self.columns:
            self.column.append(column)
            return

        self.column = [column]
