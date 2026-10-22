# CampusBike - Git exercise

This repository is the starting point for the Lecture 8 Git exercise in Software Engineering.
You work in pairs: Person A and Person B.

The full steps are in the exercise sheet. This page is a short overview.

## What is in here

`campusbike.py` is a small program with a few settings and a price function.
Try it:

```
python3 campusbike.py
```

On Windows, use `python` instead of `python3`.

## Getting started

1. **Person A:** click **Fork** (top right) to make your own copy of this repository.
2. **Person A:** on your fork, go to **Settings**, then **Collaborators**, then **Add people**, and add Person B.
3. **Person B:** accept the invitation (check your email or https://github.com/notifications).
4. **Both:** clone **A's fork**, not this repository:

```
git clone https://github.com/A-USERNAME/campusbike-git.git
cd campusbike-git
```

## The five parts

1. Setup (fork, invite, clone)
2. A merge conflict on `main`
3. Two branches that merge cleanly
4. A pull request with a conflict
5. Read the history with `git log --oneline --graph` and `git blame`

## Rules

- Push only to A's fork. You cannot push to this repository.
- Do not open a pull request to this repository. In Part 4, the pull request goes to A's fork: change **base repository** to A's fork.
- Make all changes on your own computer, not in the GitHub web editor.
- Use `git commit -m "message"` so no editor opens.
- Use `git pull --no-rebase` when Git asks how to combine changes.
