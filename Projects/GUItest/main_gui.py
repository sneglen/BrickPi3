import tkinter  # GUI support
import os  # get file name
import time  # sleep function
import brickpi3  # BrickPi3 drivers


class Gui_test:

	def __init__(self):
		self.BP = brickpi3.BrickPi3()  # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
		self.gui = tkinter.Tk()  # Create GUI instance
		self.file_name = os.path.basename(__file__)
		self.composeGUI()

	def getBrickInfo(self):
		print("Manufacturer:", self.BP.get_manufacturer())
		print("Board:       ", self.BP.get_board())
		print("HW version:  ", self.BP.get_version_hardware())
		print("FW version:  ", self.BP.get_version_firmware())
		print("ID:          ", self.BP.get_id())
		print("Voltage 3v3: ", self.BP.get_voltage_3v3())
		print("Voltage 5V:  ", BP.get_voltage_5v())
		print("Voltage 9V:  ", self.BP.get_voltage_9v())
		print("Voltage bat: ", self.BP.get_voltage_battery())
		print("RP3:    ", os.popen("vcgencmd measure_temp").readline(), "\n")

	def exitProgram(self):
		print("Button: Exit")
		self.gui.quit()
		self.BP.set_led(0)  # set the LED brightness (0 to 100)
		self.BP.reset_all()  # Unconfigure the sensors, disable the motors, and restore the LED control

	##def quit(self):
	##    print("Button: quit")
	##    self.root.destroy()
	##
	##
	##def throttleLED(throttle):
	##    BP.set_led(int(throttle))

	def composeGUI(self):
		self.gui.title("BrickPi3 - LEGO")
		self.gui.geometry('400x200')
		self.gui.resizable(False, False)

		self.exitButton = tkinter.Button(self.gui, text="Exit", command=self.exitProgram, height=2, width=6)
		self.exitButton.pack(side='right')

		self.infoButton = tkinter.Button(self.gui, text="Info", command=self.getBrickInfo, height=2, width=8)
		self.infoButton.pack(side='left')

		##    scaleButton = tkinter.Scale(gui, command = throttleLED, orient = 'horizontal')
		##    scaleButton.pack(side = 'bottom')

		self.gui.mainloop()


if __name__ == '__main__':
	gui_instante = Gui_test()