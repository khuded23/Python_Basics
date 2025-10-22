Python Virtual Environment in Mac/linux

Make a directory:

	
		mkdir some_project


Install Python Venv:


		python3 -m venv some_project_venv (name of your venv) 


Activate the venv:


		source some_project_venv/bin/activate

		

<img width="1404" height="254" alt="image" src="https://github.com/user-attachments/assets/b86d1b3e-c68e-44d8-b99c-580851b36637" />



Installing modules :

		
		pip install <module name>
		
Once you have all your modules installed , if you want the same modules installed in another environment, instead of installing each module again, we can collect the names of the installed modules in this venv and use a requirement.txt file in other environment.


Use pip freeze command to show all the installed modules and it version:



Now save these output in a requirement.txt 

```
beautifulsoup4==4.9.3
bs4==0.0.1
certifi==2021.5.30
charset-normalizer==2.0.3
idna==3.2
requests==2.26.0
soupsieve==2.2.1
urllib3==1.26.6
```


Next time when creating a new VirtualEnv , use the reqiurement.txt to install all modules
```

pip3 -r requirements.txt
```
