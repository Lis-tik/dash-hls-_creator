from lxml import etree
import os
import json

class CreateMPD:
    def __init__(self):
        self.data_list = []
        self.global_path = ''
        self.tree = None

    def createMPD(self):
        queue_list = [f for f in os.listdir('./options') if f.endswith('.json')]

        for index in queue_list:
            with open(f'./options/{index}', 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.data_list.append(data)

        self.global_path = list(self.data_list[0].keys())[0]
            
        self.giveMainData()

    def XML_loader(self):
        with open("manifest.mpd", "rb") as f:
            self.tree = etree.parse(f)

        ns = {'ns': 'urn:mpeg:dash:schema:mpd:2011'}
        adaptation_sets = self.tree.xpath('//ns:AdaptationSet', namespaces=ns)

        for aset in adaptation_sets:
            print(etree.tostring(aset, pretty_print=True, encoding='unicode'))

            
    def giveMainData(self):
        work_data = self.data_list[0][self.global_path]
        for content in work_data:
            for audio in content['audio']:
                print(None)

        self.XML_loader()
                

        # adaptation_sets = tree.xpath("//AdaptationSet")
        # for i, aset in enumerate(adaptation_sets):
        #     print(f"AdaptationSet {i+1}:\n{etree.tostring(aset, pretty_print=True, encoding='unicode')}\n")

if __name__ == '__main__':
    main = CreateMPD()
    main.createMPD()


