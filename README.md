# RunIT-QT-Browser
Python QT5 web browser.

![find](https://user-images.githubusercontent.com/29865797/29841798-8064a46e-8d0f-11e7-8fbb-ed445c454b39.jpg)
#RunIT-QT Browser Copyright (c) 2015 JJ Posti <techtimejourney.net>
#RunIT-QT comes with ABSOLUTELY NO WARRANTY;
#for details see: http://www.gnu.org/copyleft/gpl.html.
#This is free software, and you are welcome to redistribute it under
#GPL Version 2, June 1991
#This is the 0.6 version(Autumn 2017)

This release contains very notable coding changes. The browser is now separated into different modules and code is partially rewritten and commenting is improved. Layout issues have been resolved together with many memory management issues, which were present in the previous releases. The result should be a more robust and a lot more functional browser. The outlook has also received an upgrade via CSS.

_________

Dependencies (Debian base as an example)

sudo apt-get install wget python-pyqt5 ca-certificates python-pyqt5.qtwebkit

The above should be all you need. Depending on your distribution the actual package mix and names might differ. Wget, which is used for downloading, should be there by default in all common distributions. Ca-certificates is used for https page loading and remains important. Python packages supply functionalities and webview for the browser.

Browser will not try load any page upon start. The user gets to choose if page x or y should be loaded. Home icon points to PostX Gnu/Linux start page. Please note that if you supply a page as an argument, to the browser, then you should load the argument page first.

_________

Features:

-Argument support (since 0.6): Start browser like this python /some/path/run.py ‘gooogle.fi’ and follow statusbar instructions.

-Find text from html(since 0.6): Enter find:something to address field and press enter to find the first entry. Press enter again to find the second entry etc.

Right-click menu:Save image functionality(since 0.6). Right-click upon an image and choose Copy Image address. Next choose Save image and the Save as dialog should open.

-Web inspector.

-Open link in a new window.

-Notification support. From 0.6 onwards xfce4-notifyd is no longer needed. Notifications get printed to statusbar.

-Download files (via wget) and bookmark online locations. From 0.6 onwards: Download receives a dialog, which lets you choose destination and file name. Bookmarks are now formatted as actual html links. You still need to copy and paste the file location to addressbar before pressing the download arrow from the toolbar.

-Back, Forward, home, zoom buttons etc. are there. Info button is added from 0.6 onwards.

-Search switch: easily use multiple search engines by adding a keyword to the search switch field. Then add the actual word to the search field. Default search engine is Privatelee (switch field left empty) . Currently added additional search engines are: Wikipedia search, Wolfram Alpha and Youtube search. 0.6 release adds Google.com.

Tip. Hover the mouse cursor over the switch field to  get instructional tooltip about the available search engines.

-The browser should support common Linux plugins after they are installed. QT´s native HTML playback does not work in full screen mode. RunIT Browser integrates with HTML5-GTK-Player, which does support full screen playback.

___________

Executing

If needed make python files executable: chmod +x filename.py

Run with: python run.py

______________________________________
Original post is at:
http://www.techtimejourney.net/runit-qt-v-0-6-arrives/
