import pandas as pd


# Define required columns
sch_cols = ['學校名稱', '公/私立']
stu_cols = ['學校名稱', '總計', '男生計', '女生計', '體系別']

out_path = 'data/cs_students(10).csv'


# Collect data of each academic year
for i in range(103, 113):
    sch = pd.read_csv(f'ori_files/{i}_schools.csv')
    stu = pd.read_csv(f'ori_files/{i}_students.csv')

    # Data for schools
    sch = sch[sch_cols]

    # Data for CS bachelor's degree students
    cs = stu[
        ((stu['科系名稱']=='資訊工程系') | (stu['科系名稱']=='資訊工程學系')) &
        (stu['日間∕進修別']=='D 日') &
        ((stu['等級別']=='B 學士') | (stu['等級別']=='B 四技'))
    ].copy()
    cs = cs[stu_cols]

    data = pd.merge(cs, sch, on='學校名稱')

    # Exception Handling: school merging 
    data['學校名稱'] = data['學校名稱'].replace({
        '國立新竹教育大學':'國立清華大學',
        '國立高雄第一科技大學':'國立高雄科技大學', '國立高雄應用科技大學':'國立高雄科技大學', '國立高雄海洋科技大學':'國立高雄科技大學',
        '國立交通大學':'國立陽明交通大學', '國立陽明大學':'國立陽明交通大學'})
    data = data.groupby('學校名稱', as_index=False).agg({
    '總計': 'sum', 
    '男生計': 'sum',
    '女生計': 'sum',   
    '體系別': 'first',
    '公/私立': 'first'
    })
    # Exception Handling: school name change 
    data['學校名稱'] = data['學校名稱'].replace({
        '興國管理學院':'中信金融管理學院', '慈濟技術學院':'慈濟科技大學', '致理技術學院':'致理科技大學',
        '桃園創新技術學院':'南亞技術學院',
        '德霖技術學院':'宏國德霖科技大學', '東方設計學院':'東方設計大學', '崇右技術學院':'崇右影藝科技大學', '台北海洋技術學院':'台北海洋科技大學',
        '大華科技大學':'敏實科技大學', '亞東技術學院':'亞東科技大學',
        '經國管理暨健康學院':'德育護理健康學院', '高苑科技大學':'台鋼科技大學'
        })

    # Translate attributes to English
    data['體系別'] = data['體系別'].replace({'1 一般':'General', '2 技職':'Tech', '3 師範':'General'})
    data['公/私立'] = data['公/私立'].replace({'公立':'Public', '私立':'Private'})
    data = data.rename(columns={'學校名稱': 'School', '體系別': 'Type', '總計': 'Total', '男生計': 'Male', '女生計': 'Female', '公/私立': 'Ownership'})
    # Add information of academic year
    data.insert(0, 'Year', i)


    if i == 103:
        data.to_csv(out_path, mode='w', index=False, header=True, encoding='utf-8-sig')
    else:
        data.to_csv(out_path, mode='a', index=False, header=False, encoding='utf-8-sig')
