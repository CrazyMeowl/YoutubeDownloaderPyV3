from tkinter import *
import os

#function to change the link of playlist written by Meowl
def convertlink(link1):
	if "?list" in link1:
		s = link1.find("?list")
		s = s + 6
	elif "&list" in link1:
		s = link1.find("&list")
		s = s + 6
	if "&index" in link1:
		e = link1.find("&index")
	elif "&t" in link1:
		e = link1.find("&t")
	else:
		e = len(link1)
	link2 = "https://www.youtube.com/playlist?list="+link1[s:e]
	return link2

#root of the window
root = Tk()
root.title('YoutubeDownloader 3.2 by Cú')

#Create a lable widget
Credit = Label(root, text="YouTube Downloader -=- Written By Meowl")#.grid(row = 0,column = 0)
LNintructrion = Label(root, text="Enter video name or paste your link")
Numintruction = Label(root, text="Enter the number of video (playlist)")
Clearspace1 = Label(root, text="	")
Clearspace2 = Label(root, text="	")
Clearspace3 = Label(root, text="	")
Format = Label(root, text="Format: ")
##shoving it onto the screen
Credit.grid(row = 0,column = 0)
LNintructrion.grid(row = 2,column = 0)
Numintruction.grid(row = 4,column = 0)
Clearspace1.grid(row = 1,column = 0)
Clearspace2.grid(row = 0,column = 1)
Clearspace3.grid(row = 6,column = 0)
Format.grid(row = 3,column = 2)
#LinkOrNameTextBox
LNTextBox = Entry(root,width = 50, borderwidth = 4)
LNTextBox.grid(row = 3,column = 0)
Numtextbox = Entry(root,width = 50, borderwidth = 4)
Numtextbox.grid(row = 5,column = 0)
Numtextbox.insert(0,"1")



VidandAudRow = 2;
form = [0]
#function to do when click button
def video(form):
	formtext = Label(root, text="Video Selected")
	formtext.grid(row = VidandAudRow + 1,column = 3)
	form.append(1)
	#form2 = 1
	#print(form2)
def audio(form):
	formtext = Label(root, text="Audio Selected")
	formtext.grid(row = VidandAudRow + 1,column = 3)
	form.append(0)
	#form2 = 0
	#print(form2)
def StartDownload(form):
	i = len(form)-1
	#print(form[i])
	LN = LNTextBox.get()
	N =  Numtextbox.get()
	if len(LN) == 0 :
		WarningLN = Label(root, text="Warning: You haven't enter the link or name box!!")
		WarningLN.grid(row = 6, column = 0)
	else:							   #Warning: You haven't enter the link or name box!!
		Clearspace4 = Label(root, text="                                                                                       ")
		Clearspace4.grid(row = 6,column = 0)
		try:
			NN = int(N)
			Clearspace5 = Label(root, text="                                                                                ")
			Clearspace5.grid(row = 7,column = 0)
			#start if no alert
			Status = Label(root, text="-=-=-=-=- Processing -=-=-=-=-")
			Status.grid(row = 6, column = 0)
			Vs = "--playlist-end NNNNN "
			search = 'youtube-dl -i '
			outfolder = "-o Downloaded/%(title)s.%(ext)s "
			#check if vid
			if form[i] == 1 :
				#search = search + "--download-archive DownloadList.txt " + Vs + "--recode-video mp4 " + '"ytsearchNNNNN:LN"'
				#youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
				search = search + "--download-archive DownloadList.txt " + Vs + "-f bestvideo+bestaudio "  + outfolder + '"ytsearchNNNNN:LN"'
			else:
				search = search + "--download-archive DownloadList.txt " + Vs + "--extract-audio --audio-format mp3 " + outfolder + '"ytsearchNNNNN:LN"'
			#Check for Link
			if ".com" in LN and "list" in LN:
				LN = convertlink(LN)
				if "ytsearchNNNNN:LN" in search:
					search = search.replace('"ytsearchNNNNN:LN"',LN)
					#print("NNNNLN")
				else:
					search = search + LN
					#print("NNNNNLN")
			elif ".com" in LN :
				if "ytsearchNNNNN:LN" in search:
					search = search.replace('"ytsearchNNNNN:LN"',LN)
					#print("NNNNLN2")
				else:
					search = search + LN
					#print("NNNNNLN2")
				search = search.replace(Vs,"")
			else:
				search = search.replace(Vs,"")
			search = search.replace("NNNNN",N)
			search = search.replace("LN",LN)
			#print(search)
			run = os.system(search)
			print(run)
			if run == 0:
				print('-=-=-=-=- D O N E -=-=-=-=-')
				Status = Label(root, text="-=-=-=-=- D O N E -=-=-=-=-")
			else:
				print('-=-=-=-=- ERROR:1 -=-=-=-=-')
				Status = Label(root, text="-=-=-=-=- ERROR:1 -=-=-=-=-")
			Status.grid(row = 6, column = 0)
			#done if no alert
		except:
			WarningN = Label(root, text="Warning: Please enter number to number box")
			WarningN.grid(row = 7, column = 0)

#default form is audio
audio(form)
#button 
VidButton = Button(root, text="Video",width = 15, command = lambda : video(form)).grid(row = VidandAudRow,column = 2)
#VidButton.grid(row = 2,column = 0)
AudButton = Button(root, text="Audio",width = 15, command = lambda : audio(form)).grid(row = VidandAudRow,column = 3)
#myButton.grid(row = 2,column = 0)


DownloadButton = Button(root, text="Download",width = 15, command = lambda : StartDownload(form)).grid(row = 5,column = 2)
ExitButton = Button(root, text="Exit",width = 15, command = quit).grid(row = 5,column = 3)

root.mainloop()