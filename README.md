A simple and bugged script to extract bibliograhic metadata from Wikisource books, and put them in a csv. 

The script is slow and it crash frequently, but it's my fault because I can't really use the try/except intructions.
This is my very first coding attempt, so please come here and make it better :-)

Details
====
I'm using [wikipedia.py](https://github.com/goldsmith/Wikipedia/blob/master/wikipedia/wikipedia.py), a nice Python wrapper for MediaWiki API. I modified it because, by default, it just allows you to use Wikipedia API (and not Wikisource). The MediaWiki API gives you a much cleaner HTML than a traditional get request. 

Wikisource also has a nice OAI-MPH feed, but it just takes the books that have an Index page: there are no structured data for old "main namespace" texts. 

Using the xx.source dump is another way to get the job done. But this way you can feed the script a simple list of books, so you can handpick them beforehand (which is nice, you maybe don't want everything). 

 
