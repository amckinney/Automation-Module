# File: Automation Module
# Author: Alex McKinney
# Date: August 19, 2015
#
# Description: This is a framework for creating your own automation scripts
#              in python. Simply import the module 'automation' after
#              downloading this module, and you will have access to the
#              functions written here.
#              This module is intended to modified for your particular
#              automation task. Follow the directions littered throughout the
#              code in order to use this script effectively.
#              Hope you enjoy it!
#

import os
import re
import sys
import getopt
import datetime

class Automation:

    ### YOUR CODE HERE ###
    # Define any instance variables you might need for your particular
    # automation task.
    error = None
    status = None
    config = None
    options = None
    logData = None
    outputFile = None
    outputDirectory = None

    def __init__(self):


    def printUsage(self):
        print " ------------ "
        print "USAGE:"
        ### YOUR CODE HERE ###
        print " ------------ "

    def parseArgumentsForOptions(self, argv):
        ### YOUR CODE HERE ###
        # Define commandLineOptions for your script.
        # Example:
        # commandLineOptions = "hc:" (help, configFile)
        self.options, args = getopt.getopt(argv, commandLineOptions)
        checkOptions()
        return options

    def checkOptions(self):
        if not bool(self.options):
            exitCleanly()

    def displayError(self):
        print "----------------------------------------------"
        print str(self.error)
        print "----------------------------------------------"
        exitWithError()

    def parseOptions(self):
        for opt, arg in self.options:
        ### YOUR CODE HERE ###
        # Use the commandLineOption definitions here.
        # Example:
        #     if opt == "-h":
        #         exitCleanly()
        #     elif opt == "-c":
        #         self.config = str(arg)
        #     initializeLog()


    def setVariablesFromConfig(self):
        verifyConfigFieldsExist()
        populateConfigVariables()

    def verifyConfigFieldsExist(self):
        configFile = open(self.config, "r").read()
        ### YOUR CODE HERE ###
        # Include Config File Fields (Keys) in fieldArray.
        # Example:
        # fieldArray = ["API_Key:", "Domain:"] (Login Credentials)
        for field in fieldArray:
            if not re.search(field, configFile):
                self.error = ("ERROR: Config missing fields!" +
                                "\n\tIn function: 'verifyConfigFieldsExist'")
                raise ValueError

    def populateConfigVariables(self):
        configFile = open(self.config, "r")
        ### YOUR CODE HERE ###
        # Include simple regular expression patterns to access your config data.
        # Example:
        # apiRegex     = "API_Key: (\S+)"
        # domainRegex  = "Domain: (\S+)"

        for line in configFile:
            ### YOUR CODE HERE ###
            # Search each line for the defined regular expressions above/
            # Example:
            # if re.search(apiRegex, line):
            #     self.apiKey = re.search(apiRegex, line).group(1)
            # elif re.search(domainRegex, line):
            #     self.domain = re.search(domainRegex, line).group(1)

    def executeScript(self):
        ### YOUR CODE HERE ###
        # This is where the bulk of your implementation will begin.
        # Check if the arguments were correctly set, then start the main
        # function.
        # Example:
        # if argumentsAreSet():
        #    mainAction()

    def argumentsAreSet(self):
        ### YOUR CODE HERE ###
        # Verify that the arguments are valid for their respective fields
        # Example:
        # return (verifyApiKey(self.apiKey) and verifyDomain(self.domain))

    def initializeLog(self):
        ### YOUR CODE HERE ###
        outputDirectoryName = "ExampleDirectory"
        currentDirectory = os.getcwd()
        self.outputDirectory = os.path.join(os.getcwd(), outputDirectoryName)
        self.outputFile = determineLogName()

        if not os.path.exists(self.outputDirectory):
            os.makedirs(self.outputDirectory)
        os.chdir(self.outputDirectory)
        self.logData = open(self.outputFile, "w+")
        os.chdir(currentDirectory)

    def determineLogName(self):
        baseName = "exampleLog"
        date = datetime.datetime.now()
        dateString = "-{0}_{1}_{2}-{3}_{4}_{5}".format(
            str(date.month),
            str(date.day),
            str(date.year),
            str(date.hour),
            str(date.minute),
            str(date.second))
        logName = baseName + dateString + ".log"
        return logName

    def logResult(self):
        ### YOUR CODE HERE ###
        # Determine the status, based on the result of the script.
        # Typically a PASS, WARNING, or FAIL based on conditionals.
        self.status = "exampleStatus"
        self.logData.write(self.status)

    def printSummary(self):
        print "----------------------------------------------"
        print "Overall Run: " + self.status
        print "----------------------------------------------"

    def exitWithError(self):
        printUsage()
        sys.exit(1)

    def exitCleanly(self):
        printUsage()
        sys.exit(0)
