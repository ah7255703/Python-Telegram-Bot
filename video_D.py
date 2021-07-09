import requests
from bs4 import BeautifulSoup
import validators


def Video_D(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://www.getfvid.com','Alt-Used': 'www.getfvid.com','Connection': 'keep-alive',
        'Referer': 'http://www.getfvid.com/','Upgrade-Insecure-Requests': '1','Pragma': 'no-cache','Cache-Control': 'no-cache','TE': 'Trailers',}

    # Validating The Video Url 
    valid = validators.url(url)
    if valid == True :
        isValid = True
    else:
        isValid = False
    # requesting the server to get markup response
    response = requests.post('http://www.getfvid.com/downloader', headers=headers,data={'url': url}).content
    soup = BeautifulSoup(response,'html.parser')
    # if the video Private or not 
    alert = soup.select_one('.alert')
    if alert == "None":
        ISprivate = True
    else:
        ISprivate = False
    # isavailable Video 
    if ISprivate == True or isValid == False :
        ISavailable = False
    else:
        ISavailable = True
    try:
        V_title = soup.find('input',{'type':'hidden'}).get('value')
        D_video_link = soup.select_one('.btns-download > p:nth-child(2) > a:nth-child(1)').get('href')
        D_audio_link = soup.select_one('.btns-download > p:nth-child(3) > a:nth-child(1)').get('href')
    except:
        V_title = D_audio_link = D_video_link = "Not Available"
    Video_Data = {'FbLink':url,'Private':ISprivate ,'Title':V_title,'Valid':isValid,'Available':ISavailable,'D_Links':[D_video_link,D_audio_link]}
    return Video_Data
