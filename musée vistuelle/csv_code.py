import csv
from bs4 import BeautifulSoup

# 读取HTML文件
with open('/Users/lianchen/Documents/musée vistuelle/books.html', 'r', encoding='utf-8') as file:
    html_data = file.read()

# 解析HTML
soup = BeautifulSoup(html_data, 'html.parser')

# 提取数据
books = []
for row in soup.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) == 2:
        year = cols[0].text.strip()
        details = cols[1].text.strip()
        # 检查详细信息是否包含逗号，以确定它是否是一条有效的书籍记录
        if ',' in details:
            details_parts = details.split(',')
            authors = details_parts[0].split('and') if 'and' in details_parts[0] else details_parts[0]
            title = details_parts[1].strip()
            publisher_and_pages = details_parts[2].split('p.') if len(details_parts) > 2 else ['','']
            publisher = publisher_and_pages[0].strip()
            pages = publisher_and_pages[1].strip() if len(publisher_and_pages) > 1 else ''

            books.append({
                'Year': year,
                'Authors': authors,
                'Title': title,
                'Publisher': publisher,
                'Pages': pages
            })

# 将提取的数据保存到CSV文件中
output_file_path = '/Users/lianchen/Documents/musée vistuelle/books_output.csv'
with open(output_file_path, 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=['Year', 'Authors', 'Title', 'Publisher', 'Pages'])
    writer.writeheader()
    for book in books:
        writer.writerow(book)

print("Output saved to:", output_file_path)
