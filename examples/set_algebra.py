"""Sets algebra: union, intersection etc."""
from redis import Redis
import settings

if __name__ == '__main__':
    client = Redis(
        host=settings.HOST,
        port=settings.PORT,
        password=settings.PASSWORD,
        decode_responses=True
    )

    name_first = 'kj:set_1'  # key for the first set
    name_second = 'kj_set_2' # key for the second set

    # Create the first set
    client.sadd(name_first, 'marchew')
    client.sadd(name_first, 'bakłażan')
    client.sadd(name_first, 'cebula')

    # Create second set
    client.sadd(name_second, 'cebula')
    client.sadd(name_second, 'pomidor')
    client.sadd(name_second, 'marchew')

    # Get union of the sets. Note: we don't store it in Redis, just get the result.
    print(client.sunion(name_first, name_second))

    # Get intersection of the sets.
    print(client.sinter(name_first, name_second))

    # Get difference of the sets (note: this one is not symmetric!)
    print(client.sdiff(name_first, name_second))

    # All of the above have have "store" versions with which we can store results in
    # some new set. For instance:
    print(client.sunionstore('kj:union', [name_first, name_second]))
    print(client.smembers('kj:union'))