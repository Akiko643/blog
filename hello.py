from flask import Flask
app = Flask(__name__)

snake_html = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Snake</title>
    <script src="https://cdn.jsdelivr.net/npm/p5@1.1.9/lib/p5.js"></script>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div id="score">0</div>
    <!-- <script src="sketch.js"></script>
    <script src="snake.js"></script> -->
    <script>
      function Food(x, y) {
        this.x = x;
        this.y = y;
        this.show = () => {
          fill(100, 250, 100);
          rect(this.x * scl, this.y * scl, scl, scl);
        };
      }

      function Snake(x, y) {
        //   this.x = x;
        //   this.y = y;
        this.xdir = 1;
        this.ydir = 0;
        //   this.tails = [];
        this.X = [];
        this.X.push(x);
        this.Y = [];
        this.Y.push(y);
        this.food;
        //   console.log(this.X, this.Y);
        this.show = () => {
          fill(200, 50, 150);
          rect(this.X[0] * scl, this.Y[0] * scl, scl, scl);
          fill(250, 100, 200);
          for (let i = 1; i < this.X.length; i++) {
            rect(this.X[i] * scl, this.Y[i] * scl, scl, scl);
          }
          // rect(this.x * scl, this.y * scl, scl, scl);
        };

        this.move = () => {
          for (let i = this.X.length - 1; i > 0; i--) {
            this.X[i] = this.X[i - 1];
            this.Y[i] = this.Y[i - 1];
          }
          this.X[0] = (this.X[0] + this.xdir + 30) % 30;
          this.Y[0] = (this.Y[0] + this.ydir + 30) % 30;
        };
        this.updir = (x, y) => {
          this.xdir = x;
          this.ydir = y;
        };
        this.death = () => {
          // let dis;
          for (let i = 1; i < this.X.length; i++) {
            let dis = dist(this.X[0], this.Y[0], this.X[i], this.Y[i]);
            console.log(dis, 'distance');
            if (dis < 1) {
              let text = 'Your score is ';
              text += score;
              alert(text);
              let len = this.X.length;
              for (let j = 1; j < len; j++) {
                this.X.pop();
                this.Y.pop();
              }
              score = 0;
              document.getElementById('score').innerText = score;
              return;
            }
          }
        };
        this.eat = () => {
          if (this.X[0] == this.food.x && this.Y[0] == this.food.y) {
            this.X.push(this.food.x);
            this.Y.push(this.food.y);
            this.generate();
            score++;
            document.getElementById('score').innerText = score;
          }
        };

        this.generate = () => {
          let x = Math.floor(Math.random() * 30),
            y = Math.floor(Math.random() * 30);
          console.log(x, y);
          if (x == this.x && y == this.y) {
            this.generate();
            return;
          }
          for (let i = 0; i < this.X.length; i++) {
            if (this.X[i] == x && this.Y[i] == y) {
              this.generate();
              return;
            }
          }
          this.food = new Food(x, y);
        };
      }
      let scl = 20,
        h = scl * 30,
        w = scl * 30,
        cnt = 0,
        score = document.getElementById('score').innerText;

      let snake;

      function setup() {
        createCanvas(h, w);
        fill(50);
        snake = new Snake(8, 8);
        snake.generate();
      }

      function draw() {
        background(100);
        frameRate(12);
        snake.show();
        snake.food.show();
        frameRate(12 + score / 2);
        //   if (cnt == 5) {
        snake.move();
        snake.death();
        snake.eat();
        // cnt %= 5;
        //   }
        //   cnt++;
        //   rect(8 * scl, 8 * scl, scl, scl);
        //   snake.death();
      }

      function keyPressed() {
        if (snake.xdir != 1 && keyCode == LEFT_ARROW) {
          snake.updir(-1, 0);
        }
        if (snake.xdir != -1 && keyCode == RIGHT_ARROW) {
          snake.updir(1, 0);
        }
        if (snake.ydir != -1 && keyCode == DOWN_ARROW) {
          snake.updir(0, 1);
        }
        if (snake.ydir != 1 && keyCode == UP_ARROW) {
          snake.updir(0, -1);
        }
      }
    </script>
  </body>
</html>

'''

@app.route('/snake')
def hello_world():
    return snake_html