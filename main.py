from gui import MyGui
from api_manager import ApiManager

gui = MyGui(None)
api_manager = ApiManager(gui)
gui.api_manager = api_manager
gui.run_root()