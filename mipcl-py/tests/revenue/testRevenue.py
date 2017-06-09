#!/usr/bin/python
from revenue import Revenue

# for each plane type:
#     (Number of planes,  f   (q1, r1),  (q2, r2), (q3, r3))
planes = [
  (2, 75000, (35, 10), (40, 10), (60, 10))
]

# for each of 3 periods:
#     in each of 3 options:
#         prices of tickets of each of 3 classes
options = [
 ((1500, 1000, 500), (1250,  850, 400), (1000,  700, 300)),
 ((1750, 1250, 700), (1500, 1000, 500), (1250,  850, 400)),
 ((1800,  800, 450), (1200,  850, 500), ( 900,  600, 450))
]

# (No., period, parent, Probability, (Demands for Option 1), (Demands for Option 2), (Demands for Option 3))
nodes = [
 ( 0, 0),
 ( 1, 1,  0, 0.1,  ( 25,  40, 100), ( 30,  50, 120), ( 35,  70, 130)),
 ( 2, 1,  0, 0.6,  ( 40,  90, 100), ( 50,  85, 100), ( 70,  90, 140)),
 ( 3, 1,  0, 0.3,  ( 90,  90, 110), (100,  95, 105),  (120,  95, 135)),
 ( 4, 2,  1, 0.1,  ( 40,  85, 100), ( 50,  90, 105), ( 65,  85, 125)),
 ( 5, 2,  1, 0.6,  ( 20, 100, 120), ( 80, 120, 130), (100, 160, 180)),
 ( 6, 2,  1, 0.3,  (100,  40,  25), (110,  60,  80), (160, 100, 120)),
 ( 7, 2,  2, 0.1,  ( 40,  85, 100), ( 50,  90, 105), ( 65,  85, 125)),
 ( 8, 2,  2, 0.6,  ( 20, 100, 120), ( 80, 120, 130), (100, 160, 180)),
 ( 9, 2,  2, 0.3,  (100,  40,  25), (110,  60,  80), (160, 100, 120)),
 (10, 2,  3, 0.1,  ( 40,  85, 100), ( 50,  90, 105), ( 65,  85, 125)),
 (11, 2,  3, 0.6,  ( 20, 100, 120), ( 80, 120, 130), (100, 160, 180)),
 (12, 2,  3, 0.3,  (100,  40,  25), (110,  60,  80), (160, 100, 120)),
 (13, 3,  4, 0.1,  ( 60,  80, 100), ( 70, 100, 120), ( 80, 110, 160)),
 (14, 3,  4, 0.6,  ( 60,  20, 100), ( 80,  80, 120), (120,  90, 140)),
 (15, 3,  4, 0.3,  (100,  80, 120), (140,  90, 130), (160, 120, 140)),
 (16, 3,  5, 0.1,  ( 60,  80, 100), ( 70, 100, 120), ( 80, 110, 160)),
 (17, 3,  5, 0.6,  ( 60,  20, 100), ( 80,  80, 120), (120,  90, 140)),
 (18, 3,  5, 0.3,  (100,  80, 120), (140,  90, 130), (160, 120, 140)),
 (19, 3,  6, 0.1,  ( 60,  80, 100), ( 70, 100, 120), ( 80, 110, 160)),
 (20, 3,  6, 0.6,  ( 60,  20, 100), ( 80,  80, 120), (120,  90, 140)),
 (21, 3,  6, 0.3,  (100,  80, 120), (140,  90, 130), (160, 120, 140)),
 (22, 3,  7, 0.1,  ( 60,  80, 100), ( 70, 100, 120), ( 80, 110, 160)),
 (23, 3,  7, 0.6,  ( 60,  20, 100), ( 80,  80, 120), (120,  90, 140)),
 (24, 3,  7, 0.3,  (100,  80, 120), (140,  90, 130), (160, 120, 140)),
 (25, 3,  8, 0.1,  ( 60,  80, 100), ( 70, 100, 120), ( 80, 110, 160)),
 (26, 3,  8, 0.6,  ( 60,  20, 100), ( 80,  80, 120), (120,  90, 140)),
 (27, 3,  8, 0.3,  (100,  80, 120), (140,  90, 130), (160, 120, 140)),
 (28, 3,  9, 0.1,  ( 60,  80, 100), ( 70, 100, 120), ( 80, 110, 160)),
 (29, 3,  9, 0.6,  ( 60,  20, 100), ( 80,  80, 120), (120,  90, 140)),
 (30, 3,  9, 0.3,  (100,  80, 120), (140,  90, 130), (160, 120, 140)),
 (31, 3, 10, 0.1,  ( 60,  80, 100), ( 70, 100, 120), ( 80, 110, 160)),
 (32, 3, 10, 0.6,  ( 60,  20, 100), ( 80,  80, 120), (120,  90, 140)),
 (33, 3, 10, 0.3,  (100,  80, 120), (140,  90, 130), (160, 120, 140)),
 (34, 3, 11, 0.1,  ( 60,  80, 100), ( 70, 100, 120), ( 80, 110, 160)),
 (35, 3, 11, 0.6,  ( 60,  20, 100), ( 80,  80, 120), (120,  90, 140)),
 (36, 3, 11, 0.3,  (100,  80, 120), (140,  90, 130), (160, 120, 140)),
 (37, 3, 12, 0.1,  ( 60,  80, 100), ( 70, 100, 120), ( 80, 110, 160)),
 (38, 3, 12, 0.6,  ( 60,  20, 100), ( 80,  80, 120), (120,  90, 140)),
 (39, 3, 12, 0.3,  (100,  80, 120), (140,  90, 130), (160, 120, 140))
]

prob = Revenue("test1")
prob.model(planes,options,nodes)
prob.optimize()
prob.printSolution()

