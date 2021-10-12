import PySimpleGUI as sg
import json

class App():
    '''Enquete sobre programação'''
    def __init__(self):
        #layout 
        tela = sg.theme_background_color('blueviolet')
    
        self.layout = [
            [sg.Text('Nome:'), sg.Input(size=(20,0), key='nome')],
            [sg.Text('Idade:'), sg.Input(size=(20,0), key='idade')],
            [sg.Text('Qual a sua linguagem de programação favorita? ')],
            [sg.Radio("Python", 'linguagem', key='python'),sg.Radio("Javascript", 'linguagem', key='js')],
            [sg.Radio('Java', 'linguagem', key='java'),sg.Radio('PHP', 'linguagem', key='php')],
            [sg.Button('Enviar')],
            [sg.Output(size=(30,20))]
        ]

        #screen
        self.screen = sg.Window('Enquete').layout(self.layout)
        
        

    def Run(self):
        while True:
            #Extraindo os dados 
            self.button, self.dados = self.screen.read()
          

            nome = self.dados['nome']
            idade = self.dados['idade']
            py = self.dados['python']
            js = self.dados['js']
            java = self.dados['java']
            php = self.dados['php']
            print(f'nome: {nome}')
            print(f'idade {idade}')
            print(f'linguagem: {py}')
            print(f'linguagem: {js}')
            print(f'linguagem: {java}')
            print(f'linguagem: {php}')

            filename = 'banco_de_dados.json'
            with open(filename, 'a') as file_js:
                json.dump(self.dados, file_js)
                file = json.load(file_js)
                
            
                
tela = App()
tela.Run()
