import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMenuBar, QAction
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QTimer, QSize

import subprocess

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.numero_de_confirmações = 3
        self.nome = "Iusley Lacerda"  # Valor pré-setado para o nome
        self.email = "ilacerda@alpargatas.com"  # Valor pré-setado para o email
        self.file_list = ["1", "2", "3"]

        self.initUI()

    def set_numero_de_confirmações(self):
        selected_option = self.comboBox.currentText()
        self.numero_de_confirmações = int(selected_option)

    def set_nome(self):
        self.nome = self.nomeLineEdit.text()

    def set_email(self):
        self.email = self.emailLineEdit.text()

    def run_file(self):
        self.set_numero_de_confirmações()
        self.set_nome()
        self.set_email()

        try:
            subprocess.run(["python", "gemba_WALK_automation.py", str(self.numero_de_confirmações), self.nome, self.email], check=True)
        except FileNotFoundError:
            print("Arquivo gemba_WALK_automation.py não encontrado!")

    def update_title_animation(self):
        # Esta função atualiza o título com uma animação simples
        if self.animation_frame == 0:
            self.setWindowTitle("Automação - Gemba Walk")
        else:
            self.setWindowTitle("Automação - Gemba Walk" + "." * self.animation_frame)
        self.animation_frame = (self.animation_frame + 1) % 4

    def initUI(self):
        self.setWindowTitle("Automação - Gemba Walk")
        self.setGeometry(100, 100, 400, 220)  # Aumentei a altura para acomodar melhor os elementos

        # Defina um ícone para a janela
        self.setWindowIcon(QIcon("icon.png"))

        main_layout = QVBoxLayout()

        # Título centralizado
        title_label = QLabel("Automação - Gemba Walk")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 18px; margin-bottom: 10px;")
        main_layout.addWidget(title_label)

        header_layout = QHBoxLayout()
        header_label = QLabel("Selecione a quantidade de Confirmações:")
        header_label.setStyleSheet("font-size: 16px; margin-right: 10px;")
        self.comboBox = QComboBox()
        self.comboBox.addItems(self.file_list)
        self.comboBox.setStyleSheet("font-size: 16px;")
        header_layout.addWidget(header_label)
        header_layout.addWidget(self.comboBox)
        main_layout.addLayout(header_layout)

        nome_layout = QHBoxLayout()
        nome_label = QLabel("Nome:")
        nome_label.setStyleSheet("font-size: 16px; margin-right: 10px;")
        self.nomeLineEdit = QLineEdit(self.nome)  # Defina o valor pré-setado
        self.nomeLineEdit.setStyleSheet("font-size: 16px;")
        nome_layout.addWidget(nome_label)
        nome_layout.addWidget(self.nomeLineEdit)
        main_layout.addLayout(nome_layout)

        email_layout = QHBoxLayout()
        email_label = QLabel("Email:")
        email_label.setStyleSheet("font-size: 16px; margin-right: 10px;")
        self.emailLineEdit = QLineEdit(self.email)  # Defina o valor pré-setado
        self.emailLineEdit.setStyleSheet("font-size: 16px;")
        email_layout.addWidget(email_label)
        email_layout.addWidget(self.emailLineEdit)
        main_layout.addLayout(email_layout)

        # Adicionando um espaço em branco
        main_layout.addSpacing(10)

        button_layout = QHBoxLayout()
        self.button = QPushButton("Executar", self)
        self.button.clicked.connect(self.run_file)

        # Personalize a aparência do botão usando CSS e adicione um ícone
        self.button.setStyleSheet("background-color: #007BFF; color: white; font-size: 16px;")
        self.button.setIcon(QIcon("execute_icon.png"))
        self.button.setIconSize(QSize(24, 24))  # Defina o tamanho do ícone
        button_layout.addWidget(self.button)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Configurar animação de título
        self.animation_frame = 0
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.update_title_animation)
        self.animation_timer.start(500)  # Atualizar a cada 500 ms (0,5 segundos)

        # Conectar o evento returnPressed dos campos de entrada ao slot de execução do botão
        self.nomeLineEdit.returnPressed.connect(self.run_file)
        self.emailLineEdit.returnPressed.connect(self.run_file)

        # Criar um menu de arquivo com um item "Sair"
        menubar = QMenuBar(self)
        menubar.setGeometry(0, 0, 400, 20)  # Define a geometria do menu
        file_menu = menubar.addMenu('Arquivo')
        exit_action = QAction('Sair', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
