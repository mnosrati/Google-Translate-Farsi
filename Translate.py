from selenium import webdriver
import numpy
import string
import time

class Translate:
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome("./driver/chromedriver", chrome_options=options)
    driver.set_page_load_timeout(-1)

    Farsi = []
    Farsi_POS = []
    English_DEF = []
    English_EXM = []
    English_POS = []
    Example = []
    Synonym = ""


    page="https://translate.google.com/#view=home&op=translate&sl=en&tl=fa&text="
    divs="gt-cd-c"

    def translate(self,word):

        self.Farsi = []
        self.Farsi_POS = []
        self.English_DEF = []
        self.English_EXM = []
        self.English_POS = []
        self.Example = []
        self.Synonym = ""


        self.driver.get(self.page + word)


        contents = self.driver.find_elements_by_class_name(self.divs)
        fa=contents[0].text.splitlines()
        en=contents[1].get_attribute('innerHTML')
        ex=contents[2].get_attribute('innerHTML')
        sy=contents[3].text


        #Get Farsi window
        #------------------------------------------------------------
        translation=""
        newFlag=0
        for i in range(0,len(fa)):
            tmpStr=fa[i]

            if(tmpStr[0].isupper() and tmpStr != 'Frequency'):
                self.Farsi_POS.append(tmpStr)
                newFlag=1
            else:
                if(self.isEnglish(tmpStr)==False):
                    if(newFlag==1):
                        if(translation!=""):
                            self.Farsi.append(translation)
                        translation = tmpStr
                        newFlag=0
                    else:
                        translation = translation + "؛ " + tmpStr
        if(translation!=""):
            self.Farsi.append(translation)



        #Get English window
        #------------------------------------------------------------
        self.driver.get("data:text/html;charset=utf-8,{en}".format(en=en))
        poses=self.driver.find_elements_by_class_name("gt-cd-pos")
        for pos in poses:
            self.English_POS.append(pos.text)

        def_list=self.driver.find_elements_by_class_name("gt-def-list")

        for i in range(0,len(def_list)):
            def_lines=def_list[i].text.splitlines()
            for j in range(0,len(def_lines)):
                if(def_lines[j].isdigit()):
                    self.English_DEF.append(def_lines[j+1])
                    try:
                        self.English_EXM.append(def_lines[j+2])
                    except IndexError:
                        self.English_EXM.append("(no example)")




        #Get English examples
        #------------------------------------------------------------
        self.driver.get("data:text/html;charset=utf-8,{ex}".format(ex=ex))
        exmps=self.driver.find_elements_by_class_name("gt-ex-top")

        for exmp in exmps:
            self.Example.append(exmp.text)




        #Get Synonyms
        #------------------------------------------------------------
        self.Synonym=sy




    def isEnglish(self,s):
        try:
            s.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return False
        else:
            return True

        '''
        self.driver.get("data:text/html;charset=utf-8,{fa}".format(fa=fa))
        ss=self.driver.find_elements_by_class_name("gt-cd-pos")
        for item in ss:
            print(item.text)




        '''
    def close(self):
        self.driver.quit()
