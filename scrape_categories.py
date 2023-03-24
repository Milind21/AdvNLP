import wikipedia as w
#import requests
#from bs4 import BeautifulSoup as bs

def get_paragraphs(para,i):
    res = ""
    while "==" not in para[i]:
        res += para[i]
        i+=1
    return res

def store(symptoms,disease_name,plant_name):
    #print(disease_name)
    file1 = open("dataset.txt", "a")  # append mode
    if(symptoms!=""):
        file1.write("\n"+symptoms+"\t"+plant_name+" "+disease_name+"\n")
    file1.close()

def getPlantName(plant_name):
    list_of_tokens = plant_name.split()
    
    res = ""

    for i in range(len(list_of_tokens)):
        if i == 0 or i == 1:
	        continue
        if "disease" in list_of_tokens[i].lower():
	        return res
        res = res + " "+ list_of_tokens[i]
    
    return res

query = "Lists of Plant Diseases"
result = w.search(query)

list_of_disease_categories = w.page(result[0])
list_of_diseases_links = (list_of_disease_categories.links)

print(len(list_of_diseases_links))
pagecount = 0
totalcount = 0
# TODO automate it for other links
for link in list_of_diseases_links:
    plant_name = getPlantName(link)
    single_plant_disease_page = w.page(link,auto_suggest=False)
    single_plant_disease_links = single_plant_disease_page.links

    #To Do automate for other links inside the outer for-loop
    for plant_specific_link in single_plant_disease_links:
        try:
            single_disease_page = w.page(plant_specific_link,auto_suggest=False)
            totalcount += 1
        except:
            continue
        single_disease_content = single_disease_page.content

        single_disease_content_paragraphs = single_disease_content.split("\n")
        flag = 0
        for i in range(len(single_disease_content_paragraphs)):
            para = single_disease_content_paragraphs[i]
            if ("hosts and symptoms" in para.lower() or "symptoms" in para.lower()) and "==" in para:
                pagecount += 1
                print(pagecount)
                to_store_paragraphs = get_paragraphs(single_disease_content_paragraphs,i+1)
                store(to_store_paragraphs, plant_specific_link,plant_name)
                flag = 1
                break

