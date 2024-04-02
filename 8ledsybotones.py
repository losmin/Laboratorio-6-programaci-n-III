import tkinter as tk
import serial

# Configuración de la conexión serial con Arduino
arduino = serial.Serial('COM3', 9600)  # Ajusta el puerto serial según tu configuración

class LedPushbuttonGUI:
    def __init__(self, master):
        self.master = master
        master.title("Estado de LEDs y PushBottons")

        # Crear los círculos para representar los LEDs
        self.led_circles = []
        for i in range(8):
            led = tk.Canvas(master, width=20, height=20, bg="white", highlightthickness=1, highlightbackground="black")
            led.grid(row=0, column=i, padx=5, pady=5)
            self.led_circles.append(led)

        # Crear los rectángulos para representar los pulsadores
        self.pushbutton_rects = []
        for i in range(4):
            pushbutton = tk.Canvas(master, width=40, height=20, bg="white", highlightthickness=1, highlightbackground="black")
            pushbutton.grid(row=1, column=i, padx=5, pady=5)
            self.pushbutton_rects.append(pushbutton)

    def update_leds(self, led_states):
        for i, state in enumerate(led_states):
            if state == '1':
                self.led_circles[i].create_oval(2, 2, 18, 18, fill="red", outline="")
            else:
                self.led_circles[i].create_oval(2, 2, 18, 18, fill="white", outline="")

    def update_pushbuttons(self, pushbutton_states):
        for i, state in enumerate(pushbutton_states):
            if state == '1':
                self.pushbutton_rects[i].create_rectangle(2, 2, 38, 18, fill="green", outline="")
            else:
                self.pushbutton_rects[i].create_rectangle(2, 2, 38, 18, fill="white", outline="")

    def read_serial(self):
        if arduino.in_waiting > 0:
            data = arduino.readline().decode().strip()
            led_states = data[:8]
            pushbutton_states = data[8:]
            self.update_leds(led_states)
            self.update_pushbuttons(pushbutton_states)
        self.master.after(100, self.read_serial)

root = tk.Tk()
gui = LedPushbuttonGUI(root)
gui.read_serial()
root.mainloop()