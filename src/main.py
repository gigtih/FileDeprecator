# 11/09/2022
# @gigtih

from sys import argv

functions_list = [
    "GetService",
    "task.wait",
    "FindFirstChild",
    "Destroy"
    # "game"
]

DEPRECATOR_VERSION = "0.2"

def deprecate_file(pathToFile: str):
    if not ".lua" in pathToFile:
        exit("File does not contain .lua")

    with open(pathToFile, "r") as file:
        deprecated_file_path = input("Please insert the path & name of the deprecated file: ")
        file_content = file.readlines()
        print("\nDEPRECATING...")
        with open(deprecated_file_path + ".lua", 'w') as deprecatedFile:
            deprecatedFile.write("--[[ File deprecated with file deprecator by gigtih, https://github.com/gigtih/FileDeprecator Version: {0} ]]\n\n".format(str(DEPRECATOR_VERSION)))

            for lineContent in file_content:
                if functions_list[0] in lineContent:
                    deprecatedFile.write(lineContent.replace("game:GetService", "Game:service"))
                elif functions_list[1] in lineContent:
                    deprecatedFile.write(lineContent.replace("task.wait", "Wait"))
                elif functions_list[2] in lineContent:
                    deprecatedFile.write(lineContent.replace(":FindFirstChild", ":findFirstChild"))
                elif functions_list[3] in lineContent:
                    deprecatedFile.write(lineContent.replace(":Destroy", ":destroy"))
                else:
                    deprecatedFile.write(lineContent)

            deprecatedFile.close()

        file.close()
        print("\n{0} was successfully deprecated, deprecated file can be found at: {1}".format(file.name, deprecatedFile.name))

    return



if len(argv) == 1:
    print("Here some commands:\n--version\n--deprecate <filepath>")
    exit(0)

if argv[1] == "--version":
    print("The current deprecator version is: " + DEPRECATOR_VERSION)
elif argv[1] == "--deprecate":
    deprecate_file(argv[2].strip())