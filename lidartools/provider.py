# -*- coding: utf-8 -*-

"""
***************************************************************************
    provider.py
    ---------------------
    This script initializes the valid providers, depending on Wine and OS.
    ---------------------
    Date                 : January 2017, August 2018
    Copyright            : (C) 2017 Boundless, http://boundlessgeo.com
                         : (C) 2014 Agresta S. Coop, http://agresta.org
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
__date__ = 'August 2012'
__copyright__ = '(C) 2012, Victor Olaya'

__author__ = 'Inigo Escamochero'
__date__ = 'June 2014'
__copyright__ = '(C) 2014, Agresta S. Coop, http://agresta.org'

__author__ = 'Martin Isenburg'
__date__ = 'August 2018'
__copyright__ = '(C) 2018, rapidlasso GmbH, http://rapidlasso.com'

import os
from qgis.PyQt.QtGui import QIcon
from processing.core.AlgorithmProvider import AlgorithmProvider
from processing.core.ProcessingConfig import ProcessingConfig, Setting
from processing.tools.system import isWindows

from .lastools.LAStoolsUtils import LAStoolsUtils
from .lastools.lasground import lasground
from .lastools.lasheight import lasheight
from .lastools.lasclassify import lasclassify
from .lastools.laszip import laszip
from .lastools.lasindex import lasindex
from .lastools.lasclip import lasclip
from .lastools.lasquery import lasquery
from .lastools.lascolor import lascolor
from .lastools.lasthin import lasthin
from .lastools.lasnoise import lasnoise
from .lastools.lassort import lassort
from .lastools.lastile import lastile
from .lastools.lasgrid import lasgrid
from .lastools.lasview import lasview
from .lastools.lasboundary import lasboundary
from .lastools.lasinfo import lasinfo
from .lastools.las2dem import las2dem
from .lastools.blast2dem import blast2dem
from .lastools.las2iso import las2iso
from .lastools.las2tin import las2tin
from .lastools.las2las_filter import las2las_filter
from .lastools.las2las_project import las2las_project
from .lastools.las2las_transform import las2las_transform
from .lastools.blast2iso import blast2iso
from .lastools.lasprecision import lasprecision
from .lastools.lasvalidate import lasvalidate
from .lastools.lasduplicate import lasduplicate
from .lastools.las2txt import las2txt
from .lastools.txt2las import txt2las
from .lastools.las2shp import las2shp
from .lastools.shp2las import shp2las
from .lastools.lasmerge import lasmerge
from .lastools.lassplit import lassplit
from .lastools.lascanopy import lascanopy
from .lastools.lasoverage import lasoverage
from .lastools.lasoverlap import lasoverlap
from .lastools.laspublish import laspublish
from .lastools.lasground_new import lasground_new
from .lastools.lascontrol import lascontrol
from .lastools.lasdiff import lasdiff
from .lastools.lasheight_classify import lasheight_classify

from .lastools.lastilePro import lastilePro
from .lastools.lasgroundPro import lasgroundPro
from .lastools.las2demPro import las2demPro
from .lastools.lasheightPro import lasheightPro
from .lastools.laszipPro import laszipPro
from .lastools.lasgridPro import lasgridPro
from .lastools.lasduplicatePro import lasduplicatePro
from .lastools.lassortPro import lassortPro
from .lastools.lasclassifyPro import lasclassifyPro
from .lastools.lasthinPro import lasthinPro
from .lastools.lasnoisePro import lasnoisePro
from .lastools.lasindexPro import lasindexPro
from .lastools.lascanopyPro import lascanopyPro
from .lastools.blast2demPro import blast2demPro
from .lastools.lasboundaryPro import lasboundaryPro
from .lastools.lasinfoPro import lasinfoPro
from .lastools.las2lasPro_filter import las2lasPro_filter
from .lastools.las2lasPro_project import las2lasPro_project
from .lastools.las2lasPro_transform import las2lasPro_transform
from .lastools.lasoveragePro import lasoveragePro
from .lastools.txt2lasPro import txt2lasPro
from .lastools.las2txtPro import las2txtPro
from .lastools.blast2isoPro import blast2isoPro
from .lastools.lasvalidatePro import lasvalidatePro
from .lastools.lasmergePro import lasmergePro
from .lastools.lasviewPro import lasviewPro
from .lastools.lasoverlapPro import lasoverlapPro
from .lastools.laspublishPro import laspublishPro
from .lastools.lasgroundPro_new import lasgroundPro_new
from .lastools.lasheightPro_classify import lasheightPro_classify

from .lastools.flightlinesToDTMandDSM import flightlinesToDTMandDSM
from .lastools.flightlinesToCHM import flightlinesToCHM
from .lastools.flightlinesToSingleCHMpitFree import flightlinesToSingleCHMpitFree
from .lastools.hugeFileClassify import hugeFileClassify
from .lastools.hugeFileGroundClassify import hugeFileGroundClassify
from .lastools.hugeFileNormalize import hugeFileNormalize

from .fusion.OpenViewerAction import OpenViewerAction
from .fusion.ASCII2DTM import ASCII2DTM
from .fusion.CanopyMaxima import CanopyMaxima
from .fusion.CanopyModel import CanopyModel
from .fusion.Catalog import Catalog
from .fusion.ClipData import ClipData
from .fusion.CloudMetrics import CloudMetrics
from .fusion.Cover import Cover
from .fusion.DTM2TIF import DTM2TIF
from .fusion.DTM2ASCII import DTM2ASCII
from .fusion.FirstLastReturn import FirstLastReturn
from .fusion.GridMetrics import GridMetrics
from .fusion.GridSurfaceCreate import GridSurfaceCreate
from .fusion.TinSurfaceCreate import TinSurfaceCreate
from .fusion.Csv2Grid import Csv2Grid
from .fusion.GroundFilter import GroundFilter
from .fusion.MergeData import MergeData
from .fusion.FilterData import FilterData
from .fusion.PolyClipData import PolyClipData
from .fusion.ImageCreate import ImageCreate
from .fusion.IntensityImage import IntensityImage
from .fusion.DensityMetrics import DensityMetrics
from .fusion.MergeDTM import MergeDTM
from .fusion.TopoMetrics import TopoMetrics
from .fusion.TreeSeg import TreeSeg
from .fusion.SplitDTM import SplitDTM
from .fusion.MergeRaster import MergeRaster
from .fusion.SurfaceStats import SurfaceStats
from .fusion.ReturnDensity import ReturnDensity  # spellok
from .fusion.GridSurfaceStats import GridSurfaceStats
from .fusion.FusionUtils import FusionUtils


class LidarToolsAlgorithmProvider(AlgorithmProvider):

    def __init__(self):
        super().__init__()
        self.activate = False

    def _loadAlgorithms(self):
        self.algs = []

        # LAStools for processing single files

        if (isWindows() or LAStoolsUtils.hasWine()):
            lastools = [
                lasground(), lasheight(), lasclassify(), lasclip(), lastile(),
                lascolor(), lasgrid(), las2dem(), blast2dem(), las2iso(), blast2iso(),
                lasview(), lasboundary(), lasinfo(), lasprecision(), las2tin(),
                lasvalidate(), lasduplicate(), las2txt(), txt2las(), laszip(),
                lasindex(), lasthin(), lassort(), lascanopy(), lasmerge(),
                las2shp(), shp2las(), lasnoise(), lassplit(), las2las_filter(),
                las2las_project(), las2las_transform(), lasoverage(), lasoverlap(),
                lasquery(), laspublish(), lasground_new(), lascontrol(), lasdiff(),
                lasheight_classify()
            ]
        else:
            lastools = [
                lasinfo(), lasprecision(), lasvalidate(), las2txt(), txt2las(),
                laszip(), lasindex(), lasmerge(), las2las_filter(), las2las_project(),
                las2las_transform(), lasquery(), lasdiff()
            ]
        self.algs.extend(lastools)

        # LAStools Production for processing folders of files

        if (isWindows() or LAStoolsUtils.hasWine()):
            lastoolsPro = [
                lastilePro(), lasgroundPro(), las2demPro(), lasheightPro(), laszipPro(),
                lasduplicatePro(), lasgridPro(), lassortPro(), lasclassifyPro(), lasthinPro(),
                lasnoisePro(), lasindexPro(), lascanopyPro(), blast2demPro(), lasboundaryPro(),
                lasinfoPro(), las2lasPro_filter(), las2lasPro_project(), las2lasPro_transform(),
                lasoveragePro(), txt2lasPro(), las2txtPro(), blast2isoPro(), lasvalidatePro(),
                lasmergePro(), lasviewPro(), lasoverlapPro(), laspublishPro(), lasgroundPro_new(),
                lasheightPro_classify()
            ]
        else:
            lastoolsPro = [
                laszipPro(), lasindexPro(), lasinfoPro(), las2lasPro_filter(), las2lasPro_project(),
                las2lasPro_transform(), txt2lasPro(), las2txtPro(), lasvalidatePro(), lasmergePro()
            ]
        self.algs.extend(lastoolsPro)

        # some examples for LAStools Pipelines

        if (isWindows() or LAStoolsUtils.hasWine()):
            lastoolsPipe = [
                flightlinesToDTMandDSM(), flightlinesToCHM(), flightlinesToSingleCHMpitFree(), hugeFileClassify(),
                hugeFileGroundClassify(), hugeFileNormalize()
            ]
        else:
            lastoolsPipe = []
        self.algs.extend(lastoolsPipe)

        # FUSION

        if isWindows():
            self.actions.append(OpenViewerAction())
            fusiontools = [
                Catalog(), CloudMetrics(), CanopyMaxima(), CanopyModel(), ClipData(),
                Csv2Grid(), Cover(), FilterData(), GridMetrics(), GroundFilter(),
                GridSurfaceCreate(), MergeData(), TinSurfaceCreate(), PolyClipData(),
                DTM2TIF(), DTM2ASCII(), FirstLastReturn(), ASCII2DTM(), ImageCreate(),
                IntensityImage(), DensityMetrics(), MergeDTM(), TopoMetrics(), TreeSeg(),
                SplitDTM(), MergeRaster(), SurfaceStats(), ReturnDensity(), GridSurfaceStats()  # spellok
            ]
            for alg in fusiontools:
                alg.group, alg.i18n_group = alg.trAlgorithm('Fusion')
            self.algs.extend(fusiontools)

    def initializeSettings(self):
        AlgorithmProvider.initializeSettings(self)
        if not isWindows():
            ProcessingConfig.addSetting(Setting(
                self.name(),
                LAStoolsUtils.WINE_FOLDER,
                self.tr('Wine folder'), '', valuetype=Setting.FOLDER))

    def id(self):
        return 'lidartools'

    def name(self):
        return self.tr('Tools for LiDAR data')

    def icon(self):
        return QIcon(os.path.dirname(__file__) + '/lidar.png')

    def getSupportedOutputTableExtensions(self):
        return ['csv']
