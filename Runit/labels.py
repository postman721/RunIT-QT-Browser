#This module contains RunIT Broser's label texts as staticmethods.
class Labels:
#Begin page loading.
    @staticmethod
    def begin():
        text=('Loading...')
        return text

#When page loading ends.
    @staticmethod
    def complete():
        text=('Loading finished.')
        return text
        
#####Last action (prints).

    #Downloaded something.
    @staticmethod
    def loadings():
        text=('Last action: Downloaded an object.')
        return text
     
    #Bookmarked something. 
    @staticmethod
    def bookmarked():
        text=('Last action: Bookmark created.')
        return text

    #Find something. 
    @staticmethod
    def finding():
        text=('Last action: Find text.')
        return text        

    #Open HTML-GTK-Player.
    @staticmethod
    def html5():
        text=('Last action: HTML5 player opened.')
        return text
 
    #Printing a page.
    @staticmethod
    def printer():
        text=('Last action: Print.')
        return text 
