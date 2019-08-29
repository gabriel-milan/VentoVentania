# All list
__all__ = ["WindData"]

#
# Imports
#
# Mandatory imports
from Akuanduba.core.messenger.macros import *
from Akuanduba.core.constants import *
from Akuanduba.core import NotSet, AkuandubaDataframe
# Your imports go here:
from collections import deque

#
# Your DATAFRAME must always have inheritance from AkuandubaDataframe
#
class WindData (AkuandubaDataframe):

  #
  # Here EDMs and other stuff will not be available yet, this is just for attributes initialization and superclass init
  #
  def __init__(self, name):

    # Mandatory stuff
    AkuandubaDataframe.__init__(self, name)

    # Initializing stuff
    self.__windSpeed = 0
    self.__historyWind = deque (maxlen = 30)
    self._timestampQueue = []
    for i in range (30):
      self._timestampQueue.append(i)

  #
  # Getters and setters
  #
  def getSpeed (self):
    return self.__windSpeed

  def setSpeed (self, value):
    self.__windSpeed = value
    self.__historyWind.append (value)

  #
  # "toRawObj" method is a mandatory method that delivers a dict with the desired data
  # for file saving
  #
  def toRawObj(self):
    d = {
          "WindSpeed" : self.getSpeed(),
          }
    return d

  def getHistory (self):

    try:
      data = {
        "WindSpeed" : list(self.__historyWind),
        "time" : list(self._timestampQueue[:len(self.__historyWind)])
      }
    except:
      return 0

    return data
