youtube-videos-stream.py is used to identity the YouTube Live Stream videos.

How to use it:
Based on my another Python script https://github.com/banhao/scrape-youtube-channel-videos-url, you will get the Youtube video links such as "CBCtv-202001011120.list"
	
	python3 youtube-videos-stream.py CBCtv-202001011120.list
	
Example result CBCtv-videos-stream.list was uploaded.

This can be run in Windows or Linux. but don't use the 'root' to run the script in Linux, because seems in Linux you can't use 'root' account to open a browser.

Please install the "selenium" first.
	
	https://pypi.org/project/selenium/

And you also need to download the browser drivers
	
	https://selenium-python.readthedocs.io/installation.html#drivers

Test results:

	OS			|	Window10	|	Linux
	Python3 + FireFox	|	passed		|	passed
	Python3 + Chrome	|	passed		|	haven't installed the chrome 
------------------------------------------------------------------------

I didn't tested in IE and Edge, because I rarely use that 2 browers.

Notice: The script will read the Links from the URL List and use the browser to load the page, so that's why need to sleep 10 seconds. But this time depend on your network and computer performance. If you adjest it to a small number and no enough for the browser to load the page the script will get error.  

