__all__ = ["SendDataTool"]

# Mandatory imports
from Akuanduba.core import AkuandubaTool, StatusCode, NotSet, retrieve_kw
from Akuanduba.core.messenger.macros import *
# Your imports go here:
# import WhateverYouWant

#
# Your TOOL must always have inheritance from AkuandubaTool
#
class SendDataTool(AkuandubaTool):

  #
  # Here EDMs and other stuff will not be available yet, this is just for attributes initialization and superclass init
  #
  def __init__(self, name, **kw):

    # Mandatory stuff
    AkuandubaTool.__init__(self, name)

    # Initialize stuff
    # self.__whatever = 0

  #
  # At this point, the context will be set and all EDMs, services and tools will already be attached to it
  # If you need to get anything from context to set something on this tool's initialization, this is the time
  #
  def initialize(self):

    # Lock the initialization. After that, this tool can not be initialized once again
    self.init_lock()
    return StatusCode.SUCCESS


  #
  # This method will run once every Akuanduba loop only. Use this to get the data you want from context, process it
  # and store it on another dataframe or whatever you wanna do.
  #
  def execute(self,context):

    # Getting dataframe
    dataframe = context.getHandler("WindData")

    # Sending data (on this example just prints a warning)
    MSG_WARNING (self, "DATA'S BEING SENT")

    # Always return SUCCESS
    return StatusCode.SUCCESS

  #
  # This will call finalization for this service
  #
  def finalize(self):
    self.fina_lock()
    return StatusCode.SUCCESS