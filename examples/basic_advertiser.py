#!/usr/bin/env python3

import sys
from logging import DEBUG
from time import sleep

from bleson import get_provider, Advertiser, Advertisement

# Get the wait time from the first script argument or default it to 10 seconds

def advertuser_
WAIT_TIME = int(sys.argv[1]) if len(sys.argv)>1 else 10

adapter = get_provider().get_adapter()

advertiser = Advertiser(adapter)
advertisement = Advertisement()
advertisement.name = "123123"

advertiser.advertisement = advertisement

advertiser.start()
sleep(WAIT_TIME)
advertiser.stop()

