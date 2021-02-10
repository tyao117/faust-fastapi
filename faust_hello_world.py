import faust
import uuid

app = faust.App(
        'greetings',
        broker='kafka://localhost:9092',
        )


class Greeting(faust.Record, serializer='json', isodates=True):
    message: str
    uuid: str

greetings_topic = app.topic('greetings', value_type=Greeting)

@app.agent(greetings_topic)
async def get_greetings(greetings):
    """Receives the message and prints the greeting in the logger
    """
    async for greeting in greetings:
        print(greeting.message)
        print(greeting.uuid)

@app.timer(5)
async def produce():
    for i in range(100):
        await get_greetings.send(value={
            "message": f'hello from {i}',
            "uuid": uuid.uuid1()
            })

if __name__ == '__main__':
    app.main()
