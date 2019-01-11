# download-url-parser

> When I use third party software to download episodes on film websites, I have to click each download url and it's really bothering me. 
  So it's another victory for laziness ╮(╯▽╰)╭

## Usage

```js
change YOUR_URL in run.bat
for example:
python web_parser.py https://www.dy2018.com/i/100389.html
```

outputs

```
episodes at this time: 40
ftp://g:g@tv.kaida365.com:2166/浪漫星星40.mp4
...
ftp://g:g@tv.kaida365.com:2166/浪漫星星01.mp4
```

## Requirements

lxml

```
$ pip install lxml
```

## Acknowledgments

For need of matching "ftp://" or "ed2k://" urls in html tags, some websites may have coding errors and parse errors by using etree, so use: content.decode and set errors argument as 'ignore'

## TODO

[x] expand the scope of applications
