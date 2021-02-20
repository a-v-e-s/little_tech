"""
btos_cnat_raed_tihs.py:
A big mddile fnegir to the aoimglrtihc cohnsiresp of txet
"""


import random, re


def parser(string):
    # here is our regular expression:
    patt = re.compile(r'\b[A-Za-z]{4,}\b')
    # find the matches, build the new string
    new_string = ''
    for word in string.split():
        # hyphenated words:
        if '-' in word:
            parts = word.split('-')
            for part in parts:
                if re.fullmatch(patt, part):
                    new_part = scrambler(part)
                    if not part is parts[-1]:
                        new_string += ''.join(new_part) + '-'
                    else:
                        new_string += ''.join(new_part) + ' '
                else:
                    new_string += part + ' '
            continue
        # otherwise...
        if re.fullmatch(patt, word):
            new_word = scrambler(word)
            new_string += ''.join(new_word) + ' '
        else:
            new_string += word + ' '
    # take off the last space and return it:
    new_string.rstrip(' ')
    return new_string


def scrambler(word):
    # beginning and end of the word in a list:
    to_fill = [word[:1], word[-1:]]
    # all the other letters in another list:
    to_b_scrambled = list(word[1:-1])
    while len(to_b_scrambled):
        # pick a middle letter at random,
        # place it in the to_fill list,
        # then remove it:
        choice = random.choice(to_b_scrambled)
        tmp = to_fill[:-1]
        tmp.append(choice)
        tmp.append(str(to_fill[-1:][0]))
        to_fill = tmp
        to_b_scrambled.remove(choice)
    new_word = ''.join(to_fill)
    # if it's the same we have to retry:
    if new_word == word:
        return scrambler(word)
    else:
        return new_word


def obfuscate(_input):
    _input = str(_input)
    return parser(_input)


if __name__ == '__main__':

    code = 99
    try:

        from kivy.app import App
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.textinput import TextInput
        from kivy.uix.button import Button
        import sys

    except ImportError:

        try:
            print(parser(sys.argv[1]))
            code = 1
        except IndexError:
            print('Enter your input in double quotes ("") after the module name!')
            code = 2

    else:

        class Gui(BoxLayout):

            def __init__(self, **kwargs):
                super().__init__(**kwargs)

                self.minimum_height = 300
                self.minimum_width = 200
                self.orientation = 'vertical'
                self.padding = [0, 0, 0, 0]
                self.spacing = 2

                self._input = Input()
                self.add_widget(self._input)
                self.button = BigRed()
                self.add_widget(self.button)
                self.output = Output()
                self.add_widget(self.output)

                self.button.bind(on_press=self.obfuscate(self._input))

            def obfuscate(self, _input):
                _input = str(_input)
                self.output.text = parser(_input)


        class Input(TextInput):

            def __init__(self, **kwargs):
                super().__init__(**kwargs)

                self.background_color = [0,0,8,1]
                self.foreground_color = [ 0.9, 0.9, 0.9, 1 ]
                self.cursor_color = [ 0.9, 0.9, 0.9, 1 ]
                self.font = 'fonts/LiberationMono-Bold.ttf'


        class BigRed(Button):

            def __init__(self, **kwargs):
                super().__init__(**kwargs)

                self.text = 'Obfuscate!'


        class Output(TextInput):

            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.back_ground_color = [0, 0, 0, 1]
                self.foreground_color = [0, 0.9, 0, 1]
                self.cursor_color = [0, 0.9, 0, 1]
                self.font = 'fonts/LiberationMono-Bold.ttf'


        class Obfuscator(App):

            def build(self):
                return Gui()

        try:
            Obfuscator().run()
        except Exception:
            code = 3
            print(sys.exc_info())
        else:
            code = 0

    finally:
        if code:
            print(sys.exc_info())
        exit(code)
