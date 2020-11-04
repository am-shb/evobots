### Instructions
These files are created based on the instructions available here
<https://www.reddit.com/r/ludobots/wiki/pyrosim/quadruped>

### How to run
```
python parallelHillclimber.py
```

### Objects

| Obj |    X   |    Y   |   Z   | Shape |     |      | r1 | r2 | r3 |  r  |  g  |  b  |
|:---:|:------:|:------:|:-----:|:-----:|:---:|:----:|:--:|:--:|:--:|:---:|:---:|:---:|
|  O0 |    0   |    0   |  L+R  |  l=L  | w=L | h=2R |    |    |    | 0.5 | 0.5 | 0.5 |
|  O1 |    0   |    L   |  L+R  |  l=L  | r=R |      |  0 |  1 |  0 |  1  |  0  |  0  |
|  O2 |    L   |    0   |  L+R  |  l=L  | r=R |      |  1 |  0 |  0 |  0  |  1  |  0  |
|  O3 |    0   |    -L  |  L+R  |  l=L  | r=R |      |  0 |  1 |  0 |  0  |  0  |  1  |
|  O4 |    -L  |    0   |  L+R  |  l=L  | r=R |      |  1 |  0 |  0 |  1  |  0  |  1  |
|  O5 |    0   |  1.5L  | L/2+R |  l=L  | r=R |      |  0 |  0 |  1 |  1  |  0  |  0  |
|  O6 |  1.5L  |    0   | L/2+R |  l=L  | r=R |      |  0 |  0 |  1 |  0  |  1  |  0  |
|  O7 |    0   |  -1.5L | L/2+R |  l=L  | r=R |      |  0 |  0 |  1 |  0  |  0  |  1  |
|  O8 |  -1.5L |    0   | L/2+R |  l=L  | r=R |      |  0 |  0 |  1 |  1  |  0  |  1  |

### Joints

| Joint | 1st_O | 2nd_O |    X   |    Y   |  Z  | n1 | n2 | n3 |
|:-----:|:-----:|:-----:|:------:|:------:|:---:|:--:|:--:|:--:|
|   J0  |   0   |   1   |    0   |   L/2  | L+R | -1 |  0 |  0 |
|   J1  |   1   |   5   |    0   |  1.5L  | L+R | -1 |  0 |  0 |
|   J2  |   0   |   2   |   L/2  |    0   | L+R |  0 |  1 |  0 |
|   J3  |   2   |   6   |  1.5L  |    0   | L+R |  0 |  1 |  0 |
|   J4  |   0   |   3   |    0   |   -L/2 | L+R |  1 |  0 |  0 |
|   J5  |   3   |   7   |    0   |  -1.5L | L+R |  1 |  0 |  0 |
|   J6  |   0   |   4   |   -L/2 |    0   | L+R |  0 | -1 |  0 |
|   J7  |   4   |   8   |  -1.5L |    0   | L+R |  0 | -1 |  0 |

### Results
(click on giphs for full video)
#### Video 1
[![quadruped1](https://j.gifs.com/vlVJRg.gif)](https://www.youtube.com/watch?v=wFxerCKnwjU&list=PLGOvUx2-xFjlMaDiUEBhRU6gBggwJrozB&index=7)

#### Video 2
[![quadruped2](https://j.gifs.com/zvZlQ7.gif)](https://www.youtube.com/watch?v=xnqehx_pvcA&list=PLGOvUx2-xFjlMaDiUEBhRU6gBggwJrozB&index=8)

#### Video 3
[![quadruped3](https://j.gifs.com/D14E6Y.gif)](https://www.youtube.com/watch?v=ngjPvs5SEPU&list=PLGOvUx2-xFjlMaDiUEBhRU6gBggwJrozB&index=9)

#### Video 4
[![quadruped4](https://j.gifs.com/P74Jgl.gif)](https://www.youtube.com/watch?v=yRjnbaC0pRI&list=PLGOvUx2-xFjlMaDiUEBhRU6gBggwJrozB&index=10)

#### Video 5
[![quadruped5](https://j.gifs.com/2xVJ2P.gif)](https://www.youtube.com/watch?v=bkqVWigzA5M&list=PLGOvUx2-xFjlMaDiUEBhRU6gBggwJrozB&index=11)

#### Video 6
[![quadruped6](https://j.gifs.com/VA6Zo9.gif)](https://www.youtube.com/watch?v=vyrVRXyAL8M&list=PLGOvUx2-xFjlMaDiUEBhRU6gBggwJrozB&index=12)

#### Video 7
[![quadruped7](https://j.gifs.com/XL4Vql.gif)](https://www.youtube.com/watch?v=9h-9772nXZo&list=PLGOvUx2-xFjlMaDiUEBhRU6gBggwJrozB&index=13)