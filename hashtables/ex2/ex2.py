#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    
    # Insert Tickets
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Retrieve a starter
    city = hash_table_retrieve(hashtable, 'NONE')

    # Comprehension to create an array of cities called Route
    for i, _ in enumerate(route):
        route[i] = city
        city = hash_table_retrieve(hashtable, city)

    return route
