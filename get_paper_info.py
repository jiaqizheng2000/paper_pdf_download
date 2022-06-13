import arxiv

def get_authors(authors, first_author=False):
    output = str()
    if first_author == False:
        output = ", ".join(str(author) for author in authors)
    else:
        output = authors[0]
    return output


def sort_papers(papers):
    output = dict()
    keys = list(papers.keys())
    keys.sort(reverse=True)
    for key in keys:
        output[key] = papers[key]
    return output


def get_daily_papers(query=" ", max_results=20):
    """
    @param query: str
    @return paper_with_code: dict
    """

    # output
    content = dict()

    search_engine = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    for result in search_engine.results():

        paper_id = result.get_short_id()
        paper_title = result.title
        paper_url = result.entry_id
        paper_url_pdf=paper_url.replace('abs','pdf')
        paper_url_link.append(paper_url_pdf)
        paper_title_new=paper_title.replace(':',' ')
        paper_name.append(paper_title_new)

        paper_abstract = result.summary.replace("\n", " ")
        paper_authors = get_authors(result.authors)
        paper_first_author = get_authors(result.authors, first_author=True)
        primary_category = result.primary_category

        publish_time = result.published.date()

        print("Time = ", publish_time,
              " title = ", paper_title,
              " author = ", paper_first_author)

if __name__ == "__main__":
    paper_url_link=[]
    paper_name=[]
    data_collector = []
    keywords = dict()
    keywords["contact angle"] = "\"contact angle\""

    for topic, keyword in keywords.items():
        print("Keyword: " + topic)
        get_daily_papers(query=keyword, max_results=1000)
        print("\n")

    paper_url_file=open('contact angle/paper_url_link.txt', 'w')
    for i in range(len(paper_url_link)):
        paper_url_file.write(paper_url_link[i]+'\n')

    paper_url_file=open('contact angle/paper_name.txt', 'w')
    for i in range(len(paper_name)):
        paper_url_file.write(paper_name[i]+'\n')