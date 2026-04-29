


from typing import List
from models import User, Property




class Notification:
    """
   """


    def __init__(self, notification_id: int, user: User):
        self.notification_id = notification_id
        self.user = user
        self.messages: List[str] = []


    def update(self, prop: Property):
        """
        
        """
        if prop.is_available:
            msg = (f'Property "{prop.title}" is now available! '
                   f'Notifying {self.user.email}')
        else:
            msg = (f'Property "{prop.title}" is no longer available.')
        self.messages.append(msg)
        # In production: trigger email via EmailService


    def get_messages(self) -> List[str]:
        
        return list(self.messages)
