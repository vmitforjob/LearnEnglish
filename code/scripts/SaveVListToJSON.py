import json

from code.data.VList import VList
from code.data.VLists import VLists

class SaveVListToJSON:
    def saveVListToJSON(self, vList: VList = VList()):
        with open(f'../../source/listsData.json', 'r') as outfile:
            loadVLists = self.loadVListsFromJSON()
            loadVLists.vLists.append(vList)
            loadVLists.vLists.reverse()

        with open(f'../../source/listsData.json', 'w', encoding='utf-8') as outfile:
            outfile.write(loadVLists.to_json(indent=4, ensure_ascii=False))

    def loadVListsFromJSON(self):
        with open(f'../../source/listsData.json', 'r') as outfile:
            vLists = VLists()
            if outfile.read():
                outfile.seek(0)
                vListsFromFile = vLists.from_json(json.dumps(json.load(outfile)))
                for l in vListsFromFile.vLists:
                    vLists.vLists.append(l)
        return vLists
