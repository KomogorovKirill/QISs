# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 668)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Init = QtWidgets.QWidget()
        self.tab_Init.setObjectName("tab_Init")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_Init)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_API_Token = QtWidgets.QLineEdit(self.tab_Init)
        self.lineEdit_API_Token.setObjectName("lineEdit_API_Token")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_API_Token)
        self.label_API_Token = QtWidgets.QLabel(self.tab_Init)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_API_Token.sizePolicy().hasHeightForWidth())
        self.label_API_Token.setSizePolicy(sizePolicy)
        self.label_API_Token.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.label_API_Token.setFont(font)
        self.label_API_Token.setObjectName("label_API_Token")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_API_Token)
        self.lineEdit_Channel = QtWidgets.QLineEdit(self.tab_Init)
        self.lineEdit_Channel.setObjectName("lineEdit_Channel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Channel)
        self.pushButton_Apply_API_Token = QtWidgets.QPushButton(self.tab_Init)
        self.pushButton_Apply_API_Token.setEnabled(False)
        self.pushButton_Apply_API_Token.setObjectName("pushButton_Apply_API_Token")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pushButton_Apply_API_Token)
        self.label_Chennel = QtWidgets.QLabel(self.tab_Init)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.label_Chennel.setFont(font)
        self.label_Chennel.setObjectName("label_Chennel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_Chennel)
        self.label_Instance = QtWidgets.QLabel(self.tab_Init)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.label_Instance.setFont(font)
        self.label_Instance.setObjectName("label_Instance")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_Instance)
        self.lineEdit_Instance = QtWidgets.QLineEdit(self.tab_Init)
        self.lineEdit_Instance.setObjectName("lineEdit_Instance")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Instance)
        self.gridLayout_12.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_INFO_QPU_List = QtWidgets.QComboBox(self.tab_Init)
        self.comboBox_INFO_QPU_List.setEnabled(False)
        self.comboBox_INFO_QPU_List.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_INFO_QPU_List.setObjectName("comboBox_INFO_QPU_List")
        self.gridLayout_2.addWidget(self.comboBox_INFO_QPU_List, 4, 0, 1, 1)
        self.pushButton_INFO_Get_Info_on_Qubit = QtWidgets.QPushButton(self.tab_Init)
        self.pushButton_INFO_Get_Info_on_Qubit.setEnabled(False)
        self.pushButton_INFO_Get_Info_on_Qubit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_INFO_Get_Info_on_Qubit.setObjectName("pushButton_INFO_Get_Info_on_Qubit")
        self.gridLayout_2.addWidget(self.pushButton_INFO_Get_Info_on_Qubit, 4, 1, 1, 2)
        self.label_INFO_QPU_Select = QtWidgets.QLabel(self.tab_Init)
        self.label_INFO_QPU_Select.setObjectName("label_INFO_QPU_Select")
        self.gridLayout_2.addWidget(self.label_INFO_QPU_Select, 2, 0, 2, 1)
        self.horizontalSlider_INFO_Num_of_Qubits = QtWidgets.QSlider(self.tab_Init)
        self.horizontalSlider_INFO_Num_of_Qubits.setEnabled(False)
        self.horizontalSlider_INFO_Num_of_Qubits.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_INFO_Num_of_Qubits.setMaximum(0)
        self.horizontalSlider_INFO_Num_of_Qubits.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_INFO_Num_of_Qubits.setObjectName("horizontalSlider_INFO_Num_of_Qubits")
        self.gridLayout_2.addWidget(self.horizontalSlider_INFO_Num_of_Qubits, 1, 1, 1, 2)
        self.label_INFO_Selected_Qubit = QtWidgets.QLabel(self.tab_Init)
        self.label_INFO_Selected_Qubit.setObjectName("label_INFO_Selected_Qubit")
        self.gridLayout_2.addWidget(self.label_INFO_Selected_Qubit, 2, 2, 2, 1)
        self.label_INFO_Num_of_Qubits = QtWidgets.QLabel(self.tab_Init)
        self.label_INFO_Num_of_Qubits.setObjectName("label_INFO_Num_of_Qubits")
        self.gridLayout_2.addWidget(self.label_INFO_Num_of_Qubits, 0, 1, 1, 2)
        self.label_INFO_qubits = QtWidgets.QLabel(self.tab_Init)
        self.label_INFO_qubits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_INFO_qubits.setObjectName("label_INFO_qubits")
        self.gridLayout_2.addWidget(self.label_INFO_qubits, 2, 1, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.tab_Init)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_QPU_Available = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_QPU_Available.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_QPU_Available.setObjectName("pushButton_QPU_Available")
        self.horizontalLayout_6.addWidget(self.pushButton_QPU_Available)
        self.pushButton_QPU_Characteristics = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_QPU_Characteristics.setEnabled(False)
        self.pushButton_QPU_Characteristics.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_QPU_Characteristics.setObjectName("pushButton_QPU_Characteristics")
        self.horizontalLayout_6.addWidget(self.pushButton_QPU_Characteristics)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.pushButton_Clear_All = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_Clear_All.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Clear_All.setObjectName("pushButton_Clear_All")
        self.verticalLayout_6.addWidget(self.pushButton_Clear_All)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Console_Output = QtWidgets.QLabel(self.frame_2)
        self.label_Console_Output.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Console_Output.setObjectName("label_Console_Output")
        self.verticalLayout.addWidget(self.label_Console_Output)
        self.textEdit_Console_Output = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_Console_Output.setEnabled(True)
        self.textEdit_Console_Output.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textEdit_Console_Output.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_Console_Output.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_Console_Output.setReadOnly(True)
        self.textEdit_Console_Output.setObjectName("textEdit_Console_Output")
        self.verticalLayout.addWidget(self.textEdit_Console_Output)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame_2, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_Init, "")
        self.tab_QRNG = QtWidgets.QWidget()
        self.tab_QRNG.setObjectName("tab_QRNG")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_QRNG)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frame = QtWidgets.QFrame(self.tab_QRNG)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_QRNG_RadioButtons = QtWidgets.QFrame(self.frame)
        self.frame_QRNG_RadioButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_QRNG_RadioButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_QRNG_RadioButtons.setObjectName("frame_QRNG_RadioButtons")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_QRNG_RadioButtons)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_QRNG_Check = QtWidgets.QRadioButton(self.frame_QRNG_RadioButtons)
        self.radioButton_QRNG_Check.setChecked(True)
        self.radioButton_QRNG_Check.setObjectName("radioButton_QRNG_Check")
        self.horizontalLayout_5.addWidget(self.radioButton_QRNG_Check)
        self.radioButton_QRNG_Simulator_Check = QtWidgets.QRadioButton(self.frame_QRNG_RadioButtons)
        self.radioButton_QRNG_Simulator_Check.setEnabled(True)
        self.radioButton_QRNG_Simulator_Check.setObjectName("radioButton_QRNG_Simulator_Check")
        self.horizontalLayout_5.addWidget(self.radioButton_QRNG_Simulator_Check)
        self.radioButton_NIST_Check = QtWidgets.QRadioButton(self.frame_QRNG_RadioButtons)
        self.radioButton_NIST_Check.setObjectName("radioButton_NIST_Check")
        self.horizontalLayout_5.addWidget(self.radioButton_NIST_Check)
        self.gridLayout_6.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_QRNG_RadioButtons, 0, 0, 1, 1)
        self.frame_QRNG_Simulator = QtWidgets.QFrame(self.frame)
        self.frame_QRNG_Simulator.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_QRNG_Simulator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_QRNG_Simulator.setObjectName("frame_QRNG_Simulator")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_QRNG_Simulator)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_QRNG_SIMULATOR_Qubits = QtWidgets.QLabel(self.frame_QRNG_Simulator)
        self.label_QRNG_SIMULATOR_Qubits.setObjectName("label_QRNG_SIMULATOR_Qubits")
        self.gridLayout_3.addWidget(self.label_QRNG_SIMULATOR_Qubits, 2, 1, 1, 1)
        self.label_QRNG_SIMULATOR_Num_of_Qubits = QtWidgets.QLabel(self.frame_QRNG_Simulator)
        self.label_QRNG_SIMULATOR_Num_of_Qubits.setAlignment(QtCore.Qt.AlignCenter)
        self.label_QRNG_SIMULATOR_Num_of_Qubits.setObjectName("label_QRNG_SIMULATOR_Num_of_Qubits")
        self.gridLayout_3.addWidget(self.label_QRNG_SIMULATOR_Num_of_Qubits, 0, 0, 1, 2)
        self.pushButton_QRNG_SIMULATO_Start = QtWidgets.QPushButton(self.frame_QRNG_Simulator)
        self.pushButton_QRNG_SIMULATO_Start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_QRNG_SIMULATO_Start.setObjectName("pushButton_QRNG_SIMULATO_Start")
        self.gridLayout_3.addWidget(self.pushButton_QRNG_SIMULATO_Start, 3, 0, 1, 2)
        self.label_QRNG_SIMULATOR_Num_of_Qubits_2 = QtWidgets.QLabel(self.frame_QRNG_Simulator)
        self.label_QRNG_SIMULATOR_Num_of_Qubits_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_QRNG_SIMULATOR_Num_of_Qubits_2.setObjectName("label_QRNG_SIMULATOR_Num_of_Qubits_2")
        self.gridLayout_3.addWidget(self.label_QRNG_SIMULATOR_Num_of_Qubits_2, 2, 0, 1, 1)
        self.horizontalSlider_QRNG_SIMULATOR_Num_of_Qubits = QtWidgets.QSlider(self.frame_QRNG_Simulator)
        self.horizontalSlider_QRNG_SIMULATOR_Num_of_Qubits.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_QRNG_SIMULATOR_Num_of_Qubits.setMinimum(1)
        self.horizontalSlider_QRNG_SIMULATOR_Num_of_Qubits.setMaximum(10)
        self.horizontalSlider_QRNG_SIMULATOR_Num_of_Qubits.setPageStep(1)
        self.horizontalSlider_QRNG_SIMULATOR_Num_of_Qubits.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_QRNG_SIMULATOR_Num_of_Qubits.setObjectName("horizontalSlider_QRNG_SIMULATOR_Num_of_Qubits")
        self.gridLayout_3.addWidget(self.horizontalSlider_QRNG_SIMULATOR_Num_of_Qubits, 1, 0, 1, 2)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        self.gridLayout_8.addWidget(self.frame_QRNG_Simulator, 0, 1, 2, 1)
        self.frame_QRNG = QtWidgets.QFrame(self.frame)
        self.frame_QRNG.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_QRNG.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_QRNG.setObjectName("frame_QRNG")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_QRNG)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_QRNG_QPU_Select = QtWidgets.QLabel(self.frame_QRNG)
        self.label_QRNG_QPU_Select.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_QRNG_QPU_Select.setObjectName("label_QRNG_QPU_Select")
        self.verticalLayout_2.addWidget(self.label_QRNG_QPU_Select)
        self.comboBox_QRNG_QPU_List = QtWidgets.QComboBox(self.frame_QRNG)
        self.comboBox_QRNG_QPU_List.setEnabled(False)
        self.comboBox_QRNG_QPU_List.setEditable(False)
        self.comboBox_QRNG_QPU_List.setObjectName("comboBox_QRNG_QPU_List")
        self.verticalLayout_2.addWidget(self.comboBox_QRNG_QPU_List)
        self.label_QRNG_JobID = QtWidgets.QLabel(self.frame_QRNG)
        self.label_QRNG_JobID.setAlignment(QtCore.Qt.AlignCenter)
        self.label_QRNG_JobID.setObjectName("label_QRNG_JobID")
        self.verticalLayout_2.addWidget(self.label_QRNG_JobID)
        self.lineEdit_QRNG_JobID = QtWidgets.QLineEdit(self.frame_QRNG)
        self.lineEdit_QRNG_JobID.setClearButtonEnabled(True)
        self.lineEdit_QRNG_JobID.setObjectName("lineEdit_QRNG_JobID")
        self.verticalLayout_2.addWidget(self.lineEdit_QRNG_JobID)
        self.pushButton_QRNG_JobID_Check = QtWidgets.QPushButton(self.frame_QRNG)
        self.pushButton_QRNG_JobID_Check.setEnabled(True)
        self.pushButton_QRNG_JobID_Check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_QRNG_JobID_Check.setObjectName("pushButton_QRNG_JobID_Check")
        self.verticalLayout_2.addWidget(self.pushButton_QRNG_JobID_Check)
        self.pushButton_QRNG_JobID_Cancel = QtWidgets.QPushButton(self.frame_QRNG)
        self.pushButton_QRNG_JobID_Cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_QRNG_JobID_Cancel.setObjectName("pushButton_QRNG_JobID_Cancel")
        self.verticalLayout_2.addWidget(self.pushButton_QRNG_JobID_Cancel)
        self.pushButton_QRNG_JobID_Download = QtWidgets.QPushButton(self.frame_QRNG)
        self.pushButton_QRNG_JobID_Download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_QRNG_JobID_Download.setObjectName("pushButton_QRNG_JobID_Download")
        self.verticalLayout_2.addWidget(self.pushButton_QRNG_JobID_Download)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2_QRNG_Num_of_Qubits = QtWidgets.QLabel(self.frame_QRNG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2_QRNG_Num_of_Qubits.sizePolicy().hasHeightForWidth())
        self.label_2_QRNG_Num_of_Qubits.setSizePolicy(sizePolicy)
        self.label_2_QRNG_Num_of_Qubits.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2_QRNG_Num_of_Qubits.setObjectName("label_2_QRNG_Num_of_Qubits")
        self.verticalLayout_3.addWidget(self.label_2_QRNG_Num_of_Qubits)
        self.horizontalSlider_QRNG_Num_of_Qubits = QtWidgets.QSlider(self.frame_QRNG)
        self.horizontalSlider_QRNG_Num_of_Qubits.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_QRNG_Num_of_Qubits.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_QRNG_Num_of_Qubits.setSizePolicy(sizePolicy)
        self.horizontalSlider_QRNG_Num_of_Qubits.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_QRNG_Num_of_Qubits.setMaximum(0)
        self.horizontalSlider_QRNG_Num_of_Qubits.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_QRNG_Num_of_Qubits.setObjectName("horizontalSlider_QRNG_Num_of_Qubits")
        self.verticalLayout_3.addWidget(self.horizontalSlider_QRNG_Num_of_Qubits)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_QRNG_Num_of_Qubits = QtWidgets.QLabel(self.frame_QRNG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_QRNG_Num_of_Qubits.sizePolicy().hasHeightForWidth())
        self.label_QRNG_Num_of_Qubits.setSizePolicy(sizePolicy)
        self.label_QRNG_Num_of_Qubits.setMinimumSize(QtCore.QSize(80, 0))
        self.label_QRNG_Num_of_Qubits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_QRNG_Num_of_Qubits.setObjectName("label_QRNG_Num_of_Qubits")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_QRNG_Num_of_Qubits)
        self.label_QRNG_Qubits = QtWidgets.QLabel(self.frame_QRNG)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_QRNG_Qubits.sizePolicy().hasHeightForWidth())
        self.label_QRNG_Qubits.setSizePolicy(sizePolicy)
        self.label_QRNG_Qubits.setObjectName("label_QRNG_Qubits")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_QRNG_Qubits)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_ALPHA = QtWidgets.QLabel(self.frame_QRNG)
        self.label_ALPHA.setObjectName("label_ALPHA")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_ALPHA)
        self.lineEdit_ALPHA = QtWidgets.QLineEdit(self.frame_QRNG)
        self.lineEdit_ALPHA.setEnabled(True)
        self.lineEdit_ALPHA.setClearButtonEnabled(True)
        self.lineEdit_ALPHA.setObjectName("lineEdit_ALPHA")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ALPHA)
        self.label_QRNG_Shots = QtWidgets.QLabel(self.frame_QRNG)
        self.label_QRNG_Shots.setObjectName("label_QRNG_Shots")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_QRNG_Shots)
        self.label_QRNG_OptLevel = QtWidgets.QLabel(self.frame_QRNG)
        self.label_QRNG_OptLevel.setObjectName("label_QRNG_OptLevel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_QRNG_OptLevel)
        self.lineEdit_QRNG_Shots = QtWidgets.QLineEdit(self.frame_QRNG)
        self.lineEdit_QRNG_Shots.setClearButtonEnabled(True)
        self.lineEdit_QRNG_Shots.setObjectName("lineEdit_QRNG_Shots")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_QRNG_Shots)
        self.lineEdit_QRNG_OptLevel = QtWidgets.QLineEdit(self.frame_QRNG)
        self.lineEdit_QRNG_OptLevel.setClearButtonEnabled(True)
        self.lineEdit_QRNG_OptLevel.setObjectName("lineEdit_QRNG_OptLevel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_QRNG_OptLevel)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.pushButton_QRNG_Start = QtWidgets.QPushButton(self.frame_QRNG)
        self.pushButton_QRNG_Start.setEnabled(False)
        self.pushButton_QRNG_Start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_QRNG_Start.setObjectName("pushButton_QRNG_Start")
        self.verticalLayout_3.addWidget(self.pushButton_QRNG_Start)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout_8.addWidget(self.frame_QRNG, 1, 0, 2, 1)
        self.frame_NIST = QtWidgets.QFrame(self.frame)
        self.frame_NIST.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_NIST.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_NIST.setObjectName("frame_NIST")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_NIST)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_NIST_Key_Length = QtWidgets.QLineEdit(self.frame_NIST)
        self.lineEdit_NIST_Key_Length.setClearButtonEnabled(True)
        self.lineEdit_NIST_Key_Length.setObjectName("lineEdit_NIST_Key_Length")
        self.gridLayout_5.addWidget(self.lineEdit_NIST_Key_Length, 1, 1, 1, 1)
        self.lineEdit_NIST_Parameters_on_Default = QtWidgets.QLineEdit(self.frame_NIST)
        self.lineEdit_NIST_Parameters_on_Default.setEnabled(True)
        self.lineEdit_NIST_Parameters_on_Default.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.lineEdit_NIST_Parameters_on_Default.setReadOnly(True)
        self.lineEdit_NIST_Parameters_on_Default.setObjectName("lineEdit_NIST_Parameters_on_Default")
        self.gridLayout_5.addWidget(self.lineEdit_NIST_Parameters_on_Default, 3, 1, 1, 1)
        self.lineEdit_NIST_Tests_Supplys = QtWidgets.QLineEdit(self.frame_NIST)
        self.lineEdit_NIST_Tests_Supplys.setEnabled(True)
        self.lineEdit_NIST_Tests_Supplys.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.lineEdit_NIST_Tests_Supplys.setReadOnly(True)
        self.lineEdit_NIST_Tests_Supplys.setObjectName("lineEdit_NIST_Tests_Supplys")
        self.gridLayout_5.addWidget(self.lineEdit_NIST_Tests_Supplys, 2, 1, 1, 1)
        self.label_NIST_Directory_to_Dataset = QtWidgets.QLabel(self.frame_NIST)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.label_NIST_Directory_to_Dataset.setFont(font)
        self.label_NIST_Directory_to_Dataset.setObjectName("label_NIST_Directory_to_Dataset")
        self.gridLayout_5.addWidget(self.label_NIST_Directory_to_Dataset, 0, 0, 1, 1)
        self.pushButton_NIST_Start = QtWidgets.QPushButton(self.frame_NIST)
        self.pushButton_NIST_Start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_NIST_Start.setObjectName("pushButton_NIST_Start")
        self.gridLayout_5.addWidget(self.pushButton_NIST_Start, 6, 0, 1, 2)
        self.lineEdit_NIST_Directory_to_Dataset = QtWidgets.QLineEdit(self.frame_NIST)
        self.lineEdit_NIST_Directory_to_Dataset.setText("")
        self.lineEdit_NIST_Directory_to_Dataset.setClearButtonEnabled(True)
        self.lineEdit_NIST_Directory_to_Dataset.setObjectName("lineEdit_NIST_Directory_to_Dataset")
        self.gridLayout_5.addWidget(self.lineEdit_NIST_Directory_to_Dataset, 0, 1, 1, 1)
        self.label_NIST_Key_Length = QtWidgets.QLabel(self.frame_NIST)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.label_NIST_Key_Length.setFont(font)
        self.label_NIST_Key_Length.setObjectName("label_NIST_Key_Length")
        self.gridLayout_5.addWidget(self.label_NIST_Key_Length, 1, 0, 1, 1)
        self.label_NIST_Tests_Supplys = QtWidgets.QLabel(self.frame_NIST)
        self.label_NIST_Tests_Supplys.setObjectName("label_NIST_Tests_Supplys")
        self.gridLayout_5.addWidget(self.label_NIST_Tests_Supplys, 2, 0, 1, 1)
        self.label_NIST_Num_of_Bitstream = QtWidgets.QLabel(self.frame_NIST)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.label_NIST_Num_of_Bitstream.setFont(font)
        self.label_NIST_Num_of_Bitstream.setObjectName("label_NIST_Num_of_Bitstream")
        self.gridLayout_5.addWidget(self.label_NIST_Num_of_Bitstream, 4, 0, 1, 1)
        self.lineEdit_NIST_Format_of_Data = QtWidgets.QLineEdit(self.frame_NIST)
        self.lineEdit_NIST_Format_of_Data.setEnabled(True)
        self.lineEdit_NIST_Format_of_Data.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.lineEdit_NIST_Format_of_Data.setWhatsThis("")
        self.lineEdit_NIST_Format_of_Data.setReadOnly(True)
        self.lineEdit_NIST_Format_of_Data.setObjectName("lineEdit_NIST_Format_of_Data")
        self.gridLayout_5.addWidget(self.lineEdit_NIST_Format_of_Data, 5, 1, 1, 1)
        self.lineEdit_NIST_Num_of_Bitstream = QtWidgets.QLineEdit(self.frame_NIST)
        self.lineEdit_NIST_Num_of_Bitstream.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_NIST_Num_of_Bitstream.setClearButtonEnabled(True)
        self.lineEdit_NIST_Num_of_Bitstream.setObjectName("lineEdit_NIST_Num_of_Bitstream")
        self.gridLayout_5.addWidget(self.lineEdit_NIST_Num_of_Bitstream, 4, 1, 1, 1)
        self.label_NIST_Parameters_on_Default = QtWidgets.QLabel(self.frame_NIST)
        self.label_NIST_Parameters_on_Default.setObjectName("label_NIST_Parameters_on_Default")
        self.gridLayout_5.addWidget(self.label_NIST_Parameters_on_Default, 3, 0, 1, 1)
        self.label_NIST_Format_of_Data = QtWidgets.QLabel(self.frame_NIST)
        self.label_NIST_Format_of_Data.setObjectName("label_NIST_Format_of_Data")
        self.gridLayout_5.addWidget(self.label_NIST_Format_of_Data, 5, 0, 1, 1)
        self.pushButton_Path_for_NIST_Dialog = QtWidgets.QPushButton(self.frame_NIST)
        self.pushButton_Path_for_NIST_Dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Path_for_NIST_Dialog.setObjectName("pushButton_Path_for_NIST_Dialog")
        self.gridLayout_5.addWidget(self.pushButton_Path_for_NIST_Dialog, 0, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_5)
        self.gridLayout_8.addWidget(self.frame_NIST, 2, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.frame_QRNG_Output = QtWidgets.QFrame(self.frame)
        self.frame_QRNG_Output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_QRNG_Output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_QRNG_Output.setObjectName("frame_QRNG_Output")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_QRNG_Output)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.textEdit_QRNG_Output = QtWidgets.QTextEdit(self.frame_QRNG_Output)
        self.textEdit_QRNG_Output.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_QRNG_Output.setReadOnly(True)
        self.textEdit_QRNG_Output.setObjectName("textEdit_QRNG_Output")
        self.gridLayout_7.addWidget(self.textEdit_QRNG_Output, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_QRNG_Output)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_7.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_QRNG_Output, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.frame, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_10)
        self.tabWidget.addTab(self.tab_QRNG, "")
        self.tab_QKD = QtWidgets.QWidget()
        self.tab_QKD.setObjectName("tab_QKD")
        self.tabWidget.addTab(self.tab_QKD, "")
        self.tab_Fourie = QtWidgets.QWidget()
        self.tab_Fourie.setObjectName("tab_Fourie")
        self.tabWidget.addTab(self.tab_Fourie, "")
        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.horizontalSlider_QRNG_Num_of_Qubits.valueChanged['int'].connect(self.label_QRNG_Num_of_Qubits.setNum)
        self.pushButton.clicked.connect(self.textEdit_QRNG_Output.clear)
        self.horizontalSlider_INFO_Num_of_Qubits.valueChanged['int'].connect(self.label_INFO_Selected_Qubit.setNum)
        self.horizontalSlider_QRNG_SIMULATOR_Num_of_Qubits.valueChanged['int'].connect(self.label_QRNG_SIMULATOR_Num_of_Qubits_2.setNum)
        self.pushButton_Clear_All.clicked.connect(self.textEdit_Console_Output.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QIS_Benchmark_v.0.1"))
        self.label_API_Token.setText(_translate("MainWindow", "API Token:"))
        self.pushButton_Apply_API_Token.setText(_translate("MainWindow", "Подтвердить"))
        self.label_Chennel.setText(_translate("MainWindow", "Channel:"))
        self.label_Instance.setText(_translate("MainWindow", "Instance:"))
        self.pushButton_INFO_Get_Info_on_Qubit.setText(_translate("MainWindow", "Дополнительные сведения"))
        self.label_INFO_QPU_Select.setText(_translate("MainWindow", "Выберите КВУ:"))
        self.label_INFO_Selected_Qubit.setText(_translate("MainWindow", "0"))
        self.label_INFO_Num_of_Qubits.setText(_translate("MainWindow", "Выберите кубит:"))
        self.label_INFO_qubits.setText(_translate("MainWindow", "Кубит: "))
        self.pushButton_QPU_Available.setText(_translate("MainWindow", "Доступные КВУ"))
        self.pushButton_QPU_Characteristics.setText(_translate("MainWindow", "Дополнительная информация"))
        self.pushButton_Clear_All.setText(_translate("MainWindow", "Очистить"))
        self.label_Console_Output.setText(_translate("MainWindow", "Console:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Init), _translate("MainWindow", "Инициализация"))
        self.radioButton_QRNG_Check.setText(_translate("MainWindow", "КГСЧ"))
        self.radioButton_QRNG_Simulator_Check.setText(_translate("MainWindow", "Симулятор КГСЧ"))
        self.radioButton_NIST_Check.setText(_translate("MainWindow", "NIST"))
        self.label_QRNG_SIMULATOR_Qubits.setText(_translate("MainWindow", "Кубит"))
        self.label_QRNG_SIMULATOR_Num_of_Qubits.setText(_translate("MainWindow", "Размер регистра:"))
        self.pushButton_QRNG_SIMULATO_Start.setText(_translate("MainWindow", "Запустить КГСЧ на симуляторе"))
        self.label_QRNG_SIMULATOR_Num_of_Qubits_2.setText(_translate("MainWindow", "1"))
        self.label_QRNG_QPU_Select.setText(_translate("MainWindow", " Выберите КВУ:"))
        self.label_QRNG_JobID.setText(_translate("MainWindow", "JobID: "))
        self.pushButton_QRNG_JobID_Check.setText(_translate("MainWindow", "Сведения"))
        self.pushButton_QRNG_JobID_Cancel.setText(_translate("MainWindow", "Отменить"))
        self.pushButton_QRNG_JobID_Download.setText(_translate("MainWindow", "Скачать результаты"))
        self.label_2_QRNG_Num_of_Qubits.setText(_translate("MainWindow", "Размер регистра:"))
        self.label_QRNG_Num_of_Qubits.setText(_translate("MainWindow", "0"))
        self.label_QRNG_Qubits.setText(_translate("MainWindow", "Кубит"))
        self.label_ALPHA.setText(_translate("MainWindow", "Alpha: "))
        self.lineEdit_ALPHA.setText(_translate("MainWindow", "0.01"))
        self.label_QRNG_Shots.setText(_translate("MainWindow", "Shots: "))
        self.label_QRNG_OptLevel.setText(_translate("MainWindow", "Opt.Level: "))
        self.lineEdit_QRNG_Shots.setText(_translate("MainWindow", "20000"))
        self.lineEdit_QRNG_OptLevel.setText(_translate("MainWindow", "0"))
        self.pushButton_QRNG_Start.setText(_translate("MainWindow", "Запустить КГСЧ"))
        self.lineEdit_NIST_Key_Length.setText(_translate("MainWindow", "20000"))
        self.lineEdit_NIST_Parameters_on_Default.setText(_translate("MainWindow", "0"))
        self.lineEdit_NIST_Tests_Supplys.setText(_translate("MainWindow", "1"))
        self.label_NIST_Directory_to_Dataset.setText(_translate("MainWindow", "Папка с СП:"))
        self.pushButton_NIST_Start.setText(_translate("MainWindow", "Запустить NIST STS"))
        self.label_NIST_Key_Length.setText(_translate("MainWindow", "Длина СП:"))
        self.label_NIST_Tests_Supplys.setText(_translate("MainWindow", "Покрытие:"))
        self.label_NIST_Num_of_Bitstream.setText(_translate("MainWindow", "\'bitstream\':"))
        self.lineEdit_NIST_Format_of_Data.setText(_translate("MainWindow", "0"))
        self.lineEdit_NIST_Num_of_Bitstream.setText(_translate("MainWindow", "1"))
        self.label_NIST_Parameters_on_Default.setText(_translate("MainWindow", "Параметры:"))
        self.label_NIST_Format_of_Data.setText(_translate("MainWindow", "Формат:"))
        self.pushButton_Path_for_NIST_Dialog.setText(_translate("MainWindow", "Browse"))
        self.pushButton.setText(_translate("MainWindow", "Очистить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_QRNG), _translate("MainWindow", "КГСЧ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_QKD), _translate("MainWindow", "ККС ВРК"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Fourie), _translate("MainWindow", "Фурье"))
        self.menu.setTitle(_translate("MainWindow", "Меню 1"))
        self.menu_2.setTitle(_translate("MainWindow", "Меню 2"))
        self.action.setText(_translate("MainWindow", "Меню 1.1"))