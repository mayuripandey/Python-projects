


# return value should be a list, each item is a string containing name, jobTitle(professor or researcher) and professorship, seperated by '&'

from bs4 import BeautifulSoup
import requests


def getNameFromNSDept():
    faculty_name = "Natural Science"
    pro_list = ["https://www.tu-chemnitz.de/physik/AFKO/staff.html.en",
                "https://www.tu-chemnitz.de/physik/OPKM/groupmembers_opkm.php",
              "https://www.tu-chemnitz.de/physik/EXSE/mitarbeiter.html",
                "https://www.tu-chemnitz.de/physik/HLPH/teaching.html",
                "https://www.tu-chemnitz.de/physik/MAGFUN/mitarbeiter.html",
                "https://www.tu-chemnitz.de/physik/PHKP/mitarbeiter.html.en",
                "https://www.tu-chemnitz.de/physik/SNWP/mitarbeiter.html",
                "https://www.tu-chemnitz.de/physik/SFKS/mitarbeiter.html.en",
                "https://www.tu-chemnitz.de/physik/TPKDS/en/mitarbeiter.php",
                "https://www.tu-chemnitz.de/physik/TQPS/prof/team.html",
                "https://www.tu-chemnitz.de/physik/HLPH/members.php",
                "https://www.tu-chemnitz.de/physik/CPHYS/Staff/index.html",
                "https://www.tu-chemnitz.de/physik/KSND/professur/mitglieder.html.en",
                "https://www.tu-chemnitz.de/physik/THUS/de/staff.php",
              ]

    pro_name = ["Professorship of Solid Surfaces Analysis", "Professorship of Optics and Photonics of Condensed Matter, in particular Sensor Systems and Analytics",
                "Professorship of Experimental Sensor Science", "Professorship of Semiconductor Physics", "Professorship of Functional Magnetic Materials",
                "Professorship of Physics of Cognitive Processes", "Professur Simulation naturwissenschaftlicher Prozesse", "Professorship of Structure and Function of Cognitive Systems",
                "Professorship for Theoretical Physics of Complex Dynamic Systems","Professorship for Theoretical Physics of Quantum Mechanical Processes and Systems",
                "Semiconductor Physics", "Research Group: Theoretical Physics, in particular Computational Physics", "Research Group:Complex Systems and Non-linear Dynamics",
                "Research Group:Theory Unordered Systems",
               ]

    name_list = []
    prof_name = []
    pro_id = 0
    while pro_id < len(pro_list):
        r = requests.get(pro_list[pro_id])
        soup = BeautifulSoup(r.text, 'html.parser')
        if pro_id == 0 or pro_id == 1 or pro_id == 2 or pro_id == 3 or pro_id == 4 or pro_id == 5 or pro_id == 6 or pro_id == 7 or pro_id == 9 or pro_id == 12:
            prof_name = soup.find_all("div", class_="h4")
        elif pro_id == 8:
            row_list = soup.find_all("tr")
            for row in row_list:
                    if row.find("td"):
                        prof_name.append(row.find_all("td")[0])

        elif pro_id == 10:
            table = soup.find("table", class_="table-hover")
            trs = table.find_all("tr")
            for tr in trs:
                td = tr.find_all("td")
                if len(td) > 0:
                    if (td[0].find("a") != None):
                        name = td[0].find("a").text
                        name_list.append(name.replace(u"Former Group Members", " "))
        elif pro_id == 11:
            main = soup.find("main", class_="page-content")
            trs = main.find_all("tr")
            for tr in trs:
                td = tr.find_all("td")
                if len(td) > 0:
                    if (td[0].find("strong") != None):
                        name = td[0].find("strong").text
                        name_list.append(name.replace(u"\xa0", " "))

        elif pro_id == 13:
            prof_name = soup.find_all("td", class_="bold")
        if pro_id == 14:
            table = soup.find("table", class_="ohne")
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
            name = name.replace("Secretary", "")
            name = name.replace("Head", "")
            name = name.replace("Team", "")
            name = name.replace("Most group members still work at TU Ilmenau (Corona pandemic).", "")
            name = name.replace("Students", "")
            name = name.replace("These students will defend their final thesis at TU Ilmenau within the next months", "")
            name = name. replace("Former Members", "")


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

print(getNameFromNSDept())

