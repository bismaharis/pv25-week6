import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QSlider, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class FontColorAdjuster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tugas Week 6")
        self.setGeometry(100, 100, 600, 300)
        self.setStyleSheet("background-color: #2e2e2e;")  # dark mode
        self.initUI()

    def initUI(self):
        self.label = QLabel("F1D022055", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 30))
        self.label.setStyleSheet("background-color: rgb(200,200,200); color: rgb(0,0,0);")

        self.fontSizeSlider = self._makeSlider(20, 60, 30, 2)

        self.bgColorSlider = self._makeSlider(0, 255, 200, 15)

        self.fontColorSlider = self._makeSlider(0, 255, 0, 15)

        self.fontSizeSlider.valueChanged.connect(self.changeFontSize)
        self.bgColorSlider.valueChanged.connect(self.updateLabelStyle)
        self.fontColorSlider.valueChanged.connect(self.updateLabelStyle)

        layout = QVBoxLayout()

        layout.addWidget(self.label)
        layout.addLayout(self._makeSliderWithLabel("Font Size", self.fontSizeSlider))
        layout.addLayout(self._makeSliderWithLabel("Background Color", self.bgColorSlider))
        layout.addLayout(self._makeSliderWithLabel("Font Color", self.fontColorSlider))

        self.setLayout(layout)

    def _makeSlider(self, minval, maxval, default, tick_interval):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(minval)
        slider.setMaximum(maxval)
        slider.setValue(default)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(tick_interval)
        slider.setSingleStep(tick_interval)
        return slider

    def _makeSliderWithLabel(self, text, slider):
        layout = QHBoxLayout()
        label = QLabel(text)
        label.setStyleSheet("color: white;")
        label.setFixedWidth(140)
        layout.addWidget(label)
        layout.addWidget(slider)
        return layout

    def changeFontSize(self):
        size = self.fontSizeSlider.value()
        font = self.label.font()
        font.setPointSize(size)
        self.label.setFont(font)

    def updateLabelStyle(self):
        bg = self.bgColorSlider.value()
        fg = self.fontColorSlider.value()
        self.label.setStyleSheet(
            f"background-color: rgb({bg},{bg},{bg}); color: rgb({fg},{fg},{fg});"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontColorAdjuster()
    window.show()
    sys.exit(app.exec_())
