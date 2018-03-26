# -*- coding: utf-8 -*-
import requests
from urllib.parse import quote
import json


class DEtoENTranslator:
    translator_url = "https://d2.duolingo.com/api/1/dictionary/hints/de/en?"

    def _generate_tokens_param(self, words):
        params = '["' + '","'.join(words) + '"]'
        return "tokens=" + quote(params)

    def _parse_translate_results_into_english_words_list(self, content):
        return json.loads(str(content, "utf-8"))

    def _build_de_en_translate_url(self, words):
        return self.translator_url + self._generate_tokens_param(words)

    def chunks(self, l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def german_word_list_to_english(self, words):
        eng_meanings = {}
 
        for c in list(self.chunks(words, 200)):
            de_en_url = self._build_de_en_translate_url(c)
            r = requests.get(de_en_url)
            if r.status_code == 200:
                eng_meanings.update(self._parse_translate_results_into_english_words_list(r.content))
            else:
                print("some error")

        return eng_meanings


# local test
if __name__ == "__main__":
    s = DEtoENTranslator()
    print(s.german_word_list_to_english(['guten', 'abend']))
