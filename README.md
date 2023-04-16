# URLshortener-
In this  project  i hav e implemented the python code for url shortener  
In this program, we define a URLShortener class that can be used to generate short, random URLs for long URLs.

The shorten_url() method generates a random 6-character string using Python's random.choices() function and adds it to a dictionary of URLs,
along with the original long URL.

The expand_url() method takes a short URL as an argument and looks it up in the dictionary of URLs. If the short URL is found in the dictionary,
the method returns the corresponding long URL.

To use the URLShortener class, we first create an instance of the class using shortener = URLShortener().
We can then call the shorten_url() method with a long URL to generate a short URL.
Finally, we can call the expand_url() method with a short URL to get the corresponding long URL.

Note that this implementation of a URL shortener is not suitable for production use, as it stores all URLs in memory and does not persist them to disk or a database.
A real URL shortener would need to be implemented using a more robust storage mechanism.
