import requests
import json

class TheMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "" # requires an api key
        

    def listMovie(self,sort,param,number,title):
        try:
            pages = (number//20)+1        
            for i in range(pages):
                a = i+1
                if a < pages:
                    a = str(a)
                    re =requests.get(self.api_url + sort + "/"  + param + "?api_key=" + self.api_key + "&language=en-US&page=" + a)
                    res = re.text
                    res = json.loads(res)         
                    for i in range(20):
                        print(res["results"][i][title])
                elif a == pages:
                    a = str(a)
                    re =requests.get(self.api_url + sort +"/" + param + "?api_key=" + self.api_key + "&language=en-US&page=" + a)
                    res = re.text
                    res = json.loads(res)
                    newnumber = number-((pages-1)*20)  
                    for i in range(newnumber):
                        print(res["results"][i][title])
        except Exception:
            pass

    def searchMovie(self,sort,keyword,number,title):
        try:
            pages = (number//20)+1
            re = requests.get(self.api_url + "search/"+ sort +"/?api_key=" + self.api_key + "&language=en-US&query="+keyword+"&page=1&include_adult=false")
            re = re.text
            re = json.loads(re)
            apiPage = re["total_pages"]
            if pages <= apiPage:
                for i in range(pages):
                    a = i+1
                    if a < pages:
                        a = str(a)
                        re =requests.get(self.api_url + "search/"+ sort +"/?api_key=" + self.api_key + "&language=en-US&query="+keyword+"&page="+a+"&include_adult=false")
                        res = re.text
                        res = json.loads(res)         
                        for i in range(20):
                            print(res["results"][i][title])
                    elif a == pages:
                        a = str(a)
                        re =requests.get(self.api_url + "search/"+ sort +"/?api_key=" + self.api_key + "&language=en-US&query="+keyword+"&page="+a+"&include_adult=false")
                        res = re.text
                        res = json.loads(res)
                        newnumber = number-((pages-1)*20)  
                        for i in range(newnumber):
                            print(res["results"][i][title])
            if pages > apiPage:
                pages = apiPage
                for i in range(pages):
                    a = i+1
                    if a < pages:
                        a = str(a)
                        re =requests.get(self.api_url + "search/"+ sort +"/?api_key=" + self.api_key + "&language=en-US&query="+keyword+"&page="+a+"&include_adult=false")
                        res = re.text
                        res = json.loads(res)         
                        for i in range(20):
                            print(res["results"][i][title])
                    elif a == pages:
                        a = str(a)
                        re =requests.get(self.api_url + "search/"+ sort +"/?api_key=" + self.api_key + "&language=en-US&query="+keyword+"&page="+a+"&include_adult=false")
                        res = re.text
                        res = json.loads(res)
                        newnumber = number-((pages-1)*20)  
                        for i in range(newnumber-1):
                            print(res["results"][i][title])
        except Exception:
            pass
      





        
movie = TheMovieDb()



print("Welcome! What you want to do?".center(50,"*"))
while True:
    val = input("1-Find Movies\n2-Find TV Series\n3-Exit\nChoose: ")

    if val == "3":
        break

    elif val == "1":
        while True:
            val = input("1-Popular\n2-Top rated\n3-Upcoming\n4-Now playing\n5-Search movie with keywords\n6-Main menu\nChoose: ")
            if val == "6":
                break
            elif val == "1":
                movie.listMovie("movie","popular",int(input("How many movies do you want to list? ")),"original_title")
            elif val == "2":
                movie.listMovie("movie","top_rated",int(input("How many movies do you want to list? ")),"original_title")
            elif val == "3":
                movie.listMovie("movie","upcoming",int(input("How many movies do you want to list? ")),"original_title")
            elif val == "4":
                movie.listMovie("movie","now_playing",int(input("How many movies do you want to list? ")),"original_title")
            elif val == "5":
                movie.searchMovie("movie",input("Enter a keyword: "),int(input("How many movies do you want to list? ")),"original_title")
            else:
                print("Type correctly! (Like numbers: 1,2,3...)".rjust(50,"*"))
 

    elif val == "2":
        while True:
            try:
                val = input("1-Popular\n2-Top rated\n3-Search series with keywords\n4-Get TV on the air\n5-Main menu\nChoose: ")
                if val == "5":
                    break
                elif val == "1":
                    movie.listMovie("tv","popular",int(input("How many movies do you want to list? ")),"name")
                elif val == "2":
                    movie.listMovie("tv","top_rated",int(input("How many movies do you want to list? ")),"name")
                elif val == "3":
                    movie.searchMovie("tv",input("Enter a keyword: "),int(input("How many movies do you want to list? ")),"name")
                elif val == "4":
                    movie.listMovie("tv","on_the_air",int(input("How many movies do you want to list? ")),"name")
                else:  
                    print("Type correctly! (Like numbers: 1,2,3...)".rjust(50,"*"))
            except Exception :
                print("Type correctly!")
 
    
    else:
        print("Type correctly!(Like numbers: 1,2,3...)".center(100,"*"))
 


