# Snake Pro

A simple adaptation of the popular Snake game, built with new challenges and game mechanics. The project is built using Pygame. This readme will be updated as the development progresses.

# Objective
Object-oriented programming (OOP) and interactive applications were my motivations for this project. I like Python’s syntax and structure. Having spent considerable time learning it in this program I decided to do my final project based on it. Snake games have been relatively the same for decades and I decided to try some new ideas in building my version of it.

# How to run
I built this on my Ubuntu WSL terminal. So you have to install Pygame to play it.
```
pip install pygame
```
After installing and cloning the repo, execute ```snake_pro.py``` to run the game.
My intent was to turn it into an installable package using Pyinstaller. Here is a YouTube demo of my progress so far https://youtu.be/LpTHsr_kUus.

# What I have learned
Object-Oriented Programming has its drawbacks. Code can quickly become verbose which makes it harder to keep track of parameter changes. Also renaming variables and functions can be a pain as you have to trace every variable declaration and function call to update them. Executing logic can also be tricky when deciding when and where to make function calls, implement conditions to respond to events, and change parameters. This is probably not an issue for more experienced engineers, but it is nice to notice it as a beginner.

Apps with interactive designs such as games look deceptively simple to do. They are not. Creating events and responses only seem obvious after you get it right, but it involves trying and testing a lot of things repeatedly, sometimes breaking the code too.
