# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class AutheticatedAction(Action):

    def name(self) -> Text:
        return "action_autheticated"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        email = tracker.get_slot("email")
        otp = tracker.get_slot("otp")
        if email is not None and otp is not None:
            dispatcher.utter_message(template="utter_autheticated_successfully")
        else:
            dispatcher.utter_message(template="utter_authetication_failed")

        return []
