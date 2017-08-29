#This module contains the New page functionalities for RunIT-QT Browser.
#####Modules
from PyQt5 import QtCore, QtGui, QtWebKitWidgets,QtWidgets
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebKitWidgets import QWebPage, QWebView
from PyQt5.QtWidgets import QFileDialog,QApplication
import os, sys, subprocess
from subprocess import Popen 
#####################################
#Declaring     def __init__(self, parent=None): gives us an ability to use this module as an independent window - but still in the 
#main program because of super(NewPage, self).__init__(parent) that follows.

class NewPage(QWebPage):
    def __init__(self, parent=None):
        super(NewPage, self).__init__(parent)
          
    def userAgentForUrl(self, url):
        ''' Returns a User Agent that will be seen by the website. '''
        return "Mozilla/5.0 (X11; Linux) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
    
    def triggerAction(self, action, checked=False):
        if action == QWebPage.OpenLinkInNewWindow:
            self.createWindow(QWebPage.WebBrowserWindow)

        elif action == QWebPage.DownloadImageToDisk:
            clipboard = QApplication.clipboard()
            http_location=str(clipboard.text())
            print "Image location:" + http_location 
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(None,"Save as","","All Files (*)", options=options)
            if fileName:
                subprocess.Popen(['wget', http_location, '-O', fileName])                                      
        return super(NewPage, self).triggerAction(action, checked)

class NewWindow(QWebView):
    def __init__(self, parent=None):
        super(NewWindow, self).__init__(parent)

        self.NewPage = NewPage(self)
        
        self.setPage(self.NewPage)

    def createWindow(self, windowType):
        if windowType == QWebPage.WebBrowserWindow:
            self.webView = NewWindow()
            self.webView.setAttribute(Qt.WA_DeleteOnClose, True)
            return self.webView
        return super(NewWindow, self).createWindow(windowType)
