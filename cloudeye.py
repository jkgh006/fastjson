# -*- coding: utf-8 -*-

import random
import requests
import time
from string import ascii_lowercase

# your API-key in "http://ijiandao.info/?a=list"
key = 'input your key'

# your personal sub-domain, like: [user].ijiandao.win
uniq_domain = 'ksorvd'


class CloudEye:
    def __init__(self,randoms=None):
        self.unique = uniq_domain
        if randoms is None:
            self.random = ''.join([random.choice(ascii_lowercase) for _ in range(10)])
        else:
            self.random = randoms
        self.useragent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"

    def getRandomDomain(self, custom='poc'):
        """
        full domain = [random].[custom].[unique].ijiandao.win
        e.g. fezarvgo.poc.ee8a6f.ijiandao.win
        """
        self.custom = custom
        if self.random:
            return '%s.%s.%s.lunlun.wyzxxz.cn' % (self.random, self.custom, self.unique)
        else:
            return '%s.%s.lunlun.wyzxxz.cn' % (self.custom, self.unique)

    def getDnsRecord(self, delay=2):
        time.sleep(delay)
        if self.random:
            query = self.random + '.' + self.custom
        else:
            query = self.custom
        api_base = 'http://lunlun.wyzxxz.cn/api/{key}/{domain}/dns/'.format(key=key, domain=query)
        return requests.get(api_base,headers={"User-Agent":self.useragent}).content

    def getHttpRecord(self, delay=2):
        time.sleep(delay)
        if self.random:
            query = self.random + '.' + self.custom
        else:
            query = self.custom
        api_base = 'http://lunlun.wyzxxz.cn/api/{key}/{domain}/web/'.format(key=key, domain=query)
        return requests.get(api_base,headers={"User-Agent":self.useragent}).content

    def verifyDNS(self, delay=2):
        return 'lunlun.wyzxxz.cn' in self.getDnsRecord(delay)

    def verifyHTTP(self, delay=2):
        return 'lunlun.wyzxxz.cn' in self.getHttpRecord(delay)


def queryDnsRecord(domain, delay=2):
    time.sleep(delay)
    domain = domain.replace(uniq_domain + '.lunlun.wyzxxz.cn', '').rstrip('.')
    api_base = 'http://lunlun.wyzxxz.cn/api/{key}/{domain}/DNSLog/'.format(key=key, domain=domain)
    return requests.get(api_base).content


def queryHttpRecord(domain, delay=2):
    time.sleep(delay)
    domain = domain.replace(uniq_domain + '.lunlun.wyzxxz.cn', '').rstrip('.')
    api_base = 'http://lunlun.wyzxxz.cn/api/{key}/{domain}/ApacheLog/'.format(key=key, domain=domain)
    return requests.get(api_base).content


if __name__ == '__main__':
    c = CloudEye(randoms="")
    a = c.getRandomDomain('cdxy')
    print 'http://' + a
    try:
        requests.get('http://' + a, timeout=1)
    except Exception:
        pass
    print c.verifyDNS(delay=0)
    print c.verifyHTTP(delay=0)
    print c.getDnsRecord(delay=0)
    print c.getHttpRecord(delay=0)