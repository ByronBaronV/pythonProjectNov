# Significant Issue: Database Integration
## Problem
When trying to query the database, I encountered a "SQLAlchemy Object Not Bound to Session" error.
## Solution
I realized that I needed to use `db.session.add()` and `db.session.commit()` within an application context. I fixed this by wrapping database operations in `with app.app_context():` blocks.
## Lessons Learned
Always ensure that database operations are performed within the appropriate Flask application context to maintain proper session management.

# Issue: What is SQLAlchemy
## Problem
I didn't know what SQLAlchemy is and what is used for
## Solution
I checked in YouTUbe and realized that 'SQLAlchemy' is a powerful and flexible library for working with databases in Python, allowing us to map database ros and tables to objects in Python.
## Lesson Learned
Always check which libraries are needed for your project and the specific role of each one. This kind of tools are also called Object Relational Mapper (ORM).

# Issue: What is PEP8 Guidelines
## Problem
I was suggested to follow the PEP 8 Style Guidelines 
## Solution
I checked in YouTube for more information on these guidelines and registered the 3 more compelling videos.
## Lesson Learned
I learned that PEP 8 is the official style guide for Python code. It provides coding conventions to improve the readability and consistency of Python code.

# Issue: Backup Strategies