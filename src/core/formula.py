import math
from typing import Dict, Tuple, Any, Optional

class FormulaManager:
    def __init__(self):
        self.formulas: Dict[str, dict] = {}
        
    def evaluate_formula(self, formula_text: str, variables: Dict[str, float], 
                        formula_name: Optional[str] = None) -> Tuple[Optional[float], str, str]:
        """
        Evaluates a mathematical formula with given variables.
        Returns (result_value, formatted_result, error_message)
        """
        try:
            # Add math functions to evaluation context
            math_context = {
                'pi': math.pi,
                'e': math.e,
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'sqrt': math.sqrt,
                'pow': math.pow,
                'abs': abs
            }
            
            # Combine variables and math functions
            eval_context = {**variables, **math_context}
            
            # Calculate result
            result = eval(formula_text, {"__builtins__": {}}, eval_context)
            return result, f"{result:.2f}", ""
            
        except Exception as e:
            return None, "--", str(e)
    
    def add_formula(self, name: str, formula: str) -> bool:
        """Adds a new formula to the manager"""
        if name in self.formulas:
            return False
        
        self.formulas[name] = {
            "formula": formula,
            "result_value": None
        }
        return True
    
    def get_formula(self, name: str) -> Optional[dict]:
        """Retrieves formula data by name"""
        return self.formulas.get(name)
