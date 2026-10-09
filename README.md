# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The game's purpose is that its a game to guess the number select from a certain selected range. The game was built with streamlit. The player/user has a choice to try guess the secret number with limited attempts, including hints that can be turned off or on. Those hints will help you get the secret number by saying go higher or lower depending on your guessed number and comparing it to how close you are to the secret number. 
- [ ] Detail which bugs you found.
I found three bugs inside the game. One was the hint feedback of a guess number was inverted, for instance, guess a low number and told the player/user to go lower and out of bounds. Second bug was that attempt tracker would end the game at 1 attempt left instead at zero attempts. Third bug was when clicking the "New Game" button it would cause the application to do nothing with a warning that the game is over and only resets the counter.
- [ ] Explain what fixes you applied.
 For the inverted hint message I went to the check_guess function and swapped the messages to the correct orientation. For the attempt tracker, I adjusted the st.session_state.attempts to have the attempt tracker to start from 0 instead of 1, so the player/user has a chance to use all their attempts. For the "New Game" button I set the status of the game to playing, clear the history of the attempts, set the score back to 0, and made the program reselect the secret number from its appropriate range. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The player/user starts up the game; they could either start guess or look at the developer debug info to check on the secret number. The secret number is 59.
2. The player/user enters a guess of 65 and click submit; the game will correctly respond in the hint message box to go lower.
3. The player/user enter a guess of 45 and click submit; the game will correctly response in the hint message box to go higher.
4. One path is that they eventually get the secret number with all or almost all of their guesses and the program gives the player "Correct!" message and "You won! The secret was 59. Final score: 35".
5. The other path is they eventually use all their attempts and the players will get a message of "Out of attempts!The secret was 59. Score: -15".
6. If the player want to replay the game after losing or winning, they can click "New Game" button and it will restart everything including the attempt counter.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
