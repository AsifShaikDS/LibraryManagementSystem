# Library Management System

A console application for managing books, users and checkouts, written to practise layered
design in Python rather than to solve a hard problem.

## Design

Three layers, each with one job:

```
main.py                 menu loop and dispatch
managers/               book, user and checkout operations
models/                 Book, User, Checkout
storage/storage.py      JSON load and save
```

`Storage` is the only module that touches the filesystem. It serialises via each object's
`__dict__` and reconstructs typed objects on load, so the managers work with `Book` and `User`
instances and never with dictionaries. Every operation writes to `library_management.log`
through the standard `logging` module — including the rejected ones, which is what makes the
log worth reading.

## Features

- **Users** — add and authenticate.
- **Books** — add, list, and check availability. Duplicate ISBNs are rejected rather than
  silently overwritten.
- **Checkouts** — check out and check in, with availability updated on both sides.

## Running it

```bash
python main.py
```

No dependencies beyond the standard library. Data persists to `books.json`, `users.json` and
`checkouts.json` in the working directory; they are created on first write.

## What I would do differently

**The managers ask for their own input.** `BookManager.add_book()` calls `input()` directly,
which means the domain layer owns the user interface. The consequence shows up the moment you
want anything other than this one console: the logic cannot be called from a web handler, and
it cannot be tested without simulating keystrokes. `add_book(title, author, isbn)` returning a
result — and `main.py` doing the prompting — is the same code with the dependency pointing
the right way. Almost every other item below follows from this one.

**`Storage._dict_to_object` guesses types from which keys are present.** A dict with `isbn`
and no `user_id` becomes a `Book`; add a field to one model and the branch that matches
changes underneath you. The type belongs in the serialised data, or each collection should
have its own loader that already knows what it is reading.

**Every save rewrites the whole file, and a crash mid-write truncates it.** Writing to a
temporary file and replacing the original makes the write atomic. There is also no locking,
so two processes would silently overwrite each other.

**There are no tests**, which is the direct cost of the first point. With the managers taking
arguments, the duplicate-ISBN rule, the availability transitions and the checkout round trip
are a short unit test file.

**Committed files that should not be in version control:** `__pycache__/`, the log, and the
three JSON data files. A `.gitignore` and a small seed script instead.

**No IDs on checkouts and no dates enforced**, so there is no way to distinguish two loans of
the same book, and nothing prevents a check-in for a book that was never checked out. A real
version needs a checkout identifier and the state machine written down.
