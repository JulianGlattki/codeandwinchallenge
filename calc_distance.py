# -*- coding: utf-8 -*-

'''
    get in IT / msg coding challenge "code and win" 
    see https://www.get-in-it.de/coding-challenge?lp=true?utm_source=magazin&utm_medium=advertorial&utm_campaign=coding-challenge-2020#mitmachen


    Please note: 
    The starting city has to have the ID 1 in the input data. 
    The given cities need to be have an ID from 1 to n. 

    Author: Julian Glattki
'''
import csv 
from math import inf, sin, cos, sqrt, atan2, radians
from itertools import chain, combinations

class City: 
    def __init__(self, id, name, street, nr_in_street, zipcode, place, latitude, longitude): 
        self.id = id
        self.name = name
        self.street = street
        self.nr_in_street = nr_in_street
        self.zipcode = zipcode
        self.place = place
        self.latitude = latitude
        self.longitude = longitude

    def get_distance_to(self, city): 
        radius_of_earth = 6370.0 # radius of earth in km 

        diff_longitude = self.longitude - city.longitude
        diff_latitude = self.latitude - city.latitude 

        # haversine formula to calculate the distance between the given coordinates
        a = sin(diff_latitude / 2)**2 + cos(city.latitude) * cos(self.latitude) * sin(diff_longitude / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return radius_of_earth * c
        
    def to_string(self): 
        return "ID: " + str(self.id) + "\n  " + self.name  + "\n  " + self.street + "\n  " + self.nr_in_street + "\n  " + self.zipcode + "\n  " + self.place + "\n-----------------------" 

class Index: 
    def __init__(self, current_vertex, vertex_set): 
        self.current_vertex = current_vertex
        self.vertex_set = vertex_set
    
    def __hash__(self): 
        result = self.current_vertex
        result = 31 * result + (frozenset(self.vertex_set).__hash__() if self.vertex_set is not None else 0)
        return result

def parse_csv_to_cities(): 
    cities = []

    with open('msg_standorte_deutschland.csv') as csvfile: 
        reader = csv.reader(csvfile)
        csvfile.readline()

        for row in reader: 
            cities.append(City(int(row[0]), row[1], row[2], str(row[3]), str(row[4]), row[5], radians(float(row[6])), radians(float(row[7]))))
    
    return cities

def traveling_salesman(adjacency_matrix, cities):
    min_cost_holder = {} # storing the minimum cost for a path 
    parent_holder = {} # storing the last traversed vertex of the path with minimum cost

    all_sets_sorted = generate_all_combinations(len(adjacency_matrix))

    # here we are finding the minimum costs from each vertex 
    # to each set (in which the vertex is not present) 
    for tuple in all_sets_sorted: 
        set_holder = set(tuple) 

        for vertex in range(1, len(adjacency_matrix)):
            if vertex in set_holder: 
                continue

            index = Index(vertex, set_holder)

            min_cost = inf
            min_prev_vertex = 0

            for prev_vertex in set_holder: 
                cost = adjacency_matrix[prev_vertex][vertex] + get_cost(set_holder, prev_vertex, min_cost_holder)

                if cost < min_cost: 
                    min_cost = cost
                    min_prev_vertex = prev_vertex
            
            if len(set_holder) == 0: # this happens for {} i.e. empty set
                min_cost = adjacency_matrix[0][vertex]

            min_cost_holder[index.__hash__()] = min_cost
            parent_holder[index.__hash__()] = min_prev_vertex
    
    # here we are finding the best possible tour that leads back to the start
    set_holder = set(range(1, len(adjacency_matrix)))
    
    minimum = inf
    prev_vertex = -1

    for vertex in set_holder: 
        cost = adjacency_matrix[vertex][0] + get_cost(set_holder, vertex, min_cost_holder)

        if cost < minimum:
            minimum = cost
            prev_vertex = vertex
    
    index = Index(0, set_holder)
    parent_holder[index.__hash__()] = prev_vertex

    # we map it back to the input data and return it
    tour = generate_tour(parent_holder, len(adjacency_matrix), cities)
    return [minimum, tour]

def generate_tour(parent_holder, total_vertices, cities): 
    set_holder = set(range(0, total_vertices))     
    tour = []
    start = 0

    while True: 
        tour.append(next(x for x in cities if start + 1 == x.id)) # getting the corresponding city
        set_holder.remove(start)
        index = Index(start, set_holder)
        start = parent_holder.get(index.__hash__())

        if start is None or start == 0: 
            break
    
    tour.append(next(x for x in cities if 1 == x.id))
    return tour
    
        
def get_cost(set, prev_vertex, min_cost_holder): 
    set.remove(prev_vertex)
    index = Index(prev_vertex, set)
    cost = min_cost_holder.get(index.__hash__())
    set.add(prev_vertex) 
    return cost
    
def generate_all_combinations(size): 
    # generates all possible sets (as tuples) from 1 to size (exclusive)
    input = range(1, size)
    all_combinations_generator = (combinations(input, r) for r in range(len(input)+1))
    all_combinations = list(chain.from_iterable(all_combinations_generator))
    return all_combinations

def create_adjacency_matrix(cities): 
    adjacency_matrix = []

    for city in cities: 
        row = []
        for other_city in cities: 
            row.append(city.get_distance_to(other_city))
        adjacency_matrix.append(row)
    
    return adjacency_matrix

def print_solution(cost_and_tour): 
    print('Solution:')
    print('Minimum possible distance is ' + str(cost_and_tour[0]))
    print('---------------------------------------------------------')
    print('The distance can be achieved through the following path: ')

    tour_short = ''
    for city in cost_and_tour[1]: 
        print(city.to_string())
        tour_short += str(city.id) + ' ' + city.name + ' --> '

    print('---------------------------------------------------------')
    print('Or in short: ')
    print(tour_short[:- 3])
    print('Minimum possible distance is ' + str(cost_and_tour[0]))

def main(): 
    print('Programm has started. It might take a few minutes.')
    print('Calculating the best path now...')
    cities = parse_csv_to_cities()
    adjacency_matrix = create_adjacency_matrix(cities)
    best_cost_and_tour = traveling_salesman(adjacency_matrix, cities)
    print_solution(best_cost_and_tour)

if __name__ == '__main__': 
    main()


