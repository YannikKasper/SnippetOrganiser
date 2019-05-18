import requests
import json
langTrans = {
    "bas": "VBA",
    "py": "Python",
    "md": "Markdown",
    "cmd": "Batch",
    "bat": "Batch",
    "sh": "Bash",
    "lua":"Lua",
    "tex":"Latex",
    "c": "C",
    "cpp":"C++",
    "js":"JavaScript",
    "html":"HTML",
    "css":"CSS",
    "sql":"SQL"
}
key = "P9EQ9LPGkbNHyi6bK6jx"
#rle: 9-FTkPbyQTyzx_kZhoPw
#my: P9EQ9LPGkbNHyi6bK6jx
server = "gitlab.com"
#rle: git.rle.de
#my: gitlab.com


def snippetAPI():
    snippetObject = {}
    r = requests.get("https://"+ server +"/api/v4/snippets/",
                     headers={"PRIVATE-TOKEN": key})

    allSnippets = json.loads(r.text)

    allSnippetsNames = {x["id"]: x["title"] for x in allSnippets}
    allSnippetsIDs = [x["id"] for x in allSnippets]
    allSnippetsEndings = []

    for snippet in allSnippets:
        folder = snippet["description"].split("\n")[0].split("\r")[0]
        if snippet["file_name"].split(".")[-1] not in langTrans.keys():
            language = "Others"
        else:
            language = langTrans[snippet["file_name"].split(".")[-1]]
        if language not in snippetObject.keys():
            snippetObject[language] = {}
        if folder not in snippetObject[language].keys():
            snippetObject[language][folder] = {}
        if snippet["title"] not in snippetObject[language][folder].keys():
            snippetObject[language][folder][snippet["title"]]={}
        snippetObject[language][folder][snippet["title"]]["id"] = snippet["id"]
        snippetObject[language][folder][snippet["title"]]["description"] = snippet["description"]
    return snippetObject


def postSnippet(title, file_name, folder, description, content):
    r = requests.post("https://"+ server +"/api/v4/snippets/", json={"title": title, "file_name": file_name, "content": content, "description": folder+"\n"+description, "visibility": "internal"},
                        headers={"PRIVATE-TOKEN": key})

def updateSnippet(id,title, file_name, folder, description, content):
    r = requests.put("https://"+ server +"/api/v4/snippets/"+ str(id),
                        json={"title": title, "file_name": file_name, "content": content, "description": folder+"\n"+description, "visibility": "internal"},
                        headers={"PRIVATE-TOKEN": key})

def deleteSnippet(id):
    r = requests.delete("https://"+ server +"/api/v4/snippets/"+str(id),
                        headers={"PRIVATE-TOKEN": key})

def singleSnippetApi(id):
    r = requests.get("https://"+ server +"/api/v4/snippets/" + str(id) + "/raw",
                        headers={"PRIVATE-TOKEN": key})
    return r.text

def singleSnippetMeta(id):
    r = requests.get("https://"+ server +"/api/v4/snippets/" + str(id),
                        headers={"PRIVATE-TOKEN": key})

    return json.loads(r.text)

