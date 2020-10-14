
<h1 style="text-align:center">CoronaVirus Cases Monitoring & Alerting Tool
</h1>



This is a simple monitering & alerting tool for those of you who are worried (Paranoid xD ) about the covid-19 propagation in a certain country. 




## Prerequisites
You need to install and config [Selenium WebDriver](https://www.selenium.dev/downloads/)

- Installing Selenium with pip 
    
```console
    $ pip install  -U selenium
```
- Selenium requires also a driver to interface with the chosen browser. Firefox, for example, requires geckodriver.
Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Choose the corresponding package depending on you system from [here](https://github.com/mozilla/geckodriver/releases), For linux64  you can run this : 
    
```console
$ cd /usr/bin
$ wget https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz
$ tar -xf geckodriver-v0.27.0-linux64.tar.gz
```



## Setup 
You  will need to set up in ```config.py```: 

	- A gmail address in order to be able to send situation update notification emails.
	- List of countries you want to moniter  
	- List of emails users or subscribers  to send update notifications too 
	- Cloud service or a laptop laying arround to run the app on. 

## Concept

The idea is to scrape data from this [CoronaVirus](https://www.worldometers.info/coronavirus/)  website save it in a Log file periodicaly. 
And at each update intervall , check if the scrapped data for the alert_countires correspond to the data our logs, if not update the logs and send notification emails for the subscribers. 


## Desclaimer 

This tool is based on the data from the [CoronaVirus website ](https://www.worldometers.info/coronavirus/) and it may be outdated. 
The tool may not function proporly if the website changed it's structure because the scraping depend on the content of the webpage.