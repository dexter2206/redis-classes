"""An example of increment and decrement."""
from redis import Redis
import settings

if __name__ == '__main__':
    client = Redis(
        host=settings.HOST,
        port=settings.PORT,
        password=settings.PASSWORD,
        decode_responses=True
    )

    x_name = 'kj:x'
    
    # Let's set some number using integral value
    client.set(x_name, 10)

    # Increment our x by 1 and see the result
    client.incr(x_name)
    print(client.get(x_name))

    # Decrement it back and see if we get the original value
    client.decr(x_name)
    print(client.get(x_name))

    # Now increment by an amount different than one. Note: we can only use integer here!
    client.incrby(x_name, 3)
    print(client.get(x_name))

    # Decrementation works the same way
    client.decrby(x_name, 20)
    print(client.get(x_name))

    # We can also increment by float, but using incrbyfloat
    client.incrbyfloat(x_name, 3.5)
    print(client.get(x_name))

    # Note: at this point x can no longer be interpreted as integer.
    # Therefore, incrby/decrby won't work - we need to use incrbyfloat!
    try:
        client.incrby(x_name, 3)
    except Exception as exc:
        print(exc)
