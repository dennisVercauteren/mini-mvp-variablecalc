import dearpygui.dearpygui as dpg
from typing import Callable

class CallbackManager:
    def __init__(self, formula_manager, slider_manager):
        self.formula_manager = formula_manager
        self.slider_manager = slider_manager
        
    def insert_text_at_cursor(self, text: str):
        """Adds text to the formula input box"""
        current = dpg.get_value("formula_input")
        dpg.set_value("formula_input", current + text)
    
    def update_all_formulas(self):
        """Updates all formula results when any slider changes"""
        try:
            # Get current slider values
            variables = {}
            for name, data in self.slider_manager.get_all_sliders().items():
                variables[name] = dpg.get_value(data["tag"])
            
            # Update each formula
            for name, data in self.formula_manager.formulas.items():
                result_value, result_text, error = self.formula_manager.evaluate_formula(
                    data["formula"], 
                    variables,
                    name
                )
                data["result_value"] = result_value
                
                if dpg.does_item_exist(data.get("result_tag")):
                    dpg.set_value(data["result_tag"], result_text)
                if dpg.does_item_exist(data.get("error_tag")):
                    dpg.set_value(data["error_tag"], error)
                    
        except Exception as e:
            print(f"Error in update_all_formulas: {e}")
    
    def update_available_variables(self):
        """Updates the list of available variables in the UI"""
        var_list = ["Available variables (click to use):"]
        var_list.extend([f"[{name}] - Slider" for name in self.slider_manager.get_all_sliders().keys()])
        var_list.extend([f"[{name}] - Formula Result" for name in self.formula_manager.formulas.keys()])
        dpg.set_value("available_vars", "\n".join(var_list))
    
    def slider_callback(self, sender):
        """Called when any slider value changes"""
        self.update_all_formulas()
    
    def insert_variable(self, sender, var_name):
        """Called when a variable name is clicked"""
        self.insert_text_at_cursor(var_name)
