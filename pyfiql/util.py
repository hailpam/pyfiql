
def pretty_printing(root, level):
    '''
        Prints the Abstract Syntax Tree out using the stringify methods available on the model classes.
    '''
    pretty = '%s%s' % (''.join(['\t' for x in range(level)]), root.constraint)
    print(pretty)
    level += 1
    if root.l_child:
        pretty_printing(root.l_child, level)
    if root.r_child:
        pretty_printing(root.r_child, level)
