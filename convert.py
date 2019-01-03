from PIL import Image
import binascii


def encode_message(message):
	'''
	Converts a message to it's binary equivalent
	'''
	binary =  bin(int(binascii.hexlify(message.encode('ascii')),16))
	return binary[2:]


def decode_message(binary):
	'''
	Converts binary back to string
	'''
	message = binascii.unhexlify('%x' % int(binary,2))
	return message.decode('ascii')




def encode_image(text_data, default_image = "basketball.png"):
	'''
		Hide the text data in the image
	'''

	image = Image.open(default_image)
	binary_data = encode_message(text_data)
	width, height = image.size
	
	new_pixels = []
	index = 0

	pixels = list(image.getdata())
	length_of_binary = len(binary_data)
	
	for pixel in pixels:
		alpha, red, green, blue = pixel
		
		if index < length_of_binary:
			new_red = int(bin(red)[:-1] +binary_data[index],2)
			index+=1
		else:

			new_red = red
		if index < length_of_binary:
			new_green = int(bin(green)[:-1]+ binary_data[index],2)
			index+=1
		else:
			new_green = green

		if index < length_of_binary:
			new_blue = int(bin(green)[:-1]+binary_data[index],2)
			index+=1

		else:
			new_blue = blue

		new_pixel = (alpha,new_red, new_green, new_blue)
		new_pixels.append(new_pixel)

	image.putdata(new_pixels)

	image.save("basketball_new.png")
	
	return length_of_binary
	






def decode_image(length_of_binary,default_image="basketball_new.png"):
	'''
		The num_of_pixels_needed variable has the first number of pixels where the Text would be encoded in. The rest of the pixels are irrelevant
	'''
	
	image = Image.open(default_image)
	pixels = list(image.getdata())
	
	length_of_pixels = len(pixels)
	
	binary = ''
	for pixel in pixels:
		alpha, red, green, blue = pixel
		
		binary+= bin(red)[-1] + bin(green)[-1] + bin(blue)[-1]
		
	return binary[0:length_of_binary]	


def main():

	#image_path = input"Enter image file name")
	option = input("1. Hide text in image\n2. To retrieve text from image\n\n")
	
	if option == "1":
		message = input("Enter message to hide: ")
	
		print("Your new Image will be saved in baskeball_new.png")
		length_of_binary = encode_image(message)
		f = open("tempfile.txt", "w")
		f.write(str(length_of_binary))

	elif option == "2":
		f = open("tempfile.txt", "r")
		length_of_binary = int(f.read())
		binary = decode_image(length_of_binary)
		print("The hidden text was : " + decode_message(binary))



if __name__ == "__main__":
	main()
