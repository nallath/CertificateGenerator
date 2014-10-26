__author__ = 'jaime'

from xhtml2pdf import pisa             # Convert html to pdf
from DefaultString import DefaultString
from Value import Value
from DefaultNumber import DefaultNumber

from MainGui import MainGUI

from fnmatch import fnmatch
import wx
app = wx.App()
MainGUI(None)
app.MainLoop()


#Check HTML for %variable% tags and replace them.
def replaceValues(sourceHTML, valueList):
    for value in valueList:
        tag = '%' + str(value.getName()) + '%'
        sourceHTML = sourceHTML.replace(tag,str(value.getValue()))
    return sourceHTML

def checkIfAllValuesAreFound(sourceHTML):
    if fnmatch(sourceHTML,'%*%') == -1:
        return True
    return False

# Utility function
def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
            sourceHtml,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    # close output file
    resultFile.close()                 # close output file

    # return True on success and False on errors
    return pisaStatus.err

# Main program
if __name__=="__main__":
    pisa.showLogging()
    # Define your data
    with open('test.html','r') as f:
        sourceHtml = f.read()
    #sourceHtml = "<html><body><p>Name: %name% <br/>" \
     #            "              Age:  %age% <br/>" \
     #            "Sealed?: %sealType% <br>"\
      #           "facial hair: %faceHair% <br>"\
       #          "<p></body></html>"


    outputFilename = "test2.pdf"
    valueList = []
    valueList.append(Value('name',          value = 'Derpina'))
    valueList.append(Value('age',           DefaultNumber(18,42)))
    valueList.append(Value('race',         DefaultString(["Hispanic","Caucasian","Asian","Black"])))
    valueList.append(Value('hair',          DefaultString(["Brown","Blond","Red"])))
    valueList.append(Value('eyes',          DefaultString(["Green","Blue","Brown"])))
    valueList.append(Value('teeth',         DefaultString(["All natural"])))
    valueList.append(Value('faceHair',      DefaultString(["Clean shaved", "Mustache","Beard","Stubble"])))
    valueList.append(Value('idMethod',      DefaultString(["Fingerprints","Dental"])))
    valueList.append(Value('relationState', DefaultString(["Married","Single","Registered partnership",])))
    valueList.append(Value('mortuary',      DefaultString(["Random"])))
    valueList.append(Value('sealType',      DefaultString(["Not sealed"])))
    valueList.append(Value('synopsis',      DefaultString([""])))
    valueList.append(Value('investigator',  DefaultString([""]))) #Add random name generator instead of string list
    valueList.append(Value('caseNum',       DefaultNumber(1206184, 1802190)))
    valueList.append(Value('placeFound',    DefaultString([""])))
#    valueList.append(Value( ))

    sourceHtml = replaceValues(sourceHtml, valueList)
    print sourceHtml
    if(checkIfAllValuesAreFound(sourceHtml) == False):
        print 'Not all variables were removed from the template!'
    convertHtmlToPdf(sourceHtml, outputFilename)