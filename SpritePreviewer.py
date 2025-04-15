#Zhu Zhu
#u1537009
#Dingyu Shi
#u1496474

# Me(Zhu Zhu) and Dingyu Shi were working together in the library.
# Since Dingyu Shi's laptop was broken, She used library's computer and we created a shared google doc and worked togther.
# Therefore there is only me committed and pushed all the updates for gitub.

import math
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))

    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))
    return frames

class SpritePreview(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 20
        self.frames = load_sprite('spriteImages', self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here
        self.timer = QTimer()
        self.current_frame = 0
        self.is_running = False

        # Make the GUI in the setupUI method
        self.setupUI()

        self.slider.valueChanged.connect(self.update_fps_display)
        self.start_button.clicked.connect(self.toggle_animation)
        self.timer.timeout.connect(self.update_frame)

        self.update_fps_display()

        self.menu()

    def menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        pause_action = QAction("Pause",self)
        pause_action.triggered.connect(self.pause_animation)
        file_menu.addAction(pause_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)


    def pause_animation(self):
        if self.is_running:
            self.timer.stop()
            self.start_button.setText("Start")
            self.is_running = False


    def update_fps_display(self):
        fps = self.slider.value()
        self.fps_value_label.setText(str(fps))
        delay = int(1000 / fps)
        self.timer.setInterval(delay)

    def toggle_animation(self):
        if not self.is_running:
            self.update_fps_display()
            self.timer.start()
            self.start_button.setText("Stop")
            self.is_running = True
        else:
            self.timer.stop()
            self.start_button.setText("Start")
            self.is_running = False

    def update_frame(self):
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.image_label.setPixmap(self.frames[self.current_frame])

    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        # picture display
        self.image_label = QLabel()
        self.image_label.setPixmap(self.frames[0])

        # FPS
        self.fps_label = QLabel("Frames per second")
        self.fps_value_label = QLabel("1")

        # a slider
        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setRange(1, 20)
        self.slider.setValue(1)

        # scale bar
        self.slider.setTickInterval(4)
        self.slider.setTickPosition(QSlider.TickPosition.TicksRight)

        # a button
        self.start_button = QPushButton('Start')

        # github name
        self.text = QLabel('Dancing Pikachu')

        # layout
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.text)
        left_layout.addWidget(self.image_label)
        left_layout.addWidget(self.fps_label)
        left_layout.addWidget(self.start_button)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.slider)
        right_layout.addWidget(self.fps_value_label)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        frame.setLayout(main_layout)
        self.setCentralWidget(frame)


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()

if __name__ == "__main__":
    main()