from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from . import connector

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("PERSON")
        email = tracker.get_slot("email")
        number = tracker.get_slot("phone-number")
        connector.user_commit(name,email,number)
        dispatcher.utter_message(text=f"Thanks for jumping into our website {name}, our costumer support employee will contact you")

        return []
