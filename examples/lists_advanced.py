"""More advanced examples of using lists with Redis."""
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
    for i in range(10):
        client.rpush(list_name, i)

    # The rpop and lpop remove first value from right/left end respectively. The removed element
    # is returned
    right = client.rpop(list_name)
    print(f'Right {right}')
    left = client.lpop(list_name)
    print(f'Left {left}')
    print(client.lrange(list_name, 0, -1))

    # You can also remove from right side and push to the left side.
    # Useful for organizing cyclic list...
    value = client.rpoplpush(list_name, list_name)
    print(f'Current elemen: {value}')
    print(client.lrange(list_name, 0, -1))

    # Trim the list so that it only contains elements of indices 0-4.
    # Note: invalid ranges are not causing an error! We can used ltrim to limit number
    # of elements in the list to given amount.
    client.ltrim(list_name, 0, 4)
    print(client.lrange(list_name, 0, -1))
