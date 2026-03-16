# Decimal ↔ Binary Converter

**Project #9 of the 100 Python Live Projects Series**

**GitHub Repository:** [https://github.com/nishchup489-afk/decimal_binary_converter](https://github.com/nishchup489-afk/decimal_binary_converter)

**Live Preview:** [https://binary-decimal.onrender.com](https://binary-decimal.onrender.com)

---

# Project Overview

This project demonstrates how numbers are converted between the **Decimal (Base‑10)** and **Binary (Base‑2)** number systems using Python.

The project is implemented in two versions:

1. **CLI Version (sample.py)** — pure Python implementation of the conversion algorithms.
2. **Web Version** — a modern web application using **FastAPI + Jinja2 templates + TailwindCSS**.

The goal of this project is to understand the **fundamental algorithm computers use to represent numbers internally**.

All digital computers ultimately operate in **binary**, meaning every integer must eventually be represented using only:

```
0 and 1
```

---

# Stack Used

### Core Language

* Python 3

### Backend

* FastAPI

### Templating

* Jinja2

### Frontend

* HTML
* TailwindCSS

### Deployment

* Render

---

# Mathematical Background

Computers represent numbers using **Base‑2 (Binary)**.

Binary numbers follow positional notation similar to decimal numbers.

Example:

```
Binary: 1011
```

Expanded form:

```
1×2³ + 0×2² + 1×2¹ + 1×2⁰
```

Which equals:

```
8 + 0 + 2 + 1 = 11
```

So:

```
1011₂ = 11₁₀
```

---

# Decimal → Binary Algorithm

The algorithm used in the CLI version follows the classical **Division‑by‑2 method**.

Steps:

1. Divide the number by **2**.
2. Record the **remainder**.
3. Divide the quotient again by **2**.
4. Continue until the number becomes **0**.
5. Read the remainders **from bottom to top**.

Example:

Decimal → Binary

```
13 ÷ 2 = 6 remainder 1
6 ÷ 2 = 3 remainder 0
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1
```

Reading remainders bottom‑up:

```
1101
```

So:

```
13₁₀ = 1101₂
```

---

# Binary → Decimal Algorithm

To convert binary to decimal we use **powers of two**.

Each digit position represents:

```
2⁰, 2¹, 2², 2³ ...
```

Example:

```
Binary: 10101
```

Calculation:

```
1×2⁴ + 0×2³ + 1×2² + 0×2¹ + 1×2⁰
```

```
16 + 0 + 4 + 0 + 1 = 21
```

So:

```
10101₂ = 21₁₀
```

---

# CLI Version (sample.py)

The CLI implementation contains the core algorithms without any web framework.

## Decimal → Binary Function

```
def decimal_to_binary(number):

    binary_digits = []

    while number > 0:
        remainder = number % 2
        binary_digits.append(str(remainder))
        number //= 2

    binary_digits.reverse()

    return "".join(binary_digits)
```

### Explanation

```
number % 2
```

Finds the remainder when dividing by 2.

This remainder will always be **0 or 1**, which forms the binary digit.

```
binary_digits.append()
```

Stores each remainder in a list.

However, remainders are produced **in reverse order**, so we must reverse the list:

```
binary_digits.reverse()
```

Finally we combine digits into a string:

```
"".join(binary_digits)
```

---

## Binary → Decimal Function

```
def binary_to_decimal(binary_n):

    decimal = 0

    binary_n = binary_n[::-1]

    for i, bit in enumerate(binary_n):
        decimal += int(bit) * (2 ** i)

    return decimal
```

### Explanation

```
binary_n[::-1]
```

Reverses the binary string so the index aligns with powers of two.

Example:

```
1011
```

Becomes

```
1101
```

Now the index corresponds to:

```
i = 0 → 2⁰

i = 1 → 2¹

i = 2 → 2²
```

Then each bit contributes:

```
int(bit) * (2 ** i)
```

which accumulates into the decimal value.

---

# FastAPI Implementation

The web version exposes the algorithms through HTTP routes.

## Home Route

```
@app.get("/", response_class=HTMLResponse)
```

This renders the **main UI page** using Jinja2 templates.

```
return templates.TemplateResponse(
    "index.html",
    {"request": request}
)
```

FastAPI requires the request object to render templates.

---

## Decimal → Binary Route

```
@app.post("/dtb")
```

Receives a decimal number submitted from the form.

```
decimal: int = Form()
```

FastAPI automatically parses the form input.

The algorithm function is then executed:

```
result = decimal_to_binary(decimal)
```

Finally the result is returned to the template:

```
{"result": result}
```

---

## Binary → Decimal Route

```
@app.post("/btd")
```

This endpoint accepts a binary string.

The conversion function is called:

```
result = binary_to_decimal(binary)
```

The result is then rendered in the UI.

---

# UI Implementation

The frontend is intentionally minimal and focuses on usability.

Features:

* Two conversion modes
* Dynamic form switching
* Server‑side rendering
* TailwindCSS styling

The result returned from FastAPI is displayed using Jinja templating:

```
{% if result %}
Result: {{ result }}
{% endif %}
```

---

# What This Project Teaches

This project covers several fundamental computer science concepts:

• Binary number systems

• Base conversion algorithms

• Python control flow

• List manipulation

• FastAPI routing

• HTML form handling

• Template rendering with Jinja2

• Full stack deployment

---

# Try the Project

Live Demo

[https://binary-decimal.onrender.com](https://binary-decimal.onrender.com)

GitHub Repository

[https://github.com/nishchup489-afk/decimal_binary_converter](https://github.com/nishchup489-afk/decimal_binary_converter)

---

# Part of the 100 Python Projects Journey

This project is part of the **100 Python Live Projects challenge**, designed to build real‑world Python skills through consistent practice and public projects.

Each project focuses on a different concept ranging from algorithms to full stack development.

Stay tuned for the next project.
