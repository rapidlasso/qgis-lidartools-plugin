# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    This script initializes the plugin, making it known to QGIS.
    ---------------------
    Date                 : January 2017, August 2018
    Copyright            : (C) 2017 Boundless, http://boundlessgeo.com
                         : (C) 2018 rapidlasso GmbH, http://rapidlasso.com
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
__copyright__ = '(C) 2018 rapidlasso GmbH, http://rapidlasso.com'

import os
import site
site.addsitedir(os.path.abspath(os.path.dirname(__file__) + '/ext-libs'))

def classFactory(iface):
    from plugin import LidarTools
    return LidarTools(iface)
