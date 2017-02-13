Object-oriented programming 
##############################
(**Programação orientada a objetos**)

Daniel Moser

Feb 14th, 2017

2nd IAG Python Boot Camp

.. contents:: Table of contents


What is OOP?
===============
**OOP** is a programming paradigm. It is usually compared with the traditional **procedural** programming.

The procedural programming is based on *procedures* (i.e., routines and sub-routines), where the procedures and data variables are **independent**. Examples: Cobol, C, Fortran...

.. code:: 

    program Fibonacci;

    function fib(n: Integer): Integer;
    var a: Integer = 1;
        b: Integer = 1;
        f: Integer;
        i: Integer;
    begin
      if (n = 1) or (n = 2) then
         fib := 1
      else
        begin
          for i := 3 to n do
          begin
             f := a + b;
             b := a;
             a := f;
          end;
          fib := f;
        end;
    end;

    begin
      WriteLn(fib(6));
    end.

OOP is based in **objects**, a variable that combines *methods* (procedures) and *attributes* (data). 

Examples of *OOP compatible* languages: C#, C++, Java, Lisp, Python, Ruby...

.. code:: python

    class Fibonacci:
       def __init__(self):
           self.cache = {}
       def fib(self, n):
           if self.cache.has_key(n):
               return self.cache[n]
           if n == 1 or n == 2:
                return 1
           else:
               a = 1
               b = 1
               for i in range(2, n):
                   f = a + b;
                   b = a;
                   a = f;
               self.cache[n] = f;
               return f;


    fibonaccyCounter = Fibonacci()
    # print(fibonaccyCounter.fib(600))

    # %time fibonaccyCounter.fib(600)
    # %time fibonaccyCounter.fib(600)

Why *OOP compatible*? Because usually in a OOP language one can still work as a  **procedural** language...

Examples of pure OOP languages: Smalltalk and Self.


OOP Concepts: abstraction, class and object
=============================================
- **abstraction** is the process of defining only the essential aspects in a specific context, ignoring non-relevant characteristics. 

- **class** is an *abstraction* that defines a **type** of object and what objects of that type have within them (their **attributes**) and also defines what kind of actions that type of object is able to perform (**methods**).

:: 

    "Class has no life, it's just a concept."

- **object** (or class **instance**) is a living variable, created according to a (conceptual) class.

- **constructor** has a special function: it serves to initialize attributes and runs automatically whenever you create a new object.


Examples
==========
.. code:: python

    class testing:
        """This is a IAG Python Boot Camp class definition"""

        def __init__(self, init_value):
            """This is a constructor"""
            self.some_value = init_value
            return

        def double_attr(self):
            """This is a method that double the ``some_value`` atribute"""  
            self.some_value *= 2 
            return


OOP Concepts: heritage 
=========================
- **heritage** is the mechanism by which one *class* can be extended to another one. The inheritance mechanism allows a class (subclass) to share the source code of another class (superclass), taking advantage of its behaviors (methods) and possible variables (attributes). 

.. code:: python

    class Pets(object):
        owner = "Python Boot Camp"

        def __init__(self, name, age, condition='healthy'):
            print("A new pet entry!")
            self.name = name
            self.age = age
            self.condition = condition

        def __repr__(self):
            return "Pet '{0}', {1} year(s)".format(self.name, self.age)

    class Dog(Pets):
        def bark(self):
            print(" Woof-woof!!")
            return

    class Monkey(Pets):
        def __init__(self, name, age, condition=''):
            """Overwriting the Pets() constructor"""
            condition = 'custom'
            Pets.__init__(self, name, age, condition)

        def gibber(self):
            print(" (gibber)!!")
            return

    class Horse(Pets):
        def __init__(self, name, age):
            super(Horse, self).__init__(name, age)

        def neigh(self):
            print(" Neigh!!")
            return

    class Cat(Pets):
        def __init__(self):
            super(Pets, self).__init__()

        def meow(self):
            print(" Meow!!")
            return

- **specialization** is the inheritance process in which a subclass is created from existing superclass(es).

- **generalization** is the process in which a superclass is created from existing subclasses. 

- Python supports **multiple inheritance**:

.. code:: python

    class Toys:
        color = 'light blue'

    class Lassie(Pets, Toys):
        pass 

Must read: `Python’s super() considered super! <https://rhettinger.wordpress.com/2011/05/26/super-considered-super/>`_


Ways of combining classes and their properties
=================================================
- **association** is the mechanism by which one object uses the resources (*attributes*) of another. 

.. code:: python

    class A(object):
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def addNums():
            self.b + self.c

    class B(object):
        def __init__(self, d, e):
            self.d = d
            self.e = e

        def addAllNums(self, Ab, Ac):
            x = self.d + self.e + Ab + Ac
            return x

    ting = A("yo", 2, 6)
    ling = B(5, 9)

    print ling.addAllNums(ting.b, ting.c)

- **coupling** or **aggregation**: is the process where a (sub)class is (integrally) incorporated as an attribute of another one.

.. code:: python

    class A(object):
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def addNums():
            self.b + self.c

    class B(object):
        def __init__(self, d, e, A):
            self.d = d
            self.e = e
            self.A = A

        def addAllNums(self):
            x = self.d + self.e + self.A.b + self.A.c
            return x

    ting = A("yo", 2, 6)
    ling = B(5, 9, ting)

    print ling.addAllNums()

- **composition**: is similar to the aggregation, but only incorporating a specific version of the subclass.

.. code:: python

    class A(object):
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def addNums():
            self.b + self.c

    class B(object):
        def __init__(self, d, e):
            self.d = d
            self.e = e
            self.A = A("yo", 2, 6)

        def addAllNums(self):
            x = self.d + self.e + self.A.b + self.A.c
            return x

    ling = B(5, 9)

    print ling.addAllNums() 

::

    Remember: those "association/combination" names may vary in the literature.

Encapsulation and polymorphism 
================================
- **encapsulation**: In an object oriented program, one can restrict access to methods and attributes. 

.. code:: python

    class C(object):
        def __init__(self):
            self.a = 1    # OK to access directly
            self._a = 2   # should be considered private
            self.__a = 3  # considered private, name Disfigured

::

    Warning! Some people say that *encapsulation* can prevent the data from being modified. This is **not** the case in Python (and even Java[!]. Other methods need to used to avoid modification).


- **polymorphism**: is the principle by which two or more classes can invoke methods that have the same identification (signature) but distinct, specialized behaviors for each one.

.. code:: python

    class Person(object):
        def pay_bill():
            raise NotImplementedError

    class Millionare(Person):
        def pay_bill():
            print "Here you go! Keep the change!"

    class GradStudent(Person):
        def pay_bill():
            print "Can I owe you ten bucks or do the dishes?"

.. There are four types of polymorphism that a programming language may have (note that not every object-oriented language has implemented all types of polymorphism):

- **interface**: is a contract between the class and the outside world. When a class contemplates/implements an interface, it is committed to providing the behavior expected by the interface.

- **packages** (or **namespaces**) are references for class/interface organization.

.. code:: python

    import scipy

    scipy.interpolate
    scipy.interpolate.quad

    scipy.integrate


Other OOP Concepts
====================
- **ducktyping** (or duck typing) 

As far as the function ``in_the_forest`` is concerned, the ``Person`` object is a *duck*:

.. code:: python

    class Duck:
        def quack(self):
            print("Quaaaaaack!")
        def feathers(self):
            print("The duck has white and gray feathers.")

    class Person:
        def quack(self):
            print("The person imitates a duck.")
        def feathers(self):
            print("The person takes a feather from the ground and shows it.")
        def name(self):
            print("John Smith")

    def in_the_forest(duck):
        duck.quack()
        duck.feathers()

    def game():
        donald = Duck()
        john = Person()
        in_the_forest(donald)
        in_the_forest(john)

    game()


- **message (passing)** is the selection of the code to execute in response to a **method call**, typically by looking up the method in a table associated with the object. This feature is known as **dynamic dispatch**, and distinguishes an object from an **abstract data type**, which has a fixed (static) implementation of the operations for all instances. [*Not covered here*]


OOP pro et contra
===================
Advantages of OOP:

- A more logical and better encapsulated code division. 
- This makes maintaining and extending the code easier and with less risk of inserting bugs. 
- It is also easier to reuse the code.
- It is easier to manage the development of this type of software when we have a large team. 

Disadvantages of OOP

- Learning of the object-oriented programming paradigm is more complicated. In traditional procedural programming, just decorate a few dozen commands and you can already make a simple program.
- Hardly an object-oriented language will be able to run over non-object-oriented languages.


Extra
======
- **UML** (Unified Modeling Language) is a general-purpose, developmental, modeling language in the field of software engineering, that is intended to provide a standard way to visualize the design of a system.

- **SysML** (Systems Modeling Language) can be seen as a *system view* of the application, or as an extension of subsets of UML.

This kind of tools can be used, for example, together with **abstraction** level concepts for automatic programming (or automatic coding)!


Exercises
==========
#. What ``dir()`` do?

#. What ``hasattr(), getattr(), setattr()`` and ``delattr()`` do? 

#. What is happening here?

.. code:: 

  class test:
      def __init__(self):
          print "init 1"

      def __init__(self):
          print "init 2"

#. How can you change a class (global) attribute?

#. What ``isinstance(variable, class)`` do?

#. Is ``Lassie`` an instance of ``Pets`` or ``Toys``?

#. What ``instance.__base__`` do?

#. About **interfaces**. Understand what is happening here:

.. code:: python

    """http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html"""

    class WhatIHave:
        def g(self): pass
        def h(self): pass

    class WhatIWant:
        def f(self): pass

    class ProxyAdapter(WhatIWant):
        def __init__(self, whatIHave):
            self.whatIHave = whatIHave

        def f(self):
            # Implement behavior using
            # methods in WhatIHave:
            self.whatIHave.g()
            self.whatIHave.h()

    class WhatIUse:
        def op(self, whatIWant):
            whatIWant.f()

    # Approach 2: build adapter use into op():
    class WhatIUse2(WhatIUse):
        def op(self, whatIHave):
            ProxyAdapter(whatIHave).f()

    # Approach 3: build adapter into WhatIHave:
    class WhatIHave2(WhatIHave, WhatIWant):
        def f(self):
            self.g()
            self.h()

    # Approach 4: use an inner class:
    class WhatIHave3(WhatIHave):
        class InnerAdapter(WhatIWant):
            def __init__(self, outer):
                self.outer = outer
            def f(self):
                self.outer.g()
                self.outer.h()

        def whatIWant(self):
            return WhatIHave3.InnerAdapter(self)

    whatIUse = WhatIUse()
    whatIHave = WhatIHave()
    adapt= ProxyAdapter(whatIHave)
    whatIUse2 = WhatIUse2()
    whatIHave2 = WhatIHave2()
    whatIHave3 = WhatIHave3()
    whatIUse.op(adapt)
    # Approach 2:
    whatIUse2.op(whatIHave)
    # Approach 3:
    whatIUse.op(whatIHave2)
    # Approach 4:
    whatIUse.op(whatIHave3.whatIWant())
