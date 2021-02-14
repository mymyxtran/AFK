from storeScraper import StoreScraper
import sys

if __name__ == "__main__":
    print(sys.argv[1])
    # print("Hi")
    scraper = StoreScraper(int(sys.argv[1]))
    # scraper.test_tryHMScraper()
    scraper.test_aritziaScraper()