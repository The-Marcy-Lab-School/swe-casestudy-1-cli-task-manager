# Application Investigation

By answering these questions, you will be required to think critically about
how the application is designed and understand WHY it is designed this way.
Your aim should be to:

* learn as much as you can from this application so that you can build an
  application of your own that leverages these same skills
* communicate clearly about the concepts you are using and the decisions you
  make for how you implement them.

**Table of Contents**

- [Investigation Questions](#investigation-questions)
  - [User Interface Design](#user-interface-design)
  - [Data Types](#data-types)
  - [Variables \& Scope](#variables--scope)
  - [Functions](#functions)
  - [Conditional Logic](#conditional-logic)
  - [Modules](#modules)
  - [Looping \& Iteration](#looping--iteration)
  - [Lists and Dictionaries](#lists-and-dictionaries)
  - [Iteration Helpers](#iteration-helpers)
  - [Error Handling and Debugging](#error-handling-and-debugging)
  - [Code Style](#code-style)
- [Extension Opportunities](#extension-opportunities)
  - [Tips](#tips)

## Investigation Questions

### User Interface Design

The user interface is how humans interact with our programs. Even in a simple
command-line application, thoughtful design choices matter. They decide
whether using it feels confusing or feels pleasant.

**Question 1**

Look at the menu display in `show_menu()`. The menu shows numbered options
(1, 2, 3, 4) and asks the user to "Choose an option (1-4)". Why do you think
the menu uses numbers for the options? What are the potential downsides of
having the user type out in words what they would like to do? For example:
"Choose an option: add an item, view tasks, complete a task, exit".

**Question 2**

In the `view_tasks()` function, tasks are displayed with checkboxes: `[x]` for
completed tasks and `[ ]` for incomplete tasks. Do you think this visual
representation is easy to understand? What alternative ways of displaying this
information can you think of?

**Question 3**

Look at the `clear_screen()` call at the end of the `while` loop in
`show_menu()`. It occurs after a final `input()` asking the user to press
Enter. How would the user experience change if we did not clear the screen?
How would it change if we removed the `input()` that comes right before it?

**Question 4**

When a user completes a task, the program shows a message like
`Task "walk the dog" marked as completed!`. Why is it important that the user
sees these messages? How would the user experience change without them?

**My Notes:**

* ...
* ...
* ...

### Data Types

Whether you are designing a new application or learning about an existing one,
we always start by asking: _how is the data represented_? Once we know how to
represent the data, we are better able to design how the application uses and
manipulates it.

**Question 1**

Go to the `tasks.py` file and look at the `tasks` variable. It is a list of
dictionaries. Each dictionary represents a task in the list, with a
`description` string and an `is_complete` boolean. We could also have
represented `is_complete` with the numbers `0` and `1`, or the strings
`"complete"` and `"incomplete"`. If it were up to you, which would you choose
and why?

**Question 2**

In `tasks.py` in the `add_task` function, there is this conditional statement:
`if not description`. What does `not description` evaluate to when
`description` is an empty string, and what is the purpose of this conditional?

**Question 3**

In `menu.py`, the user's chosen task number `task_choice` is converted with
`int()` before being passed to `complete_task`. Why is this necessary? What
does `input()` always give you, no matter what the user types?

**My Notes:**

* ...
* ...
* ...

### Variables & Scope

Understanding where variables are created (their **scope**) and therefore
where they can be reached is crucial for building well-structured
applications.

**Question 1**

In `show_menu()` in `menu.py`, the variable `is_running` starts as `True` and
is set to `False` when the user chooses Exit. Trace what happens to the loop
the moment that assignment runs. Why does the loop not stop immediately at
that line?

**Question 2**

In `show_menu()`, look at the `task_choice` variable. We could have written
the code without it:

```python
complete_task(int(input("Enter task number to complete: ")) - 1)
```

What are the tradeoffs of these two approaches? Which one would you rather
debug?

**Question 3**

Look at the `tasks` list in `tasks.py`. What is the scope of the `tasks`
variable? What would happen if we moved it inside one of the functions? Why
would that break the application?

**My Notes:**

* ...
* ...
* ...

### Functions

Functions are the building blocks of reusable code. They let us break a
complex problem into smaller, manageable pieces and avoid repeating ourselves.

**Question 1**

In `menu.py`, look at how the `input()` function is called. Based on what you
see, how many parameters does it seem to take? If you were the designer of
that function, what name would you give its parameter?

**Question 2**

What if the programmer had written all the task logic directly in `menu.py`
instead of creating separate functions? For example, imagine copying the body
of `clear_tasks()` directly to where it is called:

```python
elif menu_choice == "3":
    tasks.clear()
    print("\nAll tasks cleared!")
```

Would this code even work as written? What would `menu.py` need in order for
it to work, and what are the downsides of doing this for every task function?

**Question 3**

What if we combined all the task functions (`add_task`, `complete_task`,
`view_tasks`, `clear_tasks`) into one giant function called
`handle_task_operations()`? What parameters would it need in order to cover
every operation?

**My Notes:**

* ...
* ...
* ...

### Conditional Logic

Conditional statements let a program behave differently depending on its
state. Without them, a program would run exactly the same way every time.

**Question 1**

In `menu.py`, `show_menu()` uses `if` / `elif` to handle the menu choices.
What would happen if every branch were a separate `if` instead? Trace what
happens when a user enters "1".

**Question 2**

Look at `add_task()` in `tasks.py`. The first lines check `if not description`
and return early. This is called a "guard clause". What would happen if we
removed it and a user added a task with no description?

**Question 3**

Look at `view_tasks()`. It checks `if len(tasks) == 0` before displaying
anything. What would the user see if we removed that check and the list was
empty?

**My Notes:**

* ...
* ...
* ...

### Modules

A module is a file containing code that can be imported and used elsewhere.
Rather than writing everything in one file, this project splits the code into
three modules: `main.py`, `menu.py`, and `tasks.py`. The result is called
"separation of concerns".

**Question 1**

Look at the top of `menu.py`. You will see `add_task` imported from `tasks`.
What would happen if we called `add_task()` in `menu.py` without that import?
Why do we have to import it explicitly?

**Question 2**

In `menu.py`, the import names four functions but **not** the `tasks` list
itself. Nothing stops us importing it, since `tasks.py` defines it at module
level. Why do you think the programmer chose not to?

**Question 3**

If we wanted to add a feature letting the user mark every task complete at
once, how would you split that work across the modules?

**My Notes:**

* ...
* ...
* ...

### Looping & Iteration

Loops take repetitive work and boil it down to a process that repeats without
retyping the same code. Choosing the right loop and making sure it terminates
are crucial skills.

**Question 1**

Look at `show_menu()` in `menu.py`. A `while is_running` loop keeps the menu
going until the user exits. What would happen if we forgot to set
`is_running = False` for option 4?

**Question 2**

Why is a `while` loop the right choice for the menu, rather than a `for` loop?

**Question 3**

What would happen if we changed the condition to `while True` and removed
`is_running` entirely? What would you need instead to get out of the loop?

**My Notes:**

* ...
* ...
* ...

### Lists and Dictionaries

Lists and dictionaries are the two most common ways to build collections.
A list is a good choice for a group of similar values. A dictionary is a good
way to represent one thing with several pieces of data attached.

**Question 1**

The whole collection is a list of task dictionaries, each with
`"description"` and `"is_complete"` keys. Suppose we represented tasks as a
list of strings instead, like `["walk the dog", "take out the trash"]`. What
are the tradeoffs?

**Question 2**

What other ideas do you have for telling complete and incomplete tasks apart?

**My Notes:**

* ...
* ...
* ...

### Iteration Helpers

Python gives you tools that handle the bookkeeping of looping so you can
focus on what happens each time round.

**Question 1**

In `view_tasks()` in `tasks.py`, the loop is
`for index, task in enumerate(tasks, start=1)`. What is `enumerate` giving
you that a plain `for task in tasks` would not? What does `start=1` change,
and why does this program want it?

**Question 2**

The loop variable is called `task`. What would happen if we renamed it to
`item` or `t`? Would the code still work the same way? Would it read the same
way?

**Question 3**

The line that builds the checkbox uses a conditional expression:
`mark = "x" if task["is_complete"] else " "`. Rewrite that as a regular
`if`/`else` block. Which version do you prefer here, and why?

**My Notes:**

* ...
* ...
* ...

### Error Handling and Debugging

Real applications have to handle unexpected situations gracefully.
Anticipating and responding to bad input is essential for building software
that does not fall over.

**Question 1**

What happens when the user types letters where a number is expected? Find the
check in `menu.py` that handles this. What would happen without it?

**Question 2**

Look at `complete_task()` in `tasks.py`. It checks `if task_index < 0`
explicitly. In Python, `tasks[-1]` is perfectly valid and gives you the
**last** item. So what would happen if a user typed `0` and we removed that
check? Would the program crash, or would it do something worse than crash?

**Question 3**

How does the application handle being asked to complete a task that does not
exist?

**Question 4**

What debugging techniques could you use to understand what is happening when
the program does not behave as expected?

**My Notes:**

* ...
* ...
* ...

### Code Style

Code style is the conventions and formatting that make code readable. In most
languages the computer does not care about indentation. **In Python it does**
— indentation is what defines a block.

**Question 1**

Look at the indentation in `tasks.py`. Python uses 4 spaces per level by
convention. Try removing one level of indentation inside a function and run
the program. What is the difference between indentation being a *style*
choice and being a *syntax* rule?

**Question 2**

Find the variables, functions, parameters and dictionary keys in the
application. Do their names clearly describe what they hold or do? What
patterns do you notice? Why does `is_complete` start with `is`?

**Question 3**

How are the imports, functions and blocks organized within each file? Is there
a logical, consistent flow that makes the code easy to follow?

**Question 4**

Why do you think some files live in the `src` folder while others sit at the
root of the project? What is the benefit of that separation?

**My Notes:**

* ...
* ...
* ...

## Extension Opportunities

Now that the core Task Manager app is complete, it is time to add new
features. Pick at least one. If you finish quickly, try more.

* **Toggle Complete**: Right now you can only mark a task complete. Refactor
  the "Complete Task" option so the user can toggle a task between complete
  and incomplete.

* **Delete Task**: Add a menu option to remove a single task from the list.

* **Show Completed Tasks**: Add a menu option that displays only completed
  tasks.

* **Show Incomplete Tasks**: Add a menu option that displays only tasks that
  are not complete.

* **Mark All as Completed**: Add a menu option that marks every task complete.

* **Show Task Stats**: Add a message to `view_tasks` showing how many tasks
  are complete versus incomplete.

* **Data Persistence**: Save the tasks to a `.json` file when the user exits,
  and read them back when the app starts again. Look into the `json` module,
  specifically `json.dump()` and `json.load()`, along with Python's built-in
  `open()` function.

### Tips

- Add a new menu option for each feature you implement.
- Do not delete old functionality — just extend your app.
- Test your feature with at least 3 or 4 tasks to make sure it works.
