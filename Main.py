#!/usr/bin/python
# -*- coding: utf-8 -*-
#

#from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import MainWindow
import SchedulingGuiHand
from grammar04 import *
from AlgtASAP import *
from AlgtALAP import *
from AlgtASAP_3 import *

Dirty = False

class WindowGuiHand(QDialog,SchedulingGuiHand.Ui_GuiHand):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.comboBox.currentIndexChanged.connect(self.selection)
        #self.graphicsView.wheelEvent = WindowGuiHand.wheelEvent(event)
        
    
    def wheelEvent(self,event):
        factor = 1.41 ** (-event.delta() / 240.0)
        self.graphicsView.scale(factor, factor)
  
    
    def selection(self):
        print (self.comboBox.currentText())
        if self.comboBox.currentText() == "Unconstrained":
           self.label_2.setEnabled(False) 
           self.spinBox.setEnabled(False)
           self.label_4.setEnabled(False)
           self.spinBox_2.setEnabled(False)
           self.label_5.setEnabled(False)
           self.spinBox_3.setEnabled(False)
           self.label_6.setEnabled(False)
           self.spinBox_4.setEnabled(False)
           self.label_7.setEnabled(False)
           self.spinBox_5.setEnabled(False)
           self.checkBoxOpt.setEnabled(True)
        elif self.comboBox.currentText() == "Time constrained":
           self.label_2.setEnabled(True) 
           self.spinBox.setEnabled(True)
           self.label_4.setEnabled(False)
           self.spinBox_2.setEnabled(False)
           self.label_5.setEnabled(False)
           self.spinBox_3.setEnabled(False)
           self.label_6.setEnabled(False)
           self.spinBox_4.setEnabled(False)
           self.label_7.setEnabled(False)
           self.spinBox_5.setEnabled(False)
           self.checkBoxOpt.setEnabled(False)
        elif self.comboBox.currentText() == "Resource constrained":
           self.label_2.setEnabled(False) 
           self.spinBox.setEnabled(False)
           self.label_4.setEnabled(True)
           self.spinBox_2.setEnabled(True)
           self.label_5.setEnabled(True)
           self.spinBox_3.setEnabled(True)
           self.label_6.setEnabled(True)
           self.spinBox_4.setEnabled(True)
           self.label_7.setEnabled(True)
           self.spinBox_5.setEnabled(True)
           self.checkBoxOpt.setEnabled(False)
        return self.comboBox.currentText()
        

    
        
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        self.label_info.setText("")
        self.label.setText("")
        #self.plainTextEdit_2.setPlainText("")
        if self.radioButton_2.isChecked():	
            if self.plainTextEdit_2.toPlainText() == "" :
                msg = "The input is empty"
                self.msgBox = QMessageBox() 
                self.msgBox.setText(msg)
                self.msgBox.exec_()
                
                ################################################
                # white
                ################################################
                scene = QGraphicsScene(self)
                item = QGraphicsPixmapItem(QPixmap("whitepaper.jpg"))
                scene.addItem(item)
                item.setFlags(QGraphicsItem.ItemIsSelectable|
                       QGraphicsItem.ItemIsMovable)
                self.graphicsView.setScene(scene)
           
            else:
                if TransfomerText(str(self.plainTextEdit_2.toPlainText())):
                   scene = QGraphicsScene(self)
                   item = QGraphicsPixmapItem(QPixmap("GraphScheduling.png"))
                   scene.addItem(item)
                   item.setFlags(QGraphicsItem.ItemIsSelectable|
                       QGraphicsItem.ItemIsMovable)
                   self.graphicsView.setScene(scene)
                else:
                   msg = "There is an error in the syntax"
                   self.msgBox = QMessageBox() 
                   self.msgBox.setText(msg)
                   self.msgBox.exec_()
                   ################################################
                   # white
                   ################################################
                   scene = QGraphicsScene(self)
                   item = QGraphicsPixmapItem(QPixmap("whitepaper.jpg"))
                   scene.addItem(item)
                   item.setFlags(QGraphicsItem.ItemIsSelectable|
                       QGraphicsItem.ItemIsMovable)
                   self.graphicsView.setScene(scene)
                         
                   
        if  self.radioButton_1.isChecked():	
            if self.plainTextEdit.toPlainText() == "" :
                msg = "The input is empty"
                self.msgBox = QMessageBox() 
                self.msgBox.setText(msg)
                self.msgBox.exec_()
            else:
				#######################################################
				# ASAP 
				#######################################################
                if self.radioButton_a.isChecked():
                    print ("******** UNCOSNTRAINED ASAP *************")	
                    if self.comboBox.currentText() == "Unconstrained":
                        pattern
                        try:
                            input_string=str(self.plainTextEdit.toPlainText())
                            #input_string="a+b"
                            print input_string
                            pattern.parseString(input_string)
                            if self.checkBoxOpt.isChecked():
                                SpecialFunction()
                            #Result.clear()
                            while Result:
							    Result.pop()
                            evaluateStack(exprStack)
                            #ShowResult()
                        except ParseException as err:
                            msg = "There is an error in the syntax"
                            self.msgBox = QMessageBox() 
                            self.msgBox.setText(msg)
                            self.msgBox.exec_()
                            L=['Parse Failure',input_string]
                            
                            ################################################
                            # white
                            ################################################
                            scene = QGraphicsScene(self)
                            item = QGraphicsPixmapItem(QPixmap("whitepaper.jpg"))
                            scene.addItem(item)
                            item.setFlags(QGraphicsItem.ItemIsSelectable|
                                 QGraphicsItem.ItemIsMovable)
                            self.graphicsView.setScene(scene)
                            
                            
                        StringR =ShowResult()
                        self.plainTextEdit_2.setPlainText(StringR)    
                        if TransfomerText(StringR):
                           scene = QGraphicsScene(self)
                           item = QGraphicsPixmapItem(QPixmap("GraphScheduling.png"))
                           scene.addItem(item)
                           item.setFlags(QGraphicsItem.ItemIsSelectable|
                               QGraphicsItem.ItemIsMovable)
                           self.graphicsView.setScene(scene)
                       
                        StringSummary = ""
                       
                        if TotalOperations[0] > 0:
                             StringSummary = StringSummary + str(TotalOperations[0]) + " Additions\n"
                        if TotalOperations[1] > 0:
                             StringSummary = StringSummary + str(TotalOperations[1]) +" Subtractions\n" 
                        if TotalOperations[2] > 0:
                             StringSummary = StringSummary + str(TotalOperations[2])+" Multiplications\n"
                        if TotalOperations[3] > 0:
                             StringSummary = StringSummary + str(TotalOperations[3]) +" Divisions\n" 
                       
                        self.label.setText( StringSummary)
                        TotalOperations[0] = 0
                        TotalOperations[1] = 0
                        TotalOperations[2] = 0
                        TotalOperations[3] = 0
                    elif self.comboBox.currentText() == "Time constrained":
                        print ("*********  TIME CONSTRAINED ASAP ***********")
                        #Result.clear()
                        while Result:
                            Result.pop()
                            evaluateStack(exprStack)
                        try:
                            pattern.parseString( str(self.plainTextEdit.toPlainText()) )
                            if self.checkBoxOpt.isChecked():
                                SpecialFunction()
                            Result.clear()
                            evaluateStack(exprStack)
                            #ShowResult()
                        except ParseException as err:
                            msg = "There is an error in the syntax"
                            self.msgBox = QMessageBox() 
                            self.msgBox.setText(msg)
                            self.msgBox.exec_()
                            #L=['Parse Failure',input_string]
                        #ShowResult()
                        StringR = ShowResulConstraint("Time constrained", self.spinBox.value(),0)
                        
                        if StringR == "It's impossible to solve in that number of clks steps":
                            message = "It can not be solved"
                            self.label_info.setText( "<font color=red size=12><b>" + message + "</b></font>")
                            ################################################
                            # white
                            ################################################
                            scene = QGraphicsScene(self)
                            item = QGraphicsPixmapItem(QPixmap("whitepaper.jpg"))
                            scene.addItem(item)
                            item.setFlags(QGraphicsItem.ItemIsSelectable|
                                 QGraphicsItem.ItemIsMovable)
                            self.graphicsView.setScene(scene)
                        else:
                            self.plainTextEdit_2.setPlainText(StringR)    
                            if TransfomerText(StringR):
                               scene = QGraphicsScene(self)
                               item = QGraphicsPixmapItem(QPixmap("GraphScheduling.png"))
                               scene.addItem(item)
                               item.setFlags(QGraphicsItem.ItemIsSelectable|
                                  QGraphicsItem.ItemIsMovable)
                               self.graphicsView.setScene(scene)
                               self.label_info.setText( "<font color=blue size=72><b>" + "It's done" + "</b></font>")
                        
                        
                        StringSummary = ""
                       
                        if TotalOperations[0] > 0:
                             StringSummary = StringSummary + str(TotalOperations[0]) + " Additions\n"
                        if TotalOperations[1] > 0:
                             StringSummary = StringSummary + str(TotalOperations[1]) +" Subtractions\n" 
                        if TotalOperations[2] > 0:
                             StringSummary = StringSummary + str(TotalOperations[2])+" Multiplications\n"
                        if TotalOperations[3] > 0:
                             StringSummary = StringSummary + str(TotalOperations[3]) +" Divisions\n" 
                       
                        self.label.setText( StringSummary)
                        TotalOperations[0] = 0
                        TotalOperations[1] = 0
                        TotalOperations[2] = 0
                        TotalOperations[3] = 0
                        
                    elif self.comboBox.currentText() == "Resource constrained":
                        print ("******** RESOURCE CONSTRAIDED ASAP *************")
                        
                        try:
                            pattern.parseString( str(self.plainTextEdit.toPlainText()) )
                            if self.checkBoxOpt.isChecked():
                                SpecialFunction()
                            Result.clear()
                            Units=[0,0,0,0]
                            Units=[self.spinBox_2.value(),self.spinBox_3.value(),self.spinBox_4.value(),self.spinBox_5.value()]
                            
                            
                            RES=evaluateStackR(exprStack,Units)
                            
                            if RES != "It's imposible":							   
                               HuResource=[0,0,0,0]
                               try:
                                   StringR=ShowResultR()
                                   SUM=0
                                   for var in HuResource:
                                      SUM = SUM + int(var)
                                   print ("************",HuResource,SUM)
                                   print ("XXXXXXXXXX",SUM)
                                   if SUM == 0:
                                       self.plainTextEdit_2.setPlainText(StringR)    
                                       if TransfomerText(StringR):
                                           scene = QGraphicsScene(self)
                                           item = QGraphicsPixmapItem(QPixmap("GraphScheduling.png"))
                                           scene.addItem(item)
                                           item.setFlags(QGraphicsItem.ItemIsSelectable|
                                              QGraphicsItem.ItemIsMovable)
                                           self.graphicsView.setScene(scene)
                                           self.label_info.setText( "<font color=blue size=72><b>" + "It's done" + "</b></font>")
                               except:
                                   message = "It can not be solved"
                                   self.label_info.setText( "<font color=red size=12><b>" + message + "</b></font>")
                                   ################################################
                                   # white
                                   ################################################
                                   scene = QGraphicsScene(self)
                                   item = QGraphicsPixmapItem(QPixmap("whitepaper.jpg"))
                                   scene.addItem(item)
                                   item.setFlags(QGraphicsItem.ItemIsSelectable|
                                       QGraphicsItem.ItemIsMovable)
                                   self.graphicsView.setScene(scene)  
                            if RES == "It's imposible" or SUM > 0 :
                                message = "It can not be solved"
                                self.label_info.setText( "<font color=red size=12><b>" + message + "</b></font>")
                                ################################################
                                # white
                                ################################################
                                scene = QGraphicsScene(self)
                                item = QGraphicsPixmapItem(QPixmap("whitepaper.jpg"))
                                scene.addItem(item)
                                item.setFlags(QGraphicsItem.ItemIsSelectable|
                                     QGraphicsItem.ItemIsMovable)
                                self.graphicsView.setScene(scene)
							
                            
                               
                               
                            #ShowResult()
                        except ParseException as err:
                            msg = "There is an error in the syntax"
                            self.msgBox = QMessageBox() 
                            self.msgBox.setText(msg)
                            self.msgBox.exec_()
                            #L=['Parse Failure',input_string]
                        
                        
                       
                if self.radioButton_b.isChecked():
					#######################################################
				    # ALAP 
				    #######################################################
                    if self.comboBox.currentText() == "Unconstrained":
                        print ("******** UNCOSNTRAINED ALAP *************")	
                        try:
                            pattern.parseString( str(self.plainTextEdit.toPlainText()) )
                            if self.checkBoxOpt.isChecked():
                                SpecialFunction()
                            #Result.clear()
                            while Result:
							    Result.pop()
                            evaluateStack(exprStack)
                            #evaluateStack(exprStack)
                            ShowResult()
                        
                            StringSummary = ""
                       
                            if TotalOperations[0] > 0:
                                StringSummary = StringSummary + str(TotalOperations[0]) + " Additions\n"
                            if TotalOperations[1] > 0:
                                StringSummary = StringSummary + str(TotalOperations[1]) +" Subtractions\n" 
                            if TotalOperations[2] > 0:
                                StringSummary = StringSummary + str(TotalOperations[2])+" Multiplications\n"
                            if TotalOperations[3] > 0:
                                StringSummary = StringSummary + str(TotalOperations[3]) +" Divisions\n" 
                        
                            self.label.setText( StringSummary)
                            TotalOperations[0] = 0
                            TotalOperations[1] = 0
                            TotalOperations[2] = 0
                            TotalOperations[3] = 0
                        
                        except ParseException as err:
                            msg = "There is an error in the syntax"
                            self.msgBox = QMessageBox() 
                            self.msgBox.setText(msg)
                            self.msgBox.exec_()
                            #L=['Parse Failure',input_string]
                        StringR =AlgoALAP()
                        self.plainTextEdit_2.setPlainText(StringR)
                        if TransfomerText(StringR):
                          scene = QGraphicsScene(self)
                          item = QGraphicsPixmapItem(QPixmap("GraphScheduling.png"))
                          scene.addItem(item)
                          item.setFlags(QGraphicsItem.ItemIsSelectable|
                             QGraphicsItem.ItemIsMovable)
                          self.graphicsView.setScene(scene)  
                    elif self.comboBox.currentText() == "Time constrained":
                        print ("*********  TIME CONSTRAINED ALAP ***********")
                        #Result.clear()
                        while Result:
                            Result.pop()
                            evaluateStack(exprStack)
                        try:
                            pattern.parseString( str(self.plainTextEdit.toPlainText()) )
                            if self.checkBoxOpt.isChecked():
                                SpecialFunction()
                            #Result.clear()
                            while Result:
                                Result.pop()
                                evaluateStack(exprStack)
                            evaluateStack(exprStack)
                            ShowResult()
                        except ParseException as err:
                            msg = "There is an error in the syntax"
                            self.msgBox = QMessageBox() 
                            self.msgBox.setText(msg)
                            self.msgBox.exec_()
                            #L=['Parse Failure',input_string]
                        #ShowResult()
                        StringR = AlgoALAPConstraint("Time constrained", self.spinBox.value(),0)
                        
                        
                        
                        if StringR == "It's impossible to solve in that number of clks steps":
                            message = "It can not be solved"
                            self.label_info.setText( "<font color=red size=12><b>" + message + "</b></font>")
                            ################################################
                            # white
                            ################################################
                            scene = QGraphicsScene(self)
                            item = QGraphicsPixmapItem(QPixmap("whitepaper.jpg"))
                            scene.addItem(item)
                            item.setFlags(QGraphicsItem.ItemIsSelectable|
                                 QGraphicsItem.ItemIsMovable)
                            self.graphicsView.setScene(scene)
                        else:
                            self.plainTextEdit_2.setPlainText(StringR)    
                            if TransfomerText(StringR):
                               scene = QGraphicsScene(self)
                               item = QGraphicsPixmapItem(QPixmap("GraphScheduling.png"))
                               scene.addItem(item)
                               item.setFlags(QGraphicsItem.ItemIsSelectable|
                                  QGraphicsItem.ItemIsMovable)
                               self.graphicsView.setScene(scene)
                               self.label_info.setText( "<font color=blue size=72><b>" + "It's done" + "</b></font>")
                        
                        
                        
                     
                       
                        StringSummary = ""
                       
                        if TotalOperations[0] > 0:
                             StringSummary = StringSummary + str(TotalOperations[0]) + " Additions\n"
                        if TotalOperations[1] > 0:
                             StringSummary = StringSummary + str(TotalOperations[1]) +" Subtractions\n" 
                        if TotalOperations[2] > 0:
                             StringSummary = StringSummary + str(TotalOperations[2])+" Multiplications\n"
                        if TotalOperations[3] > 0:
                             StringSummary = StringSummary + str(TotalOperations[3]) +" Divisions\n" 
                       
                        self.label.setText( StringSummary)
                        TotalOperations[0] = 0
                        TotalOperations[1] = 0
                        TotalOperations[2] = 0
                        TotalOperations[3] = 0
                        
                    elif self.comboBox.currentText() == "Resource constrained":
                        print ("******** RESOURCE CONSTRAIDED ALAP *************")
                        try:
                            pattern.parseString( str(self.plainTextEdit.toPlainText()) )
                            if self.checkBoxOpt.isChecked():
                                SpecialFunction()
                            #Result.clear()
                            while Result:
                                Result.pop()
                                evaluateStack(exprStack)
                            Units=[0,0,0,0]
                            Units=[self.spinBox_2.value(),self.spinBox_3.value(),self.spinBox_4.value(),self.spinBox_5.value()]
                            
                            #CounterOperationsR[0] = 0
                            #CounterOperationsR[1] = 0
                            #CounterOperationsR[2] = 0
                            #CounterOperationsR[3] = 0
                            
                            #CentinelOperationsR[0] = 1
                            #CentinelOperationsR[1] = 1
                            #CentinelOperationsR[2] = 1
                            #CentinelOperationsR[3] = 1
                                                        
                            RES=evaluateStackR(exprStack,Units)
                            if RES != "It's imposible":	
                                #HuResource[0] = 0
                                #HuResource[1] = 0
                                #HuResource[2] = 0
                                #HuResource[3] = 0
                                SUM=0
                                for val in Units:
                                    SUM = val +SUM
                                #print ("************",HuResource[0],SUM)
                                print ("XXXXXXXXXX",SUM)
                                if SUM != 0:
							   
                                   ShowResultR()
                                   StringR=AlgoALAPR(Units)
                                   self.plainTextEdit_2.setPlainText(StringR)    
                                   if TransfomerText(StringR):
                                       
                                       
                                       StringSummary = ""
                                       print ("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                                       if TotalOperationsR[0] > 0:
                                           StringSummary = StringSummary + str(TotalOperationsR[0]) + " Additions\n"
                                       if TotalOperationsR[1] > 0:
                                            StringSummary = StringSummary + str(TotalOperationsR[1]) +" Subtractions\n" 
                                       if TotalOperationsR[2] > 0:
                                           StringSummary = StringSummary + str(TotalOperationsR[2])+" Multiplications\n"
                                       if TotalOperationsR[3] > 0:
                                           StringSummary = StringSummary + str(TotalOperationsR[3]) +" Divisions\n" 
                       
                                       self.label.setText( StringSummary)
                                       TotalOperationsR[0] = 0
                                       TotalOperationsR[1] = 0
                                       TotalOperationsR[2] = 0
                                       TotalOperationsR[3] = 0
                                       NumUnitR=0
                                       HuResource = [0,0,0,0,0]
                                       
                                       self.label_info.setText( "<font color=blue size=72><b>" + "It's done" + "</b></font>")
                                       
                                       scene = QGraphicsScene(self)
                                       item = QGraphicsPixmapItem(QPixmap("GraphScheduling.png"))
                                       scene.addItem(item)
                                       item.setFlags(QGraphicsItem.ItemIsSelectable|
                                           QGraphicsItem.ItemIsMovable)
                                       self.graphicsView.setScene(scene)
                                       
                       
                                       
                            
                            if RES == "It's imposible" or SUM == 0:
                                message = "It can not be solved"
                                self.label_info.setText( "<font color=red size=12><b>" + message + "</b></font>")
                                ################################################
                                # white
                                ################################################
                                scene = QGraphicsScene(self)
                                item = QGraphicsPixmapItem(QPixmap("whitepaper.jpg"))
                                scene.addItem(item)
                                item.setFlags(QGraphicsItem.ItemIsSelectable|
                                     QGraphicsItem.ItemIsMovable)
                                self.graphicsView.setScene(scene)	
                        except ParseException as err:
                            msg = "There is an error in the syntax"
                            self.msgBox = QMessageBox() 
                            self.msgBox.setText(msg)
                            self.msgBox.exec_()
                            #L=['Parse Failure',input_string]
                
                if self.radioButton_c.isChecked():
                    print ("******** RESOURCE CONSTRAIDED HU's *************")	
                    try:
                        pattern.parseString(str(self.plainTextEdit.toPlainText()) )
                        SpecialFunction()
                        #Result.clear()
                        while Result:
                            Result.pop()
                        Units=[0,0,0,0]
                        Units=[self.spinBox_2.value(),self.spinBox_3.value(),self.spinBox_4.value(),self.spinBox_5.value()]
                           
                        CounterOperationsR = [0,0,0,0,0]
                        CentinelOperationsR = [1,1,1,1,1]
                            
                        RES=evaluateStackR(exprStack,Units)
                        if RES != "It's imposible":	
                            HuResource = [0,0,0,0,0]
                            SUM=0
                            for val in HuResource:
                                SUM = val +SUM
                            print ("************",HuResource[0],SUM)
                            print ("XXXXXXXXXX",SUM)
                            if SUM == 0:
                                try:
                                    ShowResultR()
                                    StringR=AlgoALAPR(Units)
                                    self.plainTextEdit_2.setPlainText(StringR)    
                                    if TransfomerText(StringR):
                                        scene = QGraphicsScene(self)
                                        item = QGraphicsPixmapItem(QPixmap("GraphScheduling.png"))
                                        scene.addItem(item)
                                        item.setFlags(QGraphicsItem.ItemIsSelectable|
                                            QGraphicsItem.ItemIsMovable)
                                        self.graphicsView.setScene(scene)
                                        self.label_info.setText( "<font color=blue size=72><b>" + "It's done" + "</b></font>")
                                except:
                                    message = "It can not be solved"
                                    self.label_info.setText( "<font color=red size=12><b>" + message + "</b></font>")
                                    ################################################
                                    # white
                                    ################################################
                                    scene = QGraphicsScene(self)
                                    item = QGraphicsPixmapItem(QPixmap("whitepaper.jpg"))
                                    scene.addItem(item)
                                    item.setFlags(QGraphicsItem.ItemIsSelectable|
                                    QGraphicsItem.ItemIsMovable)
                                    self.graphicsView.setScene(scene)
                            
                        if RES == "It's imposible" or SUM > 0:
                            message = "It can not be solved"
                            self.label_info.setText( "<font color=red size=12><b>" + message + "</b></font>")
                            ################################################
                            # white
                            ################################################
                            scene = QGraphicsScene(self)
                            item = QGraphicsPixmapItem(QPixmap("whitepaper.jpg"))
                            scene.addItem(item)
                            item.setFlags(QGraphicsItem.ItemIsSelectable|
                                 QGraphicsItem.ItemIsMovable)
                            self.graphicsView.setScene(scene)
                    except ParseException as err:
                        msg = "There is an error in the syntax"
                        self.msgBox = QMessageBox() 
                        self.msgBox.setText(msg)
                        self.msgBox.exec_()
                        L=['Parse Failure',input_string]
                    
                    
    @pyqtSignature("")
    def on_radioButton_2_clicked(self):
        self.radioButton_1.setChecked(False)
        self.plainTextEdit_2.setEnabled(True)
        self.groupBox.setEnabled(False)
        self.comboBox.setEnabled(False)
        self.plainTextEdit.setEnabled(False)
        self.spinBox.setEnabled(False)
        self.spinBox_2.setEnabled(False)
        self.spinBox_3.setEnabled(False)
        self.spinBox_4.setEnabled(False)
        self.spinBox_5.setEnabled(False)

    @pyqtSignature("")
    def on_radioButton_1_clicked(self):
        self.radioButton_2.setChecked(False)
        self.plainTextEdit_2.setEnabled(False)
        self.groupBox.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.plainTextEdit.setEnabled(True)
        
    @pyqtSignature("")
    def on_radioButton_a_clicked(self):
         self.comboBox.setEnabled(True)
         if self.comboBox.currentText() == "Unconstrained":
           self.label_2.setEnabled(False) 
           self.spinBox.setEnabled(False)
           self.label_4.setEnabled(False)
           self.spinBox_2.setEnabled(False)
           self.label_5.setEnabled(False)
           self.spinBox_3.setEnabled(False)
           self.label_6.setEnabled(False)
           self.spinBox_4.setEnabled(False)
           self.label_7.setEnabled(False)
           self.spinBox_5.setEnabled(False)
           self.checkBoxOpt.setEnabled(True)
         elif self.comboBox.currentText() == "Time constrained":
           self.label_2.setEnabled(True) 
           self.spinBox.setEnabled(True)
           self.label_4.setEnabled(False)
           self.spinBox_2.setEnabled(False)
           self.label_5.setEnabled(False)
           self.spinBox_3.setEnabled(False)
           self.label_6.setEnabled(False)
           self.spinBox_4.setEnabled(False)
           self.label_7.setEnabled(False)
           self.spinBox_5.setEnabled(False)
           self.checkBoxOpt.setEnabled(False)
         elif self.comboBox.currentText() == "Resource constrained":
           self.label_2.setEnabled(False) 
           self.spinBox.setEnabled(False)
           self.label_4.setEnabled(True)
           self.spinBox_2.setEnabled(True)
           self.label_5.setEnabled(True)
           self.spinBox_3.setEnabled(True)
           self.label_6.setEnabled(True)
           self.spinBox_4.setEnabled(True)
           self.label_7.setEnabled(True)
           self.spinBox_5.setEnabled(True)
           self.checkBoxOpt.setEnabled(False)
        
    @pyqtSignature("")
    def on_radioButton_b_clicked(self):
         self.comboBox.setEnabled(True)
         if self.comboBox.currentText() == "Unconstrained":
           self.label_2.setEnabled(False) 
           self.spinBox.setEnabled(False)
           self.label_4.setEnabled(False)
           self.spinBox_2.setEnabled(False)
           self.label_5.setEnabled(False)
           self.spinBox_3.setEnabled(False)
           self.label_6.setEnabled(False)
           self.spinBox_4.setEnabled(False)
           self.label_7.setEnabled(False)
           self.spinBox_5.setEnabled(False)
           self.checkBoxOpt.setEnabled(True)
         elif self.comboBox.currentText() == "Time constrained":
           self.label_2.setEnabled(True) 
           self.spinBox.setEnabled(True)
           self.label_4.setEnabled(False)
           self.spinBox_2.setEnabled(False)
           self.label_5.setEnabled(False)
           self.spinBox_3.setEnabled(False)
           self.label_6.setEnabled(False)
           self.spinBox_4.setEnabled(False)
           self.label_7.setEnabled(False)
           self.spinBox_5.setEnabled(False)
           self.checkBoxOpt.setEnabled(False)
         elif self.comboBox.currentText() == "Resource constrained":
           self.label_2.setEnabled(False) 
           self.spinBox.setEnabled(False)
           self.label_4.setEnabled(True)
           self.spinBox_2.setEnabled(True)
           self.label_5.setEnabled(True)
           self.spinBox_3.setEnabled(True)
           self.label_6.setEnabled(True)
           self.spinBox_4.setEnabled(True)
           self.label_7.setEnabled(True)
           self.spinBox_5.setEnabled(True)
           self.checkBoxOpt.setEnabled(False)
        
    @pyqtSignature("")
    def on_radioButton_c_clicked(self):
        self.comboBox.setEnabled(False)    
        self.spinBox.setEnabled(False)
        self.spinBox_2.setEnabled(True)
        self.spinBox_3.setEnabled(True)
        self.spinBox_4.setEnabled(True)
        self.spinBox_5.setEnabled(True)
        self.checkBoxOpt.setEnabled(False)
  

class MainWindow(QDialog, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.dialog = WindowGuiHand(self)
        

    def on_pushButton_clicked(self):
        self.dialog.show()
        self.hide()

def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

