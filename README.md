# Python - Android SDK tools

![beeware 1](https://github.com/Btwo2/PythonToAndroidSDK/assets/110456965/25c7b7b0-df19-4acf-967b-d5ded2c08167)

# BeeWare:

BeeWare is an open-source project for creating native apps in Python. It is a collection of tools and libraries that enable you to build native user interfaces for iOS, Android, macOS, Linux, and Windows.

Step 1: Install BeeWare
Install the BeeWare toolchain from the command line:

	pip install beeware
	
	or
  
  	https://docs.beeware.org/en/latest/tutorial/tutorial-0.html

Step 2: Create your app
You can create a new BeeWare project using the following command:

	briefcase new

Step 3: Write your Python code
Modify the app.py file in your project directory with your Python code, using Toga components as the UI library.

Step 4: Build the Android App
From the command line, run:

	briefcase create android
	briefcase build android

Step 5: Run your app on an Android device
Connect your physical Android device and run:

	briefcase run android

![256 1](https://github.com/Btwo2/PythonToAndroidSDK/assets/110456965/db74d303-b96d-4958-96fc-c95154a9fdf7)


# Buildozer & Kivy

Buildozer is a tool for creating application packages easily.

By describing your application requirements and settings such as title, icon, included modules etc into a .spec file, buildozer will use iy to create a package for Android, iOS, Windows, OSX and/or Linux.

Kivy is an open-source Python library for rapid development of applications that make use of innovative user interfaces, such as multi-touch apps. Kivy runs on Linux, Windows, OS X, Android, and iOS.

Step 1: Install Kivy and its dependencies
  
	pip install kivy

 	or

  	https://kivy.org/doc/stable/gettingstarted/installation.html

Step 2: Create your app
Write your Python code using Kivy UI components.

Step 3: Buildozer colab tool
Upload your code to the notebook and follow the thread until command "!yes | buildozer init"

	https://colab.research.google.com/drive/15dtg3rzMdwGNm8NL0AxkGQ5thKB6HoJH#scrollTo=dotCHcJtHOnF

Step 4: Customize the Buildozer spec file
Edit the generated buildozer.spec file to configure the app (like app name, package name, etc.). That's really important for android packaging
All the librarys must be included

	# Some tips
 	
	# (list) Source files to include (let empty to include all the files)
	source.include_exts = py,png,jpg,kv,atlas,mp3,ogg,wav 			 # this are the extensions you could call for the packaging like icon image in png, jpg
	Here we include the file types we’ll need to use in the app
	----------------------------------------------------------------------------------------------------------------------------
	# (list) Application requirements
	# comma separated e.g. requirements = sqlite3,kivy3
	requirements = python3, kivy==2.1.0, kivymd==1.0.2, pillow		# this are the libraries required for the code to run properly
				# Example: 
    				# Libraries used by kivy 
				# Unfortunately, these are the only combination of kivy and kivymd versions that could find work
	----------------------------------------------------------------------------------------------------------------------------
	# (str) Title of your application
	title = App Title							# this will be the text displayed on the app icon
	----------------------------------------------------------------------------------------------------------------------------
	# (str) Package name
	package.name = Package Title						# this will be the name of the package
	----------------------------------------------------------------------------------------------------------------------------
	# (str) Presplash of the application
	presplash.filename = arquive.png					# this will be the image displayed while app loads
	*must include the image file extension on source.include_exts
	----------------------------------------------------------------------------------------------------------------------------
	# (str) Icon of the application
	icon.filename = arquive.png						# this will be the image displayed on the app icon
	----------------------------------------------------------------------------------------------------------------------------

Step 6: Build APK
Run the following command to build the APK:

	!yes | buildozer -v android debug

Obs: Both tools are a little complicated for beginners, so don't worry if something goes wrong. Try searching a little, send me a message if you want but don't give up

#Comparison:
Both tools presents a great way to convert .py application to .apk

    Easy-To-Use: Beeware (by far)
    Available Resources: KivyMD + Buildozer
    Running Time: Beeware (by far)
