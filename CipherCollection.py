import PySimpleGUI as sg
import Affine.Affine as aff
import Playfair.Playfair as playf
import Vigenere.V as vig
import Vigenere.V_Auto as viga
import Vigenere.V_Ext as vige
import Vigenere.V_Full as vigf

cipher_method = ['Affine','Playfair','Vigenere','Vigenere Auto-Key','Vigenere Extended','Vigenere Full']

def aff_gui():
    # need p/c, m(coprime), b(rotate)
    layout = [
        [sg.Text('Plaintext/Ciphertext :'),sg.InputText(key='text')],
        [sg.Text('m = '),sg.OptionMenu(values=[1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25],default_value=1,key='m')],
        [sg.Text('b = '),sg.OptionMenu(values=[i for i in range(1,26)],default_value=1,key='b')],
        [sg.Button('Encrypt'),sg.Button('Decrypt')],
        [sg.Multiline(size=(100,60),disabled=True,key='res')]
    ]
    window = sg.Window(title=('Affine Cipher'), layout=layout, size=(500,280), modal=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        aff_res = ''
        temp = ''.join([char for char in values['text'] if char.isalpha()])
        if len(temp)>0:
            if event == 'Encrypt':
                aff_res = aff.encrypt(values['text'],int(values['m']),int(values['b']))
            elif event == 'Decrypt':
                aff_res = aff.decrypt(values['text'],int(values['m']),int(values['b']))
        # # update gui for result
        window.Element(key='res').Update(aff_res)    

def play_gui():
    # need p/c, k
    layout = [
        [sg.Text('Plaintext/Ciphertext :'),sg.InputText(key='text')],
        [sg.Text('k : '),sg.InputText(key='key')],
        [sg.Button('Encrypt'),sg.Button('Decrypt')],
        [sg.Multiline(size=(100,60),disabled=True,key='res')]
    ]
    window = sg.Window(title=('Playfair Cipher'), layout=layout, size=(500,280), modal=True)
    while True:
        event, values = window.read()
        playf_res = ''
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        temp = ''.join([char for char in values['text'] if char.isalpha()])
        key = ''.join([char for char in values['key'] if char.isalpha()])
        if len(temp)>0 and len(key)>0:
            if event == 'Encrypt':
                playf_res = playf.encrypt(values['text'],values['key'])
            elif event == 'Decrypt':
                playf_res = playf.decrypt(values['text'],values['key'])
        # # update gui for result
        window.Element(key='res').Update(playf_res)

def vig_gui():
    # need p/c, k
    layout = [
        [sg.Text('Plaintext/Ciphertext :'),sg.InputText(key='text')],
        [sg.Text('k : '),sg.InputText(key='key')],
        [sg.Button('Encrypt'),sg.Button('Decrypt')],
        [sg.Multiline(size=(100,60),disabled=True,key='res')]
    ]
    window = sg.Window(title=('Vigenere Cipher'), layout=layout, size=(500,280), modal=True)
    while True:
        event, values = window.read()
        vig_res = ''
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        temp = ''.join([char for char in values['text'] if char.isalpha()])
        key = ''.join([char for char in values['key'] if char.isalpha()])
        if len(temp)>0 and len(key)>0:
            if event == 'Encrypt':
                vig_res = vig.encrypt(values['text'],values['key'])
            elif event == 'Decrypt':
                vig_res = vig.decrypt(values['text'],values['key'])
        # # update gui for result
        window.Element(key='res').Update(vig_res)

def vig_a_gui():
    # need p/c, k
    layout = [
        [sg.Text('Plaintext/Ciphertext :'),sg.InputText(key='text')],
        [sg.Text('k : '),sg.InputText(key='key')],
        [sg.Button('Encrypt'),sg.Button('Decrypt')],
        [sg.Multiline(size=(100,60),disabled=True,key='res')]
    ]
    window = sg.Window(title=('Vigenere Auto-Key Cipher'), layout=layout, size=(500,280), modal=True)
    while True:
        event, values = window.read()
        vig_res = ''
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        temp = ''.join([char for char in values['text'] if char.isalpha()])
        key = ''.join([char for char in values['key'] if char.isalpha()])
        if len(temp)>0 and len(key)>0:
            if event == 'Encrypt':
                vig_res = viga.encrypt(values['text'],values['key'])
            elif event == 'Decrypt':
                vig_res = viga.decrypt(values['text'],values['key'])
        # # update gui for result
        window.Element(key='res').Update(vig_res)

def vig_e_gui():
    # need in_file, out_file, k
    layout = [
        [sg.Text('Input file :'),sg.InputText(key='infile'),sg.FileBrowse()],
        [sg.Text('Output file :'),sg.InputText(key='outfile')],
        [sg.Text('k : '),sg.InputText(key='key')],
        [sg.Button('Encrypt'),sg.Button('Decrypt')],
        [sg.Text('Output file will be created in output folder.')]
    ]
    window = sg.Window(title=('Extended Vigenere Cipher'), layout=layout, size=(500,280), modal=True)
    while True:
        event, values = window.read()
        vig_res = ''
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if len(values['infile'])>0 and len(values['outfile'])>0:
            if event == 'Encrypt':
                vige.encrypt(values['infile'],values['outfile'],values['key'])
            elif event == 'Decrypt':
                vige.decrypt(values['infile'],values['outfile'],values['key'])
        # # update gui for result

def vig_f_gui():
    # need p/c, k, vig_table_file
    layout = [
        [sg.Text('Plaintext/Ciphertext :'),sg.InputText(key='text')],
        [sg.Text('k : '),sg.InputText(key='key')],
        [sg.Text('table file : '),sg.InputText(default_text='./table/VigenereFullTable.txt',disabled=True,key='table'),sg.FileBrowse()],
        [sg.Button('Generate Table'),sg.Text('Generated vigenere table can be found at ./table/')],
        [sg.Button('Encrypt'),sg.Button('Decrypt')],
        [sg.Multiline(size=(100,60),disabled=True,key='res')]
    ]
    window = sg.Window(title=('Vigenere Full Cipher'), layout=layout, size=(500,280), modal=True)
    while True:
        event, values = window.read()
        vig_res = ''
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Generate Table':
            vigf.generate_vig_table()
            window.Element('table').Update('./table/VigenereFullTable.txt')
        temp = ''.join([char for char in values['text'] if char.isalpha()])
        key = ''.join([char for char in values['key'] if char.isalpha()])
        if len(temp)>0 and len(key)>0:
            if event == 'Encrypt':
                vig_res = vigf.encrypt(values['text'],values['key'],values['table'])
            elif event == 'Decrypt':
                vig_res = vigf.decrypt(values['text'],values['key'],values['table'])
        # # update gui for result
        window.Element(key='res').Update(vig_res)

def main():
    layout = [
        [sg.Text('Pick cipher: '),sg.OptionMenu(values=cipher_method,default_value='Affine',key='option'),sg.Button('Pick')]
    ]

    window = sg.Window('Simple Cipher Collection', layout=layout, size=(350,50))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        print(event,values)
        if event=='Pick':
            if values['option'] == 'Affine':
                aff_gui()
            elif values['option'] == 'Playfair':
                play_gui()
            elif values['option'] == 'Vigenere':
                vig_gui()
            elif values['option'] == 'Vigenere Auto-Key':
                vig_a_gui()
            elif values['option'] == 'Vigenere Extended':
                vig_e_gui()
            elif values['option'] == 'Vigenere Full':
                vig_f_gui()
    window.close()
        

if __name__ == '__main__':
    main()