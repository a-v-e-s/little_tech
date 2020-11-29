#!/usr/bin/env python3

"""
gui.py 
the graphical frontend, obviously.
"""

import btos_cnat_raed_tihs
import functools
import tkinter as tk


class Gui:
    def __init__(self):
        root = tk.Tk()
        root.title('btos_cnat_raed_tihs!')
        #root.iconbitmap(r'btos_cnat_raed_tihs!')
    
        tk.Label(root, text='Enter the string to be scrambled here:').grid(row=1, column=1)
    
        # the output text widget has to be defined here
        _input = tk.Text(root, bg='white', width=80, height=24)
        _input.grid(row=2, column=1)
        _output = tk.Text(root, bg='white', width=80, height=24)
        _output.grid(row=2, column=3)

        # I know it's ugly but we have to define a lambda function
        # so we can send arguments to the command function:
        scram = tk.Button(
            root,
            text='Scramble it!',
            command=(
                lambda x=_output:
                    x.replace('1.0', 'end', btos_cnat_raed_tihs.parser(
                        _input.get('1.0', 'end')
                    )
                )
            )
        )
        scram.grid(row=2, column=2)

        tk.Label(root, text='Output:').grid(row=1, column=3)

        """ the return key will do the same thing as the scramble button:
        root.bind(
            sequence='<Return>',
            func=functools.partial(
                _output.insert,
                '1.0',
                btos_cnat_raed_tihs.parser(
                        _input.get('1.0', 'end')
                )
            )
        )
        """

        # run it!
        root.mainloop()


if __name__ == '__main__':
    gui = Gui
    gui()