import json
import os

import decimal
from boto import dynamodb2
from boto.dynamodb2.table import Table
from datetime import datetime
import logging

ACCESS_KEY = 'AKIAIEMUJLROR4KCD2QQ'
SECRET_KEY = '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'
TABLE_NAME = "Intel_Edison"
REGION = "us-west-2"


# Save to
class dynamodb():
    def __init__(self):

        self.conn = dynamodb2.connect_to_region(
            REGION,
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
        )
        self.table = Table(
            TABLE_NAME,
            connection=self.conn

        )

    def read_from_db(self):
        results = self.table.scan()
        # logger.info('results: {}'.format(results))
        data = []
        for dynamo_item in results:
            data.append(dict(dynamo_item.items()))

        return data

    def delete_from_db(self, card_id, timestamp):
        try:
            a = self.table.get_item(card_data=card_id, timestamp=timestamp)
            a.delete()
        except Exception as e:
            print 'error: {}'.format(e)


aws = dynamodb()


"""
Functions which handle the incoming and outgoing logic.
"""


def __datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')


if __name__ == "__main__":
    print aws.read_from_db()