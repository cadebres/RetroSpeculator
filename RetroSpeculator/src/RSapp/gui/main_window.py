import tkinter as tk
from tkinter import *
import pygame
import os
import subprocess


class MainWindow(tk.Tk):
    def __init__(self, config_data):
        super().__init__()

        self.title("RetroSpeculator")
        self.configure(bg=config_data["background_color"])
        self.attributes("-fullscreen", True)

        self.config_data = config_data

        pygame.init()
        pygame.joystick.init()

        self.joystick = None
        self.connect_controller()

        self.last_hat = (0, 0)
        self.last_axis = 0
        self.last_button_state = 0

        self.protocol("WM_DELETE_WINDOW", self.close_app)

        top_bar = Frame(
            self,
            bg=config_data["bar_color"],
            height=120
        )
        top_bar.pack(side=TOP, fill=X)
        top_bar.pack_propagate(False)

        bottom_bar = Frame(
            self,
            bg=config_data["bar_color"],
            height=60
        )
        bottom_bar.pack(side=BOTTOM, fill=X)
        bottom_bar.pack_propagate(False)

        title_label = Label(
            top_bar,
            text="RetroSpeculator",
            bg=config_data["bar_color"],
            fg=config_data["text_color"],
            font=("Arial", max(32, self.winfo_screenwidth() // 24))
        )
        title_label.pack(side=LEFT, padx=25)

        version_label = Label(
            bottom_bar,
            text="Version 1.0",
            bg=config_data["bar_color"],
            fg=config_data["text_color"],
            font=("Arial", max(14, self.winfo_screenheight() // 70))
        )
        version_label.pack(side=RIGHT, padx=20)

        content = Frame(
            self,
            bg=config_data["background_color"]
        )
        content.pack(fill=BOTH, expand=True, padx=80, pady=40)

        self.buttons = []
        self.focus_index = 0

        button_font_size = max(22, self.winfo_screenwidth() // 65)

        for file in config_data["files"]:
            button = Button(
                content,
                text=file["name"],
                command=lambda path=file["path"]: self.launch_emulator(path),
                anchor="w",
                justify=LEFT,
                font=("Arial", button_font_size),
                padx=30,
                pady=20,
                bg=config_data["bar_color"],
                fg=config_data["text_color"],
                activebackground=config_data["text_color"],
                activeforeground=config_data["bar_color"],
                relief=FLAT,
                borderwidth=0,
                highlightthickness=0
            )

            button.pack(fill=X, pady=8)

            self.buttons.append(button)

        exit_button = Button(
            content,
            text="Exit",
            command=self.close_app,
            anchor="w",
            justify=LEFT,
            font=("Arial", button_font_size),
            padx=30,
            pady=20,
            bg=config_data["bar_color"],
            fg=config_data["text_color"],
            activebackground=config_data["text_color"],
            activeforeground=config_data["bar_color"],
            relief=FLAT,
            borderwidth=0,
            highlightthickness=0
        )

        exit_button.pack(fill=X, pady=8)

        self.buttons.append(exit_button)

        self.update_button_focus()

        self.bind("<Escape>", self.exit_fullscreen)
        self.bind("<Down>", self.move_down)
        self.bind("<Up>", self.move_up)
        self.bind("<Return>", self.press_selected)

        self.check_controller()

    def connect_controller(self):
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
        else:
            self.joystick = None

    def update_button_focus(self):
        for i, button in enumerate(self.buttons):
            if i == self.focus_index:
                button.configure(
                    bg=self.config_data["text_color"],
                    fg=self.config_data["bar_color"]
                )
            else:
                button.configure(
                    bg=self.config_data["bar_color"],
                    fg=self.config_data["text_color"]
                )

    def move_down(self, event=None):
        self.focus_index = (self.focus_index + 1) % len(self.buttons)

        self.buttons[self.focus_index].focus_set()
        self.update_button_focus()

    def move_up(self, event=None):
        self.focus_index = (self.focus_index - 1) % len(self.buttons)

        self.buttons[self.focus_index].focus_set()
        self.update_button_focus()

    def press_selected(self, event=None):
        self.buttons[self.focus_index].invoke()

    def check_controller(self):
        pygame.event.pump()

        if not self.joystick:
            self.connect_controller()

        if self.joystick:
            hat = self.joystick.get_hat(0)

            if hat != self.last_hat:
                if hat[1] == 1:
                    self.move_up()

                elif hat[1] == -1:
                    self.move_down()

            self.last_hat = hat

            axis = self.joystick.get_axis(1)

            if axis < -0.7 and self.last_axis >= -0.7:
                self.move_up()

            elif axis > 0.7 and self.last_axis <= 0.7:
                self.move_down()

            self.last_axis = axis

            button_state = self.joystick.get_button(0)

            if button_state and not self.last_button_state:
                self.press_selected()

            self.last_button_state = button_state

        self.after(100, self.check_controller)

    # def launch_emulator(self, path):
    #     if os.path.exists(path):
    #         os.startfile(path)

    def launch_emulator(self, path):
        if os.path.exists(path):

            self.withdraw()

            process = subprocess.Popen(path)

            process.wait()

            self.deiconify()

            self.attributes("-fullscreen", True)

            self.focus_force()

    def exit_fullscreen(self, event=None):
        self.attributes("-fullscreen", False)

    def close_app(self):
        pygame.quit()
        self.destroy()