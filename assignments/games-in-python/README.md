
# 🎮 Hangman Game Challenge

Build the classic word-guessing game using Python strings, loops, and user input.

## 🎯 Objective

Create a playable Hangman game where players guess letters to reveal a hidden word before running out of attempts. Focus on clear program structure, user-friendly I/O, and handling edge cases.

## ⏱️ Estimated time

- Approximate time to complete: 2–4 hours

## 🔢 Prerequisites

- Basic Python (variables, loops, conditionals, functions)
- Familiarity with reading from files (optional)
- Starter files: `starter-code.py` (provided)

## 🎯 Learning outcomes

After completing this assignment students will be able to:

- Use loops and conditionals to implement game logic
- Manipulate strings and lists to track game state
- Validate user input and handle common edge cases
- (Optional) Write simple unit tests for core functions

---

## 📝 Tasks

Each task contains a description, acceptance criteria and hints. Point totals are suggestions.

### 🛠️ Task 1 — Implement core Hangman (Required)

#### Description

Implement the core Hangman game logic in `starter-code.py`. The program should run in the terminal and allow a single player to guess letters until they win or run out of attempts.

#### Requirements (Acceptance criteria)

Completed submission must satisfy ALL of the following:

- Program randomly selects a secret word from a predefined list (or from `words.txt` if provided).
- Program shows the current progress using underscores and revealed letters (e.g. `_ a _ _ m a n`).
- Program accepts single-letter guesses (case-insensitive) and updates the display.
- Program tracks and displays the number of incorrect guesses remaining.
- Program prevents repeated guesses being counted multiple times and gives helpful feedback for repeated input.
- Game ends when the word is fully guessed (win) or attempts reach zero (lose). The final message shows the correct word.

Example run (truncated):

```
Welcome to Hangman!
_ _ _ _ _
Guess a letter: a
Good guess! _ a _ _ _
Incorrect guesses left: 6
```

Points: 70

#### Hints

- Keep game state (secret word, revealed letters, guessed letters, remaining attempts) in variables or a small class.
- Use `random.choice(words)` to pick a word if you keep a Python list of words.
- Normalize input with `.strip().lower()` and validate it's a single alphabetical character.

---

### 🛠️ Task 2 — Extras & Tests (Optional / Bonus)

#### Description

Add one or more optional features for extra credit, or provide unit tests for core functions.

#### Suggested extras (pick one or more)

- Load words from an external `words.txt` or `data.csv` file.
- Add a simple scoring system or high-score file.
- Implement difficulty levels that change allowed attempts or word selection.
- Provide a simple GUI or web frontend (stretch goal).
- Write unit tests for at least two functions (e.g., `reveal_letters`, `is_game_over`).

Points (bonus): up to 10–20

#### Hints

- For tests, structure core logic into functions so they can be imported by a test file.
- Use `pytest` for simple tests: `assert reveal_letters('apple', ['a','p']) == 'app__'`.

---

## 📦 Deliverables (what to submit)

- `starter-code.py` (or equivalent) containing the game implementation
- (Optional) `words.txt` or `data.csv` if you load words from a file
- `README.md` in the assignment folder with run instructions and any assumptions
- (Optional) `tests/` folder with unit tests if you implemented tests

Include the following in your `README.md`:

- How to run the program (commands)
- Any assumptions you made (word list, difficulty, input format)
- How to run tests (if included)

---

## ✅ Student checklist (before submitting)

- [ ] Code runs without errors and follows the acceptance criteria for Task 1.
- [ ] I included a `README.md` with run instructions.
- [ ] I handled invalid input and repeated guesses.
- [ ] (If requested) I included unit tests and they pass locally.

---

## 🧾 Grading rubric (suggested)

- Correctness & acceptance criteria: 70%
- Code quality & structure: 15%
- Tests & extras (if provided): 10%
- Documentation (README & clear instructions): 5%

---

## 🛠️ Local testing & evaluation

Run program (example):

```
python starter-code.py
```

Run tests (if using pytest):

```
pytest -q
```

---

## 📚 Resources

- Python `random` module docs: https://docs.python.org/3/library/random.html
- pytest quickstart: https://docs.pytest.org/en/stable/quickstart.html

---

## 📨 Submission instructions

Please submit a ZIP or push to the assigned branch with a short message containing:

- Assignment ID: `games-in-python/hangman`
- Your name and student ID
- Files included and how to run

Good luck and have fun!
