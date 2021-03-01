from bs4 import BeautifulSoup
import requests


def MathDepartment():
    faculty_name = ""
    pro_list = ["https://www.tu-chemnitz.de/mathematik/numa/people/index.de.php",
                "https://www.tu-chemnitz.de/mathematik/stochastik/index.php",
                "https://www.tu-chemnitz.de/mathematik/wima/mit.php",
                "https://www.tu-chemnitz.de/mathematik/wire/mitarbeiter.php",
                "https://www.tu-chemnitz.de/mathematik/geometrie/index.php",
                "https://www.tu-chemnitz.de/mathematik/industrie_technik/mitarbeiter/?lang=en",
                "https://www.tu-chemnitz.de/mathematik/approximation/gruppe.en.php",
                "https://www.tu-chemnitz.de/mathematik/theoretische_mathe/mitarbeiter.php",
                "https://www.tu-chemnitz.de/mathematik/algebra/",
                "https://www.tu-chemnitz.de/mathematik/discrete/index.php",
                "https://www.tu-chemnitz.de/mathematik/analysis/team.en.php",
                "https://www.tu-chemnitz.de/mathematik/ang_analysis/team.php",
                "https://www-user.tu-chemnitz.de/~potts/mitarbeiter.php",
                "https://www.tu-chemnitz.de/mathematik/fima/contact.en.php",
                "https://www.agtz.mathematik.uni-mainz.de/arakelov-geometrie/dr-robert-wilms/",
                "https://www.tu-chemnitz.de/mathematik/harmonische_analysis/index.html.en",
                "https://www.tu-chemnitz.de/mathematik/invpde/mitarbeiter.php.en"
                ]

    pro_name = ["Professur Numerische Mathematik ","Professur Stochastik ", "Professorship of Economical Mathematics", "Professorship of Scientific Computing",
                "Professorship of Geometry", "Research group mathematics in industry and technology", "Professorship Approximation Theory ","Juniorprofessur Theoretische Mathematik ",
                "Professorship of Algebra", "Algorithmische und Diskrete Mathematik", "Professorship Analysis ", "Professorship of Applied Analysis ", "Applied Functional Analysis",
                "Mathematical Finance", "Professorship of Geometry", "Harmonic Analysis", "Professorship for inverse problems"
                ]


    name_list = []
    prof_name = []
    pro_id = 0
    while pro_id < len(pro_list):
        r = requests.get(pro_list[pro_id])
        soup = BeautifulSoup(r.text, 'html.parser')
        if pro_id == 0:
             prof_name = soup.find_all("address", class_="row vcard")
        elif pro_id == 1:
            prof_name = soup.find_all("div", class_="h4")

        if pro_id == 2 or pro_id == 3  or pro_id == 7 or pro_id == 11 or pro_id == 16:
              prof_name = soup.find_all("h4", class_="fn")
        elif pro_id == 4:
         prof_name = soup.find_all("strong", class_="fn")
        elif pro_id == 5:
            parents= soup.find_all("main", {'class':'page-content'})
            for soup_item in parents:
                prof_name = soup_item.find_all("li")
        elif pro_id == 6:
            parents = soup.find_all("main", class_="page-content")
            for soup_item in parents:
             prof_name = soup_item.find_all("b")
        elif pro_id == 8:
            parents= soup.find_all("li", {'class':'current'})
            for soup_item in parents:
                prof_name = soup_item.find_all("li")

        elif pro_id == 9:
            li = soup.find("li", class_="current")
            uls = li.find("ul")
            li2 = uls.find_all("li")
            for li3 in li2:
                a = li3.find("a")
                if a.contents[0] != "Sekretariat":
                    name_list.append(a.contents[0])

        elif pro_id == 10:
            figu = soup.find("figure", class_="tucal-vcard")
            if figu != None:
                    figcap = figu.find("figcaption")
                    div = figcap.find("div", class_="h4")
                    name_list.append(div.contents[0])
                    divM = figu.findNextSibling()
                    divList = divM.find_all("div")
                    for divItem in divList:
                        a = divItem.find("a").findNextSibling()
                        name_list.append(a.contents[0])

        elif pro_id == 12:
            mainss = soup.find("main", class_="page-content")
            uls = mainss.find_all("ul")
            for ul in uls:
                as_ = ul.find_all("a")
                for a_ in as_:
                    if a_ != None:
                        name_list.append(a_.contents[0])

        elif pro_id == 13:
            div = soup.find("div", id="tucal-pagemenu")
            ol = div.find("ol")
            li = ol.find_all("li")
            for l in li:
                a = l.find("a")
                if a and (a.text != 'Professorship' and a.text != 'for Students'):
                    name_list.append(a.text)
        elif pro_id == 14:
            lis = soup.find_all("li", class_="menueebene3off")
            for li in lis:
                    a =  li.find("a")
                    if a and (a.text != 'Lehre' and a.text != 'Arbeiten'):
                        name_list.append (a.text)

        elif pro_id == 15:
            table = soup.find("table", class_="zeile tabtop")
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
            name = name. replace("Former members", "")
            name = name.replace("Sekretariat", "")


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
            nameAndFaculty = name  +'&' + pro_name[pro_id] + '&' + faculty_name
            if nameAndFaculty not in name_list:
                name_list.append(nameAndFaculty)

        pro_id += 1

    return name_list
print(MathDepartment())