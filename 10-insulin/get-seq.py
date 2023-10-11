
def insulinSequence(fileName, insulin):
    with open(fileName, "w") as targetFile:
        targetFile.write(insulin)

with open("clean_preproinsulin-seq.txt") as myInput:
    insulinSequence("lsinsulin-seq.txt", myInput.read(24))
    insulinSequence("binsulin-seq.txt", myInput.read(30))
    insulinSequence("cinsulin-seq.txt", myInput.read(35))
    insulinSequence("ainsulin-seq.txt", myInput.read(21))
