import uasyncio as asyncio

from semaphore import Semaphore


async def transition(semaphore):
    while True:
        print('Transitioning...')
        next_period = semaphore.period
        if semaphore.is_red:
            if semaphore.crossing:
                semaphore.cross_request_completed()
            semaphore.green_on()
        else:
            if semaphore.crossing:
                semaphore.red_on()
                next_period = semaphore.cross_time
            else:
                pass
        print('Will wait {} seconds'.format(next_period))
        await asyncio.sleep(next_period)


def run():
    semaphore = Semaphore(period=5, cross_time=3)

    loop = asyncio.get_event_loop()
    loop.create_task(transition(semaphore))
    loop.run_forever()
