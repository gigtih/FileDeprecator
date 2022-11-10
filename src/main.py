functions_list = [
    # "game",
    "GetService",
    "task.wait",
    "FindFirstChild"
]

DEPRECATOR_VERSION = 0.1

selected = input("Welcome to the file deprecator. Please select a option: [D] to deprecate (must be a luau file), [V] for the version\n")
lower_input = selected.lower()

def deprecate_file(pathToFile: str):
    if not(".lua" in pathToFile):
        raise("File does not contain .lua")
    
    with open(pathToFile, "r") as file:
        with open(input("Please insert the path & name of the deprecated file: ") + ".lua" , 'w') as deprecatedFile:
            file_content = file.readlines()
            for lineContent in file_content:
                for functions in functions_list:
                    if functions in lineContent:
                        match functions:
                            # case "game": deprecatedFile.write(lineContent.replace("game", "Game"))
                            case "GetService": deprecatedFile.write(lineContent.replace("GetService", "service"))
                            case "task.wait": deprecatedFile.write(lineContent.replace("task.wait", "Wait"))
                            case "FindFirstChild": deprecatedFile.write(lineContent.replace("FindFirstChild", "findFirstChild"))

            deprecatedFile.close()

        file.close()

if lower_input == 'd':
    file_path = input("Great! Now please insert a path to a file: ")
    deprecate_file(file_path)
elif lower_input == 'v':
    print("The current deprecator version is: " + str(DEPRECATOR_VERSION))
