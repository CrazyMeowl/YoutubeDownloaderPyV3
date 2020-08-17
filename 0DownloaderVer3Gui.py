from tkinter import *
import os
#root of the window
root = Tk()
root.title('YoutubeDownloader3.0 by Cú')

#Create a lable widget
Credit = Label(root, text="YouTube Downloader -= Written By Meowl")#.grid(row = 0,column = 0)
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
def audio(form):
	formtext = Label(root, text="Audio Selected")
	formtext.grid(row = VidandAudRow + 1,column = 3)
	form.append(0)
def StartDownload(form):
	i = len(form)-1
	#print(form[i])
	LN = LNTextBox.get()
	N =  Numtextbox.get()
	if len(LN) == 0 :
		WarningLN = Label(root, text="Warning: You haven't enter the link or name box!!")
		WarningLN.grid(row = 6, column = 0)
	else:							   #Warning: You haven't enter the link or name box!!
		Clearspace4 = Label(root, text="                                                                                                  ")
		Clearspace4.grid(row = 6,column = 0)
		try:
			NN = int(N)
			Clearspace5 = Label(root, text="												")
			Clearspace5.grid(row = 7,column = 0)
			#start if no alert
			Status = Label(root, text="-=-=-=-=- Processing -=-=-=-=-")
			Status.grid(row = 6, column = 0)
			Vs = "--playlist-end NNNNN "
			search = 'youtube-dl -i '
			#check if vid
			if form[i] == 1 :
				#search = search + "--download-archive DownloadList.txt " + Vs + "--recode-video mp4 " + '"ytsearchNNNNN:LN"'
				search = search + "--download-archive 0DownloadList.txt " + Vs + '"ytsearchNNNNN:LN"'
			else:
				search = search + "--download-archive 0DownloadList.txt " + Vs + "--extract-audio --audio-format mp3 "  + '"ytsearchNNNNN:LN"'
			#Check for Link
			if ".com" in LN and "playlist?list" in LN:
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
			run = os.system(search)
			print(run)
			#print(search)
			print('-=-=-=-=- D O N E -=-=-=-=-')
			Status = Label(root, text="-=-=-=-=- D O N E -=-=-=-=-")
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