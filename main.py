import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox,
    QPushButton, QFrame, QScrollArea, QLineEdit, QMessageBox, QDialog
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class ADHDChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ADHD Checker")
        self.setGeometry(0, 0, 1000, 700)
        self.initUI()

    def initUI(self):
        # Main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(30, 30, 30, 30)

        # Title Header
        title_label = QLabel("ADHD Checker")
        title_label.setFont(QFont("Inter", 30, QFont.Bold))
        title_label.setStyleSheet("color: #1C2D8C;")
        title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(title_label)

        # Search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Cari gejala...")
        self.search_bar.setFont(QFont("Inter", 12))
        self.search_bar.setFixedHeight(45)
        self.search_bar.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                background: white;
                border-radius: 10px;
                border: 1px solid #E0E0E0;
                font-size: 14px;
                color: #000000;
            }
        """)
        self.search_bar.textChanged.connect(self.filterSymptoms)
        self.main_layout.addWidget(self.search_bar)

        # Scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                background: #EBF1E6;
                width: 10px;
                margin: 5px;
            }
            QScrollBar::handle:vertical {
                background: #59694D;
                border-radius: 5px;
            }
        """)

        # Container for symptoms
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setSpacing(10)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)

        # Symptoms and their descriptions
        self.symptoms = {
            "Kesulitan menunggu giliran atau menunjukkan ketidaksabaran":
                "Anak-anak cenderung kesulitan menunggu giliran atau menunjukkan ketidaksabaran. Dalam situasi seperti bermain permainan atau menunggu dalam antrean, mereka mungkin merasa tidak nyaman jika harus menunggu terlalu lama. Ini sering terlihat dari perilaku menyela atau menjadi gelisah karena sulit menahan diri.",
            "Kesulitan menyelesaikan tugas yang membutuhkan konsentrasi":
                "Anak-anak cenderung kesulitan menyelesaikan tugas yang membutuhkan konsentrasi. Tugas-tugas seperti pekerjaan rumah atau membaca sering kali terasa menantang karena perhatian mereka mudah teralihkan oleh hal-hal kecil di sekitar mereka. Akibatnya, mereka mungkin tidak menyelesaikan tugas tepat waktu atau hanya setengah hati mengerjakannya.",
            "Sering merasa gelisah seperti mengetuk-ngetuk tangan atau kaki":
                "Anak-anak cenderung merasa gelisah seperti mengetuk-ngetuk tangan atau kaki. Mereka sering menunjukkan perilaku seperti ini saat diminta untuk duduk diam dalam waktu lama. Ketukan tangan, goyangan kaki, atau gerakan kecil lainnya sering menjadi cara mereka mengatasi rasa tidak nyaman.",
            "Kesulitan mempertahankan perhatian pada suatu aktivitas dalam waktu yang lama":
                "Anak-anak cenderung kesulitan mempertahankan perhatian pada suatu aktivitas dalam waktu yang lama. Saat bermain, belajar, atau berbicara, mereka mudah teralihkan oleh sesuatu yang lebih menarik atau berbeda. Hal ini membuat mereka sering berpindah-pindah aktivitas tanpa menyelesaikannya.",
            "Sering mencela pembicaraan atau aktivitas orang lain":
                "Anak-anak cenderung mencela pembicaraan atau aktivitas orang lain. Mereka mungkin menyela pembicaraan, menjawab pertanyaan sebelum selesai diajukan, atau ikut campur dalam aktivitas teman tanpa bermaksud mengganggu. Sering kali ini terjadi karena dorongan spontan, bukan karena niat buruk.",
            "Mudah lupa dalam menjalankan aktivitas sehari-hari":
                "Anak-anak cenderung mudah lupa dalam menjalankan aktivitas sehari-hari. Hal-hal sederhana seperti membawa bekal, menyelesaikan tugas sekolah, atau mengingat jadwal bisa sering terlewat. Ini membuat mereka tampak tidak terorganisir meskipun mereka sebenarnya tidak bermaksud demikian.",
            "Sering kehilangan barang penting seperti buku, alat tulis, atau mainan":
                "Anak-anak cenderung sering kehilangan barang penting seperti buku, alat tulis, atau mainan. Kehilangan barang-barang ini bisa terjadi karena mereka lupa di mana meletakkannya atau kurang memperhatikan saat menggunakannya. Situasi ini sering kali menyebabkan frustrasi bagi mereka dan orang-orang di sekitarnya.",
            "Sering membuat kesalahan ceroboh dan tidak memperhatikan detail":
                "Anak-anak cenderung membuat kesalahan ceroboh dan tidak memperhatikan detail. Mereka mungkin melewatkan bagian penting dari tugas, seperti salah menjawab pertanyaan karena tidak membaca instruksi dengan baik. Kesalahan seperti ini sering kali terjadi secara tidak sengaja.",
            "Sering berbicara berlebihan":
                "Anak-anak cenderung berbicara berlebihan. Mereka bisa terus berbicara tanpa henti, bahkan di saat orang lain ingin berbicara atau ketika situasi membutuhkan mereka untuk diam. Ini bukan karena mereka tidak peduli, tetapi lebih karena mereka merasa sulit untuk mengendalikan dorongan berbicara.",
        }

        self.checkboxes = {}
        self.symptom_widgets = {}

        # Add symptoms to scrollable layout
        for symptom, description in self.symptoms.items():
            widget = self.createSymptomBox(symptom, description)
            self.scroll_layout.addWidget(widget)
            self.symptom_widgets[symptom] = widget

        # Add stretch at the end for spacing
        self.scroll_layout.addStretch()
        self.scroll_content.setLayout(self.scroll_layout)

        # Set scroll content
        self.scroll_area.setWidget(self.scroll_content)
        self.main_layout.addWidget(self.scroll_area)

        # Submit button
        submit_button = QPushButton("Kirim")
        submit_button.setFont(QFont("Inter", 12, QFont.Bold))
        submit_button.setFixedHeight(30)
        submit_button.setStyleSheet("""
            QPushButton {
                background-color: #1C2D8C;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                width: 100%;
            }
            QPushButton:hover {
                background-color: #12206D;
            }
        """)
        submit_button.clicked.connect(self.checkADHD)
        self.main_layout.addWidget(submit_button, alignment=Qt.AlignCenter)

        self.setLayout(self.main_layout)

    def createSymptomBox(self, symptom, description):
        # Create container for each symptom
        container = QWidget()
        container.setStyleSheet("""
            QWidget {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #E0E0E0;
                margin-bottom: 5px;
            }
        """)
        container_layout = QVBoxLayout(container)
        container_layout.setSpacing(5)
        container_layout.setContentsMargins(15, 10, 15, 10)

        # Header with symptom and checkbox
        header_layout = QHBoxLayout()
        header_layout.setSpacing(10)

        # Dropdown button
        dropdown_btn = QPushButton("▼")
        dropdown_btn.setFixedSize(30, 30)
        dropdown_btn.setStyleSheet("""
            QPushButton {
                background-color: #1C2D8C;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #12206D;
            }
        """)

        # Symptom label
        symptom_label = QLabel(symptom)
        symptom_label.setFont(QFont("Inter", 12, QFont.Bold))
        symptom_label.setStyleSheet("color: #000000; border: none;")

        # Checkbox (with clean style, no extra borders)
        checkbox = QCheckBox()
        checkbox.setStyleSheet("""
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
            QCheckBox {
                border: none;
            }
        """)
        self.checkboxes[symptom] = checkbox

        # Add to header
        header_layout.addWidget(dropdown_btn)
        header_layout.addWidget(symptom_label)
        header_layout.addStretch()
        header_layout.addWidget(checkbox)

        # Description layout (initially hidden)
        description_frame = QFrame()
        description_frame.setStyleSheet("""
            QFrame {
                background-color: #F5F5F5;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        description_frame.setVisible(False)
        description_layout = QVBoxLayout(description_frame)
        description_label = QLabel(description)
        description_label.setFont(QFont("Inter", 12))
        description_label.setStyleSheet("color: #000000; border: none;")
        description_label.setWordWrap(True)
        description_layout.addWidget(description_label)

        # Toggle description visibility
        def toggle_description():
            is_visible = description_frame.isVisible()
            description_frame.setVisible(not is_visible)
            dropdown_btn.setText("▲" if not is_visible else "▼")

        dropdown_btn.clicked.connect(toggle_description)

        # Add to container
        container_layout.addLayout(header_layout)
        container_layout.addWidget(description_frame)

        return container

    def filterSymptoms(self, query):
        query = query.lower()
        for symptom, widget in self.symptom_widgets.items():
            if query in symptom.lower():
                widget.show()
            else:
                widget.hide()

    def checkADHD(self):
        # Map symptoms to boolean variables
        values = {symptom: checkbox.isChecked() for symptom, checkbox in self.checkboxes.items()}
        a = values["Kesulitan menunggu giliran atau menunjukkan ketidaksabaran"]
        b = values["Kesulitan menyelesaikan tugas yang membutuhkan konsentrasi"]
        c = values["Sering merasa gelisah seperti mengetuk-ngetuk tangan atau kaki"]
        d = values["Kesulitan mempertahankan perhatian pada suatu aktivitas dalam waktu yang lama"]
        e = values["Sering mencela pembicaraan atau aktivitas orang lain"]
        f = values["Mudah lupa dalam menjalankan aktivitas sehari-hari"]
        g = values["Sering kehilangan barang penting seperti buku, alat tulis, atau mainan"]
        h = values["Sering membuat kesalahan ceroboh dan tidak memperhatikan detail"]
        i = values["Sering berbicara berlebihan"]

        # Evaluate the Boolean expressions
        not_adhd = (
            (not a and not b and not c and not d and not e) or
            (not a and b and g and not i) or
            (a and not d and not e and not f) or
            (not a and not b and g and not h) or
            (a and not d and not g)
        )

        # Show result dialog
        result_dialog = ADHDResultDialog(self, is_adhd=not not_adhd)
        result_dialog.exec_()
    
class ADHDResultDialog(QDialog):
    def __init__(self, parent=None, is_adhd=False):
        super().__init__(parent)
        self.setWindowTitle("Hasil Diagnosis")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: white;")
        self.setup_ui(is_adhd)

    def setup_ui(self, is_adhd):
        layout = QVBoxLayout(self)
        layout.setSpacing(30)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel("HASIL DIAGNOSIS")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Inter", 16, QFont.Bold))
        title.setStyleSheet("color: #1C2D8C")
        layout.addWidget(title)
        
        # Result Text
        result_text = QLabel()
        result_text.setAlignment(Qt.AlignCenter)
        result_text.setFont(QFont("Inter", 14))
        
        if is_adhd:
            # ADHD positive result
            result_text.setText(
                "Anak mungkin menunjukkan tanda-tanda\n"
                "potensi ADHD.\n\n"
                "Harap periksa ke tenaga profesional\nuntuk memastikan hasil ini."
            )
            result_text.setStyleSheet("color: #3D2929;")
        else:
            # Not ADHD result
            result_text.setText(
                "Anak tidak memiliki potensi ADHD"
            )
            result_text.setStyleSheet("color: #3D2929;")
        
        layout.addWidget(result_text)
        
        # Buttons
        button_layout = QHBoxLayout()
        close_btn = QPushButton("TUTUP")
        close_btn.setFixedSize(135, 35)
        close_btn.setFont(QFont("Inter", 12, QFont.Bold))
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #1C2D8C;
                color: white;
                border: none;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #12206D;
            }
        """)
        close_btn.clicked.connect(self.accept)
        button_layout.addWidget(close_btn)
        button_layout.setAlignment(Qt.AlignCenter)
        layout.addLayout(button_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    checker = ADHDChecker()
    checker.show()
    sys.exit(app.exec_())