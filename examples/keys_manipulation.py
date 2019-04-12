"""Basic key manipulation, check available keys, delete key etc."""
from redis import Redis
import settings

if __name__ == '__main__':
    client = Redis(
        host=settings.HOST,
        port=settings.PORT,
        password=settings.PASSWORD,
        decode_responses=True
    )

    # Delete everything we have in redis so far
    client.flushall()

    # Add some example keys so we can further manipulate them
    for i in range(5):
        client.set(f'kj:number{i}', i)

    # And another number, just with different pattern
    client.set(f'kj:pi', 3.14)

    # Print all keys
    print(client.keys())

    # Print all keys that have "number" in them
    print(client.keys('*number*'))

    # Delete key "kj:number2" and see if that worked
    client.delete('kj:number2')
    print(client.keys())