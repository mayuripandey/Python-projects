
# return value should be a list, each item is a string containing name, jobTitle(professor or researcher) and professorship, seperated by '&'

from bs4 import BeautifulSoup
import requests

def getNameFromNSCDept():
    faculty_name = "Natural Science"
    pro_list = ["https://www.tu-chemnitz.de/chemie/anorg/mitarbeiter.php.en",
                "https://www.tu-chemnitz.de/physik/CHEMPHYS/mitglieder.php",
                "https://www.tu-chemnitz.de/chemie/tech/mitarbeiter.php.en",
                "https://www.tu-chemnitz.de/chemie/mc/public/mitarbeiter.php.en",
                "https://www.tu-chemnitz.de/chemie/org/mitarbeiter.html.en",
                "https://www.tu-chemnitz.de/chemie/physchem/index.html#mitarbeiter",
                "https://www.tu-chemnitz.de/chemie/elchem/seiten/mitarbeiter.php.en#inhalt",
                "https://www.tu-chemnitz.de/chemie/polymer/aksommer/mitarbeiter.php.en",
                "https://www.tu-chemnitz.de/chemie/tech/mitarbeiter.php.en",
                "https://www.tu-chemnitz.de/chemie/quant/index.html.en",
                "https://www.tu-chemnitz.de/chemie/toxi/",

                ]

    pro_name = ["Professorship of Inorganic Chemistry", "Professorship of Chemical Physics", "Professorship of Chemical Technology",
                "Professorship of Materials for Innovative Energy Concepts","Professorship of Organic Chemistry","Professorship of Physical Chemistry",
                "Professorship of Physical Chemistry/ Electrochemistry","Professorship of Polymer Chemistry", "Professorship of Chemical Technology",
                "Computer Supported Quantum Chemistry","Toxikologie und Rechtskunde"]

    name_list = []
    prof_name = []
    pro_id = 0
    while pro_id < len(pro_list):
        r = requests.get(pro_list[pro_id])
        soup = BeautifulSoup(r.text, 'html.parser')
        if pro_id == 0:
            parents = soup.find_all("table", {'class': 'horizontal grey'})
            for soup_item in parents:
                prof_name = soup_item.find_all("tr")

        elif pro_id == 1:
            parents = soup.find_all("table", {'class': 'ohne'})
            for soup_item in parents:
                prof_name = soup_item.find("td")
        elif pro_id == 2 or pro_id == 3 or pro_id == 5 or pro_id == 7 or pro_id == 8:
            prof_name = soup.find_all("div", class_="h4")

        if pro_id == 4:
            parents = soup.find_all("div", {"class": ["mitarbeiter1", "mitarbeiter3"]})
            for soup_item in parents:
                prof_name = soup_item.find_all("div")

        elif pro_id == 6:
            parents = soup.find_all("div", {'class': 'active tab-pane'})
            for soup_item in parents:
                prof_name = soup_item.find_all("a")

        elif pro_id == 9:
            # prof_name = soup.find_all("", class_="linie")
            parents = soup.find_all("main", {'class': 'page-content'})
            for soup_item in parents:
                prof_name = soup_item.find_all("a")
        elif pro_id == 10:
            parents = soup.find_all("li", {'class': 'current'})
            for soup_item in parents:
                    prof_name = soup_item.find_all("span")
        if pro_id == 11:
            table = soup.find("main", class_="page-content")
            trs = table.find_all("tr")
            for tr in trs:
                td = tr.find_all("td")
                if len(td) > 0:
                    if (td[0].find("a") != None):
                        name = td[0].find("a").text
                        name_list.append(name.replace(u"\xa0", " "))

        for item in prof_name:
            try:
                name = item.find("a").get_text()
            except:
                name = item.get_text()

            name = name.replace("Dr.", "")
            name = name.replace("Prof.", "")
            name = name.replace("-Ing.", "")
            name = name.replace("Ing.", "")
            name = name.replace("-ing.", "")
            name = name.replace("habil.", "")
            name = name.replace("nat.", "")
            name = name.replace("M.Sc.", "")
            name = name.replace("Dipl.", "")
            name = name.replace("-Math.", "")
            name = name.replace("-Inf.", "")
            name = name.replace("-INF.", "")
            name = name.replace("(Sekretariat)", "")
            name = name.replace("MBA", "")
            name = name.replace("(FH)", "")
            name = name.replace("Previous visitors", "")
            name = name.replace("alexander.auer@...", "")
            name = name.replace("Co-WorkerRoomTelephone+49 371 531...E-Mail (.tu-chemnitz.de)", "")



            name = name.lstrip()
            name = name.strip()

            # old version of normalizing text

            '''index = name.find('Dr.')
            if index != -1:
                name = name[index + 4:]

            index = name.find('Ing.')
            if index != -1:
                name = name[index + 5:]

            index = name.find('habil.')
            if index != -1:
                name = name[index + 7:]

            index = name.find('nat.')
            if index != -1:
                name = name[index + 5:]

            index = name.find('M.Sc.')
            if index != -1:
                name = name[index + 6:]'''


            name = name.replace("\t", "").replace("\r", "").replace("\n", "")
            # print(professorship)
            # name = '_'.join(name.split(' '))
            # professorship[pro_id] = '_'.join(professorship[pro_id].split(' '))
            nameAndFaculty = name + '&' + pro_name[pro_id] + '&' + faculty_name
            if nameAndFaculty not in name_list:
                name_list.append(nameAndFaculty)

        pro_id += 1

    return name_list

print(getNameFromNSCDept())