import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from extract_playlist_urls import *
from pytube import YouTube

urls = []

def switch_frame(frame):
    frame.tkraise()

# URL of the YouTube video
def download_video(urls, current_log):
    print(urls)
    for url in urls:
        video_url = url
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        current_log.insert(tk.END, f'Downloading {yt.title}...\n\n')
        root.update_idletasks()  # Update the GUI
        stream.download()
        current_log.insert(tk.END, f'{yt.title} downloaded successfully!\n\n')
        current_log.insert(tk.END, '-----------------------------------\n\n')
        root.update_idletasks()  # Update the GUI

def load_main_frame():
    extractDownload_frame.pack_forget()
    loadDownload_frame.pack_forget()
    main_frame.pack()

def browse_file():
    entry_file = tk.Entry(extractDownload_frame, width=50)
    entry_file.pack(pady=10)
    filename = filedialog.askopenfilename()
    entry_file.delete(0, tk.END)
    entry_file.insert(0, filename)
    return filename

def load_urls():
    global urls
    filename = browse_file()
    with open(filename, 'r') as f:
        urls = f.readlines()
        print(urls)

def continue_download():
    global urls
    print(urls)
    download_index = entry_download_index.get()
    download_index = int(download_index)
    download_video(urls[download_index:], ld_log_text)
    messagebox.showinfo("Success", "Videos downloaded successfully!")

def start_download():
    global urls
    download_video(urls, ed_log_text)
    messagebox.showinfo("Success", "Videos downloaded successfully!")

def load_then_download():
    main_frame.pack_forget()
    loadDownload_frame.pack()
    

def extract_then_download():
    main_frame.pack_forget()
    extractDownload_frame.pack()

def extract_playlist_urls_helper():
    global urls
    playlist_url = entry_playlist_url.get()
    try:
        urls = extract_playlist_urls(playlist_url)
        messagebox.showinfo("Success", "Playlist is found successfully!")
        btn_start_download.config(state='normal')  # Enable the button
    except:
        messagebox.showerror("Error", "Playlist not found!")
        load_main_frame()


# app configuration
root = tk.Tk()
root.title("YouTube Playlist Downloader")
root.configure(bg="darkgrey")
window_width = 400
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# main frame
main_frame = tk.Frame(root, bg="darkgrey")
main_frame.pack(fill=tk.BOTH, expand=True)

label_question = tk.Label(main_frame, text="Do you have the extracted playlist URLs already?", font=("Helvetica", 12, "bold"), bg="darkgrey")
label_question.pack(pady=10)

btn_yes = tk.Button(main_frame, text="Yes", font=("Helvetica", 10, "bold"), command=load_then_download)
btn_yes.pack(pady=10)

btn_no = tk.Button(main_frame, text="No", font=("Helvetica", 10, "bold"), command=extract_then_download)
btn_no.pack(pady=10)




# extractDownload_frame
extractDownload_frame = tk.Frame(root)

label = tk.Label(extractDownload_frame, text="Extract frame", font=("Helvetica", 12, "bold"))
label.pack(pady=10)

label_playlist_id = tk.Label(extractDownload_frame, text="Enter Playlist URL:", font=("Helvetica", 10, "bold"))
label_playlist_id.pack(pady=10)

entry_playlist_url = tk.Entry(extractDownload_frame, width=50)
entry_playlist_url.pack(pady=10)

btn_search = tk.Button(extractDownload_frame, text="Search", font=("Helvetica", 10, "bold"), command=extract_playlist_urls_helper)
btn_search.pack(pady=10)

btn_start_download = tk.Button(extractDownload_frame, text="Start Download", command=start_download, state='disabled')
btn_start_download.pack(pady=10)

ed_log_text = tk.Text(extractDownload_frame, height=10, width=50)
ed_log_text.pack(pady=10, fill=tk.BOTH, expand=True)

back_button = ttk.Button(extractDownload_frame, text="Back", command=load_main_frame)
back_button.pack(side="top", anchor="nw", padx=10, pady=10)  # Position at top-left corner

# loadDownload_frame
loadDownload_frame = tk.Frame(root)

label_choose_file = tk.Label(loadDownload_frame, text="Choose the file with the extracted URLs:", font=("Helvetica", 10, "bold"))
label_choose_file.pack(pady=10)

btn_browse = tk.Button(loadDownload_frame, text="Browse", font=("Helvetica", 10, "bold"), command=load_urls)
btn_browse.pack(pady=10)

label_download_index = tk.Label(loadDownload_frame, text="Which video you want to continue downloading from: ", font=("Helvetica", 10, "bold"))
label_download_index.pack(pady=10)

entry_download_index = tk.Entry(loadDownload_frame, width=30)
entry_download_index.pack(pady=10)

btn_start = tk.Button(loadDownload_frame, text="Continue Downloading", font=("Helvetica", 10, "bold"), command=continue_download)
btn_start.pack(pady=10)

ld_log_text = tk.Text(loadDownload_frame, height=10, width=50)
ld_log_text.pack(pady=10, fill=tk.BOTH, expand=True)

back_button = ttk.Button(loadDownload_frame, text="Back", command=load_main_frame)
back_button.pack(side="top", anchor="nw", padx=10, pady=10)  # Position at top-left corner

# Run the application
root.mainloop()
