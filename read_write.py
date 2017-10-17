page_content = {
    "index.html" :
                    {
                        "{title}" : "This is the title",
                        "{heading}" : "This is the heading",
                        "{body}" : "This is the body",
                        "{footer}" : "This is the footer"
                    },
    "about.html" : 
                    {
                        "{title}" : "This is the about title",
                        "{heading}" : "This is the about heading",
                        "{body}" : "This is the about body",
                        "{footer}" : "This is the about footer"
                    }

}




# dictionary = {
#         "{title}" : "This is the title",
#         "{heading}" : "This is the heading",
#         "{body}" : "This is the body",
#         "{footer}" : "This is the footer",
#         }

with open("template.html", "r") as readFile:
    text = readFile.read()
    
    for k, v in page_content.items():
        #text = text.replace(k, v)
        print(k, v)

with open("index.html", "w") as outputFile:
    text = outputFile.write(text)





