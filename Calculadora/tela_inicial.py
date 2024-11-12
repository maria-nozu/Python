import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import tela
import tradicional
import cientifica
import math



class controller:
    def __init__(self):
        self.tela_Window = QtWidgets.QMainWindow()
        self.tela_ui = tela.Ui_Dialog()
        self.tela_ui.setupUi(self.tela_Window)
        
        self.tradicional_Window = QtWidgets.QMainWindow()
        self.tradicional_ui = tradicional.Ui_Dialog()
        self.tradicional_ui.setupUi(self.tradicional_Window)
        
        self.cientifica_Window = QtWidgets.QMainWindow()
        self.cientifica_ui = cientifica.Ui_Dialog()
        self.cientifica_ui.setupUi(self.cientifica_Window)
        
        self.tela_ui.pushButton.clicked.connect(self.show_calc)

        self.tradicional_ui.b0.clicked.connect(self.digita)
        self.tradicional_ui.b1.clicked.connect(self.digita)
        self.tradicional_ui.b2.clicked.connect(self.digita)
        self.tradicional_ui.b3.clicked.connect(self.digita)
        self.tradicional_ui.b4.clicked.connect(self.digita)
        self.tradicional_ui.b5.clicked.connect(self.digita)
        self.tradicional_ui.b6.clicked.connect(self.digita)
        self.tradicional_ui.b7.clicked.connect(self.digita)
        self.tradicional_ui.b8.clicked.connect(self.digita)
        self.tradicional_ui.b9.clicked.connect(self.digita)
        self.tradicional_ui.bp.clicked.connect(self.digita)
        self.tradicional_ui.div.clicked.connect(self.digita)
        self.tradicional_ui.eq.clicked.connect(self.op_equal)
        self.tradicional_ui.mult.clicked.connect(self.digita)
        self.tradicional_ui.sub.clicked.connect(self.digita)
        self.tradicional_ui.sum.clicked.connect(self.digita)
        self.tradicional_ui.back.clicked.connect(self.op_back)
        self.tradicional_ui.clear.clicked.connect(self.op_clear)

        self.cientifica_ui.b0.clicked.connect(self.digita)
        self.cientifica_ui.b1.clicked.connect(self.digita)
        self.cientifica_ui.b2.clicked.connect(self.digita)
        self.cientifica_ui.b3.clicked.connect(self.digita)
        self.cientifica_ui.b4.clicked.connect(self.digita)
        self.cientifica_ui.b5.clicked.connect(self.digita)
        self.cientifica_ui.b6.clicked.connect(self.digita)
        self.cientifica_ui.b7.clicked.connect(self.digita)
        self.cientifica_ui.b8.clicked.connect(self.digita)
        self.cientifica_ui.b9.clicked.connect(self.digita)
        self.cientifica_ui.bp.clicked.connect(self.digita)
        self.cientifica_ui.eq.clicked.connect(self.op_equal)
        self.cientifica_ui.div.clicked.connect(self.digita)
        self.cientifica_ui.mult.clicked.connect(self.digita)
        self.cientifica_ui.sub.clicked.connect(self.digita)
        self.cientifica_ui.sum.clicked.connect(self.digita)
        self.cientifica_ui.pi.clicked.connect(self.op_pi)
        self.cientifica_ui.raiz.clicked.connect(self.op_raiz)
        self.cientifica_ui.quad.clicked.connect(self.op_quad)
        self.cientifica_ui.cos.clicked.connect(self.op_cos)
        self.cientifica_ui.sin.clicked.connect(self.op_sin)
        self.cientifica_ui.tg.clicked.connect(self.op_tg)
        self.cientifica_ui.back.clicked.connect(self.op_back)
        self.cientifica_ui.clear.clicked.connect(self.op_clear)



    def digita(self):
        sender = self.tradicional_Window.sender()
        self.tradicional_ui.telt.setText( self.tradicional_ui.telt.text() + sender.text() )
        sender = self.cientifica_Window.sender()
        self.cientifica_ui.telc.setText( self.cientifica_ui.telc.text() + sender.text() )

    def op_pi(self):
        self.cientifica_ui.telc.setText(self.cientifica_ui.telc.text() + str(round(math.pi,6)))
        exppi = self.cientifica_ui.telc.text()
        r = eval(exppi)
        self.cientifica_ui.telc.setText(str(r)) 


    def op_tg(self):
        try:
            r = math.tan(math.radians(float(self.cientifica_ui.telc.text())))
            self.cientifica_ui.telc.setText(str(round(r,6)))
        except:
            self.tradicional_ui.telt.setText("Error")
            self.cientifica_ui.telc.setText("Error")

    def op_sin(self):
        try:
            r = math.sin(math.radians(float(self.cientifica_ui.telc.text())))
            self.cientifica_ui.telc.setText(str(round(r,6)))
        except:
            self.tradicional_ui.telt.setText("Error")
            self.cientifica_ui.telc.setText("Error")

    def op_raiz(self):
        try:
            r = math.sqrt(float(self.cientifica_ui.telc.text()))
            self.cientifica_ui.telc.setText(str(r))
        except:
            self.tradicional_ui.telt.setText("Error")
            self.cientifica_ui.telc.setText("Error")

    def op_quad(self):
        try:
            r = pow(float(self.cientifica_ui.telc.text()),2)
            self.cientifica_ui.telc.setText(str(r))
        except:
            self.tradicional_ui.telt.setText("Error")
            self.cientifica_ui.telc.setText("Error")

    def op_cos(self):
        try:
            r = math.cos(math.radians(float(self.cientifica_ui.telc.text())))
            self.cientifica_ui.telc.setText(str(round(r,6)))
        except:
            self.tradicional_ui.telt.setText("Error")
            self.cientifica_ui.telc.setText("Error")
 

    def op_equal(self):


        expt = self.tradicional_ui.telt.text()
        expc = self.cientifica_ui.telc.text()
        
        try:

            anst = eval(expt)
            ansc = eval(expc)
            self.tradicional_ui.telt.setText(str(anst))
            self.cientifica_ui.telc.setText(str(ansc))
            
        except:
            self.tradicional_ui.telt.setText("Error")
            self.cientifica_ui.telc.setText("Error")


    def op_clear(self):
        # clear label text
        self.tradicional_ui.telt.setText("")
        self.cientifica_ui.telc.setText("")

    def op_back(self):

        exp = self.tradicional_ui.telt.text()
        self.tradicional_ui.telt.setText(exp[:-1])
        exp = self.cientifica_ui.telc.text()
        self.cientifica_ui.telc.setText(exp[:-1])


    def show_calc(self):
        if self.tela_ui.radioButton.isChecked():
            self.tradicional_Window.show()
            self.tradicional_ui.telt.setText("")
        
            
        if self.tela_ui.radioButton_2.isChecked():
            self.cientifica_Window.show()
            self.cientifica_ui.telc.setText("")

        if not(self.tela_ui.radioButton.isChecked()) and not (self.tela_ui.radioButton_2.isChecked()):
            QtWidgets.QMessageBox.about(self.tela_Window, "Erro", "escolha uma opção!")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = controller()
    controller.tela_Window.show()
    sys.exit(app.exec_())