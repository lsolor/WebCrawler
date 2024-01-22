from company_reader import get_companies
from searcher import get_top_websites
from content_analyzer import analyze_content
from reporter import report_results

def main():
    companies = get_companies('companies.txt')
    for company in companies:
        websites = get_top_websites(company)
        process_websites(company, websites)

def process_websites(company, websites):
    brand_image_path = './brand_image.png'
    tags = ['some', 'foo']

    for website in websites:
            match_found, match_details = analyze_content(website, tags, brand_image_path)
            if match_found:
                report_results(company, match_details)
                print('company %s was guilty!', company)
                return

if __name__ == "__main__":
    main()
