from util.filehandling import open_data_file_as_lines
from math import sqrt
from functools import reduce
import time

DATA_FILE = "day8in.txt"

# A point looks like (num, (x,y,z))
Point = tuple[int, tuple[int, int, int]]
Connection = tuple[float, tuple[int, int]]

# For each point
# - Add to a numbered list
# - For each point already in the list
# - - Add the distance between the two points to a list
# Grab the first 100 elements of the distance list sorted
# For each element in that list:
# - If either point is not in any breaker, create a new breaker with those two
# - If only one point is in a breaker, add the second point to that breaker
# - If both points are in a breaker, combine those two breakers
# Sort the breakers by length (O(nlogn) instead of O(n), but it's much clearer), 
#  grab the first three, multiply their lengths, return

def main():
    start_time = time.perf_counter()
    lines = list(map(str.strip, open_data_file_as_lines(DATA_FILE)))
    points = create_point_list(lines)
    distances = sorted(create_distance_set(points), key=lambda x: x[0])
    relevant_distances = distances[:1000]
    breakers = form_breakers(relevant_distances)
    lengths = sorted(list(map(len, breakers)), reverse=True)
    print(reduce(lambda x,y: x*y, lengths[:3]))
    end_time = time.perf_counter()
    print(f"Elapsed time: {end_time - start_time:.6f} seconds")

def form_breakers(connections: list[Connection]) -> list[set[int]]:
    connections_without_distances = map(lambda x: x[1], connections)
    breakers = []
    for connection in connections_without_distances:
        (p1,p2) = connection
        p1_breaker = set()
        p2_breaker = set()
        for breaker in breakers:
            if not p1_breaker and p1 in breaker:
                p1_breaker = breaker
            if not p2_breaker and p2 in breaker:
                p2_breaker = breaker
        if (not p1_breaker) and (not p2_breaker):
            breakers.append({p1,p2})
        elif p1_breaker and p2_breaker:
            breakers.remove(p1_breaker)
            if p2_breaker in breakers:
                breakers.remove(p2_breaker)
            breakers.append(p1_breaker.union(p2_breaker))
        elif p1_breaker:
            breakers.remove(p1_breaker)
            p1_breaker.add(p2)
            breakers.append(p1_breaker)
        else:
            breakers.remove(p2_breaker)
            p2_breaker.add(p1)
            breakers.append(p2_breaker)
    return breakers

def create_point_list(lines: list[str]) -> list[Point]:
    point_list = []
    for (idx, line) in enumerate(lines):
        coords = list(map(int, line.split(',')))
        point = (idx, (coords[0], coords[1], coords[2]))
        point_list.append(point)
    return point_list

def create_distance_set(points: list[Point]) -> list[Connection]:
    distances = []
    for (idx, p1) in enumerate(points):
        # TODO
        for p2 in points[idx+1:]:
            distance = get_point_distance(p1, p2)
            distances.append((distance, (p1[0], p2[0])))
    return distances

def get_point_distance(p1: Point, p2: Point) -> float:
    (_, (x1, y1, z1)) = p1
    (_, (x2, y2, z2)) = p2
    return sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


main()