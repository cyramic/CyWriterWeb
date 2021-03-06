
class Document():
    def __init__(self, xmldoc):
        self.xmldoc = xmldoc
        self.chapters = []
        self.characters = {}
        print("Initialized Document...")
        self.parseDocument()

    def parseDocument(self):
        print("I should validate against a schema...to do later")
        chapterlist = self.xmldoc.xpath("chapters/chapter")
        for c in chapterlist:
            print("Found chapter: "+str(c.attrib))
            tmpc = Chapter(c)
            self.chapters.append(tmpc)
        characterlist = self.xmldoc.xpath("characters/character")
        for c in characterlist:
            print("Found character: " + str(c.attrib))
            tmpc = Character(c)
            characters[tmpc.attrib["id"]] = tmpc

class Character():
    def __init__(self, xmldoc):
        self.firstname = ""
        self.surname = ""
        self.middlenames = []
        self.gender = ""

    def getFullName(self):
        name = self.firstname
        name += ' '.join(middlenames)
        name += " "+self.surname
        return name

class Chapter():
    def __init__(self, xmlobj):
        self.title = xmlobj.xpath("titles/title")[0].text
        self.text = xmlobj.xpath("text")[0].text