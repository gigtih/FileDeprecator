functions_list = [
    "game",
    "GetService",
    "task.wait",
    "WaitForChild",
    "FindFirstChild"
]

DEPRECATOR_VERSION = 0.1

selected = input("Welcome to the file deprecator. Please select a option: [D] to deprecate (must be a luau file), [V] for the version\n")
lowered_input = selected.lower()

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
                            case "game": deprecatedFile.write(lineContent.replace("game", "Game"))
                            case "GetService": deprecatedFile.write(lineContent.replace("GetService", "service"))
                            case "task.wait": deprecatedFile.write(lineContent.replace("task.wait", "wait"))
                            case "WaitForChild": deprecatedFile.write(lineContent.replace("WaitForChild", "waitForChild"))

            deprecatedFile.close()

        file.close()

if lowered_input == 'd':
    file_path = input("Great! Now please insert a path to a file: ")
    deprecate_file(file_path)
elif lowered_input == 'v':
    print("The current deprecator version is: " + str(DEPRECATOR_VERSION))
