# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'POO.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTimeEdit,
    QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(884, 542)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMaximumSize(QSize(0, 16777215))
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logo_frame = QFrame(self.left_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.logo_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.logo_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.logo_frame)

        self.buttons_frame = QFrame(self.left_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.buttons_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.toolBox = QToolBox(self.buttons_frame)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 123, 364))
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_agendar = QPushButton(self.page)
        self.btn_agendar.setObjectName(u"btn_agendar")
        self.btn_agendar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_agendar)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_cadastrar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Menu")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 108, 364))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_7.addWidget(self.label_8)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.toolBox.addItem(self.widget, u"Cr\u00e9ditos")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.buttons_frame)


        self.horizontalLayout.addWidget(self.left_frame)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_container.sizePolicy().hasHeightForWidth())
        self.main_container.setSizePolicy(sizePolicy)
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnMenu = QPushButton(self.top_frame)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnMenu.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/img/icons8-card\u00e1pio.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMenu.setIcon(icon)
        self.btnMenu.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btnMenu, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame, 0, Qt.AlignVCenter)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_6 = QVBoxLayout(self.pg_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.pg_home)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_6.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.Pages.addWidget(self.pg_home)
        self.pg_agendamento = QWidget()
        self.pg_agendamento.setObjectName(u"pg_agendamento")
        self.verticalLayout_9 = QVBoxLayout(self.pg_agendamento)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidget_2 = QTabWidget(self.pg_agendamento)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.label_13 = QLabel(self.tab_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 20, 494, 21))
        self.tableWidget_2 = QTableWidget(self.tab_6)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(0, 50, 671, 261))
        self.frame_5 = QFrame(self.tab_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(670, 50, 131, 261))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.btn_adicionar_consult = QPushButton(self.frame_5)
        self.btn_adicionar_consult.setObjectName(u"btn_adicionar_consult")
        self.btn_adicionar_consult.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_18.addWidget(self.btn_adicionar_consult)

        self.btn_editar_consult = QPushButton(self.frame_5)
        self.btn_editar_consult.setObjectName(u"btn_editar_consult")
        self.btn_editar_consult.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_18.addWidget(self.btn_editar_consult)

        self.btn_excluir_consult = QPushButton(self.frame_5)
        self.btn_excluir_consult.setObjectName(u"btn_excluir_consult")
        self.btn_excluir_consult.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_18.addWidget(self.btn_excluir_consult)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_4)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.frame_4 = QFrame(self.tab_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 50, 781, 291))
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.txt_nome_pac_agenda = QLineEdit(self.frame_4)
        self.txt_nome_pac_agenda.setObjectName(u"txt_nome_pac_agenda")

        self.verticalLayout_17.addWidget(self.txt_nome_pac_agenda)

        self.txt_nome_prof_agenda = QLineEdit(self.frame_4)
        self.txt_nome_prof_agenda.setObjectName(u"txt_nome_prof_agenda")

        self.verticalLayout_17.addWidget(self.txt_nome_prof_agenda)

        self.date_agenda = QDateEdit(self.frame_4)
        self.date_agenda.setObjectName(u"date_agenda")

        self.verticalLayout_17.addWidget(self.date_agenda)

        self.hora_agenda = QTimeEdit(self.frame_4)
        self.hora_agenda.setObjectName(u"hora_agenda")

        self.verticalLayout_17.addWidget(self.hora_agenda)

        self.btn_agendar_2 = QPushButton(self.frame_4)
        self.btn_agendar_2.setObjectName(u"btn_agendar_2")
        self.btn_agendar_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_17.addWidget(self.btn_agendar_2, 0, Qt.AlignHCenter)

        self.label_9 = QLabel(self.tab_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 20, 171, 16))
        self.tabWidget_2.addTab(self.tab_5, "")

        self.verticalLayout_9.addWidget(self.tabWidget_2)

        self.Pages.addWidget(self.pg_agendamento)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.tabWidget = QTabWidget(self.pg_cadastro)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(9, 9, 801, 361))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_13 = QVBoxLayout(self.tab_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)

        self.verticalLayout_13.addWidget(self.label_11)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tb_profissionais = QTableWidget(self.tab_3)
        if (self.tb_profissionais.columnCount() < 4):
            self.tb_profissionais.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_profissionais.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_profissionais.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_profissionais.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_profissionais.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tb_profissionais.setObjectName(u"tb_profissionais")
        self.tb_profissionais.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.tb_profissionais)

        self.frame = QFrame(self.tab_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_adicionar_prof = QPushButton(self.frame)
        self.btn_adicionar_prof.setObjectName(u"btn_adicionar_prof")
        self.btn_adicionar_prof.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.btn_adicionar_prof)

        self.btn_editar_prof = QPushButton(self.frame)
        self.btn_editar_prof.setObjectName(u"btn_editar_prof")
        self.btn_editar_prof.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.btn_editar_prof)

        self.btn_excluir_prof = QPushButton(self.frame)
        self.btn_excluir_prof.setObjectName(u"btn_excluir_prof")
        self.btn_excluir_prof.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.btn_excluir_prof)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addWidget(self.frame)


        self.verticalLayout_13.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 50, 791, 271))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tb_pacientes = QTableWidget(self.layoutWidget)
        if (self.tb_pacientes.columnCount() < 6):
            self.tb_pacientes.setColumnCount(6)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_pacientes.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_pacientes.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_pacientes.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_pacientes.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_pacientes.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_pacientes.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        self.tb_pacientes.setObjectName(u"tb_pacientes")

        self.horizontalLayout_5.addWidget(self.tb_pacientes)

        self.frame_3 = QFrame(self.layoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.btn_adicionar_pac = QPushButton(self.frame_3)
        self.btn_adicionar_pac.setObjectName(u"btn_adicionar_pac")
        self.btn_adicionar_pac.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.btn_adicionar_pac)

        self.btn_editar_pac = QPushButton(self.frame_3)
        self.btn_editar_pac.setObjectName(u"btn_editar_pac")
        self.btn_editar_pac.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.btn_editar_pac)

        self.btn_excluir_pac = QPushButton(self.frame_3)
        self.btn_excluir_pac.setObjectName(u"btn_excluir_pac")
        self.btn_excluir_pac.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_14.addWidget(self.btn_excluir_pac)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 494, 21))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.cadastro_profissional = QFrame(self.tab)
        self.cadastro_profissional.setObjectName(u"cadastro_profissional")
        self.cadastro_profissional.setGeometry(QRect(10, 30, 581, 221))
        sizePolicy1.setHeightForWidth(self.cadastro_profissional.sizePolicy().hasHeightForWidth())
        self.cadastro_profissional.setSizePolicy(sizePolicy1)
        self.cadastro_profissional.setFrameShape(QFrame.StyledPanel)
        self.cadastro_profissional.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.cadastro_profissional)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_cadastro_prof = QLabel(self.cadastro_profissional)
        self.label_cadastro_prof.setObjectName(u"label_cadastro_prof")
        sizePolicy1.setHeightForWidth(self.label_cadastro_prof.sizePolicy().hasHeightForWidth())
        self.label_cadastro_prof.setSizePolicy(sizePolicy1)

        self.verticalLayout_11.addWidget(self.label_cadastro_prof)

        self.txt_nome_prof = QLineEdit(self.cadastro_profissional)
        self.txt_nome_prof.setObjectName(u"txt_nome_prof")
        self.txt_nome_prof.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.txt_nome_prof)

        self.txt_cpf_prof = QLineEdit(self.cadastro_profissional)
        self.txt_cpf_prof.setObjectName(u"txt_cpf_prof")

        self.verticalLayout_11.addWidget(self.txt_cpf_prof)

        self.txt_datanasc_prof = QLineEdit(self.cadastro_profissional)
        self.txt_datanasc_prof.setObjectName(u"txt_datanasc_prof")

        self.verticalLayout_11.addWidget(self.txt_datanasc_prof)

        self.txt_genero_prof = QLineEdit(self.cadastro_profissional)
        self.txt_genero_prof.setObjectName(u"txt_genero_prof")

        self.verticalLayout_11.addWidget(self.txt_genero_prof)

        self.btnButtonProf = QPushButton(self.cadastro_profissional)
        self.btnButtonProf.setObjectName(u"btnButtonProf")
        self.btnButtonProf.setMaximumSize(QSize(500, 50))
        self.btnButtonProf.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.btnButtonProf, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_16 = QVBoxLayout(self.tab_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_2 = QFrame(self.tab_4)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_cadastro_pac = QLabel(self.frame_2)
        self.label_cadastro_pac.setObjectName(u"label_cadastro_pac")
        self.label_cadastro_pac.setGeometry(QRect(10, 10, 639, 24))
        sizePolicy1.setHeightForWidth(self.label_cadastro_pac.sizePolicy().hasHeightForWidth())
        self.label_cadastro_pac.setSizePolicy(sizePolicy1)
        self.txt_nome_pac = QLineEdit(self.frame_2)
        self.txt_nome_pac.setObjectName(u"txt_nome_pac")
        self.txt_nome_pac.setGeometry(QRect(10, 40, 639, 24))
        self.txt_cpf_pac = QLineEdit(self.frame_2)
        self.txt_cpf_pac.setObjectName(u"txt_cpf_pac")
        self.txt_cpf_pac.setGeometry(QRect(10, 70, 639, 24))
        self.txt_dataNas_pac = QLineEdit(self.frame_2)
        self.txt_dataNas_pac.setObjectName(u"txt_dataNas_pac")
        self.txt_dataNas_pac.setGeometry(QRect(10, 100, 639, 23))
        self.txt_genero_pac = QLineEdit(self.frame_2)
        self.txt_genero_pac.setObjectName(u"txt_genero_pac")
        self.txt_genero_pac.setGeometry(QRect(10, 129, 639, 24))
        self.txt_altura_pac = QLineEdit(self.frame_2)
        self.txt_altura_pac.setObjectName(u"txt_altura_pac")
        self.txt_altura_pac.setGeometry(QRect(10, 159, 639, 24))
        self.txt_peso_pac = QLineEdit(self.frame_2)
        self.txt_peso_pac.setObjectName(u"txt_peso_pac")
        self.txt_peso_pac.setGeometry(QRect(10, 189, 639, 24))
        self.btnButtonPac = QPushButton(self.frame_2)
        self.btnButtonPac.setObjectName(u"btnButtonPac")
        self.btnButtonPac.setGeometry(QRect(289, 219, 80, 23))
        self.btnButtonPac.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tab_4, "")
        self.Pages.addWidget(self.pg_cadastro)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.footer_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">SCAS</p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_agendar.setText(QCoreApplication.translate("MainWindow", u"Agendamento", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bruno Pithon", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Jo\u00e3o Paulo", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Jos\u00e9 Renan", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Jhony Alife ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tiago Alves", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"Cr\u00e9ditos", None))
        self.btnMenu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>SISTEMA DE CONTROLE DE ATENDIMENTO DE SA\u00daDE:</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/img/prescription.png\"/></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Hist\u00f3rico</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Paciente", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Profissional", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Dia", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        self.btn_adicionar_consult.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_editar_consult.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_excluir_consult.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Agenda", None))
        self.txt_nome_pac_agenda.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Paciente:", None))
        self.txt_nome_prof_agenda.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Profissional:", None))
        self.btn_agendar_2.setText(QCoreApplication.translate("MainWindow", u"Agendar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Agendar Consulta</span></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">PROFISSIONAIS:</span></p></body></html>", None))
        ___qtablewidgetitem4 = self.tb_profissionais.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem5 = self.tb_profissionais.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem6 = self.tb_profissionais.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"DATA/NASC", None));
        ___qtablewidgetitem7 = self.tb_profissionais.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"G\u00caNERO", None));
        self.btn_adicionar_prof.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_editar_prof.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_excluir_prof.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Profissional", None))
        ___qtablewidgetitem8 = self.tb_pacientes.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem9 = self.tb_pacientes.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem10 = self.tb_pacientes.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"DATA/NASC", None));
        ___qtablewidgetitem11 = self.tb_pacientes.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"G\u00caNERO", None));
        ___qtablewidgetitem12 = self.tb_pacientes.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ALTURA", None));
        ___qtablewidgetitem13 = self.tb_pacientes.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"PESO", None));
        self.btn_adicionar_pac.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_editar_pac.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_excluir_pac.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">PACIENTES:</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Paciente", None))
        self.label_cadastro_prof.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">CADASTRO DO PROFISSIONAL:</span></p></body></html>", None))
        self.txt_nome_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.txt_cpf_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txt_datanasc_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data de Nascimento:", None))
        self.txt_genero_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G\u00eanero:", None))
        self.btnButtonProf.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro Profissional", None))
        self.label_cadastro_pac.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">CADASTRO PACIENTE</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.txt_nome_pac.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.txt_cpf_pac.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.txt_dataNas_pac.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data de Nascimento:", None))
        self.txt_genero_pac.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G\u00eanero:", None))
        self.txt_altura_pac.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Altura:", None))
        self.txt_peso_pac.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Peso:", None))
        self.btnButtonPac.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Cadastro Paciente", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"@2023 - TSI", None))
    # retranslateUi

