from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil


#Functions
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another File...')



screen = Tk()
width = screen.winfo_screenwidth()
height = screen.winfo_screenheight()

title = screen.title('Youtube Download')
canvas = Canvas(screen, width=width, height=height)
canvas.configure(bg='#b8b8d1')
canvas.pack()

#image logo
logo_img = PhotoImage(file='yt_img.png')
#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image((width/2), 80, image=logo_img)

#link field
link_field = Entry(screen, width=40, font=('sans-serif', 15), )
link_label = Label(screen, text="Enter Download Link: ", font=('sans-serif', 15), bg='#b8b8d1')

#Select Path for saving the file
path_label = Label(screen, text="Select Path For Download", font=('sans-serif', 15), bg='#b8b8d1')
select_btn =  Button(screen, text="Select Path", bg='#5b5f97', padx='22', pady='5',font=('sans-serif', 15), fg='black', border=0, command=select_path)
#Add to window
canvas.create_window((width/2), 280, window=path_label)
canvas.create_window((width/2), 330, window=select_btn)

#Add widgets to window 
canvas.create_window((width/2), 170, window=link_label)
canvas.create_window((width/2), 220, window=link_field)

#Download btns
download_btn = Button(screen, text="Download File",bg='#ffc145', padx='22', pady='5',font=('sans-serif', 15), fg='black', border=0, command=download_file)
#add to canvas
canvas.create_window((width/2), 390, window=download_btn)

screen.mainloop()