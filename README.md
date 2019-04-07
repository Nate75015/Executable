Ce tutoriel à pour but de vous expliquez comment réaliser un executable avec Cx_Freeze. Ici l'executable que j'essaie de mettre en place est le fichier 2016_Extraction_Name.py. Le fichier Setup.py est le ficher de consolidation.

OS : Windows

Plateforme Execution : Anaconda 3

Python : 3.5.0

Commencer par créer un environement virtuel sur Anaconda : 

    >conda create -n Executable python=3.5.0 anaconda
    
Activer cet environement :

    >conda activate Excutable
    
Installer Cx_Freeze 5.1.1 :

    >pip install Cx_Freeze=5.1.1
    
Peut-être aurez vous besoin d'installer Visual Studio pour compiler (outil C/C++) Cx_Freeze. 
(Si tel est le cas rendez vous sur : https://docs.microsoft.com/en-us/cpp/build/vscpp-step-0-installation?view=vs-2019)
    
  


