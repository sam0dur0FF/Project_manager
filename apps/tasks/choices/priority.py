from enum import Enum


class PriorityEnum(Enum):
    LOW ='Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    CRITICAL = 'Critical'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def choices_values(cls):
        return [key.value for key in cls]
