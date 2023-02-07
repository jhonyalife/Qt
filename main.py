from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from PySide6 import QtCore
import sys
from qt_material import apply_stylesheet
from ui_main import Ui_MainWindow
from database import Data_base


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(
            "SCAS - Sistema de Controle de Atendimento de Saúde")
        appIcon = QIcon(":/")
        self.ui = Ui_MainWindow()
        self.setWindowIcon(appIcon)

        self.db = Data_base()
        self.mostrar_pacientes()
        self.mostrar_profissionais()
        self.mostrar_agenda()

        #########################################################################
        # Animação Menu
        #########################################################################

        self.btnMenu.clicked.connect(self.leftMenu)

        #########################################################################
        # Páginas do Sistemas
        #########################################################################

        self.btn_home.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_agendar.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_agendamento))
        self.btn_cadastrar.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        self.btn_adicionar_prof.clicked.connect(
            lambda: self.tabWidget.setCurrentWidget(self.tab))
        self.btn_adicionar_pac.clicked.connect(
            lambda: self.tabWidget.setCurrentWidget(self.tab_4))
        self.btn_adicionar_consult.clicked.connect(
            lambda: self.tabWidget_2.setCurrentWidget(self.tab_5))

        #########################################################################
        # BOTÕES AGENDAMENTO
        #########################################################################

        self.btn_agendar_2.clicked.connect(self.register_agendamento)
        self.btn_excluir_consult.clicked.connect(self.delete_agendamento)
        self.btn_editar_consult.clicked.connect(self.update_agendamento)

        #########################################################################
        # BOTÕES PROFISSIONAL
        #########################################################################

        self.btnButtonProf.clicked.connect(self.register_profissionais)
        self.btn_excluir_prof.clicked.connect(self.delete_profissionais)
        self.btn_editar_prof.clicked.connect(self.update_profissionais)

        #########################################################################
        # BOTÕES PACIENTE
        #########################################################################

        self.btnButtonPac.clicked.connect(self.register_pacientes)
        self.btn_editar_pac.clicked.connect(self.update_pacientes)
        self.btn_excluir_pac.clicked.connect(self.delete_paciente)

    def leftMenu(self):
        width = self.left_frame.width()

        if width == 0:
            newWidth = 200
        else:
            newWidth = 0

        self.animation = QtCore.QPropertyAnimation(
            self.left_frame, b'maximumWidth')
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    #########################################################################
    # DADOS PACIENTE
    #########################################################################

    def register_pacientes(self):
        fullDataSet = (
            self.txt_nome_pac.text(),
            self.txt_cpf_pac.text(),
            self.txt_dataNas_pac.text(),
            self.txt_genero_pac.text(),
            self.txt_altura_pac.text(),
            self.txt_peso_pac.text()
        )

        # Cadastrar no banco
        resposta = self.db.register_pacientes(fullDataSet)
        self.msg(resposta[0], resposta[1])
        self.mostrar_pacientes()

    def msg(self, tipo, mensage):
        msgBox = QMessageBox()
        if tipo.lower() == 'ok':
            msgBox.setIcon(QMessageBox.Information)
        elif tipo.lower() == "erro":
            msgBox.setIcon(QMessageBox.Critical)
        elif tipo.lower() == "aviso":
            msgBox.setIcon(QMessageBox.Warning)

        msgBox.setText(str(mensage))
        msgBox.exec_()

    def mostrar_pacientes(self):
        result = self.db.select_all_pacientes()
        self.tb_pacientes.clearContents()
        self.tb_pacientes.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_pacientes.setItem(
                    row, column, QTableWidgetItem(str(data)))

    def update_pacientes(self):

        data = []
        update_data = []

        for row in range(self.tb_pacientes.rowCount()):
            for column in range(self.tb_pacientes.columnCount()):
                data.append(self.tb_pacientes.item(row, column).text())

            update_data.append(data)
            data = []

        for comp in update_data:
            result = self.db.update_pacientes(tuple(comp))

        self.msg(result[0], result[1])

        self.mostrar_pacientes()

    def delete_paciente(self):

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído.")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            nome = self.tb_pacientes.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = self.db.delete_paciente(nome)
            self.mostrar_pacientes()

            self.msg(result[0], result[1])

    #########################################################################
    # DADOS PROFISSIONAL
    #########################################################################

    def register_profissionais(self):
        fullDataSet = (
            self.txt_nome_prof.text(),
            self.txt_cpf_prof.text(),
            self.txt_datanasc_prof.text(),
            self.txt_genero_prof.text(),
        )

        # Cadastrar no banco
        resposta = self.db.register_profissionais(fullDataSet)
        self.msg(resposta[0], resposta[1])
        self.mostrar_profissionais()

    def mostrar_profissionais(self):
        result = self.db.select_all_profissionais()
        self.tb_profissionais.clearContents()
        self.tb_profissionais.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_profissionais.setItem(
                    row, column, QTableWidgetItem(str(data)))

    def delete_profissionais(self):

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído.")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            nome = self.tb_profissionais.selectionModel(
            ).currentIndex().siblingAtColumn(0).data()
            result = self.db.delete_profissionais(nome)
            self.mostrar_profissionais()

            self.msg(result[0], result[1])

    def update_profissionais(self):

        data = []
        update_data = []

        for row in range(self.tb_profissionais.rowCount()):
            for column in range(self.tb_profissionais.columnCount()):
                data.append(self.tb_profissionais.item(row, column).text())

            update_data.append(data)
            data = []

        for comp in update_data:
            result = self.db.update_profissionais(tuple(comp))

        self.msg(result[0], result[1])

        self.mostrar_profissionais()

    #########################################################################
    # DADOS AGENDAMENTO
    #########################################################################

    def register_agendamento(self):
        fullDataSet = (
            self.txt_nome_pac_agenda.text(),
            self.txt_nome_prof_agenda.text(),
            self.date_agenda.text(),
            self.hora_agenda.text(),
        )

        # Cadastrar no banco
        resposta = self.db.register_agendamento(fullDataSet)
        self.msg(resposta[0], resposta[1])
        self.mostrar_agenda()

    def mostrar_agenda(self):
        result = self.db.select_all_agendamento()
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tableWidget_2.setItem(
                    row, column, QTableWidgetItem(str(data)))

    def delete_agendamento(self):

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído.")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            nome = self.tableWidget_2.selectionModel(
            ).currentIndex().siblingAtColumn(0).data()
            result = self.db.delete_agendamento(nome)
            self.mostrar_agenda()

            self.msg(result[0], result[1])

    def update_agendamento(self):

        data = []
        update_data = []

        for row in range(self.tableWidget_2.rowCount()):
            for column in range(self.tableWidget_2.columnCount()):
                data.append(self.tableWidget_2.item(row, column).text())

            update_data.append(data)
            data = []

        for comp in update_data:
            result = self.db.update_agendamento(tuple(comp))

        self.msg(result[0], result[1])

        self.mostrar_agenda()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_blue.xml')
    db = Data_base()
    db.create_table_pacientes()
    db.create_table_profissionais()
    db.create_table_agendamento()

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
