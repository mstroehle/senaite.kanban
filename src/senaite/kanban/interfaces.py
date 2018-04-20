# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from zope.interface import Interface


class ISenaiteKanban(Interface):
    """Marker interface that defines a Zope 3 browser layer.
    A layer specific for this add-on product.
    This interface is referenced in profiles/default/browserlayer.xml.
    All views and viewlets registered against this layer will appear on
    your Plone site only when the add-on installer has been run.
    """

class IKanbanView(Interface):
    """Publisher Print View
    """


class IKanbanCard(Interface):
    """A card-like object to be displayed in a Kanban view"""


