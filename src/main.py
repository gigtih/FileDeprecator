# 11/09/2022
# @gigtih

functions_list = [
    "GetService",
    "task.wait",
    "FindFirstChild"
    # "game",
]

DEPRECATOR_VERSION = 0.1

selected = input("Welcome to the file deprecator. Please select a option: [D] to deprecate (must be a luau file), [V] for the version\n")
lowerinput = selected.lower().strip()

def deprecate_file(pathToFile: str):
    if not(".lua" in pathToFile):
        raise("File does not contain .lua")

    with open(pathToFile, "r") as file:
        deprecated_file_path = input("Please insert the path & name of the deprecated file: ")
        file_content = file.readlines()
        print("\nDEPRECATING...")
        with open(deprecated_file_path + ".lua", 'w') as deprecatedFile:
            deprecatedFile.write("--[[ File deprecated with file deprecator by gigtih, https://github.com/gigtih/FileDeprecator ]]\n\n")
            # TODO: add game -> Game
            for lineContent in file_content: 
                if functions_list[0] in lineContent:
                    deprecatedFile.write(lineContent.replace("game:GetService", "Game:service"))
                elif functions_list[1] in lineContent:
                    deprecatedFile.write(lineContent.replace("task.wait", "Wait"))
                elif functions_list[2] in lineContent:
                    deprecatedFile.write(lineContent.replace("FindFirstChild", "findFirstChild"))
                else:
                    deprecatedFile.write(lineContent)

            deprecatedFile.close()

        file.close()
        print("\n{0} was successfully deprecated, deprecated file can be found at: {1}".format(file.name, deprecatedFile.name))

    return

if lowerinput == 'd':
    file_path = input("Great! Now please insert a path to a file: ")
    deprecate_file(file_path.strip())
elif lowerinput == 'v':
    print("The current deprecator version is: " + str(DEPRECATOR_VERSION))