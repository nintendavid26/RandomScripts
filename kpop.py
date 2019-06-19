import webbrowser
import requests
import bs4
import youtube_dl

fo = open("songs.txt","r")
already_downloaded = fo.readlines()
fo.close()



res = requests.get('https://old.reddit.com/r/kpop/',headers = {'User-agent': 'your bot 0.1'})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features="html.parser")
mvs = soup.select('span[title="[MV]"]')
mvs += soup.select('span[title="[Audio]"]')

f=open("songs.txt", "a+")
for mv in mvs:
    url = mv.parent.parent.parent.parent.attrs['data-url']
    if url not in already_downloaded:
        already_downloaded.append(url)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        f.write(url+"\r\n")
f.close()