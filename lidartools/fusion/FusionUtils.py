# -*- coding: utf-8 -*-

"""
***************************************************************************
    FusionUtils.py
    ---------------------
    Date                 : August 2012
    Copyright            : (C) 2012 by Victor Olaya
    Email                : volayaf at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""
from builtins import object

__author__ = 'Victor Olaya'
__date__ = 'August 2012'
__copyright__ = '(C) 2012, Victor Olaya'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import subprocess
from qgis.PyQt.QtCore import QCoreApplication
from processing.core.ProcessingLog import ProcessingLog
from processing.core.ProcessingConfig import ProcessingConfig
from processing.tools.system import userFolder


class FusionUtils(object):

    FUSION_FOLDER = 'FUSION_FOLDER'

    @staticmethod
    def FusionPath():
        folder = ProcessingConfig.getSetting(FusionUtils.FUSION_FOLDER)
        if folder is None:
            folder = ''

        return folder

    @staticmethod
    def tempFileListFilepath():
        filename = 'fusion_files_list.txt'
        filepath = os.path.join(userFolder(), filename)
        return filepath

    @staticmethod
    def createFileList(files):
        with open(FusionUtils.tempFileListFilepath(), 'w') as out:
            for f in files:
                out.write(f + '\n')

    @staticmethod
    def runFusion(commands, feedback):
        loglines = []
        loglines.append(
            QCoreApplication.translate('FusionUtils',
                                       'Fusion execution console output'))
        proc = subprocess.Popen(
            commands,
            shell=True,
            stdout=subprocess.PIPE,
            stdin=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            universal_newlines=False,
        ).stdout
        for line in iter(proc.readline, ''):
            loglines.append(line)
        ProcessingLog.addToLog(ProcessingLog.LOG_INFO, loglines)

    @staticmethod
    def tempGroundListFilepath():
        filename = 'fusion_groundFiles_list.txt'
        filepath = os.path.join(userFolder(), filename)
        return filepath

    @staticmethod
    def createGroundList(gfiles):
        with open(FusionUtils.tempGroundListFilepath(), 'w') as outg:
            for f in gfiles:
                outg.write(f + '\n')
