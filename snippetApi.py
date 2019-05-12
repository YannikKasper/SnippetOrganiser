import requests
import json
langTrans = {
    "bas": "VBA",
    "py": "Python"
}


def snippetAPI():
    snippetObject = {}
    r = requests.get("https://gitlab.com//api/v4/snippets",
                     headers={"PRIVATE-TOKEN": "P9EQ9LPGkbNHyi6bK6jx"})
    allSnippets = json.loads(r.text)
    # print(allSnippets)
    allSnippetsNames = {x["id"]: x["title"] for x in allSnippets}
    allSnippetsIDs = [x["id"] for x in allSnippets]
    allSnippetsEndings = []

    for snippet in allSnippets:
        folder = snippet["description"].split("\n")[0].split("\r")[0]
        language = langTrans[snippet["file_name"].split(".")[-1]]
        if language not in snippetObject.keys():
            snippetObject[language] = {}
        if folder not in snippetObject[language].keys():
            snippetObject[language][folder] = {}
        #handle dublicates
        snippetObject[language][folder][snippet["title"]] = snippet["id"]
    print(snippetObject)
    return snippetObject


def postSnippet(title, file_name, folder, description, content):
    r = requests.post("https://gitlab.com//api/v4/snippets/", json={"title": title, "file_name": file_name, "content": content, "description": folder+"\n"+description, "visibility": "internal"},
                        headers={"PRIVATE-TOKEN": "P9EQ9LPGkbNHyi6bK6jx"})

def updateSnippet(id,title, file_name, folder, description, content):
    r = requests.put("https://gitlab.com//api/v4/snippets/"+id,
                        json={"title": title, "file_name": file_name, "content": content, "description": folder+"\n"+description, "visibility": "internal"},
                        headers={"PRIVATE-TOKEN": "P9EQ9LPGkbNHyi6bK6jx"})

def deleteSnippet(id):
    r = requests.delete("https://gitlab.com//api/v4/snippets/"+str(id),
                        headers={"PRIVATE-TOKEN": "P9EQ9LPGkbNHyi6bK6jx"})

def singleSnippetApi(id):
    r = requests.get("https://gitlab.com//api/v4/snippets/" + str(id) + "/raw",
                        headers={"PRIVATE-TOKEN": "P9EQ9LPGkbNHyi6bK6jx"})
    return r.text

def singleSnippetMeta(id):
    r = requests.get("https://gitlab.com//api/v4/snippets/" + str(id),
                        headers={"PRIVATE-TOKEN": "P9EQ9LPGkbNHyi6bK6jx"})
    return r.text