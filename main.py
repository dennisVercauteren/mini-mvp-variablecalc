import dearpygui.dearpygui as dpg
from src.gui.theme import setup_theme, setup_fonts
from src.gui.windows import MainWindow
from src.gui.callbacks import CallbackManager
from src.core.slider import SliderManager
from src.core.formula import FormulaManager

def main():
    # Initialize DearPyGUI
    dpg.create_context()
    
    # Create managers
    slider_manager = SliderManager()
    formula_manager = FormulaManager()
    callback_manager = CallbackManager(formula_manager, slider_manager)
    
    # Setup theme and fonts
    default_font, title_font = setup_fonts()
    global_theme = setup_theme()
    dpg.bind_theme(global_theme)
    
    # Create main window
    main_window = MainWindow(callback_manager, formula_manager, slider_manager)
    main_window.create_main_window(default_font)
    
    # Setup viewport
    dpg.create_viewport(title="Mini Configurator", width=1280, height=800)
    dpg.configure_viewport(0, x_pos=100, y_pos=100)
    
    # Enable docking
    dpg.configure_app(docking=True, docking_space=True)
    
    dpg.setup_dearpygui()
    dpg.show_viewport()
    
    # Configure main window
    dpg.set_primary_window("main_window", True)
    
    # Start the main loop
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
    
    # Cleanup
    dpg.destroy_context()

if __name__ == "__main__":
    main()