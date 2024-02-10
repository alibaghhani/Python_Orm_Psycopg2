from abc import abstractmethod
from dataclasses import dataclass

@dataclass
class User:
    username: str
    password: str

    @abstractmethod
    def register(self):
        raise NotImplementedError("you must implement this method!")

    @abstractmethod
    def login(self):
        raise NotImplementedError("you must implement this method!")
