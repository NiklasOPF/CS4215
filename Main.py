import PartialEvaluator as pe

program = "function times_two(x) { \
    return x + x;                  \
    }"
pe.partially_evaluate(program);