from pytubefix import YouTube

url="https://www.youtube.com/watch?v=qi7Fou0WTXU"

YouTube(url).streams.first().download()