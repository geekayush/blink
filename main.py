# Import Library
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTextBrowser, QPushButton, QMenu, QMenuBar, QStatusBar, QAction
import numpy as np
import cv2
import time
import random
import autocomplete
import subprocess
import os.path
import sms
import whatsapp

# colourLoop constants
letRowNorm = ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
              "p, li { white-space: pre-wrap; }\n"
              "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>"]
letRowBold = ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
              "p, li { white-space: pre-wrap; }\n"
              "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b style=\"color: red;\">ABCDE</b></span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
              "p, li { white-space: pre-wrap; }\n"
              "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b style=\"color: red;\">FGHIJ</b></span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
              "p, li { white-space: pre-wrap; }\n"
              "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b style=\"color: red;\">KLMNO</b></span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
              "p, li { white-space: pre-wrap; }\n"
              "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b style=\"color: red;\">PQRST</b></span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
              "p, li { white-space: pre-wrap; }\n"
              "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
              "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b style=\"color: red;\">UVWXYZ</b></span></p></body></html>"]
letColBold = [["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b style=\"color: red;\">A</b>BCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">A<b style=\"color: red;\">B</b>CDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">AB<b style=\"color: red;\">C</b>DE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABC<b style=\"color: red;\">D</b>E</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCD<b style=\"color: red;\">E</b></span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>"],
              ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b style=\"color: red;\">F</b>GHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">F<b style=\"color: red;\">G</b>HIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FG<b style=\"color: red;\">H</b>IJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGH<b style=\"color: red;\">I</b>J</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHI<b style=\"color: red;\">J</b></span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>"],
              ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b style=\"color: red;\">K</b>LMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">K<b style=\"color: red;\">L</b>MNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KL<b style=\"color: red;\">M</b>NO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLM<b style=\"color: red;\">N</b>O</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMN<b style=\"color: red;\">O</b></span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>"],
              ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b style=\"color: red;\">P</b>QRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">P<b style=\"color: red;\">Q</b>RST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQ<b style=\"color: red;\">R</b>ST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQR<b style=\"color: red;\">S</b>T</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRS<b style=\"color: red;\">T</b></span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>"],
              ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b style=\"color:red;\">U</b>VWXYZ</span></p></body></html>", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">U<b style=\"color: red;\">V</b>WXYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UV<b style=\"color: red;\">W</b>XYZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVW<b style=\"color: red;\">X</b>YZ</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWX<b style=\"color: red;\">Y</b>Z</span></p></body></html>", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
               "p, li { white-space: pre-wrap; }\n"
               "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
               "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXY<b style=\"color: red;\">Z</b></span></p></body></html>"]]


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

# Face Cascades
face_cascade = cv2.CascadeClassifier(
    'haarCascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    'haarCascades/haarcascade_eye_tree_eyeglasses.xml')
# pupil_cascade = cv2.CascadeClassifier('haarcascade_eye2.xml')

# Number signifies camera
cap = cv2.VideoCapture(0)

# Eye constants
bothEyesClosedStart = False
bothEyesClosedStartTime = 0
bothFirst = 0
leftEyeClosedStart = False
leftEyeClosedStartTime = 0
leftFirst = 0
rightEyeClosedStart = False
rightEyeClosedStartTime = 0
rightFirst = 0

autocomplete.load()

NUM_ROWS_OF_LETTERS = 5
letColCount = -1
letRowCount = -1
stopRow = False
letters = [["a", "b", "c", "d", "e"], ["f", "g", "h", "i", "j"], [
    "k", "l", "m", "n", "o"], ["p", "q", "r", "s", "t"], ["u", "v", "w", "x", "y", "z"]]
currentSentence = ""
wholeText = ""
vidOpen = False


def tick():
    # Eye constants
    global bothEyesClosedStart
    global bothEyesClosedStartTime
    global bothFirst
    global leftEyeClosedStart
    global leftEyeClosedStartTime
    global leftFirst
    global rightEyeClosedStart
    global rightEyeClosedStartTime
    global rightFirst
    global timerColour
    global stopRow
    global letRowCount
    global letColCount
    global letters
    global currentSentence
    global wholeText
    global ui
    global row5
    global row6
    global vidOpen
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 1:
        # Draw Face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_grayLeft = gray[y:y+h, x:x+w//2]
            roi_grayRight = gray[y:y+h, x+w//2:x+w]
            roi_color = img[y:y+h, x:x+w]
            leftEye = eye_cascade.detectMultiScale(roi_grayLeft)
            rightEye = eye_cascade.detectMultiScale(roi_grayRight)
            # Blink
            if len(leftEye) == 0 and len(rightEye) == 0:
                if bothEyesClosedStart == False:
                    timerColour.stop()
                    bothEyesClosedStartTime = time.time()
                    bothEyesClosedStart = True
                elif time.time() - bothEyesClosedStartTime > 5:
                    sms.send("Emergency!")
                    whatsapp.send("Emergency!")
                    subprocess.call(["afplay", "emergency.wav"])
                elif time.time() - bothEyesClosedStartTime > .75 and bothFirst == 0:
                    subprocess.call(["afplay", "bleep.wav"])
                    bothFirst = 1
                    if stopRow == False:
                        stopRow = True
                    else:
                        stopRow = False
                        if letRowCount < 5:
                            currentSentence += letters[letRowCount][letColCount]
                            if len(currentSentence) == 1:
                                currentSentence = currentSentence.upper()
                        elif letRowCount == 5:
                            row5[letColCount]()
                        elif letRowCount == 6:
                            row6[letColCount]()
                        if ui.go:
                            ui.textBrowser_4.setText(currentSentence)
                            letRowCount = -1
                            letColCount = -1
                            ui.predictNextWord()
            # Left Wink
            elif len(leftEye) == 1 and len(rightEye) == 0:
                if rightEyeClosedStart == False:
                    timerColour.stop()
                    rightEyeClosedStartTime = time.time()
                    rightEyeClosedStart = True
                elif time.time()-rightEyeClosedStartTime > 1.5 and rightFirst == 0:
                    rightFirst = 1
            # Right Wink
            elif len(leftEye) == 0 and len(rightEye) == 1:
                if leftEyeClosedStart == False:
                    timerColour.stop()
                    leftEyeClosedStartTime = time.time()
                    leftEyeClosedStart = True
                elif time.time()-leftEyeClosedStartTime > 1.5 and leftFirst == 0:
                    leftFirst = 1
            # Eyes Open
            elif len(leftEye) == 1 and len(rightEye) == 1:
                bothFirst = 0
                bothEyesClosedStart = False
                bothEyesClosedStartTime = time.time()
                rightFirst = 0
                rightEyeClosedStart = False
                leftEyeClosedStartTime = time.time()
                leftFirst = 0
                leftEyeClosedStart = False
                rightEyeClosedStartTime = time.time()
                if timerColour.isActive() == False:
                    timerColour.start(1000)
            # Draw Eyes
            for (ex, ey, ew, eh) in rightEye:
                cv2.rectangle(roi_color, (ex+w//2, ey),
                              (ex+ew+w//2, ey+eh), (255, 255, 0), 2)
            for (ex, ey, ew, eh) in leftEye:
                cv2.rectangle(roi_color, (ex, ey),
                              (ex+ew, ey+eh), (0, 255, 0), 2)
    cv2.imshow('Video Feed', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        cap.release()
        cv2.destroyAllWindows()
        # server.quit()
        return 0


def close():
    cap.release()
    cv2.destroyAllWindows()
    return 0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.addLnOnly = True
        MainWindow.setObjectName(_fromUtf8("Translator"))
        MainWindow.resize(700, 500)
        self.go = True
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 320, 250))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(360, 20, 320, 250))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 280, 100, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.pauseBut)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 280, 100, 30))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.addSpace)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 280, 100, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.delLet)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 280, 100, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.pushSentenceToBody)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 280, 100, 30))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(self.reciteBut)
        self.textBrowser_3 = QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 320, 211, 41))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(240, 320, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.clicked.connect(self.nurseBut)
        self.textBrowser_4 = QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 380, 471, 51))
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(510, 380, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_8.clicked.connect(self.openCam)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuStart_Stop_Sel = QMenu(self.menuSettings)
        self.menuStart_Stop_Sel.setObjectName(_fromUtf8("menuStart_Stop_Sel"))
        self.menuFinger = QMenu(self.menuSettings)
        self.menuFinger.setObjectName(_fromUtf8("menuFinger"))
        self.menuLetter_Sel = QMenu(self.menuSettings)
        self.menuLetter_Sel.setObjectName(_fromUtf8("menuLetter_Sel"))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionWord_Sel = QAction(MainWindow)
        self.actionWord_Sel.setObjectName(_fromUtf8("actionWord_Sel"))
        self.actionBlink = QAction(MainWindow)
        self.actionBlink.setObjectName(_fromUtf8("actionBlink"))
        self.actionLeft_Wink = QAction(MainWindow)
        self.actionLeft_Wink.setObjectName(_fromUtf8("actionLeft_Wink"))
        self.actionRight_Wink = QAction(MainWindow)
        self.actionRight_Wink.setObjectName(_fromUtf8("actionRight_Wink"))
        self.actionBlink_2 = QAction(MainWindow)
        self.actionBlink_2.setObjectName(_fromUtf8("actionBlink_2"))
        self.actionLeft_Wink_2 = QAction(MainWindow)
        self.actionLeft_Wink_2.setObjectName(_fromUtf8("actionLeft_Wink_2"))
        self.actionRight_Wink_2 = QAction(MainWindow)
        self.actionRight_Wink_2.setObjectName(_fromUtf8("actionRight_Wink_2"))
        self.actionAbout_EyeTotText = QAction(MainWindow)
        self.actionAbout_EyeTotText.setObjectName(
            _fromUtf8("actionAbout_EyeTotText"))
        self.actionContact_Developer = QAction(MainWindow)
        self.actionContact_Developer.setObjectName(
            _fromUtf8("actionContact_Developer"))
        self.menuStart_Stop_Sel.addAction(self.actionBlink)
        self.menuStart_Stop_Sel.addAction(self.actionLeft_Wink)
        self.menuStart_Stop_Sel.addAction(self.actionRight_Wink)
        self.menuFinger.addAction(self.actionBlink)
        self.menuFinger.addAction(self.actionLeft_Wink)
        self.menuFinger.addAction(self.actionRight_Wink)
        self.menuLetter_Sel.addAction(self.actionBlink_2)
        self.menuLetter_Sel.addAction(self.actionLeft_Wink_2)
        self.menuLetter_Sel.addAction(self.actionRight_Wink_2)
        self.menuSettings.addAction(self.menuStart_Stop_Sel.menuAction())
        self.menuSettings.addAction(self.menuLetter_Sel.menuAction())
        self.menuSettings.addAction(self.menuFinger.menuAction())
        self.menuSettings.addSeparator()
        self.menuHelp.addAction(self.actionAbout_EyeTotText)
        self.menuHelp.addAction(self.actionContact_Developer)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.buts = [[self.pushButton, self.pushButton_2, self.pushButton_3,
                      self.pushButton_4, self.pushButton_5], [self.textBrowser_3, self.pushButton_6]]
        return 0

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Helvetica\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#555555\">\n"
                                            "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">ABCDE</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">FGHIJ</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">KLMNO</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">PQRST</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:20px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">UVWXYZ</span></p></body></html>", None))
        self.textBrowser_2.setText(_translate("MainWindow", "", None))
        self.textBrowser_2.setAlignment(QtCore.Qt.AlignLeft)
        self.textBrowser_2.setFont(QtGui.QFont("Helvetica", 14))
        self.pushButton.setText(_translate("MainWindow", "Go/Pause", None))
        self.pushButton_2.setText(_translate("MainWindow", "Space", None))
        self.pushButton_3.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_4.setText(_translate("MainWindow", "Add Line", None))
        self.pushButton_5.setText(_translate("MainWindow", "Recite", None))
        self.textBrowser_3.setText(_translate("MainWindow", "...", None))
        self.textBrowser_3.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser_3.setFont(QtGui.QFont("Helvetica", 15))
        self.textBrowser_4.setText(_translate("MainWindow", "...", None))
        self.textBrowser_4.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser_4.setFont(QtGui.QFont("Helvetica", 18))
        self.pushButton_6.setText(_translate("MainWindow", "Send SMS", None))
        self.pushButton_8.setText(_translate(
            "MainWindow", "Open Camera", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuStart_Stop_Sel.setTitle(
            _translate("MainWindow", "Left Wink", None))
        self.menuFinger.setTitle(_translate("MainWindow", "Finger", None))
        self.menuLetter_Sel.setTitle(
            _translate("MainWindow", "Right Wink", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionWord_Sel.setText(_translate("MainWindow", "Finger", None))
        self.actionBlink.setText(_translate(
            "MainWindow", "Same as Blink", None))
        self.actionLeft_Wink.setText(_translate("MainWindow", "Space", None))
        self.actionRight_Wink.setText(_translate("MainWindow", "Recite", None))
        self.actionBlink_2.setText(_translate(
            "MainWindow", "Same as Blink", None))
        self.actionLeft_Wink_2.setText(_translate("MainWindow", "Space", None))
        self.actionRight_Wink_2.setText(
            _translate("MainWindow", "Recite", None))
        self.actionAbout_EyeTotText.setText(
            _translate("MainWindow", "About EyeTotText", None))
        self.actionContact_Developer.setText(
            _translate("MainWindow", "Contact Developer", None))
        return 0

    def changeColour(self):
        global letColBold
        global letRowBold
        global letColCount
        global letRowCount
        global stopRow
        if self.go:
            if(stopRow == False):
                letRowCount += 1
                if letRowCount == (len(letRowBold)+len(self.buts)):
                    letRowCount = 0
                if letRowCount < 5:
                    self.textBrowser.setHtml(_translate(
                        "MainWindow", letRowBold[letRowCount], None))
                    for row in self.buts:
                        for but in row:
                            but.setStyleSheet(
                                'QPushButton {font-weight:normal; QTextBrowser {font-weight:normal;}}')
                elif letRowCount == 5:
                    self.textBrowser.setHtml(_translate(
                        "MainWindow", letRowNorm[0], None))
                    for e in self.buts[0]:
                        e.setStyleSheet(
                            'QPushButton {font-weight:bold;color:red;}')
                elif letRowCount == 6:
                    self.textBrowser.setHtml(_translate(
                        "MainWindow", letRowNorm[0], None))
                    for e in self.buts[0]:
                        e.setStyleSheet('QPushButton {font-weight:normal;}')
                    for e in self.buts[1]:
                        e.setStyleSheet(
                            'QPushButton {font-weight:bold;color:red;} QTextBrowser {font-weight:bold;color:red;}')
            else:
                letColCount += 1
                if letRowCount < 5 and letColCount == len(letColBold[letRowCount]):
                    letColCount = 0
                elif letColCount == len(self.buts[0]) and letRowCount == 5:
                    letColCount = 0
                elif letColCount == len(self.buts[1]) and letRowCount == 6:
                    letColCount = 0
                if letRowCount < 5:
                    self.textBrowser.setHtml(_translate(
                        "MainWindow", letColBold[letRowCount][letColCount], None))
                else:
                    for i in range(len(self.buts)):
                        for j in range(len(self.buts[i])):
                            if j == letColCount and i+NUM_ROWS_OF_LETTERS == letRowCount:
                                self.buts[i][j].setStyleSheet(
                                    'QPushButton {font-weight:bold;color:red;} QTextBrowser {font-weight:bold;color:red;}')
                            else:
                                self.buts[i][j].setStyleSheet(
                                    'QPushButton {font-weight:normal;} QTextBrowser {font-weight:normal;}')
        return 0

    def pushSentenceToBody(self):
        global currentSentence
        global wholeText
        if currentSentence != "":
            if currentSentence[-1] == " ":
                currentSentence = currentSentence[0:-1]
            wholeText += currentSentence+"."+"<br> "
            currentSentence = ""
        self.textBrowser_2.setText(wholeText)
        self.textBrowser_4.setText(currentSentence)
        self.predictNextWord()
        return 0

    def delLet(self):
        global currentSentence
        currentSentence = currentSentence[0:-1]
        self.textBrowser_4.setText(currentSentence)
        self.predictNextWord()
        return 0

    def addSpace(self):
        global currentSentence
        currentSentence += " "
        self.textBrowser_4.setText(currentSentence)
        self.predictNextWord()
        return 0

    def reciteBut(self):
        self.pushSentenceToBody()
        global wholeText
        reciteLine = wholeText.replace("<br>", "")
        subprocess.call(["python3", "speak.py", reciteLine])
        return 0
        # engine = pyttsx3.init()
        # engine.setProperty('rate', 125)
        # engine.setProperty('volume', 1.0)
        # voices = engine.getProperty('voices')
        # engine.setProperty('voice', voices[1].id)
        # engine.say("Hello, How are you?")
        # engine.runAndWait()
        # engine.stop()

    def nurseBut(self):
        global wholeText
        reciteLine = wholeText.replace("<br>", "")
        whatsapp.send(reciteLine)
        sms.send(reciteLine)
        return 0

    def pauseBut(self):
        global letRowCount
        global letColCount
        self.go = not(self.go)
        if letRowCount == 6:
            letRowCount = -1
            letColCount = -1
        return 0

    def predictNextWord(self):
        global currentSentence
        words = currentSentence.lower().split(" ")
        if words:
            if words[0] == "":
                self.textBrowser_3.setText(_translate("MainWindow", "", None))
            elif words[-1] == "":
                predWord = autocomplete.predict('', words[-2])
                if predWord:
                    predWord = predWord[0][0]
                    self.textBrowser_3.setText(
                        _translate("MainWindow", predWord, None))
                    self.textBrowser_3.setAlignment(QtCore.Qt.AlignCenter)
                else:
                    self.textBrowser_3.setText(
                        _translate("MainWindow", "", None))
                    self.textBrowser_3.setAlignment(QtCore.Qt.AlignCenter)
            else:
                predWord = autocomplete.predict(words[-1], '')
                if predWord:
                    predWord = predWord[0][0]
                    self.textBrowser_3.setText(
                        _translate("MainWindow", predWord, None))
                    self.textBrowser_3.setAlignment(QtCore.Qt.AlignCenter)
                else:
                    self.textBrowser_3.setText(
                        _translate("MainWindow", "", None))
                    self.textBrowser_3.setAlignment(QtCore.Qt.AlignCenter)
        return 0

    def getPredWord(self):
        global currentSentence
        predWord = self.textBrowser_3.toPlainText()
        predWord = str(predWord)
        if currentSentence and predWord:
            words = currentSentence.split(" ")
            if len(words) == 1:
                words[0] = predWord.title()
            else:
                words[-1] = predWord
            currentSentence = " ".join(words)+" "
            self.textBrowser_4.setText(currentSentence)
        return 0

    def openCam(self):
        print("hi")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(close)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    row5 = {0: ui.pauseBut, 1: ui.addSpace, 2: ui.delLet,
            3: ui.pushSentenceToBody, 4: ui.reciteBut}
    row6 = {0: ui.getPredWord, 1: ui.nurseBut}
    MainWindow.show()
    timer = QTimer()
    timer.timeout.connect(tick)
    timer.start(100)
    timerColour = QTimer()
    timerColour.timeout.connect(ui.changeColour)
    timerColour.start(1000)
    sys.exit(app.exec_())
