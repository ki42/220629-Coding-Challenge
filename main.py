import requests
import csv
from bs4 import BeautifulSoup

#Grab Page and Soup it
main_page = requests.get('https://en.wikipedia.org/wiki/List_of_programming_languages')
main_page_soup = BeautifulSoup(main_page.text, 'html.parser')

#Global Varible
link_and_html = []

#Open CSV
f = csv.writer(open('programming_languages.csv', 'w'))
f.writerow(['Name of Language', 'Paradigm', 'First Appeared', 'File Extensions', 'Header Sections', 'Link Count'])

#Get language list with link and HTML
language_list_raw = main_page_soup.find(class_='div_col')
language_list_items = language_list_raw.find_all('a')

for language in language_list_items:
    link = language['href']
    each_language_page = requests.get(link)
    #list or output file, only list currently
    link_and_html = [link, each_language_page]

#Loop each page    
for language_html in link_and_html:
    paradigm = ''
    first_appeared = ''
    extensions = ''
    label_list = [] 
    
#Get name
    link = language_html[0]
    getting_name_temp_1 = link.lstrip('https://en.wikipedia.org/wiki/')
    sub_list = ["Programming", "programming", "Language", "language", “(“, “)”)
    for sub in sub_list:
        getting_name_temp_2 = getting_name_temp_1.replace(sub, '')
    getting_name_temp_3 = getting_name_temp_2.replace(“_”, ' ')
    name = getting_name_temp_3.rstrip(“_”)
   
#Get rid of subscripts
    languange_page_soup = BeautifulSoup(language_html[1].text, 'html.parser')
    sup_tags = language_page_soup.find(class_='reference')
    sup_tags.decompose()
      
#Grab infobox and paradigm, appeared date, and extensions              
    infobox = language_page_soup.find(class_='infobox vevent')
    infobox.labels = infobox.find_all(class_='infobox-label')
    for labels in infobox_labels:
         label_list = [labels.contents[0]]
    must_have_tags = ['Paradigm', 'First&nbsp;appeared', 'Filename extension'] 
    check = all(item in label_list for item in must_have_tags) 
    if check is True:    
        rows = infobox.findChildren(['th', 'td'])
        for row in rows
            if row['th'].contents is 'Paradigm'
              paradigm = f'"{row['td'].string}"'
            if row['th'].contents is 'First&nbsp;appeared'
              first_appeared = f'"{row['td'].string}"'
            if row['th'].contents is 'Filename extension'
              extensions = f'"{row['td'].string}"'
                
# Get counts
    languange_page_soup_with_subscripts = BeautifulSoup(language_html[1].text, 'html.parser')
    heading_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
    heading_tags_count = num_apperances_of_tag(heading_tags, languange_page_soup_with_subscripts)
                
    body_of_article = language_page_soup_with_subscripts.find("div", {"id": "content"})
    link_count = len(body_of_article.find_all('a', href=True))
                
# Write to CSV
    f.writerow([name, paradigm , first_appeared, extensions, heading_tags_count,  link_count])
f.close()
