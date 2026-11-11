# Python Basics + Git Activity (one class period)

You will practise the Python from our slides (variables, strings, numbers) and the Git you already learned, at the same time.

## Part A: Get set up (about 10 minutes)

1. Click **Fork** (top right of this page) to copy this repo to your own GitHub account.
2. Clone YOUR fork. Replace `<your-username>` with your GitHub username:

   ```
   git clone https://github.com/<your-username>/python-basics-activity.git
   cd python-basics-activity
   ```
3. Tell Git who you are. Use your REAL full name, because your grade depends on it:

   ```
   git config user.name "Juan Dela Cruz"
   git config user.email "your-github-email@example.com"
   ```
4. Run `git status` and `git log --oneline` to see where you are.

## Part B: Do the three tasks (about 35 minutes)

Open the files in your editor, replace every `# TODO`, and test with:

```
python -m unittest -v
```

| File | Topic | What to do |
|---|---|---|
| `task1_variables.py` | Variables and names | Create variables, swap two values, pick valid names |
| `task2_strings.py` | Strings | Complete 6 small functions |
| `task3_numbers.py` | Numbers and conversion | Complete 6 small functions |

**One commit per task.** When Task 1 passes, commit it before you start Task 2:

```
git add task1_variables.py
git commit -m "Complete task 1: variables"
```

Do the same for `task2_strings.py` and `task3_numbers.py`. Use clear messages. Do NOT edit anything in the `tests` folder.

## Part C: Hand in (about 10 minutes)

1. `git log --oneline` should show at least 3 of your own commits.
2. `git push origin main`
3. On GitHub, open your fork and click **Contribute > Open pull request**.
4. Title the pull request exactly: `Section - Surname, Firstname` (example: `9A - Dela Cruz, Juan`).

## Grading (100 points)

| What | Points |
|---|---|
| Task 1 tests pass | 20 |
| Task 2 tests pass | 20 |
| Task 3 tests pass | 20 |
| One separate commit per task file | 15 |
| Commits made during class time | 10 |
| Pull request title in the right format | 10 |
| Clear commit messages (not empty, not "asdf") | 5 |

Your Git history is part of the grade, so do not squash, rewrite or delete your commits.
