import pytest
from .solution import (
    part1,
    part2,
    parse_location_ids,
    calculate_total_distance,
    calculate_similarity_score,
)


def test_parse_location_ids():
    example_input = ["3 4", "4 3", "2 5", "1 3", "3 9", "3 3"]
    left, right = parse_location_ids(example_input)
    assert left == [3, 4, 2, 1, 3, 3]
    assert right == [4, 3, 5, 3, 9, 3]


def test_calculate_total_distance():
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]
    assert calculate_total_distance(left, right) == 11


def test_calculate_similarity_score():
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]
    assert calculate_similarity_score(left, right) == 31


def test_part1():
    example_input = ["3 4", "4 3", "2 5", "1 3", "3 9", "3 3"]
    assert part1(example_input) == 11


def test_part2():
    example_input = ["3 4", "4 3", "2 5", "1 3", "3 9", "3 3"]
    assert part2(example_input) == 31