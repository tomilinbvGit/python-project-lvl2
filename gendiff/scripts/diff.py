def diff(shared_keys, file_1, file_2):
    result = "{\n"

    for key in shared_keys:
        if key not in file_2:
            result += " - {0}: {1}\n".format(key, str(file_1[key]))
        elif key not in file_1:
            result += " + {0}: {1}\n".format(key, str(file_2[key]))
        elif file_1[key] == file_2[key]:
            result += "   {0}: {1}\n".format(key, str(file_1[key]))
        else:
            result += " - {0}: {1}\n".format(key, str(file_1[key]))
            result += " + {0}: {1}\n".format(key, str(file_2[key]))

    result += "}"
    return result
