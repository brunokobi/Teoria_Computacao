import utils


def universal(progString, inString):
    # Execute the definition of the function in progString. This defines
    # the function, but doesn't invoke it.
    exec(progString)
    # Now that the function is defined, we can extract a reference to it.
    progFunction = utils.extractMainFunction(progString,
                                             locals())
    # Invoke the desired function with the desired input string.
    return progFunction(inString)
