## Keylogger
A simple keylogger for logging keystrokes. Logs are sent via a Discord bot. 

### What is a keylogger?
A keylogger is a type of spyware that records a user's keystrokes and other input actions, such as mouse clicks to capture information.

### How does it work?
1. A Discord bot awaits for inputs such as "start", "stop", and "bye bye."
2. start: Begins listening to user input and outputs the log at set intervals
3. stop: Stops listening to the user
4. bye bye: Turns off the bot

### How can this be improved?
- [ ] Persistence: For windows I could add it to the startup registry key, so it runs on boot.
- [ ] Simplicity: what can be refactored to make the code more efficient?
