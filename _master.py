import pandas as pd


# Define required columns
sch_cols = ['學校名稱', '公/私立']
grad_cols = ['學校名稱', '上學年畢業生總計', '體系別']

out_path = 'data/graduates.csv'


# Collect data of each school year
for i in range(106, 112):
    sch = pd.read_csv(f'ori_files/{i}_schools.csv')
    grad = pd.read_csv(f'ori_files/{i}_graduates.csv')

    # Data for schools
    sch = sch[sch_cols]

    # Data for master's degree graduates
    ms = grad[(grad['日間_進修別']=='D 日') & (grad['等級別']=='M 碩士') & (grad['學校名稱']!='臺北市立大學')].copy()
    # Format Handling: replace invalid symbols with 0
    ms['上學年畢業生男'] = ms['上學年畢業生男'].replace(' -', 0).astype(int)
    ms['上學年畢業生女'] = ms['上學年畢業生女'].replace(' -', 0).astype(int)
    # Compute the total number of graduates
    ms['上學年畢業生總計'] = ms['上學年畢業生男'] + ms['上學年畢業生女']
    ms = ms[grad_cols]

    data = pd.merge(ms, sch, on='學校名稱') 
    # Group data by its school name
    data = data.groupby('學校名稱', as_index=False).agg({
    '上學年畢業生總計': 'sum',    
    '體系別': 'first',
    '公/私立': 'first'
    })
    # Exception Handling: school name change 
    data['學校名稱'] = data['學校名稱'].replace({
        '大華科技大學':'敏實科技大學', '亞東技術學院':'亞東科技大學',
        '經國管理暨健康學院':'德育護理健康學院', '高苑科技大學':'台鋼科技大學'
        })

    # Translate attributes to English
    data['體系別'] = data['體系別'].replace({'1 一般':'General', '2 技職':'Tech', '3 師範':'General'})
    data['公/私立'] = data['公/私立'].replace({'公立':'Public', '私立':'Private'})
    data = data.rename(columns={'學校名稱': 'School', '上學年畢業生總計': 'gradTotal', '體系別': 'Type', '公/私立': 'Ownership'})
    # Add information of school year
    data.insert(0, 'Year', i)

    if i == 106:
        data.to_csv(out_path, mode='w', index=False, header=True, encoding='utf-8-sig')
    else:
        data.to_csv(out_path, mode='a', index=False, header=False, encoding='utf-8-sig')