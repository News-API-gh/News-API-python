# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:15:29 2017

@author: giulio
"""

###############################################################################
#                                                                             #
#                                Libraries                                    #
#                                                                             #
###############################################################################

import os #used for reading files and directories
import datetime #Check if dates are correct
import requests
import warnings

###############################################################################
#                                                                             #
#                              FUNCTIONS                                      #
#                                                                             #
###############################################################################
""" 
Here you can change the paramaters used in this script

"""

def checkDate(myDate):
    """ This function checks if an input date is real or not
        Input = date as string YYYY-MM-DD
        Output = True or False
    """
    
    y,m,d = myDate.split("-")
    try:
        datetime.datetime(int(y), int(m), int(d))
        return(True)
    except:
        return(False)

def checkLanguage(language):
    """ This function checks if selected language is supported or not
        Input = language code
        Output = True or False
    """
    languages = ["ar","en","cn","de","es","fr","he","it","nl","no","pt","ru","sv","ud"]
    if language in languages:
        return(True)
    else:
        warnings.warn("Unsupported language, skipped")
        return(False)
        
def checkCountry(country):
    """ This function checks if selected country is supported or not
        Input = country code
        Output = True or False
    """
    countries = ["ar","au","br","ca","cn","de","es","fr","gb","hk","ie","in","is","it","nl","no","pk","ru","sa","sv","us","z"]
    if country in countries:
        return(True)
    else:
        warnings.warn("Unsupported country, skipped")
        return(False)
        
def checkCategory(category):
    """ This function checks if selected category is supported or not
        Input = category label
        Output = True or False
    """
    categories = ["business","entertainment","gaming","general","health-and-medical","music","politics","science-and-nature","sport","technology"]
    if category in categories:
        return(True)
    else:
        warnings.warn("Unsupported category, skipped")
        return(False)
        
def checkSorting(sortBy):
    """ This function checks if selected sorting is supported or not
        Input = sorting label
        Output = True or False
    """
    sortBypossibilities = ["relevancy", "popularity", "publishedAt"]
    if(sortBy in sortBypossibilities):
        return(True)
    else:
        warnings.warn("Unsupported sorting, skipped")
        return(False)
        
def getTopHeadlines(apiKey, q="", source="",language="",country="",category=""):
    """ This functions gets the top headlines
        Input:
            apiKey = your News API key
            q = query to search for
            source = the source to scrap the data from, if not specified all sources are reported. This can be a string with one or more comma-separated sources
            language = add a filter by language. Suported languages are ["ar","en","cn","de","es","fr","he","it","nl","no","pt","ru","sv","ud"]
            country = add a filter by country. Supported countries are ["ar","au","br","ca","cn","de","es","fr","gb","hk","ie","in","is","it","nl","no","pk","ru","sa","sv","us","z"]
            category = add a filter by category. Supported categories are  ["busines","entertainment","gaming","general","health-and-medical","music","politics","science-and-nature","sport","technology"]
    """
    
    thisURL = "https://newsapi.org/v2/top-headlines?apiKey="+apiKey
    if(q != ""):
        thisURL += "&q="+q
    if(source != ""): 
        #if a source have been specified
        thisURL += "&sources="+source
    if(country != "" and checkCountry(country)): #if a country have been specified
        thisURL += "&country="+country
    if(language != "" and checkLanguage(language)): #if a language have been specified
        thisURL += "&language="+language
    if(category != "" and checkCategory(category)): #if a category have been specified
        thisURL += "&category="+category
        
    response = requests.get(thisURL)
    response = response.json()
    if(response["status"] == "ok"): #if ok
        return(response["articles"])   
    else: #else return the status code
        return(response["status"])

def getEverything(apiKey,q="",sortBy="",source="",language="",dateFrom="",dateTo="",page=1):
    thisURL = "https://newsapi.org/v2/everything?apiKey="+apiKey
    if(q != ""):
        thisURL += "&q="+q
    if(source != ""):#if a source have been specified
        thisURL += "&sources="+source
    if(language != ""): #if a language have been specified
        thisURL += "&language="+language
    if(page != 1): #if a page number have been specified
        thisURL += "&page="+page
    if(sortBy != "" and checkSorting(sortBy)):
        thisURL += "&sortBy="+sortBy
        
    if(dateFrom != ""): #if a dateFrom have been specified
        if(checkDate(dateFrom)): #and is valid
            thisURL += "&from="+dateFrom
        else:
            warnings.warn("Incorrect dateFrom format, skipped")
            
    if(dateTo != ""): #if a dateTo have been specified
        if(checkDate(dateTo)): #and is valid
            thisURL += "&to="+dateTo        
        else:
            warnings.warn("Incorrect dateTo format, skipped")
        
    response = requests.get(thisURL)
    response = response.json()
    
    if(response["status"] == "ok"):
        return(response["articles"])
    else:
        return(response["status"])
    
def getSources(apiKey,language="",country=""):
    thisURL = "https://newsapi.org/v2/sources?apiKey="+apiKey
    if(language != ""): #if a language have been specified
        thisURL += "&language="+language
    if(country != ""): #if a country have been specified
        thisURL += "&country="+country
    response = requests.get(thisURL)
    response = response.json()
    if(response["status"] == "ok"):
        return(response) 
      
###############################################################################
#                                                                             #
#                                  DEBUG                                      #
#                                                                             #
###############################################################################
""" 
FOR DEBUG PURPOSES
"""
        
if(__name__ == "__main__"):
    apiKey = "2809dbe4cfe044708cacd93879af483e"
    print("Hello debugger")
