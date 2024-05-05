""" This is the Template which I use to create my folders automatically """

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

""" The project_name is actually the folder which I wrote as 'src' previosuly """
project_name = "mlProject"


list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuaration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        """
        Creating Directory
        """
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory \"{filedir}\" for the file \"{filename}\"")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        """
        Creating File
        It is checking if the file already exists or if exists then the size of the file must be 0,
        then I will replace the file otherwise not
        """
        with open(filepath, "w") as f:
            logging.info(f"Creating Empty File : \"{filepath}\"")
            pass
    
    else:
        logging.info(f"{filename} is already exists")






"""
---------------------------- Informations on used Packages and CodeLines -------------------------------

* Here we are using logging.basicConfig() to fix my logging mesage format.
* Here we are using 'Path()' to resolve the issues of forward backward '/' cause for diff OS it is diff 
and also for github it might throw error,,,so the 'Path()' package from 'pathlib' will handle that.
* os.path.split() will give me 2 output ,, one is foldername and another filename. Here we have diff files
inside folders which we want to create(Just like using this "config/config.yaml" we are creating 'config' 
folder and 'config.yaml' file inside that,,,that's why we are using this.
"""

"""
------------------------------------- Informations on List of files -------------------------------------

.github/workflow/.gitkeep -> .github is actually needed at the time of deployment,, and i created .gitkeep 
                              so that it reflects in github at the time of commit, as it won't commit empty 
                              folders.
f"src/{project_name}/__init__.py" -> This will create a folder named "src/ChickenDisease" this is same as 
                                     src,, and i added __init__.py as this folder will work as a local
                                     package.
"research/trials.ipynb" -> This is needed because before implementing the actual components I will perform
                           some experiment on notebook.
"templates/index.html" -> For using Flask
"""