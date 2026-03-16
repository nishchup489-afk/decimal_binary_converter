from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app = FastAPI()



def decimal_to_binary(number: int):

    if number == 0:
        return "0"

    binary_digits = []

    while number > 0:
        remainder = number % 2
        binary_digits.append(str(remainder))
        number //= 2

    binary_digits.reverse()
    return "".join(binary_digits)


def binary_to_decimal(binary_n: str):

    if not all(bit in "01" for bit in binary_n):
        raise ValueError("Input must be binary (only 0 or 1).")

    decimal = 0
    binary_n = binary_n[::-1]

    for i, bit in enumerate(binary_n):
        decimal += int(bit) * (2 ** i)

    return decimal


# ---------- ROUTES ----------

@app.get("/", response_class=HTMLResponse)
def Home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/dtb", response_class=HTMLResponse)
def DtB(request: Request, decimal: int = Form()):
    
    result = decimal_to_binary(decimal)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result
        }
    )


@app.post("/btd", response_class=HTMLResponse)
def BtD(request: Request, binary: str = Form()):

    result = binary_to_decimal(binary)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result
        }
    )