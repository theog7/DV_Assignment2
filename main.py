import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/theog7/DV_Assignment2/main/mydvdata.csv')

data['ActualCost'] = data['RawMaterial'] + data['Workmanship'] + data['StorageCost']

data['SoldPrice'] = data['EstimatedCost'] * 1.1

data['MarginOfProfit'] = data['SoldPrice'] - data['ActualCost']

data = data[['date', 'EstimatedCost', 'RawMaterial', 'Workmanship', 'StorageCost', 'ActualCost', 'SoldPrice', 'MarginOfProfit']]

data.to_html('mydvdata.html', index=False)

with open('sty.css', 'r') as css_file:
    css_content = css_file.read()

html_code_template = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Supply Chain</title>
    <style>
    {css_content}
    </style>
</head>
<body>
    {data.to_html(index=False)}
</body>
</html>
'''

with open('mydvdata.html', 'w') as file:
    file.write(html_code_template)

