


from datetime import datetime
from typing import List, Optional




class User:
    


    def __init__(self, user_id: int, name: str, email: str, password_hash: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.session_token: Optional[str] = None
        self.created_at: datetime = datetime.now()


    def logout(self):
        
        self.session_token = None


    def update_profile(self, name: str = None, email: str = None):
       
        if name:
            self.name = name
        if email:
            self.email = email


    def __repr__(self):
        return f"User(id={self.user_id}, email={self.email})"




class Property:
    


    VALID_TYPES = ['residential', 'commercial', 'rental']


    def __init__(self, property_id: int, title: str, prop_type: str,
                 location: str, price: float, bedrooms: int,
                 amenities: List[str], is_available: bool = True):
        if prop_type not in self.VALID_TYPES:
            raise ValueError(f'Invalid property type: {prop_type}')
        self.property_id = property_id
        self.title = title
        self.prop_type = prop_type
        self.location = location
        self.price = price
        self.bedrooms = bedrooms
        self.amenities = amenities
        self.is_available = is_available
        self._observers = []  

    def register_observer(self, observer):
       
        if observer not in self._observers:
            self._observers.append(observer)


    def remove_observer(self, observer):
       
        self._observers.remove(observer)


    def set_availability(self, status: bool):
       
        self.is_available = status
        self._notify_observers()


    def _notify_observers(self):
       
        for observer in self._observers:
            observer.update(self)


    def __repr__(self):
        return f"Property(id={self.property_id}, title={self.title})"




class Favourites:
   

    def __init__(self, user: User):
        self.user = user
        self._saved: List[Property] = []


    def add_property(self, prop: Property):
       
        if prop not in self._saved:
            self._saved.append(prop)


    def remove_property(self, property_id: int):
        
        self._saved = [p for p in self._saved if p.property_id != property_id]


    def list_favourites(self) -> List[Property]:
        
        return list(self._saved)




class Viewing:
    


    VALID_STATUSES = ['pending', 'confirmed', 'cancelled']


    def __init__(self, viewing_id: int, user: User,
                 prop: Property, scheduled_date: datetime):
        self.viewing_id = viewing_id
        self.user = user
        self.prop = prop
        self.scheduled_date = scheduled_date
        self.status = 'pending'


    def confirm(self):
       
        self.status = 'confirmed'


    def cancel(self):
        
        self.status = 'cancelled'


    def __repr__(self):
        return f"Viewing(id={self.viewing_id}, status={self.status})"
