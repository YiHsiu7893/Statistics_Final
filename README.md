# Statistics Final Project
### 113 Autumn - Statistics, 曾意儒, NYCU  
Hi :)  

## Contents
- data/ : processed data for statistical analysis
- ori_files/ : original data of school information, graduate student statistics, and all student statistics
- others/ : additional data containing significant school changes
- _cs.py : code used to prepare the cs_students.csv file
- _master.py : code used to prepare the graduates.csv file
  
## Data Description  
#### 1. cs_students.csv

| Column     | Type      | Value          | Description                                    |
|------------|-----------|----------------|------------------------------------------------|
| Year       | int       | 107~112        | School year                                    |
| School     | str       |       -        | School name                                    |
| Total      | int       |       -        | Total number of CS bachelor's degree students  |
| Male       | int       |       -        | Number of male CS bachelor's students          |
| Female     | int       |       -        | Number of female CS bachelor's students        |
| Type       | category  | General/Tech   | School category                                |
| Ownership  | category  | Public/Private | School Ownership                               |
 
#### 2. graduates.csv

| Column     | Type      | Value          | Description                                    |
|------------|-----------|----------------|------------------------------------------------|
| Year       | int       | 106~111        | School year                                    |
| School     | str       |       -        | School name                                    |
| gradTotal  | int       |       -        | Total number of master's degree graduates      |
| Type       | category  | General/Tech   | School category                                |
| Ownership  | category  | Public/Private | School Ownership                               |