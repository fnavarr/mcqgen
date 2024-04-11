CREATE AND PYTHON VIRTUAL ENVIRONMENT AND PROJECT STRUCTURE

1.	First step is to create the folder project using Power Sell or Git Bass command windows:  mkdir folder
2.	Go to the created folder:  cd folder 
3.	Invoke VS Code:   code .
4.	In VS Code open the terminal, recommended use Git Bash as terminal.
5.	Go to menu: View -> Command Palette -> Python Select Environment ->
6.	Select the Python version you want to use for your project. Recommended to use stable versions.
7.	Initialize git in order to create the master branch: git init 
8.	Create the README.md file into the project folder. We can use the right mouse button over the file and select Reveal in File Exporer (Shift+Alter+R) in order to open file explorer and verify)
9.	 Create your first commit using Source Control icon, provide a comment. After committing you can publish your branch. First time you will be asked to sign oin in your git hub environment, you can select to create a public or private repository.
10.	Create your conda virtual environment with: conda create -p env python=3.8 -y
11.	To activate this environment:  conda activate “path”  # Path is your path project folder.
12.	There is another way to do it: source activate ./env  # this way your current poath is implicit.
13.	Create the .gitignore file and mention inside all folders and files that will be  ignored by git
14.	Create the requirements inside the requirement.txt file. Typical components are:
openai
langchain
streamlit
python-dotenv
PyPDF2

-e .

15.	Install the requirements: pip install -r requirements.txt

16.	Create the setup.py  in order to create our local package.
17.	Create the src folder and inside __init__.py   # this handle the folder as local package
18.	Create the project folder i.e. mcqgenerator and inide __init__.py
19.	Inside your folder project you can create the rest of python files, like mcqgenerator.py, utils.py, etc.
If we need to create an jupyter lab environment we can create the experiment folder and inside the experiment.ipynb file and also select the kernel environment (python version to use)
20.	Create the .env file in order to set the environment variables like the OPEN_API_KEY = "….."
21.	Once you finished your app it is possible to testing with: streamlit run app.py (if you used stramlit)

DEPLOYMENT OF TE APPLICATION
this example will be performed using AWS.
1.	First you need an account so register in AWS, recommended the free option. 
2.	Login with your new account https://aws.amazon.com/console 
Create your instance.
3.	Select EC2 in order to create a new instance.
4.	Select LAUNCH INSTANCE
5.	Select the environment to use, in this case we will use UBUNTU
6.	About machine the recommended is t2.large
7.	Create the Key, select new key in Key pair (login) 
8.	Select the default values and give a name. After press create, you will receive a file with the key (will be downloaded usually in download folder) wit extension .pem
9.	Check Allow SSH, Allow HTTPS and Allow HTTP traffic from the internet 
10.	Configure Storage to 16 MB
11.	Click Launch Instance to launch it
12.	 After instance is created click in the name of the instance in order to go to the instances page.
13.	Check when status shows running and click again in the name of the instance.
14.	In the folowing page you will see additional and detailed info about your instance. Click connect in order to access the console
 
After click connect, this page will be displayed, click connect again
 

15.	You will be now in the console of your machine. Now it will be necessary to update the machine software and install all the packages that are used by your app. Execute the following:
sudo apt update
sudo apt-get update
sudo apt upgrade -y
And hit enter if appears any message.


16.	Install git curl unzip tar make sudo vim get to install additional utilities, use:
sudo apt install git curl unzip tar make sudo vim wget python3-pip -y

17.	 Next, we can check components using pip and also invoke python3 in order to verify everything. 
18.	Next, we will clone the project repository from git, i.e.:
       git clone https://github.com/fnavarr/mcqgen.git
19.	In our project we need to translate the openai key which is not allowed to copy directly, so we need to do it manually, create the .env file and copy the key inside. We can use the touch command:
touch .env 
vi .env  (press insert and copy the key, save the file with escape key and the quit editor with :wq)
20.	Install the requiriments.txt using pip
pip install -r requirements.txt
21.	Now we can execute the app with:
       python3 -m streamlit run StreamlitAPP.py
22.	The app will run but we need to configure our web access using the AWS inbound rule of our instance. Go to your instance tab in your browser, then select security tab and then select security groups and click from there:
 
Click the Edit inbound rules, you will presented the Edit inbound screen:

 
From here we will add a new rule and this will appear as custom tcp, ther we will indicate the port for our app. After enter values hit save.

END OF PROCEDURE
The app should run using the public ip and the port.
