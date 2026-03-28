import streamlit as st

st.title("OOP (Object-Orianted Programming) learning guide")

st.set_page_config(layout="centered")

st.markdown("""<style>
body {background-color: #0b0f19;}
.chapter-label {color: #facc15; letter-spacing: 3px; font-weight: 700; font-size: 13px;}
.chapter-title {font-size: 46px; font-weight: 800; margin-bottom: 5px;}
.chapter-subtitle {color: #94a3b8; font-style: italic; font-size: 18px; margin-bottom: 30px;}
.section-title {color: #60a5fa; font-size: 26px; margin-top: 35px; margin-bottom: 10px;}
.tip-box {background-color: #0f2a24; border-left: 4px solid #34d399; padding: 15px; border-radius: 6px; margin-top: 20px;}
</style>""", unsafe_allow_html=True)


if "chapter" not in st.session_state:
    st.session_state.chapter = 1
    st.session_state.answered = False
if "correct" not in st.session_state:
    st.session_state.correct = False
if "selected" not in st.session_state:
    st.session_state.selected = None

def chapter(number, title, subtitle):
    st.markdown(f"""<div class="chapter-label">CHAPTER {number}</div> <div class="chapter-title">{title}</div> <div class="chapter-subtitle">{subtitle}</div> """, unsafe_allow_html=True)

if st.session_state.chapter == 1:
    chapter(
        1,
        "What is OOP?",
        "The big idea behind Object-Oriented Programming")

    st.markdown("""
                Imagine you're building a game. You need to track 50 different characters, each with a name, health,
                and attack power. Without OOP, you'd write **hundreds of variables** and functions tangled together.

                OOP lets you describe a *template* for a character once, then create as many as you want.

                OOP is a way of structuring your code around **objects** — bundles that hold both *data* (attributes)
                and *behaviour* (methods) in one place.""")

    st.markdown('<div class="section-title">The 4 Pillars of OOP</div>', unsafe_allow_html=True)

    st.markdown("""
                - **Encapsulation** — bundling data and methods, hiding internal details  
                - **Inheritance** — a class can inherit features from another class  
                - **Polymorphism** — different objects can respond to the same method differently  
                - **Abstraction** — hiding complexity, showing only what's necessary""")

    st.markdown("""<div class="tip-box">
                💡 You don't need to memorise these now. By the end of this course you'll understand them through hands-on examples.
                </div>""", unsafe_allow_html=True)

    st.markdown("")

    code1 = """
    # Even a number is an object!
    x = 42
    print(type(x))       # <class 'int'>
    print(x.bit_length()) # 6  — a method on an int!"""

    st.code(code1, language="python")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**What is an object in OOP?**")

    options = [
        "Only a variable that stores numbers",
        "A bundle of data (attributes) and behaviour (methods)",
        "A type of loop in Python",
        "A file on your computer"]

    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch1{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Exactly! An object combines both data and behaviour in one unit.")
            if st.button("Next", key="ch1_next"):
                st.session_state.chapter = 2
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 2:
    chapter(2,
    "Classes & Objects",
    "Blueprint vs. the thing itself")

    st.markdown("""A class is the blueprint. An object is what you build from it. Think of a class as a cookie cutter, and objects as the cookies.""")

    code2 = """
    class Dog:
    pass  # empty class for now

    # Creating objects (instances)
    my_dog = Dog()
    your_dog = Dog()

    print(type(my_dog))  # <class '__main__.Dog'>"""

    st.code(code2, language="python")

    st.markdown(" Each object is **independent**. Changing one doesn't affect the other.")

    st.markdown("""<div class="section-title">The __init__ method</div>""", unsafe_allow_html=True)

    st.markdown(" __init__ is a special method called automatically when you create an object. It's where you set up initial attributes.")

    code3 = """
    class Dog:
        def __init__(self, name, breed):
            self.name = name     # instance attribute
            self.breed = breed

    buddy = Dog("Buddy", "Labrador")
    rex   = Dog("Rex",   "German Shepherd")

    print(buddy.name)   # Buddy
    print(rex.breed)    # German Shepherd"""

    st.code(code3, language="python")

    st.markdown("""<div class="tip-box">
                💡 What is self? It's a reference to the specific object being created or used. When you call buddy.name, Python automatically passes buddy as self behind the scenes. You must always put self as the first parameter in any instance method. </div>""", unsafe_allow_html=True)

    st.markdown("### 🧠 Quick Check")
    st.markdown("**What does __init__ do??**")

    options = [
        "It deletes an object from memory",
        "It's called automatically when creating an object, to set up its initial state",
        "It's a required function you must call manually before using a class",
        "It defines the class name"]

    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch2{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct! __init__ is the initialiser — Python calls it for you when you do Dog().")
            if st.button("Next", key="ch2_next"):
                st.session_state.chapter = 3
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again..")

if st.session_state.chapter == 3:
    chapter(3,
            "Methods",
            "Giving your objects behaviour")
    
    st.markdown("Methods are just functions defined inside a class. They give your objects things they can do.")

    code4 = """
    class Dog:
        def __init__(self, name, breed):
            self.name  = name
            self.breed = breed
            self.tricks = []

        def bark(self):
            print(f"{self.name} says: Woof!")

        def learn_trick(self, trick):
            self.tricks.append(trick)
            print(f"{self.name} learned {trick}!")

        def show_tricks(self):
            if self.tricks:
                print(f"{self.name} can: {', '.join(self.tricks)}")
            else:
                print(f"{self.name} knows no tricks yet.")

    buddy = Dog("Buddy", "Labrador")
    buddy.bark()                 # Buddy says: Woof!
    buddy.learn_trick("sit")    # Buddy learned sit!
    buddy.learn_trick("roll over")
    buddy.show_tricks()          # Buddy can: sit, roll over"""

    st.code(code4, language="python")

    st.markdown("""<div class="section-title">Instance vs Class attributes</div>""", unsafe_allow_html=True)

    code5 = """
    class Dog:
        species = "Canis lupus familiaris"  # class attribute — shared by ALL dogs

        def __init__(self, name):
            self.name = name  # instance attribute — unique to each dog

    buddy = Dog("Buddy")
    rex   = Dog("Rex")

    print(buddy.species)   # Canis lupus familiaris
    print(rex.species)     # Canis lupus familiaris (same)
    print(buddy.name)      # Buddy
    print(rex.name)        # Rex (different)"""

    st.code(code5, language="python")

    st.markdown("""<div class="tip-box">
                💡  Class attributes are like facts about the type. Instance attributes are facts about a specific individual. </div>""", unsafe_allow_html=True)
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**If two Dog objects share a class attribute species, what happens if you change species on one instance?**")

    options = [
        "It changes for all Dog objects globally",
        "It creates a new instance attribute on that object only, shadowing the class attribute",
        "It raises an error",
        "It changes the class attribute permanently"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch3{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct! Right! Setting an attribute on an instance creates a new instance-level attribute that shadows the class one — only that object is affected.")
            if st.button("Next", key="ch3_next"):
                st.session_state.chapter = 4
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 4:
    chapter(4,
        "Encapsulation",
        "Keeping internals private — the first pillar")
    
    st.markdown("Encapsulation means hiding the internal details of an object and only exposing what's needed. It protects your data from accidental misuse.")
    
    st.markdown("""<div class="section-title">In Python, we use naming conventions to signal privacy:</div>""", unsafe_allow_html=True)
    
    st.markdown("""
                ***name*** — public, anyone can access it\n
                ***_name*** — "protected" by convention (a hint to developers)\n
                ***__name*** — "private" — Python name-mangles it to make it harder to access from outside""")
    
    code6 = """
    class BankAccount:
        def __init__(self, owner, balance):
            self.owner = owner
            self.__balance = balance  # private!

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount

        def withdraw(self, amount):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient funds!")

        def get_balance(self):  # controlled access
            return self.__balance

    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    print(acc.get_balance())  # 1500

    # acc.__balance  ← This would raise AttributeError!"""

    st.code(code6, language="python")

    st.markdown("""<div class="section-title">Properties — the Pythonic way</div>""", unsafe_allow_html=True)

    st.markdown("Python's @property decorator lets you use *method calls that look like attribute access*. This is the clean, Pythonic approach to getters/setters.")

    code7 = """
    class Circle:
        def __init__(self, radius):
            self.__radius = radius

        @property
        def radius(self):
             self.__radius

        @radius.setter
        def radius(self, value):
            if value < 0:
                raise ValueError("Radius can't be negative")
            self.__radius = value

    c = Circle(5)
    print(c.radius)   # 5  — looks like attribute access!
    c.radius = 10     # setter is called automatically"""

    st.code(code6, language="python")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**What is the purpose of encapsulation?**")

    options = [
        "To make code run faster",
        "To hide internal implementation details and control access to data",
        "To allow one class to use another class's methods",
        "To create multiple objects from one class"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch4{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Exactly! Encapsulation protects data and controls how it's accessed or modified.")
            if st.button("Next", key="ch4_next"):
                st.session_state.chapter = 5
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 5:
    chapter(5, 
        "Inheritance",
        "Building on what already exists — the second pillar")
    
    st.markdown("Inheritance lets a class **reuse and extend** the attributes and methods of another class. The parent is called the ***base class*** or ***superclass***; the child is the ***subclass***.")

    code8 = """
    class Animal:  # Base class
        def __init__(self, name, sound):
            self.name  = name
            self.sound = sound

        def speak(self):
            print(f"{self.name} says {self.sound}")

    class Dog(Animal):  # Inherits from Animal
        def __init__(self, name):
            super().__init__(name, "Woof")  # call parent's __init__
            self.tricks = []

        def fetch(self):
            print(f"{self.name} fetches the ball!")

    class Cat(Animal):
        def __init__(self, name):
            super().__init__(name, "Meow")

    buddy = Dog("Buddy")
    whiskers = Cat("Whiskers")

    buddy.speak()     # Buddy says Woof  (inherited!)
    whiskers.speak()  # Whiskers says Meow
    buddy.fetch()     # Buddy fetches the ball!"""

    st.code(code8, language="python")

    st.markdown("""<div class="tip-box">
                💡 super() gives you access to the parent class. Use it to call the parent's __init__ or any other method you want to extend rather than replace. </div>""", unsafe_allow_html=True)
    
    st.markdown("""<div class="section-title">isinstance() — checking the family tree</div>""", unsafe_allow_html=True)

    code9 = """
        print(isinstance(buddy, Dog))     # True
        print(isinstance(buddy, Animal))  # True — Dog IS-A Animal
        print(isinstance(buddy, Cat))     # False"""
    
    st.code(code9, language="python")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**What does super().__init__(...) do?**")

    options = [
        "Creates a new parent class",
        "Calls the parent class's __init__ so you don't have to duplicate that setup code",
        "Deletes the parent class",
        "Makes the class abstract"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch5{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct! super() lets you delegate to the parent, so you build on top of it rather than rewriting everything.")
            if st.button("Next", key="ch5_next"):
                st.session_state.chapter = 6
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 6:
    chapter(6,
        "Polymorphism",
        "Same interface, different behaviour — the third pillar")
    
    st.markdown("Polymorphism means 'many forms'. In OOP, it means you can call the ***same method name*** on different objects and each responds in its own way.")

    code10 = """
    class Shape:
        def area(self):
            raise NotImplementedError

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        def area(self):
            return 3.14159 * self.radius ** 2

    class Rectangle(Shape):
        def __init__(self, w, h):
            self.w, self.h = w, h
        def area(self):
            return self.w * self.h

    class Triangle(Shape):
        def __init__(self, base, height):
            self.base, self.height = base, height
        def area(self):
            return 0.5 * self.base * self.height

    # Polymorphism in action!
    shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
    for shape in shapes:
        print(f"{type(shape).__name__}: area = {shape.area():.2f}")
    # Circle: area = 78.54
    # Rectangle: area = 24.00
    # Triangle: area = 12.00"""

    st.code(code10, language="python")

    st.markdown("The loop doesn't care **which** shape it has — it just calls .area() and each object handles it correctly. This is the power of polymorphism.")

    st.markdown("""<div class="tip-box">
                💡 This is also called "method overriding" — the child class overrides the parent's version of a method. </div>""", unsafe_allow_html=True)
    
    st.markdown("""<div class="section-title">Duck Typing</div>""", unsafe_allow_html=True)

    st.markdown("Python doesn't require a shared parent class for polymorphism. If it walks like a duck and quacks like a duck, it's a duck. As long as an object has the right method, Python is happy.")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**Which best describes polymorphism?**")

    options = [
        "When one class inherits from multiple parents",
        "When many objects can respond to the same method name, each in their own way",
        "When a class has many attributes",
        "When you hide data with double underscores"]
    
    correct_answer = options[1]
    
    for option in options:
        if st.button(option, use_container_width=True, key=f"ch6{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Spot on! Polymorphism == same interface, different implementations.")
            if st.button("Next", key="ch6_next"):
                st.session_state.chapter = 7
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")
    
if st.session_state.chapter == 7:
    chapter(7,
        "Abstraction",
        "Hiding complexity — the fourth pillar")
    
    st.markdown("""Abstraction means exposing ***only what's necessary*** and hiding the implementation details. You use something without needing to know how it works inside.
                Python provides Abstract Base Classes (ABCs) via the abc module to enforce that subclasses implement certain methods.""")
    
    code11 = """
    from abc import ABC, abstractmethod

    class Vehicle(ABC):  # Abstract class — can't be instantiated
        def __init__(self, make, model):
            self.make  = make
            self.model = model

        @abstractmethod
        def start_engine(self):  # Subclasses MUST implement this
            pass

        def info(self):           # Concrete method — shared by all
            print(f"{self.make} {self.model}")

    class Car(Vehicle):
        def start_engine(self):
            print("Car engine: Vroom!")

    class ElectricCar(Vehicle):
        def start_engine(self):
            print("Electric motor: Whirr...")

    # Vehicle()  ← TypeError! Can't instantiate abstract class
    my_car = Car("Toyota", "Corolla")
    my_car.info()          # Toyota Corolla
    my_car.start_engine()  # Car engine: Vroom!"""

    st.code(code11, language="python")

    st.markdown("""Abstraction is about designing ***interfaces***. You say "all Vehicles must have a start_engine method" without specifying how each one does it.""")

    st.markdown("""<div class="tip-box">
                ⚠️ If a subclass doesn't implement ALL abstract methods, Python will raise a TypeError when you try to create an object from it. This enforces the "contract". </div>""", unsafe_allow_html=True)
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**What happens if you try to create an instance of an Abstract Base Class directly?**")

    options = [
        "It creates an empty object with no attributes",
        "Python raises a TypeError",
        "It works fine — abstract is just a label",
        "It raises an ImportError"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch7{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct! ABCs can't be instantiated. They're templates that force subclasses to implement certain methods.")
            if st.button("Next", key="ch7_next"):
                st.session_state.chapter = 8
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 8:
    chapter(8,
        "Dunder Methods",
        "Magic methods that make your objects feel native")
    
    st.markdown("Dunder (double-underscore) methods let your objects work with Python's built-in syntax — +, len(), print(), comparison operators, and more.")

    code12 = """
    class Vector:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __repr__(self):              # for developers / print()
            return f"Vector({self.x}, {self.y})"

        def __str__(self):               # for end users / str()
            return f"({self.x}, {self.y})"

        def __add__(self, other):        # v1 + v2
            return Vector(self.x + other.x, self.y + other.y)

        def __len__(self):               # len(v)
            return int((self.x**2 + self.y**2) ** 0.5)

        def __eq__(self, other):          # v1 == v2
            return self.x == other.x and self.y == other.y

    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(v1)          # (3, 4)          — uses __str__
    print(v1 + v2)     # (4, 6)          — uses __add__
    print(len(v1))      # 5               — uses __len__
    print(v1 == v2)    # False           — uses __eq__"""

    st.code(code12, language="python")

    st.markdown("""<div class="section-title">Common dunder methods</div>""", unsafe_allow_html=True)

    code13 = """
    # Representation
    __repr__   # repr(obj), used in REPL
    __str__    # str(obj), print(obj)

    # Math operators
    __add__    # obj + other
    __sub__    # obj - other
    __mul__    # obj * other

    # Comparisons
    __eq__     # obj == other
    __lt__     # obj < other

    # Container protocol
    __len__    # len(obj)
    __getitem__ # obj[key]
    __contains__ # x in obj

    # Context managers
    __enter__, __exit__  # with obj as x:"""

    st.code(code13, language="python")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**Which dunder method lets you use + between two of your objects?**")

    options = [
        "__plus__",
        "__add__",
        "__sum__",
        "__combine__"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch8{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Correct! __add__ is called when Python evaluates obj1 + obj2.")
            if st.button("Next", key="ch8_next"):
                st.session_state.chapter = 9
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 9:
    chapter(9,
        "Composition",
        "Building complex objects from simpler ones",)
    
    st.markdown("""Inheritance says "is-a". Composition says "has-a". Instead of inheriting behaviour, you ***include other objects as attributes***. This is often more flexible.""")

    st.markdown("""<div class="tip-box">
                💡Rule of thumb: prefer composition over inheritance when the relationship isn't a clear "is-a" type.""", unsafe_allow_html=True)
    
    st.markdown("")

    code14 = """
    class Engine:
        def __init__(self, horsepower):
            self.horsepower = horsepower
        def start(self):
            print(f"Engine ({self.horsepower}hp) started")

    class GPS:
        def navigate(self, destination):
            print(f"Navigating to {destination}")

    class Car:
        def __init__(self, make):
            self.make   = make
            self.engine = Engine(300)  # Car HAS-A Engine
            self.gps    = GPS()         # Car HAS-A GPS

        def drive(self, destination):
            self.engine.start()
            self.gps.navigate(destination)

    my_car = Car("BMW")
    my_car.drive("Berlin")
    # Engine (300hp) started
    # Navigating to Berlin"""

    st.code(code14, language="python")

    st.markdown("Now Engine and GPS can be reused in other classes (Boat, Plane...) without duplicating code, and without forcing an awkward inheritance hierarchy.")

    st.markdown("""<div class="section-title">Inheritance vs Composition</div>""", unsafe_allow_html=True)

    code15 = """
    # Use Inheritance when:  "A Dog IS-A Animal"
    class Dog(Animal): ...

    # Use Composition when: "A Car HAS-A Engine"
    class Car:
        engine = Engine()"""
    
    st.code(code15, language="python")

    st.markdown("### 🧠 Quick Check")
    st.markdown("**When should you prefer composition over inheritance?**")

    options = [
        "Always — inheritance is never useful",
        "When the relationship is 'has-a' rather than 'is-a'",
        "When you need to override methods",
        "When using abstract classes"]
    
    correct_answer = options[1]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch9{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Right! 'has-a' relationships are best modelled with composition. It's also easier to swap out components later.")
            if st.button("Next", key="ch9_next"):
                st.session_state.chapter = 10
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 10:
    chapter(10,
        "Putting It All Together",
        "A complete OOP project example")
    
    st.markdown("Let's build a small RPG system that uses every concept we've learned.")

    code16 = """
    from abc import ABC, abstractmethod
    import random

    # Abstraction — defines the contract
    class Character(ABC):
        def __init__(self, name, hp):
            self.name  = name
            self.__hp  = hp     # Encapsulation
            self.max_hp = hp

        @property
        def hp(self): return self.__hp

        def take_damage(self, dmg):
            self.__hp = max(0, self.__hp - dmg)
            print(f"  {self.name} takes {dmg} dmg → {self.__hp}/{self.max_hp} HP")

        @abstractmethod
        def attack(self, target): pass

        def is_alive(self): return self.__hp > 0

        def __repr__(self):  # Dunder method
            return f"{self.name} ({self.hp}/{self.max_hp} HP)"

    # Composition — Warrior has a Weapon
    class Weapon:
        def __init__(self, name, dmg):
            self.name, self.dmg = name, dmg

    # Inheritance — Warrior IS-A Character
    class Warrior(Character):
        def __init__(self, name):
            super().__init__(name, hp=100)
            self.weapon = Weapon("Sword", 25)

        def attack(self, target):  # Polymorphism
            dmg = random.randint(15, self.weapon.dmg)
            print(f"{self.name} swings {self.weapon.name}!")
            target.take_damage(dmg)

    class Mage(Character):
        def __init__(self, name):
            super().__init__(name, hp=70)
            self.mana = 100

        def attack(self, target):  # Polymorphism
            dmg = random.randint(20, 40)
            print(f"{self.name} casts Fireball!")
            target.take_damage(dmg)

    # Battle!
    hero    = Warrior("Arthur")
    villain = Mage("Morgana")
    print(hero, "vs", villain)

    while hero.is_alive() and villain.is_alive():
        hero.attack(villain)
        if villain.is_alive():
            villain.attack(hero)"""
    
    st.code(code16, language="python")

    st.markdown("""<div class="tip-box">
                🎉 You've reached the end! Try extending this: add a Healer class, a Shield item, or an experience/level system. That's where real learning happens. 🎉""", unsafe_allow_html=True)
    
    st.markdown("""<div class="section-title">What you've learned</div>""", unsafe_allow_html=True)

    st.markdown("""
                ***Classes & Objects*** — blueprints and instances\n
                ***__init__ & self*** — setting up state\n
                ***Methods*** — behaviour on objects\n
                ***Encapsulation*** — private attributes, properties\n
                ***Inheritance*** — reusing and extending with super()\n
                ***Polymorphism*** — same interface, different behaviour\n
                ***Abstraction*** — ABCs and enforced contracts\n
                ***Dunder methods*** — making objects feel native\n
                ***Composition*** — has-a vs is-a""")
    
    st.markdown("### 🧠 Quick Check")
    st.markdown("**In the RPG example, the Warrior 'has-a' Weapon and 'is-a' Character. Which pattern is each?**")

    options = [
        "Both are inheritance",
        "Weapon = inheritance, Character = composition",
        "Weapon = composition, Character = inheritance",
        "Both are composition"]
    
    correct_answer = options[2]

    for option in options:
        if st.button(option, use_container_width=True, key=f"ch10{option}"):
            st.session_state.selected = option
            st.session_state.answered = True
            if option == correct_answer:
                st.session_state.correct = True
            else:
                st.session_state.correct = False
    if st.session_state.answered:
        if st.session_state.correct:
            st.success("✅ Exactly! Warrior IS-A Character (inheritance) and Warrior HAS-A Weapon (composition). You combined both patterns.")
            if st.button("Next", key="ch10_next"):
                st.session_state.chapter = 11
                st.session_state.answered = False
                st.session_state.correct = False
                st.session_state.selected = None
        else:
            st.error("❌ Not quite right! Try again.")

if st.session_state.chapter == 11:
    chapter(
        11,
        "Congratulations!",
        "You have finished this Python OOP mini interactive course. Now it is your turn.")
    
    st.markdown("Try to make something *yours* using everything that you have learned so far.")

    st.markdown("""<div class="tip-box">
                🎉I am going to show you a game i made so you can play but try to do something similar or different to show off your skills.""", unsafe_allow_html=True)
    
    st.markdown("""<div class="section-title">Python mini game</div>""", unsafe_allow_html=True)

    code17 = """
    import pygame
    import random
    import sys

    pygame.init()

    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dodge the Enemies")

    clock = pygame.time.Clock()

    class Player:
        def __init__(self):
            self.rect = pygame.Rect(300, 500, 50, 50)
            self.speed = 6
            self.color = (0, 255, 0)

        def move(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.rect.x > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - 50:
                self.rect.x += self.speed

        def draw(self):
            pygame.draw.rect(screen, self.color, self.rect)

    # ---------------- ENEMY ----------------
    class Enemy:
        def __init__(self):
            x = random.randint(0, WIDTH - 40)
            self.rect = pygame.Rect(x, 0, 40, 40)
            self.speed = random.randint(3, 7)
            self.color = (255, 0, 0)

        def move(self):
            .rect.y += self.speed

        def draw(self):
            pygame.draw.rect(screen, self.color, self.rect)

    # ---------------- GAME ----------------
    class Game:
        def __init__(self):
            self.player = Player()
            self.enemies = []
            self.spawn_timer = 0
            self.running = True

        def spawn_enemy(self):
            self.enemies.append(Enemy())

        def check_collision(self):
            for enemy in self.enemies:
                if self.player.rect.colliderect(enemy.rect):
                    ("GAME OVER")
                    self.running = False

        def update(self):
            self.player.move()

            if enemy in self.enemies:
                .move()

            .check_collision()

            # Spawn enemies over time
            self.spawn_timer += 1
            if self.spawn_timer > 30:
                self.spawn_enemy()
                .spawn_timer = 0

        def draw(self):
            screen.fill((0, 0, 0))
            self.player.draw()

            for enemy in self.enemies:
                enemy.draw()

            pygame.display.update()

        def run(self):
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                self.update()
                self.draw()
                clock.tick(60)
    # Start game
    game = Game()
    game.run()"""
    
    st.code(code17, language="python")

    st.markdown("""<div class="section-title">Don't stop learning and enjoy.</div>""", unsafe_allow_html=True)

    st.markdown("""<div class="tip-box">
                🧠 Do you want to get tasks to practice?""", unsafe_allow_html=True)
    
    st.markdown("")
    
    if st.button("Yes", key="ch12_next"):
        st.session_state.chapter = 12
    elif st.button("No", key="ch11_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 12:
    chapter(12, 
            "Great—here's the first task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the resoult.")
    
    st.markdown("""<div class="section-title">💡 Task 1: """, unsafe_allow_html=True)

    st.markdown("""
                In book.py,  create a Book class with these attributes set in __init__:\n
                ● title, author, isbn (string, e.g. "978-0-06-112008-4")\n
                ● is_available — a boolean, starts as True\n
                Add these methods:\n
                ● checkout() — sets is_available = False. Print a message if already checked out.\n
                ● return_book() — sets is_available = True\n
                ● __str__ — returns something like: "The Hobbit by J.R.R. Tolkien [AVAILABLE]"\n
                ● __repr__ — returns Book(isbn='...')""")
       
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: Use a ternary in __str__: "[AVAILABLE]" if self.is_available else "[CHECKED OUT]""", unsafe_allow_html=True)
    
    st.markdown("")

    if st.button("Next", key="ch13_next"):
        st.session_state.chapter = 13
if st.session_state.chapter == 13:
    code18 = """
    class Book:
        def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn
            self.is_available = True

        def checkout(self):
            if not self.is_available:
                print("This book is already checked out.")
            else:
                self.is_available = False

        def return_book(self):
            self.is_available = True

        def __str__(self):
            status = "[AVAILABLE]" if self.is_available else "[CHECKED OUT]"
            return f"{self.title} by {self.author} {status}"

        def __repr__(self):
            return f"Book(isbn='{self.isbn}')"
    """
    st.code(code18, language="python")

    st.markdown("""<div class="section-title">🧠 Did you menage to finish it? Do you want next?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch14_next"):
        st.session_state.chapter = 14
    elif st.button("No", key="ch14_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 14:
    chapter(13,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the resoult.")
    
    st.markdown("""<div class="section-title">💡 Task 2: """, unsafe_allow_html=True)

    st.markdown("""
                In member.py, create a Member class:\n
                ● Attributes: name, member_id, borrowed_books (empty list)\n
                ● Class attribute: MAX_BOOKS = 3 — the most a member can borrow at once\n
                ● Method can_borrow() — returns True if they haven't hit the limit\n
                ● Method borrow(book) — appends to borrowed_books if allowed\n
                ● Method return_book(book) — removes it from borrowed_books\n
                ● __str__ — e.g. "Alice (ID: M001) — 2 books borrowed""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: Use len(self.borrowed_books) < self.MAX_BOOKS to check the limit.""", unsafe_allow_html=True)
    
    st.markdown("")
    
    if st.button("Next", key="ch15_next"):
        st.session_state.chapter = 15

if st.session_state.chapter == 15:
    code19 = """
    class Member:
        MAX_BOOKS = 3

        def __init__(self, name, member_id):
            self.name = name
            self.member_id = member_id
            self.borrowed_books = []

        def can_borrow(self):
            return len(self.borrowed_books) < self.MAX_BOOKS

        def borrow(self, book):
            if not self.can_borrow():
                print("Borrowing limit reached.")
                return       
            self.borrowed_books.append(book)

        def return_book(self, book):
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)
        def __str__(self):
            return f"{self.name} (ID: {self.member_id}) — {len(self.borrowed_books)} books borrowed"
    """
    st.code(code19, language="python")

    st.markdown("""<div class="section-title">🧠 Did you menage to finish it? Do you want next?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch16_next"):
        st.session_state.chapter = 16
    elif st.button("No", key="ch16_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 16:
    chapter(14,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the resoult.")
      
    st.markdown("""<div class="section-title">💡 Tast 3: """, unsafe_allow_html=True)

    st.markdown("""
                ● In loan.py, create a Loan class. This represents one borrowing event.\n
                ● Attributes: book (a Book object), member (a Member object), loan_date, due_date, returned (bool, starts False)\n
                ● Use Python's datetime module: from datetime import date, timedelta\n
                ● Set loan_date = date.today() and due_date = date.today() + timedelta(days=14)\n
                ● Method complete_return() — marks returned = True\n
                ● Method is_overdue() — returns True if not returned and past due date\n
                ● Method days_overdue() — returns how many days overdue (0 if not overdue)\n
                ● __str__ — something informative about the loan""")
     
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: Keep in mind—datetime, composition and instance methods""", unsafe_allow_html=True)
    
    st.markdown("")
    
    if st.button("Next", key="ch15_next"):
        st.session_state.chapter = 17

if st.session_state.chapter == 17:
    code20 = """
    from datetime import date, timedelta

    class Loan:
        def __init__(self, book, member):
            self.book = book
            self.member = member
            self.loan_date = date.today()
            self.due_date = self.loan_date + timedelta(days=14)
            self.returned = False

        def complete_return(self):
            .returned = True

        def is_overdue(self):
            return not self.returned and date.today() > self.due_date

        def days_overdue(self):
            if self.is_overdue():
                return (date.today() - self.due_date).days
            return 0

        def __str__(self):
            status = "Returned" if self.returned else "Active"
            overdue_info = ""
        
            if self.is_overdue():
                overdue_info = f" — Overdue by {self.days_overdue()} days"
        
            return (
                f"Loan: '{self.book.title}' to {self.member.name} | "
                f"Loaned: {self.loan_date} | Due: {self.due_date} | "
                f"Status: {status}{overdue_info}")
    """
    st.code(code20, language="python")

    st.markdown("""<div class="section-title">🧠 Did you menage to finish it? Do you want next?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch18_next"):
        st.session_state.chapter = 18
    elif st.button("No", key="ch18_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 18:
    chapter(15,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the resoult.")
    
    st.markdown("""<div class="section-title">💡 Task 4: """, unsafe_allow_html=True)

    st.markdown("""
                Go back to member.py and make member_id private (__member_id).\n
                ● Then add a @property so it can still be read from outside but not set directly.\n
                ● Accessing member.member_id should still work (returns the value)\n
                ● Trying member.member_id = "NEW" should raise an AttributeError (no setter)\n
                Also add a fine attribute (float, starts at 0.0) with a property. The setter should reject negative values:""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint:""", unsafe_allow_html=True)
    
    st.markdown("")

    code21 = """
    @fine.setter
    def fine(self, value):
        if value < 0:
            raise ValueError("Fine cannot be negative")
        self.__fine = value"""
    
    st.code(code21, language="python")

    if st.button("Next", key="ch19_next"):
        st.session_state.chapter = 19

if st.session_state.chapter == 19:
    code22 = """
    class Member:
        MAX_BOOKS = 3

        def __init__(self, name, member_id):
            self.name = name
            self.__member_id = member_id  # private
            self.borrowed_books = []
            self.__fine = 0.0  # private fine

        @property
        def member_id(self):
            return self.__member_id

        def can_borrow(self):
            return len(self.borrowed_books) < self.MAX_BOOKS

        def borrow(self, book):
            if not self.can_borrow():
                print("Borrowing limit reached.")
                return
            self.borrowed_books.append(book)

        def return_book(self, book):
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)

        @property
        def fine(self):
            return self.__fine

        @fine.setter
        def fine(self, value):
            if value < 0:
                raise ValueError("Fine cannot be negative")
            self.__fine = value

        def __str__(self):
            return f"{self.name} (ID: {self.member_id}) — {len(self.borrowed_books)} books borrowed"
    """
    st.code(code22, language="python")

    st.markdown("""<div class="section-title">🧠 Did you menage to finish it? Do you want next?.</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch20_next"):
        st.session_state.chapter = 20
    elif st.button("No", key="ch20_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 20:
    chapter(16,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the resoult.")
    
    st.markdown("""<div class="section-title">💡 Task 5: """, unsafe_allow_html=True)

    st.markdown("""
                In book.py, add an EBook class that inherits from Book:\n
                ● Extra attribute: file_size_mb (float) and format (e.g. "PDF", "EPUB")\n
                ● EBooks are always available — override checkout() to never change availability (print "EBooks can be borrowed by multiple members")\n
                ● Override __str__ to include format info\n""")
    
    st.markdown("")

    if st.button("Next", key="ch21_next"):
        st.session_state.chapter = 21

if st.session_state.chapter == 21:
    code23 = """
    class EBook(Book):
        def __init__(self, title, author, isbn, file_size_mb, format):
            ().__init__(title, author, isbn)
            self.file_size_mb = file_size_mb
            self.format = format

        def checkout(self):
            print("EBooks can be borrowed by multiple members")

        def __str__(self):
            status = "[AVAILABLE]"  # always available
            return (
                f"{self.title} by {self.author} "
                f"({self.format}, {self.file_size_mb}MB) {status}"
            )
    """
    st.code(code23, language="python")

    st.markdown("""<div class="section-title">🧠 Did you menage to finish it? Do you want next?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch22_next"):
        st.session_state.chapter = 22
    elif st.button("No", key="ch22_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 22:
    chapter(17,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the resoult.")
    
    st.markdown("""<div class="section-title">💡 Task 6: """, unsafe_allow_html=True)

    st.markdown("""
                In member.py, add a PremiumMember that inherits from Member:\n
                ● Premium members can borrow up to 10 books (override MAX_BOOKS)\n
                ● Premium members get a 50% fine discount — override a method apply_fine(days) that adds days * 0.10 instead of days * 0.20\n
                ● Call super().__init__() properly""")

    st.markdown("""<div class="tip-box">
                ⚠️ Hint:To override a class attribute in a subclass, just redefine it: MAX_BOOKS = 10 inside the PremiumMember class body.""", unsafe_allow_html=True)
    
    st.markdown("")

    if st.button("Next", key="ch23_next"):
        st.session_state.chapter = 23

if st.session_state.chapter == 23:
    code24 = """
    class PremiumMember(Member):
        MAX_BOOKS = 10

        def __init__(self, name, member_id):
            super().__init__(name, member_id)

        def apply_fine(self, days):
            self.fine += days * 0.10"""
    
    st.code(code24, language="python")

    st.markdown("""<div class="section-title">🧠 Did you menage to finish it? Do you want next?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch24_next"):
        st.session_state.chapter = 24
    elif st.button("No", key="ch24_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 24:
    chapter(17,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the resoult.")
    
    st.markdown("""<div class="section-title">💡 Task 7: """, unsafe_allow_html=True)

    st.markdown("""
                In library.py, create the main Library class. This is your system orchestrator — it has books, members, and loans (composition).\n
                ● Attributes: name, books (list), members (list), loans (list)\n
                ● add_book(book) — adds a Book or EBook to the library\n
                ● register_member(member) — adds a member\n
                ● checkout_book(isbn, member_id) — finds the book and member, creates a Loan, calls book.checkout() and member.borrow(book)\n
                ● return_book(isbn, member_id) — finds the active loan, calculates any fine, calls loan.complete_return()\n
                ● search_by_title(query) — returns a list of books whose title contains the query (case-insensitive)\n
                ● available_books() — returns all books where is_available == True\n
                ● member_report(member_id) — prints a summary of a member's loans and fines""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: For checkout_book, use a helper to find by isbn: next((b for b in self.books if b.isbn == isbn), None)""", unsafe_allow_html=True)
    
    st.markdown("")

    if st.button("Next", key="ch25_next"):
        st.session_state.chapter = 25

if st.session_state.chapter == 25:
    code25 = """
    from datetime import date
    from book import Book, EBook
    from member import Member, PremiumMember
    from loan import Loan

    class Library:
        def __init__(self, name):
            self.name = name
            self.books = []
            self.members = []
            self.loans = []

        def add_book(self, book):
            if isinstance(book, (Book, EBook)):
                self.books.append(book)
            else:
                print("Can only add Book or EBook instances")

        def register_member(self, member):
            if isinstance(member, Member):
                self.members.append(member)
            else:
                print("Can only register Member instances")

        def checkout_book(self, isbn, member_id):
            book = next((b for b in self.books if b.isbn == isbn), None)
            if not book:
                print(f"No book with ISBN {isbn}")
                return

            member = next((m for m in self.members if m.member_id == member_id), None)
            if not member:
                print(f"No member with ID {member_id}")
                return

            if isinstance(book, Book) and not isinstance(book, EBook) and not book.is_available:
                print(f"Book '{book.title}' is already checked out.")
                return

            if not member.can_borrow():
                print(f"{member.name} has reached borrowing limit.")
                return

            book.checkout()
            member.borrow(book)
            loan = Loan(book, member)
            self.loans.append(loan)
            print(f"{member.name} checked out '{book.title}' successfully.")

        def return_book(self, isbn, member_id):
            loan = next(
                (l for l in self.loans if l.book.isbn == isbn 
                and l.member.member_id == member_id and not l.returned),
                None)

            if not loan:
                print("No active loan found for this book and member.")
                return

            overdue_days = loan.days_overdue()
            if overdue_days > 0:
                loan.member.apply_fine(overdue_days)
                print(f"Overdue by {overdue_days} days. Fine applied to {loan.member.name}.")

            loan.complete_return()
            if isinstance(loan.book, Book) and not isinstance(loan.book, EBook):
                loan.book.return_book()
            loan.member.return_book(loan.book)
            print(f"'{loan.book.title}' returned successfully by {loan.member.name}.")

        def search_by_title(self, query):
            query_lower = query.lower()
            return [b for b in self.books if query_lower in b.title.lower()]

        def available_books(self):
            return [b for b in self.books if isinstance(b, EBook) or b.is_available]

        def member_report(self, member_id):
            member = next((m for m in self.members if m.member_id == member_id), None)
            if not member:
                print(f"No member with ID {member_id}")
                return

            member_loans = [l for l in self.loans if l.member.member_id == member_id]
            print(f"--- Report for {member.name} (ID: {member.member_id}) ---")
            print(f"Fine: ${member.fine:.2f}")
            if not member_loans:
                print("No loans.")
                return
            for loan in member_loans:
                status = "Returned" if loan.returned else "Active"
                overdue_days = loan.days_overdue()
                overdue_text = f", Overdue by {overdue_days} days" if overdue_days else ""
                print(f"{loan.book.title} | Loaned: {loan.loan_date} | Due: {loan.due_date} | Status: {status}{overdue_text}")"""
    
    st.code(code25, language="python")

    st.markdown("""<div class="section-title">🧠 Did you menage to finish it? Do you want next?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch26_next"):
        st.session_state.chapter = 26
    elif st.button("No", key="ch26_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 26:
    chapter(18,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the resoult.")
    
    st.markdown("""<div class="section-title">💡 Task 8: """, unsafe_allow_html=True)

    st.markdown("""
                Refactor book.py to use an Abstract Base Class:\n
                ● Create an abstract LibraryItem class (import ABC and abstractmethod)\n
                ● It should have abstract methods: checkout() and get_info()\n
                ● Make Book and EBook both inherit from LibraryItem\n
                ● Each implements get_info() differently — Book returns physical details, EBook returns digital details""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: Try passing a Book and an EBook to the same function. Python doesn't care which type it is — as long as it has get_info(), it works. That's polymorphism.""", unsafe_allow_html=True)
    
    st.markdown("")

    if st.button("Next", key="ch27_next"):
        st.session_state.chapter = 27

if st.session_state.chapter == 27:
    code26 = """
    from abc import ABC, abstractmethod

    class LibraryItem(ABC):
        def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn

        @abstractmethod
        def checkout(self):
            pass

        @abstractmethod
        def get_info(self):
            pass


    class Book(LibraryItem):
        def __init__(self, title, author, isbn):
            super().__init__(title, author, isbn)
            self.is_available = True

        def checkout(self):
            if not self.is_available:
                print("This book is already checked out.")
            else:
                self.is_available = False

        def return_book(self):
            self.is_available = True

        def get_info(self):
            status = "AVAILABLE" if self.is_available else "CHECKED OUT"
            return f"{self.title} by {self.author} [Physical, {status}]"

        def __str__(self):
            return self.get_info()

        def __repr__(self):
            return f"Book(isbn='{self.isbn}')"


    class EBook(LibraryItem):
        def __init__(self, title, author, isbn, file_size_mb, format):
            super().__init__(title, author, isbn)
            self.file_size_mb = file_size_mb
            self.format = format

        def checkout(self):
            print("EBooks can be borrowed by multiple members")

        def get_info(self):
            return f"{self.title} by {self.author} [Digital, {self.format}, {self.file_size_mb}MB]"

        def __str__(self):
            return self.get_info()"""
    
    st.code(code26, language="python")

    st.markdown("""<div class="section-title">🧠 Did you menage to finish it? Do you want next?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch28_next"):
        st.session_state.chapter = 28
    elif st.button("No", key="ch28_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 28:
    chapter(19,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the resoult.")
    
    st.markdown("""<div class="section-title">💡 Task 9: """, unsafe_allow_html=True)

    st.markdown("In library.py, add a method print_catalogue() that loops through all items and calls item.get_info() — demonstrating polymorphism:")

    st.markdown("""<div class="tip-box">
                ⚠️ Hint: """, unsafe_allow_html=True)
    
    st.markdown("")
    
    code27 = """
    def print_catalogue(self):
        for item in self.books:
            print(item.get_info())"""
    
    st.code(code27, language="python")

    st.markdown("")

    if st.button("Next", key="ch27_next"):
        st.session_state.chapter = 29

if st.session_state.chapter == 29:
    code28 = """
    class Library:
        def __init__(self, name):
            self.name = name
            self.books = []    
            self.members = []
            self.loans = []
    ...        

        def print_catalogue(self):
            print(f"--- Catalogue of {self.name} ---")
            for item in self.books:
            print(item.get_info())"""
    
    st.code(code28, language="python")

    st.markdown("""<div class="section-title">🧠 Did you menage to finish it? Do you want next?</div>""", unsafe_allow_html=True)

    if st.button("Yes", key="ch3_next"):
        st.session_state.chapter = 30
    elif st.button("No", key="ch3_NO_next"):
        st.markdown("""<div class="section-title">No problem, practice on your own.</div>""", unsafe_allow_html=True)

if st.session_state.chapter == 30:
    chapter(20,
            "Great—here's the next task for you.",
            "Try to finish it on your own. When you're done or stuck press 'Next' to see the resoult.")
    
    st.markdown("""<div class="section-title">💡 Task 10: """, unsafe_allow_html=True)

    st.markdown("""
                Make your objects feel native in Python by adding dunder methods:\n
                ● On Library: add __len__ (returns number of books), __contains__ (so you can do book in library), and __iter__ (so you can loop over a library with for book in library)\n
                ● On Book: add __eq__ (two books are equal if they have the same isbn) and __lt__ (compare by title alphabetically, so you can sort() a list of books)\n
                ● On Member: add __eq__ (same member_id means same member)
                Test it in main.py:""")
    
    st.markdown("""<div class="tip-box">
                ⚠️ Hint: """, unsafe_allow_html=True)
    
    st.markdown("")
    
    code29 = """
    print(len(library))          # number of books
    print(hobbit in library)     # True
    books = sorted(library.books) # uses __lt__
    for book in library:           # uses __iter__
        print(book)"""
    
    st.code(code29, language="python")

    st.markdown("")

    if st.button("Next", key="ch31_next"):
        st.session_state.chapter = 31

if st.session_state.chapter == 31:
    st.markdown("""<div class="section-title">📘 book.py — add __eq__ and __lt__""", unsafe_allow_html=True)

    code30 = """
    from abc import ABC, abstractmethod

    class LibraryItem(ABC):
        def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn

        @abstractmethod
        def checkout(self):
            pass

        @abstractmethod
        def get_info(self):
            pass

        def __eq__(self, other):
            if isinstance(other, LibraryItem):
                return self.isbn == other.isbn
            return False

        def __lt__(self, other):
            if isinstance(other, LibraryItem):
                return self.title < other.title
            return NotImplemented

    class Book(LibraryItem):
        def __init__(self, title, author, isbn):
            super().__init__(title, author, isbn)
            self.is_available = True

        def checkout(self):
            if not self.is_available:
                print("This book is already checked out.")
            else:
                self.is_available = False

        def return_book(self):
            self.is_available = True

        def get_info(self):
            status = "AVAILABLE" if self.is_available else "CHECKED OUT"
            return f"{self.title} by {self.author} [Physical, {status}]"

        def __str__(self):
            return self.get_info()

        def __repr__(self):
            return f"Book(isbn='{self.isbn}')"

    class EBook(LibraryItem):
        def __init__(self, title, author, isbn, file_size_mb, format):
            super().__init__(title, author, isbn)
            self.file_size_mb = file_size_mb
            self.format = format

        def checkout(self):
            print("EBooks can be borrowed by multiple members")

        def get_info(self):
            return f"{self.title} by {self.author} [Digital, {self.format}, {self.file_size_mb}MB]"

        def __str__(self):
            return self.get_info()"""
    
    st.code(code30, language="python")

    st.markdown("")

    if st.button("Next result", key="ch32_next"):
        st.session_state.chapter = 32

if st.session_state.chapter == 32:
    st.markdown("""<div class="section-title">👤 member.py — add __eq__""", unsafe_allow_html=True)

    code31 = """
    class Member:
        MAX_BOOKS = 3

        def __init__(self, name, member_id):
            self.name = name
            self.__member_id = member_id
            self.borrowed_books = []
            self.__fine = 0.0

        @property
        def member_id(self):
            return self.__member_id

        @property
        def fine(self):
            return self.__fine

        @fine.setter
        def fine(self, value):
            if value < 0:
                raise ValueError("Fine cannot be negative")
            self.__fine = value

        def can_borrow(self):
            return len(self.borrowed_books) < self.MAX_BOOKS

        def borrow(self, book):
            if not self.can_borrow():
                print("Borrowing limit reached.")
                return
            self.borrowed_books.append(book)

        def return_book(self, book):
            if book in self.borrowed_books:
                self.borrowed_books.remove(book)

        def apply_fine(self, days):
            self.fine += days * 0.20

        def __str__(self):
            return f"{self.name} (ID: {self.member_id}) — {len(self.borrowed_books)} books borrowed"

        def __eq__(self, other):
            if isinstance(other, Member):
                return self.member_id == other.member_id
            return False


    class PremiumMember(Member):
        MAX_BOOKS = 10

        def __init__(self, name, member_id):
            super().__init__(name, member_id)

        def apply_fine(self, days):
            self.fine += days * 0.10"""
    
    st.code(code31, language="python")

    st.markdown("")

    if st.button("Next result", key="ch33_next"):
        st.session_state.chapter = 33

if st.session_state.chapter == 33:
    st.markdown("""<div class="section-title">📚 library.py — add __len__, __contains__, __iter__""", unsafe_allow_html=True)

    code32 = """
    class Library:
        def __init__(self, name):
            self.name = name
            self.books = []
            self.members = []
            self.loans = []

        def add_book(self, book):
            self.books.append(book)

        def register_member(self, member):
            self.members.append(member)

        def __len__(self):
            return len(self.books)

        def __contains__(self, item):
            return item in self.books

        def __iter__(self):
            return iter(self.books)"""
    
    st.code(code32, language="python")

    st.markdown("")

    if st.button("Next result", key="ch34_next"):
        st.session_state.chapter = 34

if st.session_state.chapter == 34:
    st.markdown("""<div class="section-title">📝 main.py — testing everything""", unsafe_allow_html=True)

    code33 = """
    from book import Book, EBook
    from member import Member, PremiumMember
    from library import Library

    library = Library("City Library")

    book1 = Book("The Hobbit", "J.R.R. Tolkien", "978-0-06-112008-4")
    book2 = Book("1984", "George Orwell", "978-0-452-28423-4")
    ebook1 = EBook("Python 101", "John Doe", "123", 5.2, "PDF")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(ebook1)

    print(len(library))  # 3

    print(book1 in library)  # True
    print(EBook("Python 101", "John Doe", "123", 5.2, "PDF") in library)  # True (same ISBN)


    for item in library:
        print(item)

    books_sorted = sorted(library.books)
    for b in books_sorted:
        print(b)

    alice1 = Member("Alice", "M001")
    alice2 = Member("Alice Smith", "M001")
    bob = PremiumMember("Bob", "P001")
    print(alice1 == alice2)  # True
    print(alice1 == bob)     # False"""

    st.code(code33, language="python")

    st.markdown("")

    if st.button("Finish", key="ch35_next"):
        st.session_state.chapter = 35

if st.session_state.chapter == 35:
    chapter(20,
            "Congratulations! 🎉",
            "🎉You have succesfully finished OOP learning guide!🎉")
    
    st.markdown("""<div class="section-title">🎉You have finished this learning guide!🎉 I am proud of you!</div>""", unsafe_allow_html=True)
    
    st.markdown("""<div class="tip-box">
                ⚠️Don't forget to keep practicing on your own! Programming has much more skills for you to lean! I wish you the best of luck! 💡
                </div>""", unsafe_allow_html=True)
