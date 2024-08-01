import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QWidget, QComboBox, QHeaderView
from PyQt5.QtCore import Qt
from core.population import Population
from core.genetic_algorithm import GeneticAlgorithm
import core.settings as settings

class TimetableApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timetable Generator Window")
        self.setGeometry(100, 100, 1000, 700)
        
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        title_label = QLabel("Automatic Timetable Generator")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; padding: 10px;")
        
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start Algorithm")
        self.start_button.clicked.connect(self.run_algorithm)
        self.display_button = QPushButton("Display Best Timetable")
        self.display_button.clicked.connect(self.display_best_timetable)
        
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.display_button)
        
        self.timetable_label = QLabel("Timetable will be displayed here")
        self.timetable_label.setStyleSheet("font-size: 18px; padding: 10px;")
        
        self.class_selector = QComboBox()
        self.class_selector.currentIndexChanged.connect(self.display_class_timetable)
        self.class_selector.setStyleSheet("padding: 5px; font-size: 16px;")
        
        main_layout.addWidget(title_label)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.class_selector)
        main_layout.addWidget(self.timetable_label)
        
        self.timetable_table = QTableWidget()
        self.timetable_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.timetable_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.timetable_table.setStyleSheet("gridline-color: black; font-size: 14px;")
        self.timetable_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.timetable_table.setSelectionMode(QTableWidget.NoSelection)
        
        main_layout.addWidget(self.timetable_table)
        
        self.population = None
        self.generation_number = 0
        
    def run_algorithm(self):
        self.generation_number = 0
        self.population = Population(settings.POPULATION_SIZE)
        while self.population[0].get_fitness() < 1 and self.generation_number < settings.MAX_GENERATION_NUMBER:
            self.generation_number += 1
            self.population = GeneticAlgorithm.evolve(self.population)
        
        self.class_selector.clear()
        self.class_selector.addItems(settings.RAW_DATA["classes"])
        self.timetable_label.setText("Timetable generated. Display the best timetable or select a class to view its timetable.")
        
    def display_best_timetable(self):
        best_chromosome = self.population[0]
        timetable = best_chromosome.get_time_table(settings.RAW_DATA["classes"][0])
        self.update_table(timetable)
        
    def display_class_timetable(self):
        class_name = self.class_selector.currentText()
        best_chromosome = self.population[0]
        timetable = best_chromosome.get_time_table(class_name)
        self.update_table(timetable)
        
    def update_table(self, timetable):
        days = settings.RAW_DATA["days"]
        hours = settings.RAW_DATA["hours"]
        
        self.timetable_table.setColumnCount(len(days))
        self.timetable_table.setRowCount(len(hours))
        self.timetable_table.setHorizontalHeaderLabels(days)
        self.timetable_table.setVerticalHeaderLabels(hours)
        
        for day in range(len(days)):
            for hour in range(len(hours)):
                cell_value = timetable.iloc[hour, day]
                item = QTableWidgetItem(str(cell_value))
                item.setTextAlignment(Qt.AlignCenter)
                self.timetable_table.setItem(hour, day, item)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = TimetableApp()
    mainWin.show()
    sys.exit(app.exec_())
