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




def encode_image(text_data, default_image = "C:\\basketball.png"):
	'''
		Hide the text data in the image
	'''

	image = Image.open(default_image)
	binary_data = encode_message(text_data)

	width, height = image.size
	
	new_pixels = []
	same_pixels = []
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

	image.save("C:\\basketball_new.png")








def decode_image(num_of_pixels_needed, default_image="C:\\basketball_new.png"):
	'''
		The num_of_pixels_needed variable has the first number of pixels where the Text would be encoded in. The rest of the pixels are irrelevant
	'''
	



def main():

	message = "Hii"

	encode_image(message)

	length_of_message = len(message)

	num_of_pixels_needed = length_of_message ** 2


	#print(decode_message(encode_message("hello rarw")))
	##binary_message = encode_message("hello")
	#print(len(binary_message))

	#for x in binary_message:
		#print(x)


if __name__ == "__main__":
	main()