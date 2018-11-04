import tkinter  # GUI support
import os  # get file name
import time  # sleep function
import brickpi3  # BrickPi3 drivers


class Gui_test:

	def __init__(self):
		self.BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
		self.gui = tkinter.Tk()  # Create GUI instance
		self.file_name = os.path.basename(__file__)
		self.compose_GUI()


	def get_brick_info(self):
		try:
			print("Manufacturer:", self.BP.get_manufacturer())
			print("Board:       ", self.BP.get_board())
			print("HW version:  ", self.BP.get_version_hardware())
			print("FW version:  ", self.BP.get_version_firmware())
			print("ID:          ", self.BP.get_id())
			print("Voltage 3v3: ", self.BP.get_voltage_3v3())
			print("Voltage 5V:  ", self.BP.get_voltage_5v())
			print("Voltage 9V:  ", self.BP.get_voltage_9v())
			print("Voltage bat: ", self.BP.get_voltage_battery())
			print("RP3:    ", os.popen("vcgencmd measure_temp").readline())

		except:
			print("Error caught in <get_brick_info()>")


	def exit_program(self):
		print("Button: Exit")
		self.gui.quit()
		self.BP.set_led(0)  # set the LED brightness (0 to 100)
		self.BP.reset_all()  # Unconfigure the sensors, disable the motors, and restore the LED control

	def quit(self):
		print("Button: quit")
		self.root.destroy()

	def throttle_LED(self, throttle):
		self.BP.set_led(int(throttle))

	def compose_GUI(self):
		self.gui.title("BrickPi3 - LEGO")
		self.gui.geometry('400x200')
		self.gui.resizable(False, False)

		self.exit_button = tkinter.Button(self.gui, text = "Exit", command = self.exit_program, height = 2, width = 6)
		self.exit_button.pack(side='right')

		self.info_button = tkinter.Button(self.gui, text = "Info", command = self.get_brick_info, height = 2, width = 8)
		self.info_button.pack(side='left')

		self.scale_button = tkinter.Scale(self.gui, command = self.throttle_LED, orient = 'horizontal')
		self.scale_button.pack(side = 'bottom')

		self.gui.mainloop()


if __name__ == '__main__':
	gui_instance = Gui_test()