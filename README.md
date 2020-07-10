# MSG / get in it: Coding Challenge Code & Win
The task was to write a program that finds the best possible tour from .msg HQ in Munich through all other .msg site's back to Munich.
See also [here](https://www.get-in-it.de/coding-challenge)

# Questions
The following questions had to be answered for the challenge
## Why I chose the algorithm I chose (Held-Karp-Algorithm)
After realizing that this challenge is not about finding the minimum path from A to B and then realizing
that a brute force approach won't give me a solution in time, I decided to use Held-Karp as it 
significantly reduces the time needed to find the best path (but still finds it in all cases). 
For me personally it was also the most approachable algorithm and helped my in improving my dynamic programming skills. 

## Solution
1 Ismaning/Munchen (Hauptsitz)\
12 Ingolstadt\
16 Nurnberg\
20 Stuttgart\
19 St. Georgen\
4 Bretten\
21 Walldorf\
8 Frankfurt\
13 Koln/Hurth\
6 Dusseldorf\
7 Essen\
15 Munster\
14 Lingen (Ems)\
18 Schortens/Wilhelmshaven\
10 Hamburg\
11 Hannover\
3 Braunschweig\
2 Berlin\
9 Gorlitz\
5 Chemnitz\
17 Passau\
1 Ismaning/Munchen (Hauptsitz)

Minimum possible distance is: 2333.046 km\
(Please note: I used the Haversine formula to calculate distances, so the absolute distance might be slighty off. It can be
improved by using packages like geopy. I decided not to use any non-native packages so it is easier to run.)

## To run this programm 
You need to have Python 3.7.4 (it might also work on older versions, but I only tested it on 3.7.4.)

Download this repository, unzip it and open your terminal in the directory you unzipped it to. 
Type 
```
python calc_distance.py
```

The programm will run and print the solution after a few minutes. 









