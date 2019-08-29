__all__ = ['ApiService']

# Mandatory imports
from Akuanduba.core import Logger, NotSet, AkuandubaService
from Akuanduba.core.messenger.macros import *
from Akuanduba.core.constants import *
from Akuanduba.core import StatusCode, StatusTool, StatusThread
# Your own imports go here:
# import sensor_lib
import time
from flask import Flask, Response
from flask_cors import CORS

#
# Your SERVICE must always have inheritance from AkuandubaService
#
class ApiService( AkuandubaService ):

  #
  # Here EDMs and other stuff will not be available yet, this is just for attributes initialization and superclass init
  #
  def __init__(self, name, update_time = 10 * Second):

    # Mandatory stuff
    AkuandubaService.__init__(self, name)

    self._updateTime = update_time
    self.__data = 0

  #
  # At this point, the context will be set and all EDMs, services and tools will already be attached to it
  # If you need to get anything from context to set something on this service's initialization, this is the time
  #
  def initialize(self):

    # Initialize thread, as every service runs as a thread
    super().initialize()
    if self.start().isFailure():
      MSG_FATAL( self, "Impossible to initialize the %s service", self.name())
      return StatusCode.FAILURE

    # Constructing Flask app
    self.__app = Flask(__name__)
    self.__cors = CORS(self.__app, supports_credentials = True)

    # Making route for getting signal data
    @self.__app.route('/wind_data')
    def get_wind_data():

        import json
        
        def get_data():
            while True:
                while (self.__data == 0):
                    pass
                json_data = json.dumps(self.__data)
                yield "data: {}\n\n".format(json_data)
                time.sleep(1)

        return Response(get_data(), mimetype='text/event-stream')

    # Lock the initialization. After that, this tool can not be initialized once again
    self.init_lock()
    return StatusCode.SUCCESS

  #
  # This method will run once every Akuanduba loop only. Use this to get the data you want from context, process it
  # and store it on another dataframe or whatever you wanna do.
  #
  def execute( self, context ):

    datafame = self.getContext().getHandler("WindData")

    self.__data = datafame.getHistory()

    # Always return SUCCESS
    return StatusCode.SUCCESS

  #
  # This will call finalization for this service
  #
  def finalize(self):

    super().finalize()

    # Always return SUCCESS
    return StatusCode.SUCCESS

  #
  # The "run" method runs on separated threads, here you can get data and store it to the Akuanduba queue.
  # Access to context is not recommended here, since it could break the data for the "execute" loop.
  #
  def run( self ):

    # Imports
    import traceback

    # While loop
    while self.statusThread() == StatusThread.RUNNING:

        time.sleep(5)

        try:
            # Running server
            self.__app.run(host = "0.0.0.0", port = 5000, debug = False)

        except Exception:
            # Printing the exception
            print(traceback.format_exc())

    return StatusCode.FAILURE
