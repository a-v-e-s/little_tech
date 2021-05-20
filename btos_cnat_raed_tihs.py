"""
btos_cnat_raed_tihs.py:
A big mddile fnegir to the aoimglrtihc cohnsiresp of txet
"""

import random, re
import tkinter as tk


def obfuscate(_input):
    text = str(_input)
    
    # here is our regular expression:
    patt = re.compile(r'(\b[A-Za-z]{4,}\b)')
    # a list of items split by whether they match it or not:
    items = re.split(patt, text)

    scrambled_text = ''
    for item in items:
        if re.fullmatch(patt, item):
            mid_section = list(item[1:-1])
            attempts = 0
            while attempts < 100:
                attempts += 1
                random.shuffle(mid_section)
                new_item = item[:1] + ''.join(mid_section) + item[-1:]
                if new_item != item:
                    break
            scrambled_text += new_item
        else:
            scrambled_text += item

    return scrambled_text


if __name__ == '__main__':
    root = tk.Tk()
    root.title('btos_cnat_raed_tihs!')

    tk.Label(root, text='Enter the text to be scrambled here:').grid(row=1, column=1)
    _input = tk.Text(root, bg='white', wrap='word', width=60, height=24)
    _input.grid(row=2, column=1)
    _input.focus_set()

    # the output text widget has to be defined here:
    tk.Label(root, text='Output:').grid(row=1, column=3)
    _output = tk.Text(root, bg='white', wrap='word', width=60, height=24)
    _output.grid(row=2, column=3)

    # I know it's ugly but we have to define a lambda function
    # so we can send arguments to the obfuscate function:
    scram = tk.Button(
        root,
        text='Scramble it!',
        command=(
            lambda x=_output:
                x.replace('1.0', 'end', obfuscate(
                    _input.get('1.0', 'end')
                )
            )
        )
    )
    scram.grid(row=2, column=2)

    # run it!
    root.mainloop()