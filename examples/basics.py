"""A basic example of using Redis"""
from redis import Redis


if __name__ == '__main__':
    # Step 1: create client for communication with Redis
    client = Redis(
        host='localhost',   # Address (or domain name) of Redis server
        port=6379,          # Port of the server (6379 is the default)
        password='zaq12wsx',# Password. Don't set this if not configured in Redis)
        decode_responses=True # Get strings from Redis (otherwise it returns bytes)
    )

    # Set some value. Think of treating Redis like a dict here
    # i.e. performing redis[key] = value
    value = 'The quick brown fox jumped over a lazy dog.'
    key = 'test_str'
    client.set(key, value)

    # Retrieve the value back and see if we get the same what we set.
    retrieved = client.get(key)
    print(retrieved == value)

    # Let's try with numbers
    client.set('test_number', 2.0)
    retrieved = client.get('test_number')
    print(f'Retrieved: {retrieved}, type: {type(retrieved)}')
l