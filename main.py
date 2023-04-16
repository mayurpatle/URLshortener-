import string
import random

class URLShortener:
    """
    A simple URL shortener class that generates short, random URLs for long URLs.
    """

    def __init__(self):
        self.urls = {}

    def shorten_url(self, url):
        """
        Shorten a long URL to a short, random string.
        """
        # Generate a random 6-character string.
        short_url = "".join(random.choices(string.ascii_letters + string.digits, k=6))

        # Add the short URL to the dictionary of URLs.
        self.urls[short_url] = url

        return short_url

    def expand_url(self, short_url):
        """
        Expand a short URL to its original long URL.
        """
        return self.urls.get(short_url)

# Example usage: shorten a URL and then expand it.
shortener = URLShortener()

# Shorten a URL.
long_url = "https://www.python.org/"
short_url = shortener.shorten_url(long_url)

print(f"Short URL: {short_url}")
print(f"Long URL: {shortener.expand_url(short_url)}")
