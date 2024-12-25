# Statistics Final Project
### 113 Autumn - Statistics, 曾意儒, NYCU   
Data Source: [教育部統計處-學校基本統計資訊](https://depart.moe.edu.tw/ed4500/News.aspxn=5A930C32CC6C3818&sms=91B3AAE8C6388B96)

## Contents
- data/ : processed data for statistical analysis
- ori_files/ : original data of school information, graduate student statistics, and all student statistics
- others/ : additional data containing significant school changes
- plots/ : despriptive analysis, containing line plots and box plots for each category
- Descriptive.ipynb :  
- _cs.py : code used to prepare the cs_students.csv file
- _master.py : code used to prepare the graduates.csv file
- statistical_test.ipynb :
  
## Data Description  
#### 1. cs_students.csv

| Column     | Type      | Value          | Description                                    |
|------------|-----------|----------------|------------------------------------------------|
| Year       | int       | 103~112        | Academic year                                    |
| School     | str       |       -        | School name                                    |
| Total      | int       |       -        | Total number of CS bachelor's degree students  |
| Male       | int       |       -        | Number of male CS bachelor's students          |
| Female     | int       |       -        | Number of female CS bachelor's students        |
| Type       | category  | General/Tech   | School category                                |
| Ownership  | category  | Public/Private | School Ownership                               |
 
#### 2. graduates.csv

| Column     | Type      | Value          | Description                                    |
|------------|-----------|----------------|------------------------------------------------|
| Year       | int       | 103~112        | Academic year                                    |
| School     | str       |       -        | School name                                    |
| gradTotal  | int       |       -        | Total number of master's degree graduates      |
| Type       | category  | General/Tech   | School category                                |
| Ownership  | category  | Public/Private | School Ownership                               |
