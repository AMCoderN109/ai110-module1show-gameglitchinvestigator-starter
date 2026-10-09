# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? 
It gave a number like 99, and the hint said to go higher even though the bounds are between 1 and 100. Another case is when I run out of attempts and click "New Game"—it resets the attempts left counter, but I get an error that the game is over and it doesn't let me start a new game. Also, when you have one last attempt, it tells you the secret number and that your score is zero when you still have one last attempt left, not when you have zero attempts.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
Three concrete bugs are that the hints say the opposite: when you submit a high number, it says to go higher even when it's out of bounds, and it does the same in the opposite direction. The second bug is when you click "New Game," it doesn't start a new game; it just freezes with a warning that the game is over and only resets the counter. However, if you click "New Game" while you still have a few attempts left during the first play, it just resets the counter to continue the first game. The third error is when you reach 1 attempt left, you get the message that you are out of attempts instead of at zero attempts left. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|2  | Go higher | Go lower |none|
|99 | Go lower | Go higher |none|
|Attempts left: 1, submit guess| allow you to input one last number to guess | Out of attempts! The scret was... Score:... |none|
|click the start new game button |To just start guessing the eight attempts all over again | just resets the counter and provide an message of game over. Start a new game to try again |Freezes can't play again |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude code within the VS Code. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
What the AI suggested to fix one of the bugs in the code was for the hint messages. The AI suggested that we swap the hint messages. For instance, the bug was when you input a guess of, let's say, 5, the message we would get was "go lower" instead of "go higher." So, I decided that the AI should do the swap of the hint messages. I checked if the code was correct in two ways: running python -m pytest in the VS Code terminal, and going to the live website game. I first looked at the developer debug info to see what the secret number was. At the time of the test, it was 67, and then I tested numbers around it like 80—I got the correct hint message of "go lower," and the same when inputting 35, I got the hint message of "go higher." 
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
An AI suggestion to fix another bug that appeared after the hint message bug fix. The new bug was the attempt counter being off and accepting attempts that weren't made or submitted. I chose not to do the AI suggestion to fix it because I wanted to fix one bug at a time, not try to do multiple at once and lose track. Doing one bug fix at a time also makes it easier to test if the first bug work or not before confusing it with another.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided how the hint message bug was fixed in two ways. First, I asked Claude to make a test scenario for the hint message fix code. Then, in the new folder added to the test folder, I ran python -m pytest in the VS Code terminal, which gave no errors and said all eight tests ran. That told me that the AI test worked. To double-verify, I ran the web game to see it for myself in action. At the time of the test, I got 67 as my number, and tested with 80 and 35. I got the correct hint messages when I did that.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I ran both the manual test on the website game and pytest in the VS Code terminal. I'll describe the terminal test. After asking the AI to do the fix, I also asked it to create some tests. Then, I used the terminal in VS Code to run python -m pytest. When it was done running, it gave me no errors and said all eight tests ran. It showed me that the code the AI suggested for the fix was the right move, because when I double-checked manually on the website, I didn't have the reverse hint message for either a high or low number when guessing.
- Did AI help you design or understand any tests? How?
Yes, the AI helped design tests for the bug fix. The AI wrote 5 different tests to include with the 3 already-made tests. The tests scoped for normal guesses like 40, 50, and 60, and out-of-range guesses like 200 and -5. Then, the AI ran the tests first to see if their 5 tests combined with the 3 previous tests of the program would work. Then, I would use the terminal in VS Code with the command python -m pytest to check if all eight tests passed.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
