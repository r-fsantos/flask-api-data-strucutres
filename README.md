# Data Structures | APIs | Flask

This is a effort-less Flask web application, which main focus is to learn basic data structures and Flask.

In the future, the project itself will be reorganized to fit Clean Architecture, folder and files organization.

## First setup

- Install `sqlite3`, according to the OS;
- Run the following in order to create the local database, then check if it was really crteated.
  ```python
  python3

  from server import db

  db.create_all()
  ```
