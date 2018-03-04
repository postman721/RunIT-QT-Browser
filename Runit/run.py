#RunIT-QT Browser Copyright (c) 2015 JJ Posti <techtimejourney.net> 
#RunIT-QT  comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991
#This is the 0.6.3 version(March 2018)
#This version fixes HTML5 playback issues.
#####Modules
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebKitWidgets
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QVBoxLayout, QSplitter, QToolButton, QLineEdit, QLabel, QToolBar, QPushButton, QFileDialog
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebPage, QWebView, QWebInspector
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrinter
import os, sys, subprocess
from subprocess import Popen 

from win import *
from icons import *
from labels import Labels as label
#####################################
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_MainWindow(QMainWindow):
#Notice that this is the parent window.
    def __init__(self, *args, **kwargs):
        super(Ui_MainWindow, self).__init__(*args, **kwargs)    

#Begin page loading
    def begin(self):
        self.label.setText(label.begin())

    def complete(self):
        self.label.setText(label.complete())
                		
#####Download functions.

    def downloads(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self.web,"Save as","","All Files (*)", options=options)
        address=self.address.text()
        if fileName:
            subprocess.Popen(['wget', address, '-O', fileName])

#Set the label text.           
    def loadings(self):
        self.label.setText(label.loadings())
####################################################
#####Printer functions.

    def handlePreview(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def handlePaintRequest(self, printer):
        self.web.render(QPainter(printer))	

#Set the label text.
    def printme(self):
        self.label.setText(label.printer())
####################################################
#Open html5 playback. 
    def html5(self):
        subprocess.Popen(['python', '/usr/share/html5.py'])
        self.label.setText(label.html5())
####################################################
#####Page navigation functions.
        
#Back function.
    def backs(self,url):
        goback=self.web.back()
	
#Forward function.	
    def forwards(self,url):	
        self.web.forward()       

#Reload function.
    def reloads(self):	
        self.web.reload()

#System arguments support / Go to address / Find text functionality.         
    def system_arguments(self):            
        if len(sys.argv) == 1:
            url=self.address.text()
            if url.startswith('http://'):
                change=str(url)
                self.address.setText(change)
                load=self.address.text()
                self.label.setText(load)
                self.web.load(QUrl(load))
                del sys.argv[1:]
        
            elif url.startswith('https://'):
                change=str(url)
                self.address.setText(change)
                load=self.address.text()
                self.label.setText(load)
                self.web.load(QUrl(load))
                del sys.argv[1:]
            
            elif url.startswith('find:'):
                load=self.address.text()
                self.result0 = load.replace('find:', '')
                print "Finding:" + self.result0                
                self.web.findText(self.result0)
                self.label.setText(label.finding())
                del sys.argv[1:]

            else:
                add="https://" + url
                change=str(add)
                self.address.setText(change)
                load=self.address.text()
                self.label.setText(load)
                self.web.load(QUrl(load))
                del sys.argv[1:]
        
        else:    			        
             self.location = sys.argv[1:]
             self.temp=str(self.location)
             self.result0 = self.temp.replace('[', '')
             self.result1 = self.result0.replace(']', '')
             self.result_final = self.result1.replace("'", '')

             url=self.result_final
             if url.startswith('http://'):
                 change=str(url)
                 self.address.setText(change)
                 load=self.address.text()
                 self.label.setText(load)
                 self.loading1=self.web.load(QUrl(load))
                 del sys.argv[1:]
                 
             elif url.startswith('https://'):
                  change=str(url)
                  self.address.setText(change)
                  load=self.address.text()
                  self.label.setText(load)
                  self.loading1=self.web.load(QUrl(load))
                  del sys.argv[1:]

             else:
                  change=str("https://" + url)
                  self.address.setText(change)
                  load=self.address.text()
                  self.label.setText(load)
                  self.web.load(QUrl(load))
                  del sys.argv[1:]

#Home page function.
    def homes(self):
        self.home = "http://www.techtimejourney.net/postx_pages/postx.html"
        self.address.setText(self.home)
        self.web.load(QUrl(self.home))
####################################################
#####Page Zoom functions.
   
    def zoomins(self):
        self.web.setZoomFactor(self.web.zoomFactor()+.2)

    def zoomouts(self):
        self.web.setZoomFactor(self.web.zoomFactor()-.2)
                                 			        
##################################
#####Search engines & default (Now. Startpage).
    def extra(self):
        search=self.Search.text()
        text=self.switch_2.text()
        if text == ('wolf'):

#Wolfram Alpha search.
            adds1="https://www.wolframalpha.com/input/?i=" + search 
            self.web.load(QUrl(adds1))
            print adds1
        
        elif text == ('wiki'):

#Wikipedia search (english).        
            adds1="https://en.wikipedia.org/w/index.php?title=Special:Search&profile=default&fulltext=Search&search=" + search 
            self.web.load(QUrl(adds1))
            print adds1

        elif text == ('tube'):

#Youtube search (english).        
            adds1="https://www.youtube.com/results?search_query=" + search 
            self.web.load(QUrl(adds1))
            print adds1

        elif text == ('gs'):

#Startpage search (english).        
            adds1="https://startpage.com/do/search?query=" + search 
            self.web.load(QUrl(adds1))
            print adds1

        else:
            adds1="https://startpage.com/do/search?query=" + search 
            self.web.load(QUrl(adds1))
            print adds1
                                    			               
############################################
#####Bookmark functions.
    
    def bookmarks(self,widget):
        home=os.getenv("HOME")
        print home
        site=str(self.address.text())
        os.chdir(home) 
        f = open('.bookmarks.html', 'a')
        f.write("<br>" + "<a href=" + site + ">"+ site + "</a>")
        f.close()

#Set label text.    
    def notice_new_bookmark(self):
        self.label.setText(label.bookmarked())

#Open bookmarks file.
    def bookopen(self,widget):
    	home=os.getenv("HOME")
        print home
        home=os.getenv("HOME")
        os.chdir(home)
        head="file:///"
        books=".bookmarks.html"
        adds=self.address.setText(head + home + '/' + books)
        adda=self.address.text()
        self.web.load(QUrl(adda))
####################################################
#####Other functions.
#Label reset.
    def reset(self):
        self.label.setText('')
        
#About messagebox.
    def about(self):
        buttonReply = QMessageBox.question(self, "RunIT-QT Browser Copyright (c) 2015 JJ Posti <techtimejourney.net>", "RunIT-QT  comes with ABSOLUTELY NO WARRANTY;  This is free software, and you are welcome to redistribute it under  GPL Version 2, June 1991 This is the 0.6.3 version(March 2018). ___________________________________________________________________________ \n \nArgument support (since 0.6).\nStart browser like this: runit 'gooogle.fi' and follow statusbar instructions. ___________________________________________________________________________\n \nFind text from html(since 0.6).\nWrite find:something to address field and press enter to find the first entry. Press enter again to find the second entry etc. ___________________________________________________________________________\n \nRight-click menu:Save image functionality(since 0.6). Right-click upon an image and choose Copy Image address. Next choose Save image and the Save as dialog should open.", QMessageBox.Ok )
        if buttonReply == QMessageBox.Ok:
            pass                    
####################################################
#####UI Parts.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setStyleSheet("background-color:#a7a7a7;font-size: 12px;")
    
        MainWindow.setMaximumHeight(16777215)
        MainWindow.setMaximumWidth(16777215)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
            
        self.toolbar = QToolBar()
        self.toolbar.setObjectName(_fromUtf8("toolbar"))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
       
#Timer for label resets.
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.reset)
        self.timer.start(9000) #Update within every 9 seconds. 
                
#Back.        
        self.back = QToolButton()
        self.back.setStyleSheet("QToolButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QToolButton:hover{background-color:#5c5c5c;}") 
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8(":/icons/back.png")), QIcon.Normal, QIcon.Off)
        self.back.setIcon(icon)
        self.back.setObjectName(_fromUtf8("back"))
        self.back.setToolTip('Go Back')
        self.back.clicked.connect(self.backs)
        self.back.setFixedSize(24, 24)
        self.toolbar.addWidget(self.back)

#Address.        
        self.address = QLineEdit()
        self.address.setStyleSheet("QLineEdit{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QLineEdit:hover{background-color:#5c5c5c;}") 
        self.address.setObjectName(_fromUtf8("lineEdit"))
        self.address.setPlaceholderText("Type an address")
        self.address.returnPressed.connect(self.system_arguments)
        self.toolbar.addWidget(self.address)

#Forward.        
        self.forward = QToolButton()
        self.forward.setStyleSheet("QToolButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QToolButton:hover{background-color:#5c5c5c;}") 
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(_fromUtf8(":/icons/forward.png")), QIcon.Normal, QIcon.Off)
        self.forward.setIcon(icon1)
        self.forward.setObjectName(_fromUtf8("forward"))
        self.forward.setToolTip('Go Forward')
        self.forward.clicked.connect(self.forwards)
        self.forward.setFixedSize(24, 24)
        self.toolbar.addWidget(self.forward)

#Home.        
        self.home = QToolButton()
        self.home.setStyleSheet("QToolButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QToolButton:hover{background-color:#5c5c5c;}") 
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(_fromUtf8(":/icons/home.png")), QIcon.Normal, QIcon.Off)
        self.home.setIcon(icon2)
        self.home.setObjectName(_fromUtf8("home"))
        self.home.setToolTip('Go Home')
        self.home.clicked.connect(self.homes)
        self.home.setFixedSize(24, 24)
        self.toolbar.addWidget(self.home)
        
#Reload.        
        self.reloading = QToolButton()
        self.reloading.setStyleSheet("QToolButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QToolButton:hover{background-color:#5c5c5c;}") 
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(_fromUtf8(":/icons/reload.png")), QIcon.Normal, QIcon.Off)
        self.reloading.setIcon(icon3)
        self.reloading.setObjectName(_fromUtf8("reload"))
        self.reloading.setToolTip('Reload Page')
        self.reloading.clicked.connect(self.reloads)
        self.reloading.setFixedSize(24, 24)
        self.toolbar.addWidget(self.reloading)

#Html5 player.        
        self.vlc = QToolButton()
        self.vlc.setStyleSheet("QToolButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QToolButton:hover{background-color:#5c5c5c;}") 
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(_fromUtf8(":/icons/vlc_play.png")), QIcon.Normal, QIcon.Off)
        self.vlc.setIcon(icon4)
        self.vlc.setObjectName(_fromUtf8("vlc"))
        self.vlc.setToolTip('Open HTML5 player')
        self.vlc.clicked.connect(self.html5)
        self.vlc.setFixedSize(24, 24)
        self.toolbar.addWidget(self.vlc)

#Bookmark.        
        self.bookmark = QToolButton()
        self.bookmark.setStyleSheet("QToolButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QToolButton:hover{background-color:#5c5c5c;}") 
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(_fromUtf8(":/icons/bookmark.png")), QIcon.Normal, QIcon.Off)
        self.bookmark.setIcon(icon5)
        self.bookmark.setObjectName(_fromUtf8("bookmark"))
        self.bookmark.setToolTip('Bookmark addressbar location')
        self.bookmark.clicked.connect(self.bookmarks)
        self.bookmark.clicked.connect(self.notice_new_bookmark)
        self.bookmark.setFixedSize(24, 24)
        self.toolbar.addWidget(self.bookmark)

#Open Bookmarks.        
        self.see_bookmark = QToolButton()
        self.see_bookmark.setStyleSheet("QToolButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QToolButton:hover{background-color:#5c5c5c;}") 
        icon6 = QIcon()
        icon6.addPixmap(QPixmap(_fromUtf8(":/icons/seebook.png")), QIcon.Normal, QIcon.Off)
        self.see_bookmark.setIcon(icon6)
        self.see_bookmark.setObjectName(_fromUtf8("see_bookmark"))
        self.see_bookmark.setToolTip('See Bookmarks')
        self.see_bookmark.clicked.connect(self.bookopen)
        self.see_bookmark.setFixedSize(24, 24)
        self.toolbar.addWidget(self.see_bookmark)

#Download.        
        self.download = QToolButton()
        self.download.setStyleSheet("QToolButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QToolButton:hover{background-color:#5c5c5c;}") 
        icon7 = QIcon()
        icon7.addPixmap(QPixmap(_fromUtf8(":/icons/download.png")), QIcon.Normal, QIcon.Off)
        self.download.setIcon(icon7)
        self.download.setObjectName(_fromUtf8("download"))
        self.download.setToolTip('Download file from location')
        self.download.clicked.connect(self.downloads)
        self.download.clicked.connect(self.loadings)
        self.download.setFixedSize(24, 24)
        self.toolbar.addWidget(self.download)
        
#Search Switch.        
        self.switch_2 = QLineEdit()
        self.switch_2.setStyleSheet("QLineEdit{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QLineEdit:hover{background-color:#5c5c5c;}") 
        self.switch_2.setObjectName(_fromUtf8("switch_2"))
        self.switch_2.setPlaceholderText("Switch")
        self.switch_2.setFixedSize(50, 24)
        self.switch_2.setToolTip('gs=Startpage, wiki = Wikipedia,  tube = Youtube,  wolf = Wolfram Alpha. Empty = Startpage search (default)')
        self.switch_2.returnPressed.connect(self.extra)
        self.toolbar.addWidget(self.switch_2)

#Search.        
        self.Search = QLineEdit()
        self.Search.setStyleSheet("QLineEdit{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QLineEdit:hover{background-color:#5c5c5c;}") 
        self.Search.setObjectName(_fromUtf8("Search"))
        self.Search.setPlaceholderText("Search something")
        self.Search.setToolTip('Search')
        self.Search.returnPressed.connect(self.extra)
        self.toolbar.addWidget(self.Search)

#Printing.        
        self.printing = QToolButton()
        self.printing.setStyleSheet("QToolButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QToolButton:hover{background-color:#5c5c5c;}") 
        icon8 = QIcon()
        icon8.addPixmap(QPixmap(_fromUtf8(":/icons/print.png")), QIcon.Normal, QIcon.Off)
        self.printing.setIcon(icon8)
        self.printing.setObjectName(_fromUtf8("print"))
        self.printing.setToolTip('Print')
        self.printing.clicked.connect(self.handlePreview)
        self.printing.clicked.connect(self.printme)
        self.printing.setFixedSize(24, 24)
        self.toolbar.addWidget(self.printing)
        
#Zoom +.       
        self.zoom_in = QToolButton()
        self.zoom_in.setStyleSheet("QToolButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QToolButton:hover{background-color:#5c5c5c;}") 
        icon9 = QIcon()
        icon9.addPixmap(QPixmap(_fromUtf8(":/icons/zoom-in.png")), QIcon.Normal, QIcon.Off)
        self.zoom_in.setIcon(icon9)
        self.zoom_in.setObjectName(_fromUtf8("zoom_in"))
        self.zoom_in.setToolTip('Zoom +')
        self.zoom_in.clicked.connect(self.zoomins)
        self.zoom_in.setFixedSize(24, 24)
        self.toolbar.addWidget(self.zoom_in)

#Zoom -.        
        self.zoom_out = QToolButton()
        self.zoom_out.setStyleSheet("QToolButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QToolButton:hover{background-color:#5c5c5c;}") 
        icon10 = QIcon()
        icon10.addPixmap(QPixmap(_fromUtf8(":/icons/zoom-out.png")), QIcon.Normal, QIcon.Off)
        self.zoom_out.setIcon(icon10)
        self.zoom_out.setObjectName(_fromUtf8("zoom_out"))
        self.zoom_out.setToolTip('Zoom -')
        self.zoom_out.clicked.connect(self.zoomouts)
        self.zoom_out.setFixedSize(24, 24)
        self.toolbar.addWidget(self.zoom_out)

#About.
        self.about1 = QPushButton()
        self.about1.setObjectName("Info")
        self.about1.setStyleSheet("QPushButton{color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;}"
        "QPushButton:hover{background-color:#5c5c5c;}") 
        self.about1.setText("i")
        self.about1.setToolTip('Info')
        self.about1.setFixedSize(24, 24)
        self.about1.clicked.connect(self.about) 
        self.toolbar.addWidget(self.about1)
             
#Web browser.        
        self.web = NewWindow(self.centralwidget)
        self.web.titleChanged = self.setWindowTitle
        self.web.urlChanged.connect(lambda x: self.address.setText(x.toString()))
        self.web.loadStarted.connect(self.begin)        
        self.web.loadFinished.connect(self.complete)        
        
        #Label as a secondary address placeholder.
        self.label=QLabel()
        self.label.setFixedSize(500,16)
        self.label.setText("Click addressbar and press enter if you supplied arguments.")        
        self.web.setObjectName(_fromUtf8("kwebview"))
        self.web.setMaximumHeight(16777215)
        self.web.setMaximumWidth(16777215)
        
#Adding to layout.        
        MainWindow.setCentralWidget(self.centralwidget)                
        self.verticalLayout_2.addWidget(self.toolbar)
        self.verticalLayout_2.addWidget(self.web)
        self.verticalLayout_2.addWidget(self.label)            

#Web inspector.
        self.inspector = QWebInspector()

        self.web.page().settings().setAttribute(
            QWebSettings.DeveloperExtrasEnabled, True
        )
        self.inspector.setPage(self.web.page())
        
#More Browser settings.
        self.web.page().settings().setAttribute(QWebSettings.JavascriptEnabled, True)
        self.web.page().settings().setAttribute(QWebSettings.LocalContentCanAccessFileUrls, True)
        self.web.page().settings().setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)
        self.web.page().settings().setAttribute(QWebSettings.LocalStorageEnabled, True)
        self.web.page().settings().setAttribute(QWebSettings.PluginsEnabled, True)
        self.web.page().settings().setAttribute(QWebSettings.PrivateBrowsingEnabled, False)
        self.web.page().settings().setAttribute(QWebSettings.SpatialNavigationEnabled, True)
        self.web.page().settings().setAttribute(QWebSettings.AutoLoadImages, True)
        self.web.page().settings().setAttribute(QWebSettings.AcceleratedCompositingEnabled, True)
####################################################
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)        
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "RunIT-QT", None))
        self.back.setText(_translate("MainWindow", "Back", None))
        self.forward.setText(_translate("MainWindow", "Forward\n"
"", None))
        self.home.setText(_translate("MainWindow", "Home", None))
        self.reloading.setText(_translate("MainWindow", "Reload\n"
"", None))
        self.vlc.setText(_translate("MainWindow", "Vlc Play", None))
        self.bookmark.setText(_translate("MainWindow", "Bookmarkl", None))
        self.see_bookmark.setText(_translate("MainWindow", "See bookmarks", None))
        self.download.setText(_translate("MainWindow", "Download", None))
        self.printing.setText(_translate("MainWindow", "Print", None))
        self.zoom_in.setText(_translate("MainWindow", "Zoom+", None))
        self.zoom_out.setText(_translate("MainWindow", "Zoom-", None))
####################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
