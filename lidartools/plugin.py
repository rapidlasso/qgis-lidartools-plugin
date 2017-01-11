# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : January 2017
    Copyright            : (C) 2017 Boundless, http://boundlessgeo.com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Victor Olaya'
__date__ = 'January 2017'
__copyright__ = '(C) 2017 Boundless, http://boundlessgeo.com'

# This will get replaced with a git SHA1 when you do a git archive

import os
import webbrowser

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from qgis.core import QgsApplication

try:
    from processing.core.Processing import Processing
    from lidartools.provider import LidarToolsAlgorithmProvider
    processingOk = True
except:
    processingOk = False

class LidarTools:
    def __init__(self, iface):
        self.iface = iface
        if processingOk:
            self.provider = LidarToolsAlgorithmProvider()

    def initGui(self):
        if processingOk:
            Processing.addProvider(self.provider)

    def unload(self):
        if processingOk:
            Processing.removeProvider(self.provider)

    def run(self):
        pass
