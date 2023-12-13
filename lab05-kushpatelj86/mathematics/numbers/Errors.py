class FileError(Exception):
    pass


class FileNotFound(Exception):
    pass



class FilePermissionError(Exception):
    pass




def file_operations(op_type):
    if op_type == "not found":
        raise FileNotFoundError("File not found")
    elif op_type == "permission":
        raise FilePermissionError("Permission denied")
    else:
        print("File operation successful")


file_operations("permission")

