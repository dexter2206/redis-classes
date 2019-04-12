"""Solution to exercise 2"""
import logging
from redis import Redis
import examples.settings as settings

NAME_TPL = 'kj:cache:foo:{arg}'

client = Redis(
    host=settings.HOST,
    port=settings.PORT,
    password=settings.PASSWORD,
    decode_responses=True
)

def foo(arg):
    logger = logging.getLogger('foo')
    name = NAME_TPL.format(arg=arg)
    ret_val = client.get(name)
    if ret_val is None:
        logger.debug('Cache miss for arg %s', arg)
        ret_val = arg.upper()
        client.set(name, ret_val)
    else:
        logger.debug('Cache hit for arg %s', arg)
    return ret_val

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    print(foo('fooOO1'))
    print(foo('fooOO1'))
    print(foo('fizzbuzzzzz1'))
    print(foo('buzz1'))
    print(foo('fizzbuzzzzz1'))