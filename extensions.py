import glob

def getExtensions():
    """Creates a dict to hold the extensions paired to their freq
    of the files in the directory then returns that dict.
    """
    extensions = {}                                     # define dict

    files = glob.glob("*.*")                            # grab all the file names
    for fn in files:                                    # loop over the names
        ext = fn.split(".")[1]                          # split to get extension
        extensions[ext] = extensions.get(ext, 0) + 1    # update dict

    return extensions                                   # return dict



