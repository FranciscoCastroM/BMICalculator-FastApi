from typing import Optional
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return{
        "messsage": "Body mass index (BMI) is a value derived from the mass and height of a person.",
        "height": "In Meters.",
        "weight": "In kg",
        "underweight": "BMI less than 18.5",
        "normal": "BMI between 18.5 and 24.9",
        "overweight": "BMI between 25 and 29.9",
        "obese": "BMI over 30" 
}

@app.get("/api/bmicalculator/")
async def bmicalculator(height: float, weight: float, age: Optional[int] = None):
    if age is None:
        age = 0
    
    #BMI Formula, rounded to 4 decimals
    bmi = round(weight / (height**2), 4)

    #Categories (from Underweight to Obese):

    if bmi < 18.5:
        return JSONResponse(
            content={
                "result": "Underweight",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age
            },
            status_code=200)

    elif bmi >= 18.5 and bmi < 24.9:
        return JSONResponse(
            content={
                "result": "Normal weight",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age},
            status_code=200)

    elif bmi >= 25.0 and bmi < 29.9:
        return JSONResponse(
            content={
                "result": "Overweight",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age},
            status_code=200)

    elif bmi >= 30.0:
        return JSONResponse(
            content={
                "result": "Obese",
                "bmi": bmi,
                'height': height,
                'weight': weight,
                'age': age},
            status_code=200)
