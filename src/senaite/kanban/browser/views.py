# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.KANBAN
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from bika.lims import api
from bika.lims.catalog.worksheet_catalog import CATALOG_WORKSHEET_LISTING
from senaite.kanban import logger
from senaite.kanban.interfaces import IKanbanView, IKanbanCard
from zope.interface import implements


class KanbanCard(object):
    """Card Content Wrapper
    """
    implements(IKanbanCard)

    def __init__(self, uid):
        logger.debug("KanbanCardObject({})".format(uid))


class KanbanView(BrowserView):
    implements(IKanbanView)
    template = ViewPageTemplateFile("templates/kanbanview.pt")

    def __init__(self, context, request):
        super(BrowserView, self).__init__(context, request)

        self.context = context
        self.request = request

    def __call__(self):
        return self.template()

    def get_by_state(self, state):
        query = dict(portal_type="Worksheet", review_state=state)
        logger.info(repr(query))
        return api.search(query, CATALOG_WORKSHEET_LISTING)
