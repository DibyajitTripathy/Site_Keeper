import webbrowser

ffpath = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(ffpath))
ccpath = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(ccpath))

print("\n \nTo run this programme made by Dibyajit Tripathy, \n \n You need to add browser and its path to the data base \n \n (Default firefox and chrome browser has been set) ")
def menu1():
    print("\n 1.ADD \n 2.CONTINUE")
    choice=input()
    if choice=="1":
        print("\n Enter the name of the browser \n")
        xxname=input()
        print("\n Enter the path of the browser \n \n N.B: After each folder put (DOUBLE BACKWARD SLASH)\n")
        xxpath1=input()
        xxpath=('xxpath1'+'xxname.exe')
        webbrowser.register('xxname',None,webbrowser.BackgroundBrowser(xxpath))
        print(" \n Your browser has been added \n")
    else:
            def menu():
                
                print ("Welcome to Dibyajit World \n Enter your web-browser to acess \n 1.Google-chrome \n 2.Mozilla-Firefox  \n  "+ "3.xxname")
                browse=input()

                if browse=="1":
                    print ('Enter the Account you want to open \n 1.Gmail \n 2.Facebook \n 3.LInkedIn \n 4.Twitter \n 5.GitHub \n 6.Angellist \n 7.Youtube \n 8.Overleaf \n 9.Quora \n 10.IRCTC')

                    select1=input()
                    if select1=="1": 
                        webbrowser.get('chrome').open_new_tab('https://mail.google.com')
                        menu()
                    elif select1=="2": 
                        webbrowser.get('chrome').open_new_tab('https://www.facebook.com/')
                        menu()
                    elif select1=="3": 
                        webbrowser.get('chrome').open_new_tab('https://www.linkedin.com/uas/login?')
                        menu()
                    elif select1=="4": 
                        webbrowser.get('chrome').open_new_tab('https://twitter.com/login')
                        menu()
                    elif select1=="5": 
                        webbrowser.get('chrome').open_new_tab('https://github.com/')
                        menu()
                    elif select1=="6": 
                        webbrowser.get('chrome').open_new_tab('https://angel.co/')
                        menu()
                    elif select1=="7": 
                        webbrowser.get('chrome').open_new_tab('https://www.youtube.com/')
                        menu()
                    elif select1=="8": 
                        webbrowser.get('chrome').open_new_tab('https://www.overleaf.com/')
                        menu()
                    elif select1=="9": 
                        webbrowser.get('chrome').open_new_tab('https://www.quora.com/')
                        menu()
                    elif select1=="10": 
                        webbrowser.get('chrome').open_new_tab('https://www.irctc.co.in/')
                        menu()                

                elif browse =="2":
                    print ('Enter the Account you want to open \n 1.Gmail \n 2.Facebook \n 3.LInkedIn \n 4.Twitter \n 5.GitHub \n 6.Angellist \n 7.Youtube \n 8.Overleaf \n 9.Quora \n 10.IRCTC')
                    select2=input()
                    if select2=="1": 
                        webbrowser.get('firefox').open_new_tab('https://mail.google.com')
                        menu()
                    elif select2=="2": 
                        webbrowser.get('firefox').open_new_tab('https://www.facebook.com/')
                        menu()
                    elif select2=="3": 
                        webbrowser.get('firefox').open_new_tab('https://www.linkedin.com/uas/login?')
                        menu()
                    elif select2=="4": 
                        webbrowser.get('firefox').open_new_tab('https://twitter.com/login')
                        menu()
                    elif select2=="5": 
                        webbrowser.get('firefox').open_new_tab('https://github.com/')
                        menu()
                    elif select2=="6": 
                        webbrowser.get('firefox').open_new_tab('https://angel.co/')
                        menu()
                    elif select2=="7": 
                        webbrowser.get('firefox').open_new_tab('https://www.youtube.com/')
                        menu()
                    elif select2=="8": 
                        webbrowser.get('firefox').open_new_tab('https://www.overleaf.com/')
                        menu()
                    elif select2=="9": 
                        webbrowser.get('firefox').open_new_tab('https://www.quora.com/')
                        menu()
                    elif select2=="10": 
                        webbrowser.get('firefox').open_new_tab('https://www.irctc.co.in/')
                        menu()  
                elif browse =="3":
                    print ('Enter the Account you want to open \n 1.Gmail \n 2.Facebook \n 3.LInkedIn \n 4.Twitter \n 5.GitHub \n 6.Angellist \n 7.Youtube \n 8.Overleaf \n 9.Quora \n 10.IRCTC')
                    select2=input()
                    if select2=="1": 
                        webbrowser.get(xxname).open_new_tab('https://mail.google.com')
                        menu()
                    elif select2=="2": 
                        webbrowser.get('firefox').open_new_tab('https://www.facebook.com/')
                        menu()
                    elif select2=="3": 
                        webbrowser.get('firefox').open_new_tab('https://www.linkedin.com/uas/login?')
                        menu()
                    elif select2=="4": 
                        webbrowser.get('firefox').open_new_tab('https://twitter.com/login')
                        menu()
                    elif select2=="5": 
                        webbrowser.get('firefox').open_new_tab('https://github.com/')
                        menu()
                    elif select2=="6": 
                        webbrowser.get('firefox').open_new_tab('https://angel.co/')
                        menu()
                    elif select2=="7": 
                        webbrowser.get('firefox').open_new_tab('https://www.youtube.com/')
                        menu()
                    elif select2=="8": 
                        webbrowser.get('firefox').open_new_tab('https://www.overleaf.com/')
                        menu()
                    elif select2=="9": 
                        webbrowser.get('firefox').open_new_tab('https://www.quora.com/')
                        menu()
                    elif select2=="10": 
                        webbrowser.get('firefox').open_new_tab('https://www.irctc.co.in/')
                        menu()          


            menu()
menu1()


