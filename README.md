# link_extractor
A Python program which will, given any number of HTTP URLs as command line parameters, connect to each URL, extract all links from it, and
depending on the “-o” option, output either:
● one absolute URL per line
$ ./myprogram -u “https://news.ycombinator.com/” -o “stdout”
https://news.ycombinator.com/newest
https://news.ycombinator.com/newcomments
https://news.ycombinator.com/ask

● a JSON hash where the key is the base domain, and the array is the relative path
$ ./myprogram -u “https://news.ycombinator.com/” -u
“https://arstechnica.com/” -o ‘json’
{
“https://news.ycombinator.com”: [“/newest”, “/newcomments”, “/ask”,
...],

“https://arstechnica.com”: [“/”, “/civis/”,
“/store/product/subscriptions/”, ...]
