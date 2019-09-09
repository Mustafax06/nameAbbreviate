def abbreviateName(fullName, fNameStatement, mNameStatement, sNameStatement):
    output = ""
    nameLenLimit = 3
    sFullName = fullName.split()
    fName = sFullName[0]
    sName = sFullName[-1]
    if fNameStatement is True:
        output += setOutputType(fNameStatement, fName[0])
    else:
        output += setOutputType(fNameStatement, fName[0])

    # get all elements between the first and the last elements
    midNames = sFullName[1:-1]
    if mNameStatement is True:
        if len(sFullName) >= nameLenLimit:
            if len(midNames) >= 0:
                for midName in midNames:
                    output += setOutputType(mNameStatement, midName[0])
    else:
        for midName in midNames:
            print(output)
            output += setOutputType(fNameStatement, midName)

    if sNameStatement is True:
        output += setOutputType(sNameStatement, sName[0])
    else:
        output += setOutputType(fNameStatement, sName)
    print(output)


def setOutputType(short, name):
    if short is False:
        return name + " "
    else:
        return name[0] + "." + " "


fNameStatement = True
mNameStatement = True
sNameStatement = False
abbreviateName("Mustafa Kemal Demir", fNameStatement,
               mNameStatement, sNameStatement)
