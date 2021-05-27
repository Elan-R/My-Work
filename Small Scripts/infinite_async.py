# a function I made to infinitely run a group of async functions
# as an iterator that returns awaitables that return the functions'
# results
# (and code to demonstrate it)

import asyncio

async def forever_do(futures):
    """
    futures is an iterable of tuples: (awaitable, (arg1, arg2))
    """
    done = asyncio.Queue()

    def _on_completion(f):
        new_future = asyncio.ensure_future(f.coro_tuple[0](*f.coro_tuple[1]))
        new_future.add_done_callback(_on_completion)
        new_future.coro_tuple = f.coro_tuple
        done.put_nowait(f)

    async def _wait_for_one():
        return (await done.get()).result()

    for t in futures:
        f = asyncio.ensure_future(t[0](*t[1]))
        f.add_done_callback(_on_completion)
        f.coro_tuple = t

    while True:
        yield _wait_for_one()

async def main():
    from random import randint

    async def long_async_func(name):
        print(f"Worker {name} started")
        await asyncio.sleep(randint(1, 5))
        return f"Worker {name} finished"

    futures = [(long_async_func, (i,)) for i in range(10)]
    async for result in forever_do(futures):
        print(await result)


if __name__ == "__main__":
    asyncio.run(main())
