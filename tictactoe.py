import http.server
import json
import webbrowser
import threading

PORT = 8080

HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Tic Tac Toe</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-family: 'Segoe UI', Arial, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: #fff;
  }
  h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
  #status {
    font-size: 1.3rem;
    margin-bottom: 1rem;
    min-height: 2rem;
  }
  .board {
    display: grid;
    grid-template-columns: repeat(3, 120px);
    grid-template-rows: repeat(3, 120px);
    gap: 6px;
    background: rgba(255,255,255,0.15);
    padding: 6px;
    border-radius: 12px;
  }
  .cell {
    width: 120px;
    height: 120px;
    background: rgba(255,255,255,0.9);
    border: none;
    border-radius: 8px;
    font-size: 3rem;
    font-weight: bold;
    cursor: pointer;
    transition: all 0.15s;
    color: #333;
  }
  .cell:hover:not(.taken) {
    background: #fff;
    transform: scale(1.05);
  }
  .cell.taken { cursor: default; }
  .cell.x { color: #2563eb; }
  .cell.o { color: #dc2626; }
  .cell.win { background: #86efac; transform: scale(1.05); }
  #reset {
    margin-top: 1.5rem;
    padding: 12px 32px;
    font-size: 1.1rem;
    border: 2px solid #fff;
    background: transparent;
    color: #fff;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s;
  }
  #reset:hover { background: #fff; color: #764ba2; }
</style>
</head>
<body>
  <h1>Tic Tac Toe</h1>
  <div id="status">Player X's turn</div>
  <div class="board" id="board"></div>
  <button id="reset" onclick="resetGame()">New Game</button>
<script>
  let board = Array(9).fill('');
  let current = 'X';
  let gameOver = false;
  const lines = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
  ];
  const boardEl = document.getElementById('board');
  const statusEl = document.getElementById('status');

  function render() {
    boardEl.innerHTML = '';
    board.forEach((val, i) => {
      const btn = document.createElement('button');
      btn.className = 'cell' + (val ? ` taken ${val.toLowerCase()}` : '');
      btn.textContent = val;
      btn.onclick = () => makeMove(i);
      boardEl.appendChild(btn);
    });
  }

  function makeMove(i) {
    if (board[i] || gameOver) return;
    board[i] = current;
    const winner = checkWinner();
    if (winner) {
      gameOver = true;
      statusEl.textContent = `Player ${winner} wins!`;
      render();
      winner && lines.forEach(([a,b,c]) => {
        if (board[a] && board[a]===board[b] && board[b]===board[c]) {
          [a,b,c].forEach(idx => boardEl.children[idx].classList.add('win'));
        }
      });
      return;
    }
    if (!board.includes('')) {
      gameOver = true;
      statusEl.textContent = "It's a draw!";
      render();
      return;
    }
    current = current === 'X' ? 'O' : 'X';
    statusEl.textContent = `Player ${current}'s turn`;
    render();
  }

  function checkWinner() {
    for (const [a,b,c] of lines) {
      if (board[a] && board[a]===board[b] && board[b]===board[c]) return board[a];
    }
    return null;
  }

  function resetGame() {
    board = Array(9).fill('');
    current = 'X';
    gameOver = false;
    statusEl.textContent = "Player X's turn";
    render();
  }

  render();
</script>
</body>
</html>"""


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(HTML.encode())

    def log_message(self, format, *args):
        pass  # suppress logs


def main():
    server = http.server.HTTPServer(("localhost", PORT), Handler)
    print(f"Tic Tac Toe running at http://localhost:{PORT}")
    print("Press Ctrl+C to quit")
    threading.Timer(0.5, lambda: webbrowser.open(f"http://localhost:{PORT}")).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nBye!")
        server.server_close()


if __name__ == "__main__":
    main()
