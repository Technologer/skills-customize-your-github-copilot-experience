
# 📘 Assignment: Games in Python (Hangman)

## 🎯 Objective

Build a playable Hangman game in Python to practice loops, conditionals, string manipulation, and user input.

## 📝 Tasks

### 🛠️ Set Up the Game State

#### Description
Start from the provided starter code and initialize the variables needed to run the game.

#### Requirements
Completed program should:

- Randomly choose a secret word from the provided word list.
- Initialize game state variables, including guessed letters, incorrect guesses, and maximum allowed incorrect guesses.
- Display the word progress using placeholders (for example: `_ _ _ _ _`).

### 🛠️ Implement the Main Game Loop

#### Description
Create the loop that asks the user for guesses, updates the game state, and provides helpful feedback.

#### Requirements
Completed program should:

- Prompt the user to guess one letter at a time.
- Validate input so only a single alphabetic character is accepted.
- Update correctly guessed letters and reveal them in the word progress display.
- Decrease remaining attempts when a guess is incorrect.
- Prevent duplicate guesses from counting as new attempts.

### 🛠️ Finish Conditions and Results

#### Description
Add clear ending conditions so the game stops at the right time and tells the player the result.

#### Requirements
Completed program should:

- End with a win message when the full word is guessed.
- End with a lose message when the player runs out of attempts.
- Reveal the secret word at the end of the game.
- Keep output clear and student-friendly throughout gameplay.
