"""
/***************************************************************************
Name                 : timestamp2datetime
Description          : QGIS fieldcalc function to get data and time from Unix Timestamp
copyright            : (C) 2017 by Anton Biatov
email                : anton.biatov@gmail.com

 ***************************************************************************/

Your need copy this file to yours local folder "<USER>/.qgis2/python/expressions/"

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
def timestamp2dateYMD(value1, feature, parent):
    """
  <h4>Return</h4>Get Data from 'timestamp' field as 'Y-m-d'
  <p><h4>Syntax</h4>timestamp2dateYMD("Timestamp")</p><p>Return: Y-m-d</p>
  <p><h4>Example</h4>timestamp2dateYMD("1502380248")</p><p>Return: '2017-08-10'</p>
    """
    outdate = datetime.datetime.fromtimestamp(int(value1[0:10])).strftime('%Y-%m-%d')
    return outdate

@qgsfunction(args='auto', group='Custom')
def timestamp2dateDMY(value1, feature, parent):
    """
  <h4>Return</h4>Get Data from 'timestamp' field as 'd/m/Y'
  <p><h4>Syntax</h4>timestamp2dateDMY("Timestamp")</p><p>Return: d/m/Y</p>
  <p><h4>Example</h4>timestamp2dateDMY("1502380248")</p><p>Return: '10/08/2017'</p>
    """
    outdate = datetime.datetime.fromtimestamp(int(value1[0:10])).strftime('%d/%m/%Y')
    return outdate

@qgsfunction(args='auto', group='Custom')
def timestamp2time(value1, feature, parent):
    """
  <h4>Return</h4>Get Time from 'timestamp' field
  <p><h4>Syntax</h4>timestamp2time("Timestamp")</p><p>Return: H:M:S</p>
  <p><h4>Example</h4>timestamp2time("1502380248")</p><p>Return: '18:50:48'</p>
    """
    outdate = datetime.datetime.fromtimestamp(int(value1[0:10])).strftime('%H:%M:%S')
    return outdate
