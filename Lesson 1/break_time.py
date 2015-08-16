import  webbrowser
import  time

t = 1
i = 0

while (i < t) :
    print ("Before: "  +  time.ctime())
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1, autoraise=True)
    print ("After:  " + time.ctime())
    i = i + 1
    print (i)
    
    

