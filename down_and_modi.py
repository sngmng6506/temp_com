# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 20:41:30 2022

@author: sngmn
"""
import pytube
import os
import pafy

def mp4_download(url):
    yt = pytube.YouTube(url)
    t = yt.streams.filter(only_audio=True) 
    t[1].download() #t[4]가 webm , 160kbps로 가장 품질좋음  , t[1]은 120kbps이지만 mp4
    return 0 

def webmto3(file_name):
    name = list(file_name)
    while "/" in name:               #파일이름에 "/"가 있다면 빼야하는듯
        name.remove("/")
    rev_name = "".join(name)
    os.rename(rev_name+".webm",rev_name+".mp3") ## 음질손실큰지확인 ##.webm 이므로 -5 index
    return 0

def mp4to3(file_name):
    name = list(file_name)
    while "/" in name:
        name.remove("/")
    rev_name = "".join(name)
    os.rename(rev_name+".mp4",rev_name+".mp3")
    return 0

def get_name(url):
    video = pafy.new(url)
    title = video.__dict__['_title']
    return title

def get_duration(url):
    video = pafy.new(url)
    duration = video.duration
    return duration 

def get_category(url):
    video = pafy.new(url)
    category = video.category
    return category #"Music"으로 나옴 




url = "https://www.youtube.com/watch?v=5dvYeXT6O0o"
#get_duration(url)
mp4_download(url)
#mp4to3(get_name(url))


    
    
    