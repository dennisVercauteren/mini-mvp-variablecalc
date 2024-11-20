import dearpygui.dearpygui as dpg
import os

def setup_fonts():
    """Sets up the default and title fonts"""
    with dpg.font_registry():
        default_font = dpg.add_font(
            os.path.join(os.environ["WINDIR"], "Fonts", "arial.ttf"), 
            13
        )
        title_font = dpg.add_font(
            os.path.join(os.environ["WINDIR"], "Fonts", "arial.ttf"), 
            16
        )
    return default_font, title_font

def setup_theme():
    """Sets up the global theme with a dark color scheme"""
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            # Spacing
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 8, 8)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 4, 3)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 4, 4)
            dpg.add_theme_style(dpg.mvStyleVar_ItemInnerSpacing, 3, 3)
            
            # Colors
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (40, 40, 40))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (55, 55, 55))
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (76, 158, 216))
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (86, 178, 246))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (200, 200, 200))
            dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (40, 40, 40))
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (40, 40, 40))
            dpg.add_theme_color(dpg.mvThemeCol_Button, (55, 55, 55))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (65, 65, 65))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (75, 75, 75))
            
            # Rounding
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 2)
            dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 3)
            
    return global_theme
