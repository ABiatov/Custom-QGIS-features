"""
/***************************************************************************
Name                 : timestamp2datetime
Description          : QGIS fieldcalc function to get data and time from Unix Timestamp
copyright            : (C) 2017 by Anton Biatov
email                : anton.biatov@gmail.com

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
  """
from qgis.core import *
from qgis.gui import *
import datetime

@qgsfunction(args='auto', group='Custom')
def timestamp2datetime(value1, feature, parent):
    """
  <h4>Return</h4>Get Data & Time from 'timestamp' field
  <p><h4>Syntax</h4>timestamp2datetime("Timestamp")</p><p>Return: Y-m-d H:M:S</p>
  <p><h4>Example</h4>timestamp2datetime("1502380248")</p><p>Return: '2017-08-10 18:50:48'</p>
    """
    outdatetime = datetime.datetime.fromtimestamp(int(value1[0:10])).strftime('%Y-%m-%d %H:%M:%S')
    return outdatetime

@qgsfunction(args='auto', group='Custom')
def timestamp2date(value1, feature, parent):
    """
  <h4>Return</h4>Get Data from 'timestamp' field
  <p><h4>Syntax</h4>timestamp2date("Timestamp")</p><p>Return: Y-m-d</p>
  <p><h4>Example</h4>timestamp2date("1502380248")</p><p>Return: '2017-08-10'</p>
    """
    outdate = datetime.datetime.fromtimestamp(int(value1[0:10])).strftime('%Y-%m-%d')
    return outdate