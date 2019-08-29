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

  #
  # Getters and setters
  #
  def getSpeed (self):
    return self.__windSpeed

  def setSpeed (self, value):
    self.__windSpeed = value

  #
  # "toRawObj" method is a mandatory method that delivers a dict with the desired data
  # for file saving
  #
  def toRawObj(self):
    d = {
          "WindSpeed" : self.getSpeed(),
          }
    return d
