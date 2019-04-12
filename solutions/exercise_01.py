"""Solution to exercise 1"""
from redis import Redis
import examples.settings as settings

if __name__ == '__main__':
    client = Redis(
        host=settings.HOST,
        port=settings.PORT,
        password=settings.PASSWORD,
        decode_responses=True
    )

    print('I have been run {} times'.format(client.incr('kj:counter')))