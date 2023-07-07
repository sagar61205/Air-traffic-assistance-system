# Air traffic assistance system
A simple ML based website which calculates calculates calories burnt by weighing in various parameters such as DryBulb temperature, Wind speed, Relative humidity etc.

## Application interface screenshot:
![Screenshot 2021-07-05 201522](https://user-images.githubusercontent.com/5305547/127722993-50f5e6e6-27fc-40c4-adab-cfdd6c43d8ea.png)


## Application screenshot showing what the application does:
![Screenshot 2021-07-05 201606](https://user-images.githubusercontent.com/5305547/127722982-f7c61fb3-449c-493d-af19-bc2e2443f6ee.png)


# Features:
1.	VISIBILITY - Distance from which an object can be seen.
2.	DRYBULBTEMPF-Dry bulb temperature (degrees Fahrenheit). Most commonly reported standard temperature.
3.	WETBULBTEMPF-Wet bulb temperature (degrees Fahrenheit).
4.	DewPointTempF-Dew point temperature (degrees Fahrenheit).
5.	RelativeHumidity-Relative humidity (percent).
6.	WindSpeed-Wind speed (miles per hour).
7.	WindDirection-Wind direction from true north using compass directions.
8.	StationPressure-Atmospheric pressure (inches of Mercury; or ‘in Hg’).
9.	SeaLevelPressure- Sea level pressure (in Hg).
10.	Precip	Total-precipitation in the past hour (in inches).


This is a POC(Proof of concept) kind-of project. The data used here comes up with no guarantee from the creator. So, don't use it for making air traffic visibility decsions. If you do so, the creator is not responsible for anything. However, this project presents the idea that how we can use ML into practice.

## MOTIVATION 💪
Air industry is extremely prone to accident and there are various factors responsible such as limited and complicated airspace, visibity etc. This project was created keeping that in mind. This is an application which should just be used by air traffic controllers in any way but a way show the working of an end to end ML project for the domain.

In this project, I present a website in which the predictions are implemented as; Batch File PRediction(which predicts and generates a new file with predicted values based in the pre-trained model. 
For the visibility predicting application, the user can input the data and the application will predict the number of visibility for air traffic.


## Built with 🛠️
<p align="left"> <a href="https://www.arduino.cc/" target="_blank"> <img src="https://cdn.worldvectorlogo.com/logos/arduino-1.svg" alt="arduino" width="40" height="40"/> </a> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a><a href="https://flask.palletsprojects.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://heroku.com" target="_blank"> <img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a><a href="https://postman.com" target="_blank"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a><a href="https://scikit-learn.org/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a></p>       


## DEPLOYMENT 🚀
Deployment is done using deploy branch.<br/>
This website is deployed at GCP.<br/>
Github page: https://sagar61205.github.io/Air-traffic-assistance-system/ <br/>
How to use? <br/>
Value-based-prediction ==> enter the corresponding values and it will fetch the number of calories burnt.<br/>
File-based-prediction  ==> Click in 'default file prediction' to see the prediction on the already trained model OR Enter an absolute file path and clixk on 'Custom file predict'.


## Application screenshot for the 'About' section.
![Screenshot 2021-07-05 201622](https://user-images.githubusercontent.com/5305547/127049630-d1d65428-91e1-40d0-b8c9-f997624f185d.png)

## Application screenshot showing impact on visibility on flights:
![Screenshot 2021-07-05 201641](https://user-images.githubusercontent.com/5305547/127050719-732f1ddf-7045-4938-905c-26fba2520ac5.png)

## Application screenshot for batch file prediction. Here deafult prediction takes place on pre-trained dataset. A custom file file prediction can also be done.
![Screenshot 2021-07-05 201703](https://user-images.githubusercontent.com/5305547/127050754-fdf707d8-01f6-4887-9b82-ba0ac6dc50c1.png)

## Application screenshot for the important information section:
![Screenshot 2021-07-05 201742](https://user-images.githubusercontent.com/5305547/127051142-7a95cdd6-2b2e-47b1-b3ea-948661a50812.png)

## Prediction:
![visibility gif](https://user-images.githubusercontent.com/5305547/127061169-753f97bc-a449-46d8-8f1f-4a6dd602d996.gif)


