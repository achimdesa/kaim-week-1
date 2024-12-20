from urllib.parse import urlparse

def analyze_publisher_contributions(data):
    publisher_counts = data['publisher'].value_counts()
    return publisher_counts

def extract_domain(url):
    return urlparse(url).netloc

def analyze_domains(data):
    data['domain'] = data['url'].apply(extract_domain)
    return data['domain'].value_counts()

# Example Usage:
# publisher_contributions = analyze_publisher_contributions(analyst_data)
# domain_contributions = analyze_domains(analyst_data)
