from enum import Enum


class StatusEnum(Enum):
    NEW ='New'
    IN_PROGRES = 'In Progress'
    COMPLETED = 'Completed'
    CLOSED = 'Closed'
    PENDING = 'Pending'
    BLOCKED = 'Blocked'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
