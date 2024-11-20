# Mini Configurator

A dynamic calculator application that lets you create sliders and use them in mathematical formulas. The application updates all results in real-time as you adjust the sliders.

## Features

- Create sliders with custom names and ranges
- Write formulas using slider values
- Use formula results in other formulas
- Real-time updates as slider values change
- Dark theme UI with modern styling

## Project Structure

```
mini_configurator/
├── src/
│   ├── core/
│   │   ├── formula.py     # Formula evaluation and management
│   │   └── slider.py      # Slider management
│   ├── gui/
│   │   ├── theme.py       # UI theme and styling
│   │   ├── windows.py     # Main window layout
│   │   └── callbacks.py   # GUI event handlers
│   └── utils/             # Utility functions (future use)
└── main.py                # Application entry point
```

## Dependencies

- Python 3.6+
- DearPyGUI

## Installation

1. Install Python 3.6 or higher
2. Install the required package:
   ```
   pip install dearpygui
   ```

## Running the Application

Run the application using:
```
python main.py
```

## Usage

1. Create sliders:
   - Enter a name and optional range values
   - Click "Add Slider" to create
   
2. Create formulas:
   - Enter a name for your formula
   - Write your formula using slider names and math functions
   - Click "Add Formula" to create
   
3. Available functions:
   - Basic operators: +, -, *, /, **
   - Math functions: sin, cos, tan, sqrt, pow, abs
   - Constants: pi, e

4. Tips:
   - Click on slider or formula names to insert them into your formula
   - Formulas update automatically when you move sliders
   - You can use results from previous formulas in new formulas
