import dearpygui.dearpygui as dpg

class MainWindow:
    def __init__(self, callback_manager, formula_manager, slider_manager):
        self.callback_manager = callback_manager
        self.formula_manager = formula_manager
        self.slider_manager = slider_manager
        
    def create_main_window(self, default_font):
        """Creates and sets up the main application window with docking"""
        # Create dockspace
        with dpg.window(label="Mini Configurator", tag="main_window", no_title_bar=True):
            with dpg.viewport_menu_bar():
                with dpg.menu(label="Windows"):
                    dpg.add_menu_item(label="Show New Slider Window", callback=lambda: dpg.configure_item("new_slider_window", show=True))
                    dpg.add_menu_item(label="Show Active Sliders", callback=lambda: dpg.configure_item("active_sliders_window", show=True))
                    dpg.add_menu_item(label="Show New Formula Window", callback=lambda: dpg.configure_item("new_formula_window", show=True))
                    dpg.add_menu_item(label="Show Active Formulas", callback=lambda: dpg.configure_item("active_formulas_window", show=True))
            
        # New Slider Window
        with dpg.window(label="New Slider", tag="new_slider_window", width=600, height=200, pos=[10, 30]):
            dpg.bind_font(default_font)
            dpg.add_text("Create New Slider", color=(150, 255, 150))
            with dpg.group(horizontal=True):
                dpg.add_input_text(label="Name", tag="slider_name", width=100)
                dpg.add_input_float(label="Default", tag="slider_default", default_value=0, width=70)
                dpg.add_input_float(label="Min", tag="slider_min", default_value=0, width=70)
                dpg.add_input_float(label="Max", tag="slider_max", default_value=100, width=70)
            dpg.add_button(label="Add Slider", callback=self.add_new_slider)
            dpg.add_text("", tag="creation_error", color=(255, 0, 0))

        # Active Sliders Window
        with dpg.window(label="Active Sliders", tag="active_sliders_window", width=400, height=300, pos=[620, 30]):
            dpg.bind_font(default_font)
            dpg.add_text("Active Sliders", color=(150, 255, 150))
            dpg.add_group(tag="sliders_group")

        # New Formula Window
        with dpg.window(label="New Formula", tag="new_formula_window", width=600, height=300, pos=[10, 240]):
            dpg.bind_font(default_font)
            dpg.add_text("Create Formula", color=(150, 255, 150))
            dpg.add_input_text(label="Name", tag="formula_name", width=150)
            dpg.add_input_text(label="Formula", tag="formula_input", width=-1)
            dpg.add_button(label="Add Formula", callback=self.add_formula)
            dpg.add_text("", tag="formula_error", color=(255, 0, 0))
            # Available Variables Display
            dpg.add_text("", tag="available_vars")

        # Active Formulas Window
        with dpg.window(label="Active Formulas", tag="active_formulas_window", width=400, height=300, pos=[620, 240]):
            dpg.bind_font(default_font)
            dpg.add_text("Active Formulas", color=(150, 255, 150))
            dpg.add_group(tag="formulas_group")
    
    def add_new_slider(self):
        """Adds a new slider to the UI"""
        name = dpg.get_value("slider_name").strip()
        if not name or name in self.slider_manager.get_all_sliders():
            dpg.set_value("creation_error", "Error: Invalid or duplicate name")
            return
            
        try:
            default = float(dpg.get_value("slider_default"))
            min_val = float(dpg.get_value("slider_min"))
            max_val = float(dpg.get_value("slider_max"))
        except ValueError:
            dpg.set_value("creation_error", "Error: Invalid number format")
            return
            
        slider_tag = f"slider_{len(self.slider_manager.get_all_sliders())}"
        
        if self.slider_manager.add_slider(name, default, min_val, max_val, slider_tag):
            with dpg.group(parent="sliders_group"):
                dpg.add_button(
                    label=name, 
                    callback=lambda s: self.callback_manager.insert_variable(s, name)
                )
                dpg.add_slider_float(
                    default_value=default,
                    min_value=min_val,
                    max_value=max_val,
                    tag=slider_tag,
                    callback=self.callback_manager.slider_callback,
                    width=-1
                )
            
            dpg.set_value("slider_name", "")
            dpg.set_value("creation_error", "")
            self.callback_manager.update_available_variables()
    
    def add_formula(self):
        """Adds a new formula to the UI"""
        name = dpg.get_value("formula_name").strip()
        formula = dpg.get_value("formula_input").strip()
        
        if not name or not formula:
            dpg.set_value("formula_error", "Error: Name and formula required")
            return
            
        if name in self.formula_manager.formulas:
            dpg.set_value("formula_error", "Error: Formula name already exists")
            return
            
        if self.formula_manager.add_formula(name, formula):
            result_tag = f"result_{name}"
            error_tag = f"error_{name}"
            self.formula_manager.formulas[name]["result_tag"] = result_tag
            self.formula_manager.formulas[name]["error_tag"] = error_tag
            
            with dpg.group(parent="formulas_group"):
                with dpg.group(horizontal=True):
                    dpg.add_button(
                        label=name,
                        callback=lambda s: self.callback_manager.insert_variable(s, name)
                    )
                    dpg.add_text("=")
                    dpg.add_text(formula)
                    dpg.add_text("→")
                    dpg.add_text("--", tag=result_tag)
                dpg.add_text("", tag=error_tag, color=(255, 100, 100))
            
            dpg.set_value("formula_name", "")
            dpg.set_value("formula_input", "")
            dpg.set_value("formula_error", "")
            self.callback_manager.update_available_variables()
            self.callback_manager.update_all_formulas()
