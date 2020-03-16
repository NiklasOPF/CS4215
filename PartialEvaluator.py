#use semicolons to differnetiate "lines"


def partially_evaluate (program):
    modified = False  #flag that cehecks if we have been able ot improve the program.
    lines = program.split(";");
    for line in lines:
        print(line)
