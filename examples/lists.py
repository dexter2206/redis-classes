from redis import Redis
import settings

if __name__ == '__main__':
    client = Redis(
        host=settings.HOST,
        port=settings.PORT,
        password=settings.PASSWORD,
        decode_responses=True
    )
    
    list_name = 'kj:list'
    
    client.delete(list_name)

    # Append some elements
    for i in range(1, 10, 2):
        client.rpush(list_name, i)

    # Get length of the list
    print(client.llen(list_name))

    # Get elements from zero-th to second (both ends are inclusive!)
    print(client.lrange(list_name, 0, 2))

    # Get all elements. Negative indices count from the end (-1 is the last etc...)
    print(client.lrange(list_name, 0, -1))

    # Access fourth element in the lixt
    print(client.lindex(list_name, 3))

    # Change fourth element to -200
    client.lset(list_name, 3, -200)
    print(client.lindex(list_name, 3))

    # Prepend element to the list
    client.lpush(list_name, 9)
    print(client.lrange(list_name, 0, -1))

    # Remove all elements with number 9
    # The first argument is count - if set to 0 means that we want to remove all occurrences.
    # you could use different value, e.g. lrem(list_name, 1, 9) would remove first
    # occurrence of 9 etc.
    client.lrem(list_name, 0, 9)
    print(client.lrange(list_name, 0, -1))