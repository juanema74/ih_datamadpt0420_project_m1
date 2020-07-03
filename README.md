# IronHack Data Analytics Bootcamp: Proyect 1 - Making a Data Pipeline

The following Pipeline shows the quantity and percentage of workers per country, job type and living area (making difference between rural and urban areas).

![Image](https://res.cloudinary.com/springboard-images/image/upload/q_auto,f_auto,fl_lossy/wordpress/2019/05/aiexcerpt.png)

---


### 💻**Technology stack**
Python, Pandas, requests, BeautifulSoup, argparse, sqlalchemy, Pycharm and Jupyter.

### **Core technical concepts and inspiration**
- Reporting tool to analyze selected results and make better and faster decisions.
- The main_script.py will generate a .csv file updated every time the script runs.

### 🔧**Configuration**
- The data base used for this proyect is located here : /data/raw/raw_data_project_m1.db.
- Enviroment ironhack_env should be activated to run the script.

### **Pipeline usage and posible outputs**
- Case 1:
If you want to have a .csv file with all countries yo just need to put -c country and all dataset will be saved in that file. 
- Here is an example:
python main_script.py -p /Users/juandediegosuanzes/Desktop/ih_datamadpt0420_project_m1/data/raw/raw_data_project_m1.db -u https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes -c country


- Case 2:
In case you want the info of a specific country,  running the script using -c ‘name of the country selected’ will be needed to have that information. 
- Here is an example: python main_script.py -p /Users/juandediegosuanzes/Desktop/ih_datamadpt0420_project_m1/data/raw/raw_data_project_m1.db -u https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes -c Spain


The script will export a .csv per each stage of the project which will be in data/raw folder
### 📁 **Folder structure**
```
└── project
    ├── __trash__
    ├── data
        ├── raw
            ├── .csv files
        ├── processed
        └── results
    ├── notebooks
        ├── Data_v1.ipynb
        ├── data_cleaning.ipynb
    ├── p_acquisition
        ├── m_acquistion.py
    ├── p_analysis
        ├── m_analysis.py
    ├── p_reporting
        ├── m_reporting.py
    ├── p_wrangling
        ├── m_wrangling.py
    ├── .env.txt
    ├── .gitignore
    ├── main_script.py
    ├── README.MD
    ├── requeriments.txt

```

### **Further info**
- Web scraping Source: https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes
- Thanks for attending my proyect!
