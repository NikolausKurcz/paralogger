# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'paraloger_GUI1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1209, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_project_tree = QtWidgets.QLabel(self.centralwidget)
        self.label_project_tree.setObjectName("label_project_tree")
        self.verticalLayout.addWidget(self.label_project_tree)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.treeWidget)
        self.label_object_details = QtWidgets.QLabel(self.centralwidget)
        self.label_object_details.setObjectName("label_object_details")
        self.verticalLayout.addWidget(self.label_object_details)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(3, 4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.main_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.main_tabWidget.setObjectName("main_tabWidget")
        self.tab_graph = QtWidgets.QWidget()
        self.tab_graph.setObjectName("tab_graph")
        self.main_tabWidget.addTab(self.tab_graph, "")
        self.tab_table = QtWidgets.QWidget()
        self.tab_table.setObjectName("tab_table")
        self.main_tabWidget.addTab(self.tab_table, "")
        self.tab_3d = QtWidgets.QWidget()
        self.tab_3d.setObjectName("tab_3d")
        self.main_tabWidget.addTab(self.tab_3d, "")
        self.tab_analysis = QtWidgets.QWidget()
        self.tab_analysis.setObjectName("tab_analysis")
        self.groupBox_analysis_info = QtWidgets.QGroupBox(self.tab_analysis)
        self.groupBox_analysis_info.setGeometry(QtCore.QRect(19, 19, 921, 81))
        self.groupBox_analysis_info.setObjectName("groupBox_analysis_info")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_analysis_info)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 0, 521, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_hash_judge = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_hash_judge.setObjectName("label_hash_judge")
        self.gridLayout_2.addWidget(self.label_hash_judge, 1, 0, 1, 1)
        self.label_judge = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_judge.setObjectName("label_judge")
        self.gridLayout_2.addWidget(self.label_judge, 0, 0, 1, 1)
        self.label_hash_dict = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_hash_dict.setObjectName("label_hash_dict")
        self.gridLayout_2.addWidget(self.label_hash_dict, 2, 0, 1, 1)
        self.label_judge_file = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_judge_file.setObjectName("label_judge_file")
        self.gridLayout_2.addWidget(self.label_judge_file, 0, 1, 1, 1)
        self.label_hash_judge_value = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_hash_judge_value.setObjectName("label_hash_judge_value")
        self.gridLayout_2.addWidget(self.label_hash_judge_value, 1, 1, 1, 1)
        self.label_hash_crit_value = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_hash_crit_value.setObjectName("label_hash_crit_value")
        self.gridLayout_2.addWidget(self.label_hash_crit_value, 2, 1, 1, 1)
        self.tableWidget_analysis = QtWidgets.QTableWidget(self.tab_analysis)
        self.tableWidget_analysis.setGeometry(QtCore.QRect(15, 121, 911, 541))
        self.tableWidget_analysis.setObjectName("tableWidget_analysis")
        self.tableWidget_analysis.setColumnCount(0)
        self.tableWidget_analysis.setRowCount(0)
        self.label = QtWidgets.QLabel(self.tab_analysis)
        self.label.setGeometry(QtCore.QRect(30, 100, 421, 16))
        self.label.setObjectName("label")
        self.main_tabWidget.addTab(self.tab_analysis, "")
        self.tab_log = QtWidgets.QWidget()
        self.tab_log.setObjectName("tab_log")
        self.main_tabWidget.addTab(self.tab_log, "")
        self.tab_console = QtWidgets.QWidget()
        self.tab_console.setObjectName("tab_console")
        self.main_tabWidget.addTab(self.tab_console, "")
        self.horizontalLayout.addWidget(self.main_tabWidget)
        self.horizontalLayout.setStretch(1, 5)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1209, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menudebug = QtWidgets.QMenu(self.menubar)
        self.menudebug.setObjectName("menudebug")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionimport = QtWidgets.QAction(MainWindow)
        self.actionimport.setObjectName("actionimport")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actiondebug_open = QtWidgets.QAction(MainWindow)
        self.actiondebug_open.setObjectName("actiondebug_open")
        self.actionopen_console = QtWidgets.QAction(MainWindow)
        self.actionopen_console.setObjectName("actionopen_console")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionimport)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionVersion)
        self.menudebug.addAction(self.actiondebug_open)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menudebug.menuAction())

        self.retranslateUi(MainWindow)
        self.main_tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_project_tree.setText(_translate("MainWindow", "Tree"))
        self.label_object_details.setText(_translate("MainWindow", "Details:"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab_graph), _translate("MainWindow", "Graph"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab_table), _translate("MainWindow", "Table"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab_3d), _translate("MainWindow", "3D"))
        self.groupBox_analysis_info.setTitle(_translate("MainWindow", "General infos: "))
        self.label_hash_judge.setText(_translate("MainWindow", "Judge Hash:"))
        self.label_judge.setText(_translate("MainWindow", "Judge :"))
        self.label_hash_dict.setText(_translate("MainWindow", "Criteria Hash :"))
        self.label_judge_file.setText(_translate("MainWindow", "No file loaded"))
        self.label_hash_judge_value.setText(_translate("MainWindow", "no data"))
        self.label_hash_crit_value.setText(_translate("MainWindow", "no data"))
        self.label.setText(_translate("MainWindow", "Note : the grading  is not relevant at all , only there for  testing !!"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab_analysis), _translate("MainWindow", "Analysis"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab_log), _translate("MainWindow", "Log"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tab_console), _translate("MainWindow", "Console"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuAbout.setTitle(_translate("MainWindow", "Abo&ut"))
        self.menudebug.setTitle(_translate("MainWindow", "debug"))
        self.actionOpen.setText(_translate("MainWindow", "&Open"))
        self.actionimport.setText(_translate("MainWindow", "&import"))
        self.actionHelp.setText(_translate("MainWindow", "&Help"))
        self.actionVersion.setText(_translate("MainWindow", "&Version"))
        self.actionSave_as.setText(_translate("MainWindow", "&Save_as"))
        self.actiondebug_open.setText(_translate("MainWindow", "debug_open"))
        self.actionopen_console.setText(_translate("MainWindow", "open_console"))

