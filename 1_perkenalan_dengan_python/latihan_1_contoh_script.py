import os
import argparse

from time import time

import pandas as pd
from sqlalchemy import create_engine

def main (params):
    user = params['user']
    password = params['password']
    host = params['host']
    port = params['port']
    db = params['db']
    table_name = params['table_name']
    url = params['url']
