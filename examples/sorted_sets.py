"""Examples of using sorted set."""
from redis import Redis
import settings

if __name__ == '__main__':
    client = Redis(
        host=settings.HOST,
        port=settings.PORT,
        password=settings.PASSWORD,
        decode_responses=True
    )

    name = 'kj:sset'

    # Add some elements to the sorted set.
    # Note: the keys in the dictionary are elements of the set and values are their score
    client.zadd(name, {'Asia': 2, 'Ola': 1, 'Jacek': 5, 'Maciek': -1})

    # Get first and second element of our set (with respect to scores)
    print(client.zrange(name, 0, 1))

    # Get all elements of our set
    print(client.zrange(name, 0, -1))

    # Get elements with scores from 2 to 10 inclusively
    print(client.zrangebyscore(name, 2, 10))

    # Repeat that, but first increment Ola's score by 9
    print(client.zincrby(name, 9, 'Ola'))    # Note: zincrby returns the new score
    print(client.zrangebyscore(name, 2, 10))

    # Find rank of Jacek
    print(client.zrank(name, 'Jacek'))

    # Find reverse rank of Jacek
    print(client.zrevrank(name, 'Jacek'))

    # Remove Ola from the set, see if that worked
    client.zrem(name, 'Ola')
    print(client.zrange(name, 0, -1))

    # Remove all elements in a set that have score in range 0-3
    client.zremrangebyscore(name, 0, 3)
    print(client.zrange(name, 0, -1, withscores=True))