from bs4 import BeautifulSoup


# 파일 경로 설정
input_file_path = "C:\\Users\\bhlee\\Desktop\\temp\\web_app_server_gov.html"
output_file_path = "C:\\Users\\bhlee\\Desktop\\temp\\web_app_server_gov_no_a_tags.html"

# HTML 파일 읽기
with open(input_file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# 모든 <a> 태그 제거
for a_tag in soup.find_all('a'):
    a_tag.decompose()

# 수정된 HTML 파일 저장
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(str(soup))

print(f"Modified file saved to {output_file_path}")
