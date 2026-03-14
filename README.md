# Tic Tac Toe

A two-player Tic Tac Toe game built with Python. Runs as a local web app in your browser — no dependencies required.

## Features

- Two-player gameplay (X vs O)
- Color-coded moves (blue for X, red for O)
- Winning line highlighted in green
- Draw detection
- New Game button to reset

## Requirements

- Python 3.6+

## Usage

```bash
python3 tictactoe.py
```

The game will automatically open in your browser at `http://localhost:8080`. Press `Ctrl+C` in the terminal to stop the server.

## How It Works

The app uses Python's built-in `http.server` module to serve a self-contained HTML/CSS/JS game — no external libraries or frameworks needed.
