Sample Project to Utilize COVID Datasets
https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/

Data Source: Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University

Read More at
https://towardsdatascience.com/5-datasets-about-covid-19-you-can-use-right-now-46307b1406a

1. Download and install Python 3.7.*

2. Download and install Visual Studio Code (Optional)
https://code.visualstudio.com/download

2. Create a Python Virtual Environment 
    ```python -m venv env```

3. Activate Python Environment
    Visual Studio Code:View Command Pallate:
    For VS Code use Command Palette ```Terminal: Create New Integrated Terminal```
        OR
  env\scripts\activate (Windows) OR (Linux/macOS)  source env/bin/activate 
    
4. Setup Environment (If you have not setup before)
pip install -r requirements.txt 

5. To run the code ```python manage.py runserver```. The app should be available at http://127.0.0.1:8000/.

6. To Create/Modify the database use
```python manage.py makemigrations```
```python manage.py migrate```

7. To perform CRUD setup user
``python manage.py createsuperuser --username=<username> --email=<email>``