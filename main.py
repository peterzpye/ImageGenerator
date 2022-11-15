# This is a sample Python script.
import sys
import src.model.DCGAN.model as dcgan

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def cleanRootPath(root):
    if root[-1] != "/":
        return root + "/"
    return root

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataRoot = cleanRootPath(input("dataRoot: "))
    outputDir = cleanRootPath(input("outputDir: "))

    dcgan.train(dataRoot, outputDir)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
