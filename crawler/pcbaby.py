# coding=utf-8

import os
import urllib
import random
import json
from bs4 import BeautifulSoup

from crawler import Downloader, Helper
from base import Base


class PCbaby(Base):
    def __init__(self, debug=False):
        super(PCbaby, self).__init__('pcbaby', debug)
        self.score = 0

    def get_url(self, name):
        uname = unicode(name, 'utf-8')
        family_name = urllib.quote(uname[0].encode('utf-8'))
        first_name = urllib.quote(uname[1:].encode('utf-8'))
        gender = 1  # 0 girl, 1 boy
        base_url = 'http://my.pcbaby.com.cn'
        target = """{host}/intf/forCMS/getIntitleScoreJson.jsp?sex={gender}&xing={xing}\
&callback=testName&name={ming}&time={randtime}&req_enc=utf-8""".format(host=base_url,
            xing=family_name, ming=first_name, gender=gender, randtime=random.random())
        referer = '{host}/tools/nametest/?n={xing}&{ming}&{gender}'.format(
                  host=base_url, xing=family_name, ming=first_name, gender=gender)
        return [target, referer]

    def search(self, word):
        if len(word) < 2:
            return self
        filename = self.get_filename(word)
        if self.debug and os.path.exists(filename):
            data = Helper.fetch_raw_data(filename)
            soup = BeautifulSoup(data, 'html.parser')
        else:
            url, ref = self.get_url(word)
            hdrs = {
                'Host': 'm.pcbaby.com.cn',
                'Referer': ref,
            }
            d = Downloader(url, 3, 3)
            res = d.get(headers=hdrs)
            soup = BeautifulSoup(res.text, 'html.parser')
            Helper.store_raw_data(soup.prettify(), filename)

        # testName({"ids":100,"scores":[{"id":13,"content":"xxxx","score":"66"}]})
        try:
            body = soup.string.strip()[9:-1]
            d = json.loads(body)
            self.score = int(d['scores'][0]['score'])
        except Exception as e:
            print(u'raw body: {}, find score err: {}'.format(soup.string, e.message))

        return self

    def nums(self):
        return self.score


if __name__ == '__main__':
    print(PCbaby().search('何中天').nums())
