"""
Main script
"""
from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    """
    Root function for web server.
    - :return: A welcoming message
    - :rtype: dict[str, str]
    """
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str) -> dict[str, str]:
    """
    Say hello function.
    - :param name: The name of the person to say hello
    - :type name: str
    - :return: Salutation to the person
    - :rtype: dict[str, str]
    """
    return {"message": f"Hello {name}"}
