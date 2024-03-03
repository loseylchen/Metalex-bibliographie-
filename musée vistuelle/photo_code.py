import matplotlib.pyplot as plt

# 提取数据的部分
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
        # 解析书籍详细信息
        details_parts = details.split(',')
        if len(details_parts) >= 3:  # 确保列表足够长以避免 IndexError
            authors = details_parts[0].split('and') if 'and' in details_parts[0] else details_parts[0]
            title = details_parts[1].strip()
            publisher_and_pages = details_parts[2].split('p.')
            publisher = publisher_and_pages[0].strip()
            pages = publisher_and_pages[1].strip() if len(publisher_and_pages) > 1 else ''
            books.append({
                'Year': year,
                'Authors': authors,
                'Title': title,
                'Publisher': publisher,
                'Pages': pages
            })
        else:
            print("Details parts not enough:", details_parts)  # 打印问题数据以进行调试

# 生成图形的部分
# 统计每个出版年份的书籍数量
year_counts = {}
for book in books:
    year = book['Year']
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1

# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(year_counts.keys(), year_counts.values(), color='skyblue')
plt.xlabel('Year')
plt.ylabel('Number of Books')
plt.title('Number of Books Published Each Year')
plt.xticks(rotation=45)
plt.tight_layout()

# 保存图形为文件
plt.savefig('/Users/lianchen/Documents/musée vistuelle/books_published_each_year.png')

# 显示图形
plt.show()
