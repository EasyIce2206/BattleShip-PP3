## Battleships Game

Welcome to the Battleships Game! This is a Python command-line game where you can play the classic game of Battleships against the computer.

### How to Play

- The game is played on a 5x5 grid.
- You and the computer will take turns to guess the location of each other's ships.
- The first player to sink all of the opponent's ships wins the game.

### Features

- Randomly placed ships for both player and computer.
- Input validation to ensure valid moves.
- Clear and concise game messages to guide the player.

### Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/battleships-game.git
    ```
2. Navigate to the project directory:
    ```bash
    cd battleships-game
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Game

To start the game, run the following command:
```bash
python run.py
```

### Deployment on Heroku

To deploy the Battleships Game on Heroku, follow these steps:

1. Create a new Heroku app.
2. Add the following buildpacks in this order:
    1. `heroku/python`
    2. `heroku/nodejs`
3. Create a Config Var called `PORT` and set it to `8000`.
4. Connect your GitHub repository to the Heroku app.
5. Deploy the app.

Enjoy playing Battleships!