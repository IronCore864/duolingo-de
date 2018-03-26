import requests
import json
from collections import defaultdict
from de_en_translator import DEtoENTranslator


class Duolingo:
    def login(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def _get_auth_token(self):
        payload = {"identifier": self.user, "password": self.pwd}
        headers = {
            'Accept': 'application/json, text/javascript, */*',
            'q': '0.01',
            'Referer': 'https://www.duolingo.com/',
            'Origin': 'https://www.duolingo.com',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
            'charset': 'UTF-8'
        }
        r = requests.post(
            "https://www.duolingo.com/2016-04-13/login?fields=",
            json=payload,
            headers=headers
        )
        if r.status_code == 201:
            return r.cookies['auth_tkt']
        else:
            print("login error")

    def _get_vocabulary_overview(self):
        auth_token = self._get_auth_token()
        headers = {
            'Cookie': 'auth_tkt={};'.format(auth_token)
        }
        r = requests.get(
            "https://www.duolingo.com/vocabulary/overview",
            headers=headers
        )
        return (r.text)

    def _load_vocabularies(self, content):
        return json.loads(content)['vocab_overview']

    def _handle_noun_uppercase(self, word):
        if word['pos'] == 'Noun':
            word['word_string'] = word['word_string'][0].upper() + word['word_string'][1:]

    def _get_all_vocabularies(self, vocabularies):
        res = set()
        for v in vocabularies:
            self._handle_noun_uppercase(v)
            res.add(v['word_string'])
        return list(res)

    def _get_related_vocabs(self, vocab_json, processed, vocabularies):
        res = [vocab_json]

        for rid in vocab_json['related_lexemes']:
            processed.add(rid)
            for rv in vocabularies:
                if rv['lexeme_id'] == rid:
                    res.append(rv)

        return res

    def _output_vocab(self, all_related, all):
        type = all_related[0]['skill_url_title'].split(':')[0].split('-')[0]
        for v in all_related:
            all[type].append([v['word_string'], v['pos'], v['gender']])

    def _write_file(self, vocabularies, translations):
        all = defaultdict(list)

        processed = set()
        for v in vocabularies:
            if v['lexeme_id'] in processed:
                continue
            all_related_words = self._get_related_vocabs(v, processed, vocabularies)
            self._output_vocab(all_related_words, all)

        with open("output", "w") as f:
            for type, vocab_list in all.items():
                f.write(type + "\n")
                for v in vocab_list:
                    word = str(v[0])
                    pos = str(v[1]) if v[1] else ""
                    gender = str(v[2]) if v[2] else ""
                    f.write("{0: <20}{1: <15}{2: <10}\t{3}".format(word, pos, gender, translations[word]) + "\n")
                f.write("\n")

    def generate_list(self):
        overview = self._get_vocabulary_overview()
        vocabularies = self._load_vocabularies(overview)
        vocab_list = self._get_all_vocabularies(vocabularies)
        t = DEtoENTranslator()
        translations = t.german_word_list_to_english(vocab_list)
        self._write_file(vocabularies, translations)
