


from typing import List, Optional, Dict
from models import Property




class PropertyRepository:
    """
    
    """


    def __init__(self):
        self._store: Dict[int, Property] = {} 


    def save(self, prop: Property):
        
        self._store[prop.property_id] = prop


    def find_by_id(self, property_id: int) -> Optional[Property]:
        
        return self._store.get(property_id)


    def delete(self, property_id: int):
        
        self._store.pop(property_id, None)


    def find_by_filters(self, location: str = None, max_price: float = None,
                         prop_type: str = None, bedrooms: int = None) -> List[Property]:
        """
        
        """
        results = list(self._store.values())
        if location:
            results = [p for p in results
                       if location.lower() in p.location.lower()]
        if max_price is not None:
            results = [p for p in results if p.price <= max_price]
        if prop_type:
            results = [p for p in results if p.prop_type == prop_type]
        if bedrooms is not None:
            results = [p for p in results if p.bedrooms >= bedrooms]
        return results


    def get_all(self) -> List[Property]:
        
        return list(self._store.values())
