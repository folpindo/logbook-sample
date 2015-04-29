#!/bin/env python

from logbook import FileHandler, Logger

logger = Logger('[LogBook sample]')
log_handler = FileHandler('logbook-sample.log')
log_handler.push_application()
logget('Hello, world!')
