from bs4 import BeautifulSoup
import requests
import json
import re
    
def parsing_paragraph(link):

    response = requests.get(link, verify=False)
    html = response.text

    # Parse the HTML content
    soup = BeautifulSoup(html, "html.parser")

    # Find all sections with an id attribute that contains the letter "S"
    raw_abstract = soup.find_all("div", "ltx_abstract")
    abstract = ''.join(raw_abstract[0].text.split("\n")[2:])

    sections = soup.find_all("section", attrs={"id": re.compile(r"^S\d+$")})
    subsections = soup.find_all(class_= 'ltx_para', id=re.compile(r"^S\d+\.+(p|S)"))

    # Count the number of sections
    count = len(subsections)

    paragraphs = []
    section_names = []
    for i in range(count):
        paragraphs.append(re.sub(r"\n", "", subsections[i].text))
    return paragraphs

if __name__=='__main__':

    arxiv_ids = ['1506.06579'] # https://arxiv.org/abs/1805.11815
    ar5iv_links = []
    for arxiv_id in arxiv_ids:
        ar5iv_links.append(f"https://ar5iv.labs.arxiv.org/html/{arxiv_id}")
    paragraphs = parsing_paragraph(ar5iv_links[0])
