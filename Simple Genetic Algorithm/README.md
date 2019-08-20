# Simple Genetic Algorithm
The goal of the project is to start from a jibberish of characters and to make it transform, such that it would find the expected string that was initialized for the project, Speedify 8.0.0!. The following code contains a demo of the following:
1. The code will have a list of A-Z, a-z, 0-9, spaces and special characters
2. From the list it would first initialize a population of 100 random data.
3. The fitness of the population is computed
4. The top 5 of the 100 that are the strongest would then be kept, the others will be swept away
5. The 5 will then mix their strings, chromosomes, together in order to have a crossover.
6. After the crossover happens, there will be some form of mutation
7. Repeat Step 3 to 6 until we match the string


# Code
The code contains:
1. ga_template.py: The template in which the genetic algorithm uses
2. simple_ga_algo.py: The algorithm for the simple genetic algorithm


# Build & Run
To build and run the code:
```
pipenv install
pipenv run python simple_ga_algo.py
```
