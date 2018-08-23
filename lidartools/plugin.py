# -*- coding: utf-8 -*-

"""
***************************************************************************
    plugin.py
    ---------------------
    This script initializes the plugin providers and registers their GUIs.
    ---------------------    
    Date                 : January 2017, August 2018
    Copyright            : (C) 2017 Boundless, http://boundlessgeo.com
                           (C) 2018 rapidlasso GmbH, http://rapidlasso.com
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

__author__ = 'Martin Isenburg'
__date__ = 'August 2018'
__copyright__ = '(C) 2018 Boundless, http://rapidlasso.com'

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
