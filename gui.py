import btos_cnat_raed_tihs
import tkinter as tk

class Gui:
    def __init__(self):
        root = tk.Tk()
    
        tk.Label(root, text='Enter the string to be scrambled here:').grid(row=1, column=1)
    
        _input = tk.Text(root, bg='white', width=80, height=24)
        _input.grid(row=2, column=1)
        _output = tk.Text(root, bg='white', width=80, height=24)
        _output.grid(row=5, column=1)

        scram = tk.Button(
            root, text='Scramble it!',
            command=(
                lambda x=_output: x.insert('1.0', btos_cnat_raed_tihs.parser(_input.get('1.0', 'end')))
            )
        )
        scram.grid(row=3, column=1)

        tk.Label(root, text='Output:').grid(row=4, column=1)

        root.mainloop()


if __name__ == '__main__':
    gui = Gui
    gui()