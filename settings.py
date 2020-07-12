from dataclasses import dataclass

from constants import ArraySize, SortingSpeed, Algorithms


@dataclass
class Settings:
    sorting_speed: SortingSpeed = SortingSpeed.FAST
    array_size: ArraySize = ArraySize.LARGE
    algorithm: Algorithms = Algorithms.BUBBLE_SORT

