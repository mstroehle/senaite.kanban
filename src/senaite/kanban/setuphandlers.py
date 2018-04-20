# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.


from senaite.kanban import logger


def setup_handler(context):
    """
    SENAITE KANBAN setup handler
    """

    if context.readDataFile('senaite.kanban.txt') is None:
        return

    logger.info("SENAITE KANBAN setup handler [BEGIN]")

    logger.info("SENAITE KANBAN setup handler [DONE]")
