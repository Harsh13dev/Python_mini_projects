from pytube import YouTube

link = input("Enter the link of the video: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Channel name: ", yt.author)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('D:\Yt video download')