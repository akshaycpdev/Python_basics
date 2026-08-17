# Python Interview Questions & Answers 🐍

## Introduction

This README is a growing collection of **200+ Python interview questions and answers**, covering Python from **beginner to advanced level**.

It is designed as a practical revision guide for students, beginners, developers preparing for interviews, and anyone who wants to strengthen their Python fundamentals.

Topics progress from Python basics and data types to functions, OOP, exceptions, modules, iterators, generators, decorators, concurrency, testing, performance, security, web development, packaging, and interview-oriented problem solving.

New questions can be added as the repository grows.

## What You'll Find Here

- Python fundamentals
- Variables, data types, strings, lists, tuples, sets, and dictionaries
- Conditions and loops
- Functions and scope
- Modules, packages, pip, and virtual environments
- Exception and file handling
- Object-Oriented Programming
- Iterators, generators, decorators, and context managers
- Memory management and garbage collection
- GIL, threading, multiprocessing, and asyncio
- Algorithms and data structures
- Testing, debugging, logging, and profiling
- Type hints and modern Python features
- Web development and APIs
- Security fundamentals
- Packaging and deployment
- Common Python coding interview questions

## Python Interview Questions & Answers

### 1. Python Fundamentals

**1. What is Python?**
- Python is a high-level, interpreted, general-purpose programming language known for readable syntax and a large standard library.

**2. What are the main features of Python?**
- Readable syntax, dynamic typing, interpreted execution, object-oriented support, extensive libraries, portability, and automatic memory management.

**3. Who created Python?**
- Guido van Rossum created Python. It was first released publicly in 1991.

**4. Why is Python popular?**
- It is easy to learn, productive, versatile, well supported by libraries, and widely used in web development, automation, data science, AI, and scripting.

**5. Is Python compiled or interpreted?**
- Python is commonly described as interpreted. CPython first compiles source code to bytecode, which is then executed by the Python virtual machine.

**6. What is CPython?**
- CPython is the reference implementation of Python, written mainly in C.

**7. What is PEP 8?**
- PEP 8 is the main style guide for Python code.

**8. What is PEP?**
- PEP stands for Python Enhancement Proposal. PEPs describe proposed or documented changes and standards for Python.

**9. What is an interpreter?**
- An interpreter executes program instructions through a runtime rather than producing a standalone native executable first.

**10. What is Python bytecode?**
- Bytecode is an intermediate instruction format generated from Python source and executed by the Python virtual machine.

**11. What is indentation in Python?**
- Indentation defines code blocks in Python, replacing braces used by many other languages.

**12. What is a comment in Python?**
- A comment begins with # and is ignored by the Python interpreter.

**13. How do you write a multiline string?**
- Use triple-quoted strings with '''...''' or """...""".

**14. What is a variable?**
- A variable is a name bound to an object.

**15. Does Python require variable declarations?**
- No. A variable is created when a name is assigned to an object.

**16. What is dynamic typing?**
- The type belongs to the object at runtime, and a name can later be bound to an object of another type.

**17. What is strong typing?**
- Python does not silently perform many unrelated type conversions; incompatible operations generally raise TypeError.

**18. What are Python's built-in numeric types?**
- The main numeric types are int, float, and complex.

**19. What is None?**
- None is Python's singleton object representing the absence of a value.

**20. What is bool?**
- bool represents truth values: True and False.

**21. What is type()?**
- type(obj) returns the object's type.

**22. What is isinstance()?**
- isinstance(obj, cls) checks whether an object is an instance of a class or compatible subclass.

**23. What is id()?**
- id(obj) returns an integer identifying the object during its lifetime.

**24. What is mutable vs immutable?**
- Mutable objects can be changed in place; immutable objects cannot be changed after creation.

**25. Give examples of immutable types.**
- int, float, bool, str, tuple, bytes, and frozenset are common immutable types.

**26. Give examples of mutable types.**
- list, dict, set, and bytearray are common mutable types.

**27. What is a string?**
- A string is an immutable sequence of Unicode characters.

**28. How do you create a string?**
- Use single quotes, double quotes, or triple quotes.

**29. What is string slicing?**
- Slicing extracts part of a sequence using syntax such as s[start:stop:step].

**30. What is an f-string?**
- An f-string is a formatted string literal such as f'Hello {name}'.

**31. What is string interpolation?**
- It means inserting values into a formatted string, commonly using f-strings.

**32. What does len() do?**
- len(obj) returns the number of items in a sized object.

**33. What does upper() do?**
- It returns a copy of a string converted to uppercase.

**34. What does lower() do?**
- It returns a copy of a string converted to lowercase.

**35. What does strip() do?**
- It removes leading and trailing characters, whitespace by default.

### 2. Collections, Iteration & Comprehensions

**36. What is a list?**
- A list is an ordered, mutable collection that can contain duplicate values.

**37. How do you create a list?**
- Use square brackets, for example [1, 2, 3].

**38. What is a tuple?**
- A tuple is an ordered, immutable collection.

**39. Why use a tuple instead of a list?**
- Use a tuple when the collection should not be changed and when immutability communicates intent.

**40. What is a set?**
- A set is an unordered collection of unique hashable elements.

**41. What is a frozenset?**
- A frozenset is an immutable set.

**42. What is a dictionary?**
- A dictionary stores key-value pairs and provides fast average-case key lookup.

**43. Can dictionary keys be lists?**
- No. Dictionary keys must be hashable, and lists are mutable and unhashable.

**44. Can a dictionary contain duplicate keys?**
- No. Assigning an existing key replaces its previous value.

**45. What is a nested list?**
- A list containing other lists as elements is a nested list.

**46. What is a list comprehension?**
- It is a concise syntax for creating lists from an iterable, optionally with filtering.

**47. What is a dictionary comprehension?**
- It creates dictionaries concisely from an iterable.

**48. What is a set comprehension?**
- It creates sets concisely from an iterable.

**49. What is an iterator?**
- An iterator is an object that implements __iter__() and __next__() and produces values one at a time.

**50. What is an iterable?**
- An iterable is an object that can return an iterator, such as a list, tuple, string, or dictionary.

**51. Iterable vs iterator?**
- An iterable can produce an iterator; an iterator keeps iteration state and yields the next value.

**52. What is range()?**
- range() represents an immutable sequence-like range of integers and is commonly used in loops.

**53. What is enumerate()?**
- enumerate() yields pairs containing an index and an item while iterating.

**54. What is zip()?**
- zip() combines multiple iterables into tuples containing corresponding elements.

**55. What is map()?**
- map() applies a function to each item of an iterable and returns an iterator.

**56. What is filter()?**
- filter() returns an iterator containing items for which a predicate is true.

**57. What is sorted()?**
- sorted() returns a new sorted list without modifying the original iterable.

**58. What is sort()?**
- list.sort() sorts a list in place and returns None.

**59. What is a shallow copy?**
- A shallow copy creates a new outer object but keeps references to nested objects.

**60. What is a deep copy?**
- A deep copy recursively copies nested objects using copy.deepcopy().

**61. How do you copy a list?**
- Common approaches are list.copy(), list(original), original[:], or copy.copy(original).

**62. What is unpacking?**
- Unpacking assigns elements from an iterable to multiple names, such as a, b = [1, 2].

**63. What is starred unpacking?**
- Using * or ** collects or expands multiple values, such as first, *rest = values.

**64. What are operators?**
- Operators are symbols or keywords used to perform operations on values.

**65. What is the difference between == and is?**
- == compares values for equality; is checks whether two references point to the same object.

### 3. Operators, Conditions, Loops & Functions

**66. What are logical operators?**
- and, or, and not are Python's logical operators.

**67. What are membership operators?**
- in and not in test whether a value is contained in an object.

**68. What are identity operators?**
- is and is not test object identity.

**69. What is operator precedence?**
- It determines the order in which operators are evaluated.

**70. What is if/elif/else?**
- They provide conditional branching based on Boolean expressions.

**71. What is a for loop?**
- A for loop iterates over items of an iterable.

**72. What is a while loop?**
- A while loop repeatedly executes while its condition remains true.

**73. What does break do?**
- break exits the nearest loop immediately.

**74. What does continue do?**
- continue skips the rest of the current loop iteration.

**75. What does pass do?**
- pass performs no operation and is useful as a placeholder.

**76. What is a loop else clause?**
- The else block of a loop runs when the loop finishes normally, not when it exits via break.

**77. What is a function?**
- A function is a reusable block of code defined with def.

**78. Why use functions?**
- Functions improve reuse, organization, testing, readability, and maintainability.

**79. What is a parameter?**
- A parameter is a name in a function definition that receives an argument.

**80. What is an argument?**
- An argument is a value supplied when calling a function.

**81. What are default arguments?**
- They are parameter values used when the caller does not provide that argument.

**82. What are keyword arguments?**
- They pass values by parameter name, such as greet(name='Sam').

**83. What are positional arguments?**
- They pass values based on their position in the function call.

**84. What is *args?**
- *args collects extra positional arguments into a tuple.

**85. What is **kwargs?**
- **kwargs collects extra keyword arguments into a dictionary.

**86. What is return?**
- return exits a function and optionally sends a value back to the caller.

**87. What happens if a function has no return?**
- It implicitly returns None.

**88. What is a lambda?**
- A lambda is a small anonymous function expression, such as lambda x: x * 2.

**89. What is recursion?**
- Recursion is when a function calls itself until a base condition is reached.

**90. What is a docstring?**
- A docstring is a string used to document a module, class, or function.

**91. What is variable scope?**
- Scope determines where a name can be accessed.

**92. What is LEGB?**
- LEGB stands for Local, Enclosing, Global, and Built-in lookup order.

**93. What is global?**
- global declares that assignments inside a function should target a module-level name.

**94. What is nonlocal?**
- nonlocal lets a nested function rebind a name from an enclosing function scope.

**95. What is a module?**
- A module is a Python file containing definitions and executable statements.

**96. What is a package?**
- A package is a structured collection of Python modules, usually represented by a directory.

**97. What is import?**
- import loads a module or package so its names can be used.

**98. What is from ... import?**
- It imports selected names directly from a module.

**99. What is __name__?**
- It is a special module attribute containing the module's name.

**100. Why use if __name__ == '__main__'?**
- It makes code run only when the file is executed directly, not when imported.

### 4. Modules, Exceptions, Files & Data

**101. What is pip?**
- pip is the standard Python package installer for installing packages from package indexes.

**102. What is PyPI?**
- PyPI is the Python Package Index, a major repository of Python packages.

**103. What is a virtual environment?**
- It is an isolated environment with its own Python installation and packages.

**104. Why use virtual environments?**
- They prevent project dependencies from interfering with one another.

**105. What is requirements.txt?**
- It is a text file commonly used to record project dependencies and versions.

**106. What is an exception?**
- An exception is an event representing an error or unusual condition during execution.

**107. What is try/except?**
- try/except catches and handles specified exceptions.

**108. What is finally?**
- finally contains code that runs whether an exception occurs or not.

**109. What is else in exception handling?**
- The else block runs when the try block completes without raising an exception.

**110. What is raise?**
- raise explicitly raises an exception.

**111. How do you create a custom exception?**
- Define a class that inherits from Exception or another appropriate exception class.

**112. What is assert?**
- assert checks a condition and raises AssertionError if the condition is false.

**113. What is file handling?**
- File handling means opening, reading, writing, and closing files.

**114. Why use with open()?**
- The with statement automatically closes the file even if an exception occurs.

**115. What are common file modes?**
- r reads, w writes and truncates, a appends, x creates, and + enables updating; b selects binary mode.

**116. What is JSON?**
- JSON is a text-based data interchange format commonly handled with Python's json module.

**117. What is serialization?**
- Serialization converts an object or data structure into a storable or transferable representation.

**118. What is deserialization?**
- Deserialization reconstructs data from a serialized representation.

**119. What is pickle?**
- pickle is a Python-specific serialization mechanism for many Python objects.

**120. Why should pickle not be used with untrusted data?**
- Unpickling can execute arbitrary code, so untrusted pickle data should not be loaded.

**121. What is OOP?**
- Object-oriented programming organizes software around objects containing data and behavior.

**122. What is a class?**
- A class is a blueprint or type definition used to create objects.

**123. What is an object?**
- An object is an instance of a class.

**124. What is __init__()?**
- __init__() initializes an object after it is created.

**125. What is self?**
- self conventionally refers to the current instance inside an instance method.

**126. What is inheritance?**
- Inheritance allows a class to derive behavior and attributes from another class.

**127. What is encapsulation?**
- Encapsulation groups data and methods and controls how implementation details are accessed.

**128. What is polymorphism?**
- Polymorphism allows different object types to provide compatible interfaces or behavior.

**129. What is abstraction?**
- Abstraction exposes essential behavior while hiding unnecessary implementation details.

**130. What is method overriding?**
- A subclass provides its own implementation of a method inherited from a parent class.

**131. What is multiple inheritance?**
- A class can inherit from more than one base class.

**132. What is super()?**
- super() provides a convenient way to access methods or attributes from a parent class in inheritance hierarchies.

**133. What is MRO?**
- Method Resolution Order defines the order Python uses to search classes for attributes and methods.

**134. What is a class variable?**
- A class variable is shared by instances unless an instance overrides it with its own attribute.

**135. What is an instance variable?**
- An instance variable belongs to a particular object.

### 5. Object-Oriented Python

**136. What is a static method?**
- A method marked with @staticmethod that does not receive an implicit instance or class argument.

**137. What is a class method?**
- A method marked with @classmethod that receives the class as its first argument, conventionally cls.

**138. What are properties?**
- Properties provide attribute-style access while allowing custom getter, setter, or deleter behavior.

**139. What is a decorator?**
- A decorator wraps or modifies a function or class without changing its core source code.

**140. How do you write a decorator?**
- Define a callable that accepts a function and returns a wrapper or another callable.

**141. What is a generator?**
- A generator is an iterator-producing function or expression that yields values lazily.

**142. What does yield do?**
- yield pauses a generator and produces a value; execution resumes from that point later.

**143. Generator vs list?**
- A generator produces values lazily and usually uses less memory, while a list stores all values immediately.

**144. What is a generator expression?**
- It is a lazy expression similar to a comprehension, using parentheses instead of brackets.

**145. What is a context manager?**
- A context manager controls setup and cleanup around a block, commonly used with with.

**146. What are __enter__ and __exit__?**
- They are methods commonly used to implement a context manager's setup and cleanup behavior.

**147. What are dunder methods?**
- Dunder, or double-underscore, methods are special methods such as __init__, __len__, and __str__ that integrate objects with Python syntax.

**148. What is __str__()?**
- It returns a human-readable string representation of an object.

**149. What is __repr__()?**
- It returns a developer-oriented representation intended to be useful for debugging.

**150. What is hashability?**
- A hashable object has a stable hash value and can be used as a dictionary key or set element.

**151. Why are tuples sometimes hashable?**
- A tuple is hashable when all of its elements are hashable.

**152. What is a closure?**
- A closure is a function that retains access to variables from an enclosing scope.

**153. What is late binding in closures?**
- Free variables in closures are generally looked up when the inner function is called, not when it is defined.

**154. What is a namespace?**
- A namespace is a mapping from names to objects.

**155. What is garbage collection?**
- Python manages memory automatically using reference counting in CPython plus cyclic garbage collection.

**156. What is reference counting?**
- In CPython, objects track references to them; when the count reaches zero, the object can usually be deallocated.

**157. What is the GIL?**
- In standard CPython, the Global Interpreter Lock historically allows only one thread at a time to execute Python bytecode within a process.

**158. Does the GIL prevent all concurrency?**
- No. Threads can still overlap during I/O, and multiprocessing provides separate processes. Modern Python versions also have optional/free-threaded builds.

**159. Threading vs multiprocessing?**
- Threading is useful for many I/O-bound tasks; multiprocessing can use multiple CPU cores for CPU-bound work.

**160. What is asyncio?**
- asyncio provides asynchronous, cooperative concurrency using event loops, coroutines, and await.

**161. What is async?**
- async defines a coroutine function that can suspend and resume during asynchronous execution.

**162. What is await?**
- await pauses a coroutine until an awaitable completes, allowing other tasks to run.

**163. What is a coroutine?**
- A coroutine is an awaitable computation, commonly created by calling an async def function.

**164. What is a race condition?**
- A race condition occurs when program behavior depends on the timing of concurrent operations.

**165. What is a lock?**
- A lock is a synchronization primitive used to protect shared resources from conflicting concurrent access.

**166. What is a deadlock?**
- A deadlock occurs when concurrent tasks wait indefinitely for resources held by one another.

**167. What is time complexity?**
- Time complexity describes how an algorithm's running time grows with input size.

**168. What is Big O notation?**
- Big O describes an upper-bound growth rate, commonly used to express algorithmic complexity.

**169. Average lookup complexity of a dictionary?**
- Dictionary lookup is O(1) on average, though worst-case behavior can differ.

**170. Average membership complexity of a set?**
- Set membership is O(1) on average.

### 6. Advanced Python & Concurrency

**171. List append complexity?**
- Appending to the end of a Python list is amortized O(1).

**172. List insertion at the beginning complexity?**
- Inserting at index 0 is O(n) because existing elements must be shifted.

**173. What is binary search?**
- Binary search repeatedly halves a sorted search space and runs in O(log n) time.

**174. What is a stack?**
- A stack follows LIFO: last in, first out.

**175. What is a queue?**
- A queue follows FIFO: first in, first out.

**176. How can you implement a stack in Python?**
- A list with append() and pop() is a common simple stack implementation.

**177. How can you implement a queue efficiently?**
- Use collections.deque with append() and popleft().

**178. What is collections.deque?**
- deque is a double-ended queue optimized for fast appends and pops from both ends.

**179. What is collections.Counter?**
- Counter is a dictionary-like class for counting hashable objects.

**180. What is defaultdict?**
- defaultdict supplies a default value when a missing key is accessed.

**181. What is namedtuple?**
- namedtuple creates tuple subclasses whose fields can be accessed by name; collections.namedtuple is the classic implementation.

**182. What is dataclass?**
- dataclasses.dataclass generates common methods for classes primarily used to store data.

**183. What is an Enum?**
- Enum provides symbolic named constants represented as members of an enumeration.

**184. What is structural pattern matching?**
- match and case provide pattern-based branching introduced in Python 3.10.

**185. What is type hinting?**
- Type hints annotate expected types to improve readability and enable static analysis tools.

**186. Are type hints enforced at runtime?**
- Usually no. Standard Python does not automatically enforce annotations at runtime.

**187. What is Optional in typing?**
- Optional[T] traditionally means a value may be T or None; in modern Python, T | None is preferred.

**188. What is a Protocol?**
- typing.Protocol supports structural subtyping, allowing objects to satisfy an interface based on available members.

**189. What is duck typing?**
- Duck typing focuses on whether an object supports the required operations rather than its explicit class.

**190. What is static type checking?**
- A tool such as mypy or pyright analyzes type annotations without running the program.

**191. What is unit testing?**
- Unit testing verifies small pieces of code, such as individual functions, in isolation.

**192. What is unittest?**
- unittest is Python's built-in unit testing framework.

**193. What is pytest?**
- pytest is a popular third-party testing framework known for concise test syntax and rich plugins.

**194. What is mocking?**
- Mocking replaces a dependency with a controlled test double so behavior can be tested in isolation.

**195. What is logging?**
- Logging records diagnostic and operational information about a program.

**196. Why use logging instead of print?**
- Logging supports levels, formatting, handlers, filtering, and configurable output.

**197. What is debugging?**
- Debugging is the process of finding and fixing defects in software.

**198. What is pdb?**
- pdb is Python's built-in debugger.

**199. What is profiling?**
- Profiling measures program performance to identify slow or resource-intensive parts.

**200. What is cProfile?**
- cProfile is Python's built-in deterministic profiler.

**201. What is memoization?**
- Memoization caches function results so repeated calls with the same inputs can be faster.

**202. What is functools.lru_cache?**
- It provides an LRU cache decorator for storing results of function calls.

**203. What is functools.wraps?**
- wraps preserves useful metadata from the wrapped function when implementing decorators.

**204. What is functools.partial?**
- partial creates a new callable with some arguments pre-filled.

**205. What is itertools?**
- itertools provides efficient iterator-building tools such as chain, product, combinations, and groupby.

**206. What is contextlib?**
- contextlib provides utilities for creating and working with context managers.

**207. What is pathlib?**
- pathlib provides object-oriented filesystem path handling.

**208. What is os module used for?**
- os provides operating-system interfaces such as environment variables, directories, and process-related operations.

**209. What is sys module used for?**
- sys exposes interpreter and runtime information such as command-line arguments and import paths.

**210. What is subprocess?**
- subprocess lets Python create and interact with operating-system processes.

**211. What is environment variable?**
- An environment variable is external configuration stored by the operating system and accessible to programs.

**212. How should secrets be stored?**
- Keep secrets outside source code, commonly in environment variables or a dedicated secret manager.

**213. What is SQL injection?**
- SQL injection is a vulnerability where untrusted input changes a database query's intended meaning.

**214. How can SQL injection be prevented?**
- Use parameterized queries or prepared statements and avoid building SQL with untrusted string concatenation.

**215. What is REST API?**
- A REST API is a web API style that commonly uses HTTP methods and resource-oriented URLs.

**216. How can Python call an API?**
- Libraries such as urllib.request or third-party clients such as requests can send HTTP requests.

**217. What is serialization with JSON vs pickle?**
- JSON is language-independent and safer for untrusted data formats; pickle is Python-specific and unsafe for untrusted input.

**218. What is an ORM?**
- An ORM maps database records to programming-language objects, reducing the need to write raw SQL for many operations.

**219. What is Flask?**
- Flask is a lightweight Python web framework.

**220. What is Django?**
- Django is a batteries-included Python web framework with features such as routing, ORM, authentication, and administration.

**221. What is FastAPI?**
- FastAPI is a modern Python framework for building APIs using type hints and ASGI.

**222. What is ASGI?**
- ASGI is an interface specification for asynchronous-capable Python web applications and servers.

**223. What is WSGI?**
- WSGI is the traditional synchronous interface between Python web applications and web servers.

**224. What is NumPy?**
- NumPy is a library for numerical computing with efficient multidimensional arrays and vectorized operations.

**225. What is pandas?**
- pandas provides data structures and tools for data analysis, especially Series and DataFrame.

**226. What is a DataFrame?**
- A pandas DataFrame is a two-dimensional labeled data structure with rows and columns.

**227. What is machine learning?**
- Machine learning uses algorithms that learn patterns from data to make predictions or decisions.

**228. Why is Python widely used in AI?**
- It has a large ecosystem including NumPy, pandas, scikit-learn, PyTorch, TensorFlow, and many specialized libraries.

**229. What is virtualenv?**
- virtualenv is a tool for creating isolated Python environments; Python also includes venv in the standard library.

**230. What is venv?**
- venv creates lightweight isolated Python environments.

### 7. Performance, Algorithms & Testing

**231. What is pyproject.toml?**
- pyproject.toml is a standardized project configuration file used by Python packaging and tooling.

**232. What is a wheel?**
- A wheel is a built Python distribution format designed for faster installation.

**233. What is an sdist?**
- An sdist is a source distribution containing source files used to build/install a package.

**234. What is semantic versioning?**
- Semantic versioning commonly uses MAJOR.MINOR.PATCH to communicate compatibility expectations.

**235. What is dependency management?**
- Dependency management tracks and installs the external packages a project requires.

**236. What is monkey patching?**
- Monkey patching dynamically replaces or modifies attributes or functions at runtime.

**237. What is metaprogramming?**
- Metaprogramming means writing code that creates, modifies, or reasons about other code.

**238. What is a metaclass?**
- A metaclass is the class of a class and controls aspects of class creation.

**239. What is __slots__?**
- __slots__ can restrict instance attributes and may reduce memory usage by avoiding a normal per-instance __dict__.

**240. What is descriptor protocol?**
- Descriptors define objects that customize attribute access through methods such as __get__, __set__, and __delete__.

**241. What is dynamic attribute access?**
- Functions such as getattr(), setattr(), hasattr(), and delattr() allow attribute access by name at runtime.

**242. What is import caching?**
- Imported modules are normally cached in sys.modules so repeated imports do not reload the module from scratch.

**243. What is circular import?**
- A circular import occurs when modules depend on each other during import, potentially causing partially initialized modules or ImportError.

**244. How do you avoid circular imports?**
- Refactor shared code, move imports inside functions when appropriate, and reduce unnecessary module coupling.

**245. What is a namespace package?**
- A namespace package allows portions of a package to be distributed across multiple directories.

**246. What is the difference between copy and deepcopy?**
- copy.copy creates a shallow copy; copy.deepcopy recursively copies nested objects.

**247. What is a frozen dataclass?**
- A dataclass with frozen=True prevents normal attribute assignment after initialization.

**248. What is immutability useful for?**
- Immutable values are easier to reason about, safer to share, and often suitable as dictionary keys when hashable.

**249. What is caching?**
- Caching stores previously computed or retrieved data so future access can be faster.

**250. What is lazy evaluation?**
- Lazy evaluation delays computation until its result is actually needed.

**251. What is eager evaluation?**
- Eager evaluation computes a value immediately rather than delaying it.

**252. What is a callable?**
- An object is callable if it can be invoked using parentheses; callable(obj) checks this.

**253. Can functions be objects in Python?**
- Yes. Functions are first-class objects and can be assigned, passed, returned, and stored in collections.

**254. What does first-class function mean?**
- It means functions can be treated like other values, including being passed as arguments and returned from functions.

**255. What is higher-order function?**
- A higher-order function accepts functions as arguments, returns functions, or both.

**256. What is a pure function?**
- A pure function produces the same output for the same inputs and has no observable side effects.

**257. What is side effect?**
- A side effect is an observable change outside a function's returned value, such as modifying global state or writing a file.

**258. What is dependency injection?**
- Dependency injection supplies a component's dependencies from outside instead of having the component construct them itself.

**259. What is SOLID?**
- SOLID is a set of five object-oriented design principles: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion.

**260. What is DRY?**
- DRY means Don't Repeat Yourself: avoid unnecessary duplication of logic or knowledge.

**261. What is KISS?**
- KISS means Keep It Simple, Stupid: prefer simple solutions when they adequately solve the problem.

**262. What is YAGNI?**
- YAGNI means You Aren't Gonna Need It: avoid implementing speculative features before they are needed.

**263. What is clean code?**
- Clean code is readable, understandable, maintainable, and focused on clear responsibilities.

**264. What is technical debt?**
- Technical debt is the future cost created by shortcuts or design choices that make later changes harder.

**265. What is an API?**
- An API is an interface that defines how software components communicate and use each other's functionality.

**266. What is backward compatibility?**
- Backward compatibility means newer software continues to support existing clients, interfaces, or data where promised.

**267. What is semantic error?**
- A semantic error produces incorrect behavior even though the program may run without a syntax error.

**268. What is syntax error?**
- A syntax error means the source code does not follow Python's grammar and cannot be parsed normally.

**269. What is runtime error?**
- A runtime error occurs while the program is executing, often represented by an exception.

**270. What is TypeError?**
- TypeError occurs when an operation or function receives an inappropriate type of object.

**271. What is ValueError?**
- ValueError occurs when a value has the correct general type but an inappropriate value.

**272. What is KeyError?**
- KeyError occurs when a dictionary key is not found.

**273. What is IndexError?**
- IndexError occurs when a sequence index is outside the valid range.

**274. What is AttributeError?**
- AttributeError occurs when an object does not have the requested attribute.

**275. What is ImportError?**
- ImportError occurs when an import cannot be completed, such as when a requested name cannot be imported.

**276. What is ModuleNotFoundError?**
- ModuleNotFoundError is a subclass of ImportError raised when a module cannot be found.

**277. What is ZeroDivisionError?**
- ZeroDivisionError occurs when division or modulo by zero is attempted.

**278. What is StopIteration?**
- StopIteration signals that an iterator has no more values.

**279. What is a traceback?**
- A traceback shows the call stack and location of an unhandled exception.

**280. What is exception chaining?**
- Exception chaining records a relationship between exceptions using raise ... from or implicit context.

**281. What is EAFP?**
- EAFP means Easier to Ask Forgiveness than Permission: try an operation and handle exceptions when necessary.

**282. What is LBYL?**
- LBYL means Look Before You Leap: check conditions before performing an operation.

**283. EAFP vs LBYL?**
- Python often favors EAFP when attempting the operation and handling expected exceptions is simpler and race-safe.

**284. What is Python's walrus operator?**
- The := operator assigns a value to a name as part of an expression.

**285. What is the match-case statement?**
- match-case performs structural pattern matching and can replace some complex conditional logic.

**286. What is the walrus operator useful for?**
- It can avoid repeating a computation while assigning its result inside an expression.

**287. What are positional-only parameters?**
- Parameters before / in a function signature can only be passed positionally.

**288. What are keyword-only parameters?**
- Parameters after * in a function signature must be passed by keyword.

**289. What is a positional-only parameter marker?**
- A / in a function definition separates positional-only parameters from other parameters.

**290. What is a keyword-only marker?**
- A * in a function definition separates positional parameters from keyword-only parameters.

**291. What is unpacking in function calls?**
- Use * to expand an iterable into positional arguments and ** to expand a mapping into keyword arguments.

**292. What is Python's default argument evaluation behavior?**
- Default argument expressions are evaluated once when the function is defined, not on every call.

**293. Why are mutable default arguments risky?**
- A mutable default is shared between calls, which can unintentionally preserve state.

**294. How do you safely use a mutable default?**
- Use None as the default and create the mutable object inside the function.

**295. What is a namespace collision?**
- It occurs when names unintentionally overlap and one definition hides another.

**296. What is shadowing?**
- Shadowing occurs when a local or inner-scope name has the same name as a name in an outer scope.

**297. What is monkey patching commonly used for?**
- It can be useful in tests or controlled runtime customization, but excessive use can make code harder to understand.

**298. What is dependency inversion?**
- High-level code should depend on abstractions rather than concrete low-level implementations.

**299. What is the Liskov Substitution Principle?**
- Subtypes should be usable wherever their base types are expected without breaking required behavior.

**300. What is the Single Responsibility Principle?**
- A class or module should have one primary reason to change.

### 8. Web, Security, Packaging & Modern Python

**301. What is the Open/Closed Principle?**
- Software entities should be open for extension but closed for modification.

**302. What is Interface Segregation Principle?**
- Clients should not be forced to depend on methods they do not use.

**303. What is an abstract base class?**
- An ABC defines a common interface and can require subclasses to implement abstract methods.

**304. What is abc module?**
- The abc module supports abstract base classes and abstract methods.

**305. What is @abstractmethod?**
- It marks a method that concrete subclasses are expected to implement.

**306. What is protocol-oriented design in Python?**
- It focuses on supported behavior and interfaces rather than requiring a particular inheritance hierarchy.

**307. What is structural typing?**
- Structural typing considers whether an object has the required members instead of requiring explicit inheritance.

**308. What is serialization format choice important?**
- Choose formats based on interoperability, security, performance, schema needs, and data types.

**309. What is a database connection pool?**
- A connection pool reuses database connections to reduce the overhead of repeatedly creating connections.

**310. What is transaction?**
- A transaction groups database operations into a unit that can be committed or rolled back.

**311. What is ACID?**
- ACID describes database transaction properties: Atomicity, Consistency, Isolation, and Durability.

**312. What is caching in web applications?**
- Caching stores reusable results such as pages, API responses, or database data to reduce latency and load.

**313. What is rate limiting?**
- Rate limiting restricts how frequently a client can perform an operation.

**314. What is authentication?**
- Authentication verifies who a user or system is.

**315. What is authorization?**
- Authorization determines what an authenticated user or system is allowed to do.

**316. What is hashing?**
- Hashing transforms data into a fixed-size digest using a hash function.

**317. Hashing vs encryption?**
- Hashing is generally one-way; encryption is designed to be reversible with the appropriate key.

**318. What is a salt in password hashing?**
- A salt is unique random data added before password hashing to make precomputed attacks harder.

**319. Should passwords be encrypted?**
- Passwords should normally be stored as salted, slow password hashes rather than reversible encryption.

**320. What is input validation?**
- Input validation checks that incoming data meets expected type, format, range, and business rules.

**321. What is command injection?**
- Command injection occurs when untrusted input is interpreted as operating-system commands.

**322. How can command injection be reduced?**
- Avoid shell execution with untrusted strings, validate inputs, and use safe subprocess argument lists.

**323. What is a virtual machine?**
- A virtual machine is a runtime or simulated computer environment; in Python, the Python virtual machine executes bytecode.

**324. What is implementation-defined behavior?**
- It is behavior determined by a particular Python implementation rather than guaranteed identically by the language specification.

**325. What is the Python standard library?**
- It is the collection of modules distributed with Python for common tasks.

**326. What is third-party package?**
- A package developed outside Python's standard library and installed separately.

**327. What is source control?**
- Source control tracks changes to code and enables collaboration and version history.

**328. Why use Git with Python projects?**
- Git provides version history, branching, collaboration, and rollback for source code.

**329. What is CI?**
- Continuous Integration automatically builds and tests changes as they are integrated.

**330. What is CD?**
- Continuous Delivery or Deployment automates preparing or releasing software after validation.

**331. What makes Python code production-ready?**
- Clear design, tests, error handling, security, logging, dependency management, performance awareness, documentation, and maintainability.

**332. How do you improve Python performance?**
- Choose appropriate algorithms and data structures first, then profile and optimize actual bottlenecks.

**333. When should Python code be optimized?**
- Optimize measured bottlenecks after correctness and maintainability are established, unless performance requirements are known in advance.

**334. What is premature optimization?**
- Premature optimization is optimizing before understanding whether performance is actually a problem.

**335. What is profiling before optimization?**
- Profiling identifies where execution time or resources are actually being spent.

**336. What is vectorization?**
- Vectorization performs operations over whole arrays or collections using optimized underlying implementations instead of explicit Python loops.

**337. What is multiprocessing useful for?**
- It can provide true parallel execution across CPU cores for suitable CPU-bound workloads.

**338. What is I/O-bound work?**
- I/O-bound work spends significant time waiting for files, networks, databases, or other external systems.

**339. What is CPU-bound work?**
- CPU-bound work spends most of its time performing computation.

**340. What is parallelism?**
- Parallelism means multiple computations execute at the same time, often across CPU cores.

**341. What is concurrency?**
- Concurrency means multiple tasks make progress during overlapping periods, not necessarily at exactly the same instant.

**342. What is thread-safe code?**
- Thread-safe code behaves correctly when accessed concurrently by multiple threads under the intended synchronization model.

**343. What is a semaphore?**
- A semaphore controls access to a resource using a counter representing available permits.

**344. What is a future?**
- A Future represents a result that may become available later, commonly used with concurrent execution.

**345. What is concurrent.futures?**
- It provides high-level interfaces for asynchronously executing callables with thread or process pools.

**346. What is ThreadPoolExecutor?**
- It executes callables using a pool of worker threads.

**347. What is ProcessPoolExecutor?**
- It executes callables using a pool of worker processes.

**348. What is serialization overhead in multiprocessing?**
- Objects often need to be serialized to move between processes, which adds time and memory overhead.

**349. What is shared memory?**
- Shared memory lets multiple processes access a common memory region, with synchronization needed for safe updates.

**350. What is an event loop?**
- An event loop schedules and coordinates asynchronous tasks and I/O callbacks.

**351. What is non-blocking I/O?**
- Non-blocking I/O allows a program to continue handling other work instead of waiting synchronously for an I/O operation.

**352. What is backpressure?**
- Backpressure is a mechanism that prevents producers from overwhelming consumers when processing rates differ.

**353. What is a retry strategy?**
- A retry strategy attempts a failed operation again under controlled conditions, often with limits and exponential backoff.

**354. What is exponential backoff?**
- It increases the wait time between repeated retries to reduce load and collision during transient failures.

**355. What is idempotency?**
- An operation is idempotent when repeating it has the same intended effect as performing it once.

**356. What is a singleton?**
- A singleton is a design where only one instance of a component is intended to exist; it should be used cautiously.

**357. What is factory pattern?**
- A factory centralizes object creation so callers do not need to know construction details.

**358. What is strategy pattern?**
- The strategy pattern encapsulates interchangeable algorithms behind a common interface.

**359. What is dependency inversion useful for testing?**
- Depending on abstractions makes it easier to replace real dependencies with test doubles.

**360. What is code smell?**
- A code smell is a design or implementation symptom suggesting possible maintainability problems.

**361. What is refactoring?**
- Refactoring changes internal code structure without intentionally changing its external behavior.

**362. What is regression?**
- A regression is a previously working behavior that becomes broken after a change.

**363. What is integration testing?**
- Integration testing verifies that multiple components work correctly together.

**364. What is end-to-end testing?**
- End-to-end testing validates a complete user or system workflow across multiple components.

**365. What is test coverage?**
- Test coverage measures which parts of code are exercised by tests; high coverage does not guarantee high quality.

**366. What is a fixture?**
- A fixture provides reusable setup data or resources for tests.

**367. What is parametrized testing?**
- It runs the same test logic against multiple input cases.

**368. What is linting?**
- Linting analyzes source code for style issues, suspicious patterns, and possible errors.

**369. What is formatting?**
- Formatting automatically applies consistent source-code layout rules.

**370. What is Black?**
- Black is a popular opinionated Python code formatter.

**371. What is Ruff?**
- Ruff is a fast Python linter and formatter that covers many common Python code-quality checks.

**372. What is mypy?**
- mypy is a static type checker for Python.

**373. What is Pyright?**
- Pyright is a static type checker for Python with strong editor integration.

**374. What is documentation?**
- Documentation explains how code works, how to use it, and important design or operational details.

**375. What is a README?**
- A README introduces a project and explains how to understand, install, use, or contribute to it.

**376. What is a Python package index?**
- A package index is a repository from which Python packages can be discovered and installed.

**377. What is reproducible environment?**
- A reproducible environment can recreate the same dependency and runtime setup reliably.

**378. What is containerization?**
- Containerization packages an application and its dependencies into an isolated, portable runtime environment.

**379. What is Docker commonly used for with Python?**
- Docker can package Python applications with their runtime and dependencies for consistent deployment.

**380. What is dependency pinning?**
- Dependency pinning specifies exact or controlled versions to improve reproducibility.

### 9. Coding Interview Revision

**381. What is a lock file?**
- A lock file records resolved dependency versions and related metadata for reproducible installations.

**382. What is packaging?**
- Python packaging is the process of structuring, building, distributing, and installing Python software.

**383. What is an entry point?**
- An entry point defines how a package exposes executable commands or plugin integrations.

**384. What is a CLI?**
- A command-line interface lets users interact with a program through terminal commands and arguments.

**385. What is argparse?**
- argparse is Python's standard-library module for parsing command-line arguments.

**386. What is sys.argv?**
- sys.argv is a list containing command-line arguments passed to a Python program.

**387. What is input()?**
- input() reads a line of text from standard input and returns it as a string.

**388. What is print()?**
- print() writes values to standard output, typically the terminal.

**389. What is f-string conversion syntax?**
- Expressions inside f-strings can use conversion flags such as !r, !s, and !a.

**390. What is repr()?**
- repr() returns a developer-oriented string representation of an object.

**391. What is str()?**
- str() returns a human-readable string representation of an object.

**392. What is bytes?**
- bytes is an immutable sequence of integers representing byte values.

**393. What is bytearray?**
- bytearray is a mutable sequence of bytes.

**394. What is encoding?**
- Encoding converts text characters into bytes using a character encoding such as UTF-8.

**395. What is decoding?**
- Decoding converts bytes into text using a specified character encoding.

**396. Why is UTF-8 common?**
- UTF-8 can represent Unicode text and is backward compatible with ASCII for standard ASCII characters.

**397. What is a regular expression?**
- A regular expression is a pattern language for searching, matching, and transforming text.

**398. What is re module?**
- The re module provides regular-expression operations in Python.

**399. What is greedy matching?**
- A greedy quantifier tries to match as much text as possible while still allowing the overall pattern to succeed.

**400. What is non-greedy matching?**
- A non-greedy quantifier tries to match as little text as possible while still allowing the overall pattern to succeed.

**401. What is global state?**
- Global state is data accessible across multiple parts of a program and can make behavior harder to reason about.

**402. Why avoid excessive global variables?**
- They increase coupling and make testing, reasoning, and maintenance more difficult.

**403. What is dependency coupling?**
- Coupling describes how strongly software components depend on one another.

**404. What is cohesion?**
- Cohesion describes how closely related the responsibilities inside a component are.

**405. High cohesion vs low coupling?**
- Good design generally aims for highly focused components with minimal unnecessary dependencies between them.

**406. What is separation of concerns?**
- It divides a system into parts with distinct responsibilities.

**407. What is an interface?**
- An interface describes the operations and behavior that a component exposes to its users.

**408. What is API versioning?**
- API versioning manages changes so clients can continue working while new API behavior is introduced.

**409. What is graceful degradation?**
- It means providing a reduced but useful behavior when part of a system is unavailable.

**410. What is observability?**
- Observability uses logs, metrics, traces, and related signals to understand system behavior.

**411. What are metrics?**
- Metrics are numerical measurements such as request rate, latency, errors, or resource usage.

**412. What are traces?**
- Traces follow a request or operation across components to help identify latency and failures.

**413. What is structured logging?**
- Structured logging records fields in a machine-readable format such as JSON.

**414. What is a health check?**
- A health check reports whether an application or dependency is operating sufficiently for its intended purpose.

**415. What is graceful shutdown?**
- Graceful shutdown stops accepting new work and finishes or safely cancels existing work before exiting.

**416. What is signal handling?**
- Signal handling lets a program respond to operating-system signals such as termination requests.

**417. What is portability?**
- Portability is the ability for software to work across different operating systems or environments with minimal changes.

**418. What is cross-platform Python?**
- Python code that uses portable language features and libraries can often run on Windows, macOS, and Linux.

**419. What is implementation compatibility?**
- It means code behaves consistently across Python implementations where the language and library contracts guarantee it.

**420. What is a breaking change?**
- A breaking change can cause existing users or integrations to stop working without adaptation.

**421. What is deprecation?**
- Deprecation marks a feature as discouraged or scheduled for removal while giving users time to migrate.

**422. What is a release candidate?**
- A release candidate is a near-final build intended for final testing before a release.

**423. What is LTS?**
- Long-term support describes a release maintained with fixes for an extended period.

**424. What is semantic versioning in Python packages?**
- Many Python projects use MAJOR.MINOR.PATCH conventions, though each project defines its own compatibility policy.

**425. What is a coding interview?**
- A coding interview evaluates programming knowledge, problem solving, debugging, design, and communication.

**426. How should you approach a Python coding interview?**
- Clarify requirements, discuss edge cases, choose an appropriate approach, explain complexity, code clearly, and test the solution.

**427. What should you do before writing interview code?**
- Understand the input/output requirements, constraints, assumptions, and expected edge cases.

**428. Why discuss time and space complexity?**
- It shows awareness of scalability and helps compare alternative solutions.

**429. What are common Python interview topics?**
- Data structures, functions, OOP, exceptions, iterators, generators, decorators, comprehensions, concurrency, testing, and algorithms.

**430. How do you reverse a string in Python?**
- Use slicing: s[::-1].

**431. How do you find duplicates in a list?**
- Use a set or collections.Counter depending on whether you need counts.

**432. How do you remove duplicates while preserving order?**
- Use dict.fromkeys(items) for hashable items, or a custom seen set for more control.

**433. How do you check if a string is a palindrome?**
- Compare the string with its reverse, such as s == s[::-1].

**434. How do you count character frequencies?**
- Use collections.Counter(text).

**435. How do you swap two variables?**
- Use tuple unpacking: a, b = b, a.

**436. How do you find the largest value in a list?**
- Use max(values) when the list is non-empty.

**437. How do you find the second-largest distinct value?**
- Track distinct values or use a sorted set-like approach; choose based on constraints rather than blindly sorting.

**438. How do you merge two dictionaries?**
- Use {**a, **b} or a | b in Python 3.9+; later keys override earlier ones.

**439. How do you safely access a dictionary key?**
- Use dict.get(key, default) when a missing key should not raise KeyError.

**440. How do you iterate over dictionary keys and values?**
- Use for key, value in d.items().

**441. How do you sort a list of objects by a field?**
- Use sorted(items, key=lambda x: x.field).

**442. How do you sort in descending order?**
- Use sorted(items, reverse=True).

**443. How do you flatten a simple nested list?**
- Use a nested comprehension such as [x for row in rows for x in row].

**444. How do you check whether two lists share an element?**
- For hashable values, compare their sets or use a seen set depending on requirements.

**445. How do you find common elements between sets?**
- Use set_a & set_b.

**446. How do you find the union of sets?**
- Use set_a | set_b.

**447. How do you find elements only in the first set?**
- Use set_a - set_b.

**448. How do you handle missing dictionary values?**
- Use get(), setdefault(), or defaultdict depending on the desired behavior.

**449. How do you read a large file efficiently?**
- Iterate over the file object line by line instead of loading the entire file into memory.

**450. How do you process a CSV file?**
- Use Python's csv module or a library such as pandas when data-analysis features are needed.

**451. How do you parse JSON?**
- Use json.loads() for a string or json.load() for a file.

**452. How do you write JSON?**
- Use json.dumps() for a string or json.dump() for a file.

**453. How do you catch multiple exceptions?**
- Use except (TypeError, ValueError): or separate except clauses when handling differs.

**454. Why catch specific exceptions?**
- It prevents unrelated errors from being hidden and makes error handling more predictable.

**455. What is the best way to handle cleanup?**
- Use context managers such as with for resources that need deterministic cleanup.

**456. How do you make a function reusable?**
- Give it a focused responsibility, clear parameters, predictable return values, and minimal hidden state.

**457. How do you make Python code maintainable?**
- Use clear names, small focused functions, tests, documentation, consistent formatting, and appropriate abstractions.

**458. What is the difference between list and generator comprehension?**
- A list comprehension creates all results immediately; a generator expression produces them lazily.

**459. What is the difference between append and extend?**
- append adds one object as a single element; extend adds each element from an iterable.

**460. What is the difference between remove and pop?**
- remove deletes the first matching value; pop removes and returns an item by index.

**461. What is the difference between discard and remove for sets?**
- set.remove raises KeyError if absent; set.discard does nothing if absent.

**462. What is the difference between del and pop?**
- del removes without returning a value; pop removes and returns an item where supported.

**463. What is the difference between copy and assignment?**
- Assignment binds another name to the same object; copy creates a new outer object.

**464. What is the difference between is and == for None?**
- Use is None because None is a singleton and identity is the intended test.

**465. Why should you avoid using == True?**
- Boolean conditions are clearer as if condition:, and truthiness handles non-boolean values appropriately.

**466. What is truthiness?**
- Objects can be evaluated as true or false in Boolean contexts according to their truth-value rules.

**467. Which common values are falsey?**
- False, None, numeric zero values, empty strings, and empty collections are falsey.

**468. What is short-circuit evaluation?**
- and and or may stop evaluating once the final truth value is determined.

**469. What does x or default do?**
- It returns x if x is truthy; otherwise it returns default.

**470. What does x and y do?**
- It returns x if x is falsey; otherwise it evaluates and returns y.

**471. Can Python functions return multiple values?**
- Yes. Multiple expressions are returned as a tuple, which the caller can unpack.

**472. Can a function accept another function?**
- Yes. Functions are first-class objects and can be passed as arguments.

**473. Can classes be passed as arguments?**
- Yes. Classes are objects and can be passed, stored, or returned like other values.

**474. What is object composition?**
- Composition builds objects from other objects rather than relying primarily on inheritance.

**475. Composition vs inheritance?**
- Composition often provides more flexible relationships; inheritance is useful when a genuine subtype relationship exists.

**476. What is an abstract interface?**
- It defines expected behavior without requiring callers to depend on implementation details.

**477. What is duck typing in interviews?**
- Explain that Python commonly relies on supported behavior rather than requiring exact types.

**478. What is clean exception handling?**
- Catch only exceptions you can handle, add useful context, and avoid silently swallowing failures.

**479. What is fail fast?**
- Fail fast means detecting invalid conditions early rather than allowing bad state to propagate.

**480. What is defensive programming?**
- It anticipates invalid inputs, unexpected states, and failures while preserving clear behavior.

**481. What is code review?**
- Code review is a structured examination of changes to identify defects, improve design, and share knowledge.

**482. What should you look for in a Python code review?**
- Correctness, edge cases, readability, complexity, security, tests, error handling, maintainability, and unnecessary duplication.

**483. What is the most important Python interview skill?**
- The ability to reason clearly, communicate trade-offs, write correct code, and explain why the solution fits the requirements.

## Suggested Usage

1. Start with the fundamentals.
2. Try answering each question before reading the answer.
3. Practice the coding questions separately.
4. Revisit advanced topics after completing the basics.
5. Add your own notes and examples as you learn.

## Goal

Build a strong understanding of Python instead of memorizing answers. In interviews, focus on explaining **why** a solution works, its trade-offs, edge cases, and time/space complexity.

---

**Python • Learn → Practice → Revise → Interview Ready 🚀**