"""Basic examples of using sets."""
from redis import Redis
import settings

if __name__ == '__main__':
    client = Redis(
        host=settings.HOST,
        port=settings.PORT,
        password=settings.PASSWORD,
        decode_responses=True
    )

    name = 'kj:set'

    # Create some set by adding elements to it.
    client.sadd(name, 'Foo')
    client.sadd(name, 'Bar')
    client.sadd(name, 'Baz')

    # Print elements of a set
    print(client.smembers(name))

    # Notice: adding the same element twice does not change a set
    client.sadd(name, 'Baz')
    print(client.smembers(name))

    # Print total number of elements in a set
    print(client.scard(name))

    # Check if given element is in a set
    print(client.sismember(name, 'Foo'))
    print(client.sismember(name, 'FooBarBaz'))

    # Get random member of a set
    print(client.srandmember(name))

    # Remove 'Foo' from the set
    print(client.srem(name, 'Foo'))
    print(client.smembers(name))