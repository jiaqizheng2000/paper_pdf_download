import requests
import os
import time

link_path = "C:\python_project\paper_download\contact angle\paper_url_link.txt"
name_path = "C:\python_project\paper_download\contact angle\paper_name.txt"
save_path = "C:\python_project\paper_download\papers_contact_angle"

def handle(requests_pdf_url,filename):
    # download pdf
    r = requests.get(requests_pdf_url)
    with open(os.path.join(save_path,filename), 'wb+') as f:
        f.write(r.content)

def get_link_name_from_text():
    link_file = open(link_path)
    name_file = open(name_path)
    paper_url=[]
    paper_name=[]
    for line in link_file.readlines():
        paper_url.append(''.join(line).strip('\n') + '.pdf')
    for line in name_file.readlines():
        name = ''.join(line).strip('\n')+'.pdf'
        paper_name.append(name)

    for i in range(len(paper_name)):
        print('\nfilename:{}, pdf_url:{}.'.format(paper_name[i].strip('.pdf'),paper_url[i]))
        print('Downloading {} ...'.format(paper_name[i]))
        ts = time.time()
        handle(paper_url[i], paper_name[i])
        te = time.time()
        print('{:.0f}s [Complete]'.format(te-ts))

if __name__=='__main__':
    get_link_name_from_text()