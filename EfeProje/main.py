from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QTabWidget,
                           QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
                           QPushButton, QTableWidget, QTableWidgetItem, QMessageBox,
                           QComboBox, QDialog, QSpinBox, QHeaderView, QStackedWidget,
                           QFormLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
import sys
import random

# Gerçek basketbolcu verileri
PLAYERS = [
    ["LeBron James", "Los Angeles Lakers", "Forward", "39", "ABD", "25.4", "7.2", "8.1", "1.2", "0.5", "3.4"],
    ["Stephen Curry", "Golden State Warriors", "Guard", "35", "ABD", "28.1", "4.5", "4.9", "0.8", "0.2", "3.1"],
    ["Giannis Antetokounmpo", "Milwaukee Bucks", "Forward", "29", "Yunanistan", "30.8", "11.2", "6.3", "1.2", "1.0", "3.3"],
    ["Kevin Durant", "Phoenix Suns", "Forward", "35", "ABD", "28.4", "6.8", "5.5", "0.8", "1.2", "3.2"],
    ["Alperen Şengün", "Houston Rockets", "Center", "21", "Türkiye", "20.3", "9.2", "5.1", "1.2", "1.0", "2.9"],
    ["Luka Doncic", "Dallas Mavericks", "Guard", "25", "Slovenya", "33.8", "9.2", "9.8", "1.4", "0.5", "3.5"],
    ["Nikola Jokic", "Denver Nuggets", "Center", "29", "Sırbistan", "26.1", "12.3", "9.2", "1.2", "0.9", "3.1"],
    ["Joel Embiid", "Philadelphia 76ers", "Center", "30", "Kamerun", "35.3", "11.3", "5.7", "1.1", "1.8", "3.2"],
    ["Jayson Tatum", "Boston Celtics", "Forward", "26", "ABD", "27.2", "8.3", "4.9", "1.0", "0.7", "2.8"],
    ["Shai Gilgeous-Alexander", "Oklahoma City Thunder", "Guard", "25", "Kanada", "31.4", "5.5", "6.5", "2.1", "0.8", "3.3"],
    ["Devin Booker", "Phoenix Suns", "Guard", "27", "ABD", "27.5", "4.6", "7.2", "1.0", "0.4", "3.0"],
    ["Donovan Mitchell", "Cleveland Cavaliers", "Guard", "27", "ABD", "28.2", "5.1", "6.2", "1.8", "0.4", "3.1"],
    ["Cade Cunningham", "Detroit Pistons", "Guard", "22", "ABD", "22.7", "4.1", "7.5", "1.3", "0.3", "2.7"],
    ["Anthony Edwards", "Minnesota Timberwolves", "Guard", "22", "ABD", "26.4", "5.2", "5.1", "1.3", "0.5", "2.8"],
    ["Furkan Korkmaz", "Philadelphia 76ers", "Guard", "26", "Türkiye", "8.2", "2.1", "1.5", "0.5", "0.1", "1.4"],
    ["Victor Wembanyama", "San Antonio Spurs", "Center", "20", "Fransa", "20.7", "10.2", "3.4", "1.2", "3.3", "2.9"],
    ["Jaylen Brown", "Boston Celtics", "Guard", "27", "ABD", "23.1", "5.5", "3.7", "1.2", "0.3", "2.5"],
    ["Kristaps Porzingis", "Boston Celtics", "Center", "28", "Letonya", "20.2", "7.1", "1.9", "0.7", "1.8", "2.2"],
    ["Jalen Brunson", "New York Knicks", "Guard", "27", "ABD", "27.5", "3.8", "6.5", "0.9", "0.2", "2.4"],
    ["Julius Randle", "New York Knicks", "Forward", "29", "ABD", "24.1", "9.2", "5.0", "0.6", "0.3", "2.3"],
    ["Paolo Banchero", "Orlando Magic", "Forward", "21", "ABD", "22.6", "6.8", "5.4", "1.0", "0.6", "2.1"],
    ["Franz Wagner", "Orlando Magic", "Forward", "22", "Almanya", "19.7", "5.4", "3.7", "1.1", "0.4", "1.9"],
    ["Tyrese Maxey", "Philadelphia 76ers", "Guard", "23", "ABD", "25.9", "3.7", "6.2", "1.0", "0.5", "2.6"],
    ["De'Aaron Fox", "Sacramento Kings", "Guard", "26", "ABD", "26.8", "4.2", "5.5", "1.8", "0.3", "2.7"],
    ["Domantas Sabonis", "Sacramento Kings", "Center", "27", "Litvanya", "19.4", "13.7", "8.3", "0.8", "0.7", "2.4"],
    ["Lauri Markkanen", "Utah Jazz", "Forward", "26", "Finlandiya", "23.2", "8.3", "1.7", "0.9", "0.6", "2.0"],
    ["Ja Morant", "Memphis Grizzlies", "Guard", "24", "ABD", "25.1", "5.6", "8.1", "1.3", "0.3", "2.5"],
    ["Trae Young", "Atlanta Hawks", "Guard", "25", "ABD", "26.4", "2.7", "10.8", "1.4", "0.2", "3.0"],
    ["Dejounte Murray", "Atlanta Hawks", "Guard", "27", "ABD", "21.5", "5.1", "5.2", "1.4", "0.3", "2.3"],
    ["Mikal Bridges", "Brooklyn Nets", "Forward", "27", "ABD", "21.7", "4.7", "3.6", "1.1", "0.5", "2.0"],
    # ... Devam eden 80 oyuncu daha eklenecek ...
]

class ResultDialog(QDialog):
    def __init__(self, filtered_players, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Filtreleme Sonuçları")
        self.setGeometry(200, 200, 1200, 600)
        
        layout = QVBoxLayout(self)
        
        # Başlık
        title = QLabel("Filtreleme Sonuçları")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Tablo
        self.table = QTableWidget()
        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels([
            "Ad", "Takım", "Pozisyon", "Yaş", "Ülke",
            "Sayı", "Ribaund", "Asist", "Top Çalma", "Blok", "Top Kaybı"
        ])
        
        # Verileri yükle
        self.table.setRowCount(len(filtered_players))
        for i, player in enumerate(filtered_players):
            for j, value in enumerate(player):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))
        
        self.table.resizeColumnsToContents()
        self.table.setAlternatingRowColors(True)
        layout.addWidget(self.table)
        
        # Kapat butonu
        close_button = QPushButton("Kapat")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

class FilterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Basketbolcu Filtrele")
        self.setGeometry(200, 200, 400, 500)
        
        layout = QVBoxLayout(self)
        
        # Filtre seçenekleri
        self.team_combo = QComboBox()
        teams = sorted(list(set(player[1] for player in PLAYERS)))
        self.team_combo.addItems(["Hepsi"] + teams)
        
        self.position_combo = QComboBox()
        positions = sorted(list(set(player[2] for player in PLAYERS)))
        self.position_combo.addItems(["Hepsi"] + positions)
        
        self.country_combo = QComboBox()
        countries = sorted(list(set(player[4] for player in PLAYERS)))
        self.country_combo.addItems(["Hepsi"] + countries)
        
        # İstatistik filtreleri
        self.min_points = QSpinBox()
        self.min_points.setRange(0, 40)
        self.min_points.setSpecialValueText("Min Sayı")
        
        self.min_rebounds = QSpinBox()
        self.min_rebounds.setRange(0, 15)
        self.min_rebounds.setSpecialValueText("Min Ribaund")
        
        self.min_assists = QSpinBox()
        self.min_assists.setRange(0, 12)
        self.min_assists.setSpecialValueText("Min Asist")
        
        self.min_steals = QSpinBox()
        self.min_steals.setRange(0, 3)
        self.min_steals.setSpecialValueText("Min Top Çalma")
        
        self.min_blocks = QSpinBox()
        self.min_blocks.setRange(0, 3)
        self.min_blocks.setSpecialValueText("Min Blok")
        
        self.min_turnovers = QSpinBox()
        self.min_turnovers.setRange(0, 5)
        self.min_turnovers.setSpecialValueText("Min Top Kaybı")
        
        # Layout'a ekle
        layout.addWidget(QLabel("Takım:"))
        layout.addWidget(self.team_combo)
        layout.addWidget(QLabel("Pozisyon:"))
        layout.addWidget(self.position_combo)
        layout.addWidget(QLabel("Ülke:"))
        layout.addWidget(self.country_combo)
        layout.addWidget(QLabel("\nİstatistik Filtreleri:"))
        layout.addWidget(self.min_points)
        layout.addWidget(self.min_rebounds)
        layout.addWidget(self.min_assists)
        layout.addWidget(self.min_steals)
        layout.addWidget(self.min_blocks)
        layout.addWidget(self.min_turnovers)
        
        # Filtrele butonu
        filter_button = QPushButton("Filtrele")
        filter_button.clicked.connect(self.accept)
        layout.addWidget(filter_button)

class CompareDialog(QDialog):
    def __init__(self, player1, player2, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Oyuncu Karşılaştırma")
        self.setGeometry(200, 200, 800, 500)
        
        layout = QVBoxLayout(self)
        
        # Başlık
        title = QLabel("Oyuncu Karşılaştırma")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Tablo oluştur
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["İstatistik", player1[0], player2[0]])
        
        stats = [
            ("Takım", 1),
            ("Pozisyon", 2),
            ("Yaş", 3),
            ("Ülke", 4),
            ("Sayı", 5),
            ("Ribaund", 6),
            ("Asist", 7),
            ("Top Çalma", 8),
            ("Blok", 9),
            ("Top Kaybı", 10)
        ]
        
        table.setRowCount(len(stats))
        for i, (stat_name, idx) in enumerate(stats):
            # İstatistik adı
            table.setItem(i, 0, QTableWidgetItem(stat_name))
            
            # Oyuncu 1 değeri
            val1 = player1[idx]
            item1 = QTableWidgetItem(str(val1))
            table.setItem(i, 1, item1)
            
            # Oyuncu 2 değeri
            val2 = player2[idx]
            item2 = QTableWidgetItem(str(val2))
            table.setItem(i, 2, item2)
            
            # İstatistikleri karşılaştır
            if idx >= 5:  # Sayısal istatistikler
                try:
                    num1 = float(val1)
                    num2 = float(val2)
                    if idx == 10:  # Top kaybı - düşük olan daha iyi
                        if num1 < num2:
                            item1.setBackground(Qt.green)
                        elif num2 < num1:
                            item2.setBackground(Qt.green)
                    else:  # Diğer istatistikler - yüksek olan daha iyi
                        if num1 > num2:
                            item1.setBackground(Qt.green)
                        elif num2 > num1:
                            item2.setBackground(Qt.green)
                except ValueError:
                    pass
        
        table.resizeColumnsToContents()
        layout.addWidget(table)
        
        # Kapat butonu
        close_button = QPushButton("Kapat")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

class FavoritesDialog(QDialog):
    def __init__(self, favorites, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Favori Oyuncular")
        self.setGeometry(200, 200, 1200, 600)
        self.favorites = favorites
        
        layout = QVBoxLayout(self)
        
        # Başlık
        title = QLabel("Favori Oyuncularım")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Karşılaştır butonu
        compare_button = QPushButton("Seçili Oyuncuları Karşılaştır")
        compare_button.clicked.connect(self.compare_selected)
        layout.addWidget(compare_button)
        
        # Tablo
        self.table = QTableWidget()
        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels([
            "Ad", "Takım", "Pozisyon", "Yaş", "Ülke",
            "Sayı", "Ribaund", "Asist", "Top Çalma", "Blok", "Top Kaybı"
        ])
        self.table.setSelectionMode(QTableWidget.MultiSelection)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        
        # Verileri yükle
        self.table.setRowCount(len(favorites))
        for i, player in enumerate(favorites):
            for j, value in enumerate(player):
                self.table.setItem(i, j, QTableWidgetItem(str(value)))
        
        self.table.resizeColumnsToContents()
        self.table.setAlternatingRowColors(True)
        layout.addWidget(self.table)
        
        # Kapat butonu
        close_button = QPushButton("Kapat")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

    def compare_selected(self):
        selected_rows = set()
        for item in self.table.selectedItems():
            selected_rows.add(item.row())
        
        if len(selected_rows) != 2:
            QMessageBox.warning(self, "Uyarı", "Lütfen karşılaştırmak için 2 oyuncu seçin!")
            return
            
        player1 = self.favorites[list(selected_rows)[0]]
        player2 = self.favorites[list(selected_rows)[1]]
        
        dialog = CompareDialog(player1, player2, self)
        dialog.exec_()

class BasketballApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Efe'nin NBA Uygulaması")
        self.setGeometry(100, 100, 1200, 800)
        self.favorite_players = []
        
        # Ana widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        
        # Stack widget kullanarak ekranlar arası geçiş
        self.stack = QStackedWidget()
        self.layout.addWidget(self.stack)
        
        # Login ve ana ekran
        self.login_page = self.create_login_page()
        self.main_page = self.create_main_page()
        
        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.main_page)
        
        self.apply_dark_theme()

    def create_login_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        title = QLabel("NBA Oyuncu Veritabanı")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        form = QFormLayout()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        
        form.addRow("Kullanıcı Adı:", self.username)
        form.addRow("Şifre:", self.password)
        
        login_btn = QPushButton("Giriş")
        login_btn.clicked.connect(self.check_login)
        
        layout.addLayout(form)
        layout.addWidget(login_btn)
        layout.setAlignment(Qt.AlignCenter)
        
        return page

    def create_main_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        # Üst butonlar
        btn_layout = QHBoxLayout()
        
        filter_btn = QPushButton("Filtrele")
        filter_btn.clicked.connect(self.show_filter)
        btn_layout.addWidget(filter_btn)
        
        fav_btn = QPushButton("Favoriler")
        fav_btn.clicked.connect(self.show_favorites)
        btn_layout.addWidget(fav_btn)
        
        compare_btn = QPushButton("Karşılaştır")
        compare_btn.clicked.connect(self.compare_players)
        btn_layout.addWidget(compare_btn)
        
        # Çıkış butonu eklendi
        logout_btn = QPushButton("Çıkış")
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff3333;
                color: white;
            }
            QPushButton:hover {
                background-color: #cc0000;
            }
        """)
        logout_btn.clicked.connect(self.logout)
        btn_layout.addWidget(logout_btn)
        
        layout.addLayout(btn_layout)
        
        # Oyuncu tablosu
        self.table = QTableWidget()
        self.table.setSelectionMode(QTableWidget.MultiSelection)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.setup_table()
        layout.addWidget(self.table)
        
        return page

    def setup_table(self):
        headers = ["Favori", "Ad", "Takım", "Pozisyon", "Yaş", "Ülke",
                  "Sayı", "Ribaund", "Asist", "Top Çalma", "Blok", "Top Kaybı"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.load_players()

    def load_players(self):
        self.table.setRowCount(len(PLAYERS))
        for i, player in enumerate(PLAYERS):
            # Favori butonu
            fav_btn = QPushButton("☆")
            fav_btn.setStyleSheet("background: transparent; color: gold; font-size: 20px;")
            fav_btn.clicked.connect(lambda checked, p=player, b=fav_btn: self.toggle_favorite(p, b))
            self.table.setCellWidget(i, 0, fav_btn)
            
            # Oyuncu verileri
            for j, value in enumerate(player):
                item = QTableWidgetItem(str(value))
                self.table.setItem(i, j+1, item)
        
        self.table.resizeColumnsToContents()

    def check_login(self):
        if self.username.text().lower() == "efe" and self.password.text() == "0909":
            self.stack.setCurrentIndex(1)
            QMessageBox.information(self, "Başarılı", "Hoş geldin Efe!")
        else:
            QMessageBox.warning(self, "Hata", "Hatalı giriş!")

    def show_filter(self):
        dialog = FilterDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            filtered_players = PLAYERS.copy()
            
            # Temel filtreleme
            if dialog.team_combo.currentText() != "Hepsi":
                filtered_players = [p for p in filtered_players if p[1] == dialog.team_combo.currentText()]
            if dialog.position_combo.currentText() != "Hepsi":
                filtered_players = [p for p in filtered_players if p[2] == dialog.position_combo.currentText()]
            if dialog.country_combo.currentText() != "Hepsi":
                filtered_players = [p for p in filtered_players if p[4] == dialog.country_combo.currentText()]
            
            # İstatistik filtreleme
            filtered_players = [p for p in filtered_players if 
                              float(p[5]) >= dialog.min_points.value() and
                              float(p[6]) >= dialog.min_rebounds.value() and
                              float(p[7]) >= dialog.min_assists.value() and
                              float(p[8]) >= dialog.min_steals.value() and
                              float(p[9]) >= dialog.min_blocks.value() and
                              float(p[10]) >= dialog.min_turnovers.value()]
            
            # Sonuçları yeni pencerede göster
            result_dialog = ResultDialog(filtered_players, self)
            result_dialog.exec_()

    def show_favorites(self):
        if not self.favorite_players:
            QMessageBox.information(self, "Bilgi", "Henüz favori oyuncu eklenmemiş!")
            return
        
        dialog = FavoritesDialog(self.favorite_players, self)
        dialog.exec_()

    def compare_players(self):
        self.compare_selected_players()

    def compare_selected_players(self):
        selected_rows = set()
        for item in self.table.selectedItems():
            selected_rows.add(item.row())
        
        if len(selected_rows) != 2:
            QMessageBox.warning(self, "Uyarı", "Lütfen karşılaştırmak için 2 oyuncu seçin!")
            return
        
        row_list = list(selected_rows)
        player1 = PLAYERS[row_list[0]]
        player2 = PLAYERS[row_list[1]]
        
        dialog = CompareDialog(player1, player2, self)
        dialog.exec_()

    def toggle_favorite(self, player, button):
        if player in self.favorite_players:
            self.favorite_players.remove(player)
            button.setText("☆")
        else:
            self.favorite_players.append(player)
            button.setText("★")

    def logout(self):
        # Kullanıcı bilgilerini temizle
        self.username.clear()
        self.password.clear()
        # Favori listesini sıfırla
        self.favorite_players.clear()
        # Giriş ekranına dön
        self.stack.setCurrentIndex(0)
        QMessageBox.information(self, "Çıkış", "Oturum kapatıldı!")

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QMainWindow, QDialog {
                background-color: #000000;
                color: #ffffff;
            }
            QTableWidget {
                background-color: #ffffff;
                color: #000000;
                gridline-color: #cccccc;
                font-size: 12px;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QTableWidget::item:selected {
                background-color: #2196F3;
                color: white;
            }
            QHeaderView::section {
                background-color: #333333;
                color: #ffffff;
                padding: 8px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #2196F3;
                color: #ffffff;
                padding: 8px;
                border: none;
                border-radius: 4px;
                font-size: 13px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                padding: 8px;
                border: 1px solid #333333;
                border-radius: 4px;
                font-size: 13px;
            }
            QComboBox {
                background-color: #ffffff;
                color: #000000;
                padding: 8px;
                border: 1px solid #333333;
                border-radius: 4px;
                font-size: 13px;
            }
            QSpinBox {
                background-color: #ffffff;
                color: #000000;
                padding: 8px;
                border: 1px solid #333333;
                border-radius: 4px;
                font-size: 13px;
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasketballApp()
    window.show()
    sys.exit(app.exec_()) 