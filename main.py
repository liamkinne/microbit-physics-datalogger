from microbit import *

display.show(Image.DUCK); # most important part

image_x = Image(
	"90009:"
	"09090:"
	"00900:"
	"09090:"
	"90009:"
)

image_y = Image(
	"90009:"
	"09090:"
	"00900:"
	"00900:"
	"00900:"
)

image_z = Image(
	"99999:"
	"00090:"
	"00900:"
	"09000:"
	"99999:"
)

axes = {
	0 : "x",
	1 : "y",
	2 : "z"
}

axis = -1

while True:
	if (button_a.was_pressed()):
		axis += 1
		axis %= 3
		if (axes[axis] == "x"):
			display.show(image_x)
		elif (axes[axis] == "y"):
			display.show(image_y)
		elif (axes[axis] == "z"):
			display.show(image_z)

	if (button_b.was_pressed()):
		display.show(Image.TARGET)

		data = open('data.log', 'w')

		start_time = running_time()
		last_time = start_time

		while (not button_b.was_pressed() and (running_time() - start_time) < 1000 * 15):
			time_delta = running_time() - last_time
			if (time_delta > (1000/50)):
				time = running_time() - start_time

				x, y, z = accelerometer.get_values()
				if (axes[axis] == "x"):
					accel = x
				elif (axes[axis] == "y"):
					accel = y
				elif (axes[axis] == "z"):
					accel = z
				data.write(str(time) + "," + str(accel) + "\n")

				last_time = running_time();

		data.close()

		display.show(Image.DUCK)
