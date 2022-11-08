#TODO: add more functions
deprecated_functions = [
    "game", "Game",
    "task.wait", "wait",
    "GetService", "service"
]

DEPRECATOR_VERSION = 0.1

selected = input("Welcome to the file deprecator. Please select a option: [D] to deprecate (must be a luau file), [V] for the version\n")
lowered_input = selected.lower()

def deprecate_file(pathToFile: str):
    if not(".lua" in pathToFile):
        raise("File does not contain .lua")
    
    with open(pathToFile, "r+") as file:
        with open(input("Please insert the path & name of the deprecated file: ") + ".lua" , 'w') as deprecatedFile:
            file_content = file.readlines()
            for lineContent in file_content:
                for deprecatedFuncs in deprecated_functions:
                    if deprecatedFuncs in lineContent:
                        match deprecatedFuncs:
                            case "game": deprecatedFile.write("Game")
                            case "GetService": deprecatedFile.write(":service")
                            case "task.wait": deprecatedFile.write("wait")

            deprecatedFile.close()

        file.close()

if lowered_input == 'd':
    file_path = input("Great! Now please insert a path to a file: ")
    deprecate_file(file_path)
elif lowered_input == 'v':
    print("The current deprecator version is: " + str(DEPRECATOR_VERSION))