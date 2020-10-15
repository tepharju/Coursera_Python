def write_to_file(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    """
    file = open("uusi.txt","w")

    for s in sentences:
        file.write(s + "\n")

    file.close()
