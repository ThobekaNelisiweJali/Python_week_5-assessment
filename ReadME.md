# Python OOP Assessments: Chocolate Showcase & Vehicle Polymorphism Challenge

This repository contains two Python assignments that demonstrate key object-oriented programming (OOP) principles:

1. **Chocolate Showcase (Assignment 1)**  
   Learn how to design your own class using chocolates as an example. This project explores encapsulation, inheritance, and method overriding. The base class, `Chocolate`, is extended to create brand-specific subclasses such as `LindtChocolate`, `CadburyChocolate`, and `GhirardelliChocolate`.

2. **Vehicle Polymorphism Challenge (Assignment 2)**  
   See how polymorphism works by creating a base class `Vehicle` with a method `move()`, then extending it with classes like `Car`, `Plane`, and `Boat`. Each subclass provides its own implementation of `move()`, demonstrating how the same method call results in different behaviors.

---

## Table of Contents

- [Overview](#overview)
- [Assignment 1: Chocolate Showcase](#assignment-1-chocolate-showcase)
  - [Concepts Covered](#concepts-covered)
  - [Classes and Features](#classes-and-features)
  - [Usage](#usage)
- [Assignment 2: Vehicle Polymorphism Challenge](#assignment-2-vehicle-polymorphism-challenge)
  - [Concepts Covered](#concepts-covered-1)
  - [Classes and Features](#classes-and-features-1)
  - [Usage](#usage-1)
- [Prerequisites](#prerequisites)
- [Running the Code](#running-the-code)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

This project is designed to help you understand and apply object-oriented programming concepts using two real-world examples. The **Chocolate Showcase** illustrates how to encapsulate data and extend classes with inheritance, while the **Vehicle Polymorphism Challenge** demonstrates how different objects can share a common interface yet behave differently.

---

## Assignment 1: Chocolate Showcase

### Concepts Covered

- **Encapsulation:**  
  Using private attributes (e.g., `__secret_ingredient`) to hide internal details and provide controlled access.
- **Inheritance and Method Overriding:**  
  Extending a base class (`Chocolate`) into brand-specific subclasses with extra attributes and tailored behaviors.

### Classes and Features

- **Chocolate (Base Class):**  
  - **Attributes:** `brand`, `cocoa_percentage`, `weight_grams`, and a private `__secret_ingredient`.  
  - **Methods:**  
    - `display_info()`: Prints chocolate details along with the secret ingredient via a getter method.
    - `get_secret_ingredient()`: Provides controlled access to the private attribute.

- **Subclasses:**  
  - **LindtChocolate:** Adds a `flavor` attribute and overrides `display_info()` to print flavor details.
  - **CadburyChocolate:** Adds a `country_origin` attribute and overrides `display_info()` to show the country of origin.
  - **GhirardelliChocolate:** Adds a `bar_style` attribute and overrides `display_info()` for style-specific information.

### Usage

When you run the chocolate example (e.g., `chocolate_demo.py`), it creates instances of the different chocolate brands and displays their details on the console.

---

## Assignment 2: Vehicle Polymorphism Challenge

### Concepts Covered

- **Polymorphism:**  
  Demonstrates how the same method (`move()`) is implemented differently across various classes.
- **Method Overriding:**  
  Each subclass of `Vehicle` defines its own version of `move()`.

### Classes and Features

- **Vehicle (Base Class):**  
  - Contains a method `move()` that raises a `NotImplementedError` to enforce implementation in subclasses.

- **Subclasses:**  
  - **Car:** Implements `move()` to print `"Driving 🚗"`.
  - **Plane:** Implements `move()` to print `"Flying ✈️"`.
  - **Boat:** Implements `move()` to print `"Sailing ⛵"`.

### Usage

When you run the vehicle example (e.g., `vehicle_polymorphism.py`), it will create a list of vehicles and iterate over them, invoking their `move()` methods. Each vehicle will print an action corresponding to its type.

---

## Prerequisites

- **Python 3.x**: Ensure Python 3 is installed.
- Basic understanding of object-oriented concepts is helpful.

---

## Running the Code

There are two ways to run the assignments:

### Option 1: Combined File
If both assignments are in one file (e.g., `main.py`), simply run:
```bash
python main.py


Option 2: Separate Files

Alternatively, you can keep them separate:

chocolate_demo.py for the Chocolate Showcase.

vehicle_polymorphism.py for the Vehicle Polymorphism Challenge.

Run each file separately:

python chocolate_demo.py
python vehicle_polymorphism.py

Project Structure

python-oop-assessments/
├── chocolate_demo.py         # Python script for the Chocolate Showcase (Assignment 1)
├── vehicle_polymorphism.py   # Python script for the Vehicle Polymorphism Challenge (Assignment 2)
├── README.md                 # This README file
└── (Optional: LICENSE file)

Contact

For more information or inquiries, please contact thobekaj63@gmail.com.

Enjoy Coding and Stay Blessed Mate !!!


