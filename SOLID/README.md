# SOLID Principles

The SOLID principles are a set of design principles that help in creating maintainable and scalable software systems.

## 1. Single Responsibility Principle (SRP):
   This principle states that a class should have only one reason to change. It means that a class should have only one responsibility or job.

   ```python
   class Customer:
       def __init__(self, name):
           self.name = name

       def get_name(self):
           return self.name

   class EmailSender:
       def send_email(self, customer):
           # Code to send email to the customer
           pass
   ```

   In the above example, the `Customer` class has the responsibility of storing customer information, while the `EmailSender` class has the responsibility of sending emails. Each class has a single responsibility.

## 2. Open-Closed Principle (OCP):
   This principle states that software entities (classes, modules, functions) should be open for extension but closed for modification. It means that you should be able to add new functionality without modifying existing code.

   ```python
   class Shape:
       def area(self):
           pass

   class Rectangle(Shape):
       def __init__(self, width, height):
           self.width = width
           self.height = height

       def area(self):
           return self.width * self.height

   class Circle(Shape):
       def __init__(self, radius):
           self.radius = radius

       def area(self):
           return 3.14 * self.radius * self.radius
   ```

   In the above example, the `Shape` class is open for extension, as new shapes can be added by inheriting from it. However, the existing code doesn't need to be modified when adding new shapes.

## 3. Liskov Substitution Principle (LSP):
   This principle states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. It means that the behavior of the base class should be preserved in its derived classes.

   ```python
   class Bird:
       def fly(self):
           pass

   class Sparrow(Bird):
       def fly(self):
           print("Sparrow is flying")

   class Ostrich(Bird):
       def fly(self):
           raise NotImplementedError("Ostrich cannot fly")
   ```

   In the above example, both `Sparrow` and `Ostrich` are subclasses of `Bird`. They both have a `fly` method, but the behavior is different. However, the program can still work correctly when substituting a `Bird` object with either a `Sparrow` or an `Ostrich` object.

## 4. Interface Segregation Principle (ISP):
   This principle states that clients should not be forced to depend on interfaces they do not use. It means that classes should have specific interfaces tailored to their needs.

   ```python
   class Printer:
       def print(self, document):
           pass

   class Scanner:
       def scan(self, document):
           pass

   class Photocopier(Printer, Scanner):
       def print(self, document):
           # Code to print the document
           pass

       def scan(self, document):
           # Code to scan the document
           pass
   ```

   In the above example, the `Photocopier` class implements both the `Printer` and `Scanner` interfaces. However, other classes that only need printing or scanning functionality don't have to depend on the unnecessary methods.

## 5. Dependency Inversion Principle (DIP)
   This principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions. It means that the dependency should be on interfaces or abstract classes rather than concrete implementations.

   ```python
   class Database:
       def save(self, data):
           # Code to save data to the database
           pass

   class Logger:
       def log(self, message):
           # Code to log the message
           pass

   class UserService:
       def __init__(self, database, logger):
           self.database = database
           self.logger = logger

       def register_user(self, user):
           self.database.save(user)
           self.logger.log("User registered")
   ```

   In the above example, the `UserService` class depends on the abstractions (`Database` and `Logger`) rather than concrete implementations. This allows for flexibility and easier testing.
