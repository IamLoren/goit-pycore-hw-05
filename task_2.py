# -*- coding: utf-8 -*-
"""
Завдання 2: Генератор дійсних чисел та обчислення прибутку

Реалізація функції generator_numbers для ідентифікації дійсних чисел у тексті
та функції sum_profit для обчислення загальної суми.
"""

import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r'(?<= )\d+\.\d+(?= )|(?<= )\d+(?= )'
    
    matches = re.finditer(pattern, text)
    
    for match in matches:
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

