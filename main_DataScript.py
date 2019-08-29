# Akuanduba imports
from Akuanduba.core import Akuanduba, LoggingLevel, AkuandubaTrigger
from Akuanduba import ServiceManager, ToolManager, DataframeManager
from Akuanduba.core.constants import Second
from Akuanduba.triggers import TimerCondition

# This sample's imports
from dataframes.WindData import *
from services.AnemometerService import *
from tools.SendDataTool import *

# Creating services
svc = AnemometerService("Anemometer service")

# Creating tools
tool = SendDataTool ("Tool for data sending")

# Creating dataframes
windDataframe = WindData ("WindData")

# Creating time trigger
trigger  = AkuandubaTrigger("Time Trigger", triggerType = 'or')

# Append conditions and tools to trigger just adding them
# Tools appended to the trigger will only run when trigger is StatusTrigger.TRIGGERED,
# and will run in the order they've been appended
trigger += TimerCondition( "5-second condition", 5 * Second )
trigger += tool

# Creating Akuanduba
manager = Akuanduba("Akuanduba", level=LoggingLevel.INFO)

# Appending services
ServiceManager += svc

# Appending tools
#
# ToolManager += TOOL_1
# ToolManager += TOOL_2
#
ToolManager += trigger

# Apprending dataframes
DataframeManager += windDataframe

# Initializing 
manager.initialize()
manager.execute()
manager.finalize()