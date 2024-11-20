from typing import Dict, Optional

class SliderManager:
    def __init__(self):
        self.sliders: Dict[str, dict] = {}
    
    def add_slider(self, name: str, default: float, min_val: float, max_val: float, tag: str) -> bool:
        """
        Adds a new slider to the manager.
        Returns True if successful, False if name already exists.
        """
        if name in self.sliders:
            return False
            
        self.sliders[name] = {
            "tag": tag,
            "default": default,
            "min": min_val,
            "max": max_val
        }
        return True
    
    def get_slider(self, name: str) -> Optional[dict]:
        """Retrieves slider data by name"""
        return self.sliders.get(name)
    
    def get_all_sliders(self) -> Dict[str, dict]:
        """Returns all sliders"""
        return self.sliders.copy()
