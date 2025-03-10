from enum import Enum


class PriorityEnum(Enum):
    LOW ='Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    CRITICAL = 'Critical'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]