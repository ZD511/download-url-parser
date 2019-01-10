# coding=utf-8
import requests
import time
import argparse
from lxml import etree
requests.packages.urllib3.disable_warnings()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}


def get_ed2l(url):
	r = requests.get(url, headers=headers)
	enconding = requests.utils.get_encodings_from_content(r.text)
	#print(enconding)

	selector = etree.HTML(r.content.decode(enconding[0], errors='ignore'))
	ed2k_all = []
	ed2k_all = selector.xpath(
		'//*[contains(@href, "ed2k://") or contains(@href,"ftp://") or contains(@href, "thunder://")]/@href')  # 6vhao or dytt8 extract href attibute which has 'ed2k://' field
	ed2k_all += selector.xpath('//*[contains(@src, "btbo://") or contains(@src,"magnet:?")]/@src')  # piaohua

	file_name = time.strftime("%Y-%m-%d-%H%M%S", time.localtime())
	with open('%s.txt' % file_name, 'w', encoding='utf-8') as ff:
		ff.write('episodes at this time: %s\n' % len(ed2k_all))
		ff.write('\n'.join(ed2k_all))
	print('done')


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('url', type=str, help='get all download urls in a webpage')
	args = parser.parse_args()
	get_ed2l(args.url)

	# test args.url
	# 'https://www.dytt8.net/html/tv/hytv/20181229/57992.html'
	# 'http://www.6vhao.tv/dlz/2017-02-22/31328.html'
	# 'https://www.dytt8.net/html/tv/hytv/20181229/57992.html'

