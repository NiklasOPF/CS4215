import PartialEvaluator as pe

program ="1+   2 ;   \n (x**3 + x**2 - x - 1)/(x**2 + 2 * x + 1) ;"
pe.partially_evaluate(program);