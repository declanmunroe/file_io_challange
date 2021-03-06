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
                        "{section}" : "This is the about section",
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
    
    for filename, data in page_content.items():
        with open(filename, "w") as outputFile:
            for k, v in data.items():
                text = outputFile.write(data[k])
                print(k, v)

# with open("index.html", "w") as outputFile:
#     text = outputFile.write(text)





