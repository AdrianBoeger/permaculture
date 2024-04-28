import unittest
import pytest
from api.services import find_optimal_garden_beds


class TestOptimalGardenBed(unittest.TestCase):
    @pytest.mark.optimalgardenbed
    def test_bed(self):
        plants = ['Leeks', 'Tomato', 'Cucumber', 'Lettuce', 'Fennel']
        beds = 2
        # alphabetical order
        assert find_optimal_garden_beds(plants, beds) == [['Leeks', 'Lettuce', 'Tomato'], ['Cucumber', 'Fennel']]
