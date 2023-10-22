from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
def calculate(number_1: float = 0.0, number_2: float = 0.0, symbol: str = ''):
    result = None
    if symbol == '+':
        result = number_1+number_2
    if symbol == '-':
        result = number_1-number_2
    if symbol == '*':
        result = number_1*number_2
    if symbol == '/':
        if number_2 == 0:
            result = 'на ноль делить нельзя'
        else:
            result = number_1/number_2
    return {'answer': result}
