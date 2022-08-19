import time, sys
from configs.config import DBSession
from sqlalchemy.orm import Session


class BaseCurd():
    def __init__(self, db=DBSession):
        self.db = db

    def get_(self, data={}):
        return 'get_'

    def add_(self, data={}):
        return 'add_'

    def update_(self, data={}):
        return 'update_'

    def delete_(self, data={}):
        return 'delete_'