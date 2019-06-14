import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter.messagebox as msg
import configparser as cp
import ntpath
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
from scipy.fftpack import fft
from scipy.io import wavfile as wav
from matplotlib.pyplot import figure

class IniEditor(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("KemFala")
        self.geometry("1200x300")
        self.resizable(False, False)

        self.active_ini = ""
        self.active_ini_filename = ""
        self.ini_elements = {}

        self.section_add_button_left = tk.Button(self,compound=TOP, text="Selecione", command=self.file_open)
        self.section_add_button_left.pack(pady=(0,0), side=LEFT)

        self.left_frame = tk.Frame(self, width=600, bg="grey")
        self.left_frame.pack_propagate(0)


        self.section_add_button_right = tk.Button(self,compound=TOP, text="Selecione", command=self.file_open2)
        self.section_add_button_right.pack(pady=(0,0), side=RIGHT)

        # self.right_frame = tk.Frame(self, width=600, bg="lightgrey")
        # self.right_frame.pack_propagate(0)



        self.file_name_var = tk.StringVar(self)
        self.file_name_label = tk.Label(self, text="Selecione os audios a serem comparados:", fg="black", bg="white", font=(None, 12))
        self.file_name_label.pack(side=tk.TOP, expand=1, fill=tk.X, anchor="n")

      #   self.section_select = tk.Listbox(self.left_frame, selectmode=tk.SINGLE)
      #   self.section_select.configure(exportselection=False)
      #   self.section_select.pack(expand=1)
      #   self.section_select.bind("<<ListboxSelect>>", self.display_section_contents)
        # self.imgpath = "1.png"
        self.img = ImageTk.PhotoImage(Image.open("white.png"),size=50)
        self.panel = Label(self, image = self.img)
        self.panel.pack(side = "left", fill = "both", expand = "yes")
        
        self.img2 = ImageTk.PhotoImage(Image.open("white.png"),size="40x20")
        self.panel2 = Label(self, image = self.img2)
        self.panel2.pack(side = "right", fill = "both", expand = "yes")

        self.section_add_button = tk.Button(self,compound=TOP, text="Comparar", command=self.comparar)
        self.section_add_button.pack(pady=(0,0), side=BOTTOM)

        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        

    def comparar(self):
        if(np.array_equal(self.yf1, self.yf2)):
            self.left_frame.config(bg="green")
        else:
            self.left_frame.config(bg="red")
        return

    def frame_height(self, event=None):
        new_height = self.winfo_height()
        self.right_frame.configure(height=new_height)

    def file_open(self, event=None):
        self.left_frame.config(bg="grey")
        ini_file = filedialog.askopenfilename(filetypes=[("Configuration file", "*.wav")])
        if ini_file:
            N = 600
            T = 1.0 / 800.0
            x = np.linspace(0.0, N*T, N)
            y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
            rate, data = wav.read(ini_file)
            a = data.T[0]
            self.fft_out1 = fft(a)
            self.yf1 = scipy.fftpack.fft(a)
            xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
            fig, ax = plt.subplots()
            fig.set_size_inches(4.5, 2.5)
            ax.plot(xf, 2.0/N * np.abs(self.yf1[:N//2]))
            plt.savefig('1.png')
            self.update_img('1.png', 1)
    
    def file_open2(self, event=None):
        ini_file = filedialog.askopenfilename(filetypes=[("Configuration file", "*.wav")])
        if ini_file:
            N = 600
            T = 1.0 / 800.0
            x = np.linspace(0.0, N*T, N)
            y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
            rate, data = wav.read(ini_file)
            a = data.T[0]
            self.fft_out2 = fft(a)
            self.yf2 = scipy.fftpack.fft(a)
            xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
            fig, ax = plt.subplots()
            fig.set_size_inches(4.5, 2.5)
            ax.plot(xf, 2.0/N * np.abs(self.yf2[:N//2]))
            plt.savefig('2.png')
            self.update_img('2.png', 2)
    
    def update_img(self, ini_file, aux):
        if aux == 1:
            self.auximg = ImageTk.PhotoImage(Image.open(ini_file))
            self.panel.config(image = self.auximg)
            self.panel.pack(side = "left", fill = "both", expand = "yes")
        else:
            self.auximg2 = ImageTk.PhotoImage(Image.open(ini_file))
            self.panel2.config(image = self.auximg2)
            self.panel2.pack(side = "right", fill = "both", expand = "yes")    



if __name__ == "__main__":
    ini_editor = IniEditor()
    ini_editor.mainloop()