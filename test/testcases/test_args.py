import requests
import json


def test_meme():
    url = 'https://api.imgflip.com/get_memes'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    with open('meme_imgflip.json', 'wb') as outf:
        outf.write(response.content)

    meme_list = []
    with open('meme_imgflip.json', 'r') as json_file:
        meme_data = json.loads(json_file.read())
        for u in meme_data['data']['memes']:
            meme_list.append(Meme.from_json(u))

    for meme in meme_list:
        print('id={},name={},url={}'.format(meme.id, meme.name, meme.url))

class Meme:
    def __init__(self, name, url, id):
        self.name = name
        self.url = url
        self.id = id

    @staticmethod
    def from_json(json_dict):
        return Meme(json_dict['name'],json_dict['url'],json_dict['id'])

    def __repr__(self):
        return f'<meme {self.id}>'





