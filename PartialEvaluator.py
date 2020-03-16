#use semicolons to differnetiate "lines"

#def partially_evaluate(program):
#    my_list = []
#    i = 0;
#    while (i<program)
#   return 2


def partially_evaluate (program):
    modified = False  #flag that cehecks if we have been able ot improve the program.
    lines = program.split(";");
    for line in lines:
        print(line)

program = "hello; my name is Peter; I am 26 years old"
partially_evaluate(program);