import abc
import datetime

from .utils import CaseInsensitiveDict
from .keyboard import KEYBOARD


class Action(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __call__(self):
        pass


class HotKeyAction(Action):

    def __init__(self, keys):
        self._keys = keys

    def __call__(self):
        KEYBOARD.hotkey(self._keys)


class CallbackAction(Action):

    def __init__(self, callback):
        self._callback = callback

    def __call__(self):
        self._callback()


class ActionsController:

    def __init__(self):
        self._actions = CaseInsensitiveDict()

    def register(self, actions, mode=None):
        self._actions[mode] = actions

    def get_modes(self):
        result = []
        for mode in self._actions.keys():
            result.append({
                "name": mode
            })

        return result

    def get_actions(self, mode=None):
        result = []

        if mode:
            for action in self._actions[mode].keys():
                result.append({
                    "mode": mode,
                    "name": action
                })
            return result

        for mode, actions in self._actions.items():
            for name in actions:
                result.append({
                    "mode": mode,
                    "name": name
                })

        return result

    def get_action(self, action):
        mode = action["mode"]
        name = action["name"]

        return self._actions[mode][name]

    def call_action(self, action):
        callable = self.get_action(action)
        callable()

        action['timestamp'] = str(datetime.datetime.now())
        return action


raspberry_pi_os_actions = {
    "LockScreen": HotKeyAction(["ctrl", "alt", "l"]),
}


media_actions = {
    "Play": HotKeyAction(["playpause"]),
    "Pause": HotKeyAction(["playpause"]),
    "VolumeUp": HotKeyAction(["volumeup"]),
    "VolumeDown": HotKeyAction(["volumedown"]),
    "Mute": HotKeyAction(["volumemute"]),
    "Unmute": HotKeyAction(["volumemute"]),
    "PlaylistPrevious": HotKeyAction(["nexttrack"]),
    "PlaylistNext": HotKeyAction(["prevtrack"])
}


youtube_actions = {
    "Play": HotKeyAction(["K"]),
    "Pause": HotKeyAction(["K"]),
    "Mute": HotKeyAction(["M"]),
    "Unmute": HotKeyAction(["M"]),
    "VolumeUp": HotKeyAction(["up"]),
    "VolumeDown": HotKeyAction(["down"]),
    "Forward": HotKeyAction(["right"]),
    "Rewind": HotKeyAction(["left"]),
    "FastForward": HotKeyAction(["L"]),
    "FastRewind": HotKeyAction(["J"]),
    "Captions": HotKeyAction(["C"]),
    "Fullscreen": HotKeyAction(["F"]),
    "ExitFullscreen": HotKeyAction(["F"])
}


netflix_actions = {
    "Play": HotKeyAction(["space"]),
    "Pause": HotKeyAction(["space"]),
    "Mute": HotKeyAction(["M"]),
    "Unmute": HotKeyAction(["M"]),
    "VolumeUp": HotKeyAction(["up"]),
    "VolumeDown": HotKeyAction(["down"]),
    "Forward5s": HotKeyAction(["right"]),
    "Rewind5s": HotKeyAction(["left"]),
    "Fullscreen": HotKeyAction(["F"]),
    "ExitFullscreen": HotKeyAction(["F"]),
    "Skip": HotKeyAction(["S"]),
}


hbo_max_actions = {
    "Play": HotKeyAction(["space"]),
    "Pause": HotKeyAction(["space"]),
    "Fullscreen": HotKeyAction(["F"]),
    "ExitFullscreen": HotKeyAction(["F"]),
}


ACTIONS_CONTROLLER = ActionsController()
ACTIONS_CONTROLLER.register(raspberry_pi_os_actions, mode="RaspberryPiOS")
ACTIONS_CONTROLLER.register(media_actions, mode="Media")
ACTIONS_CONTROLLER.register(youtube_actions, mode="YouTube")
ACTIONS_CONTROLLER.register(netflix_actions, mode="Netflix")
ACTIONS_CONTROLLER.register(hbo_max_actions, mode="HBOMax")
