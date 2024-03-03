import pandas as pd

# 从 CSV 文件中读取数据
df = pd.read_csv('/Users/lianchen/Documents/musée vistuelle/site/books.csv')

# 添加 HTML 表格
html_table = "<table style='width: 100%;'>"

# 添加表头
html_table += (
    "<tr>"
    "<th style='text-align: left;'>Year</th>"
    "<th style='text-align: left;'>Authors</th>"
    "<th style='text-align: left;'>Title</th>"
    "<th style='text-align: left;'>Publisher</th>"
    "</tr>"
)

# 遍历 DataFrame，为每行添加 HTML 标签
for index, row in df.iterrows():
    html_table += (
        "<tr>"
        f"<td>{row['Year']}</td>"
        f"<td>{row['Authors']}</td>"
        f"<td>{row['Title']}</td>"
        f"<td>{row['Publisher']}</td>"
        "</tr>"
    )

# 结束 HTML 表格
html_table += "</table>"

# 将 HTML 表格写入到文件中
with open('/Users/lianchen/Documents/musée vistuelle/site/output_table.html', 'w') as file:
    file.write(html_table)
