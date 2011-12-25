"""
Wings, the only program to give your jpegs wings 
(and secret data)!
This is a little script i threw together after learning about
dangerous kitten. anyway:

Wings version 1.0
Author: Posiden
"""
import tarfile
import sys
import os


class wings:
	def combine(self, imageName, fileName, newName):
		if not os.access(imageName, os.F_OK) or not os.access(fileName, os.F_OK):
			print 'Error one of the parameters does not exist'
			exit()
		fileData = None
		if not fileName.endswith('tar.gz'):
			#tar and compress the file
			archive = tarfile.open('temp.tar.gz', mode='w:gz')
			archive.add(fileName)
			archive.close()
			#open the file and get our data
			file = open('temp.tar.gz', 'rb')
			fileData = file.read()
			file.close()
			os.remove('temp.tar.gz')
		else:
			#just get our data and gtfo
			file = open(fileName, 'rb')
			fileData = file.read()
			file.close()
		#now for the image
		image = open(imageName, 'rb')
		imageData = image.read()
		image.close()
		#new file ^_^
		newFile = open(newName, 'wb')
		newFile.write(imageData)
		newFile.write(fileData)
		newFile.close()

	def split(self, imageName):
		if not os.access(imageName, os.F_OK):
			print 'specified image does not exist'
			exit()
		combined = open(imageName, 'rb')
		halves = combined.read().split('\xff\xd9')
		combined.close()
		data = ''.join(halves[1:])
		newFile = open('data.tar.gz', 'wb')
		newFile.write(data)
		newFile.close()
		# I tried to decompress using tarfile but it was zomg fail
		# So I shall cheat!


if __name__ == '__main__':

	if len(sys.argv) > 1:
		if sys.argv[1] == '-c' or sys.argv[1] == '--combine':
			if len(sys.argv) != 5:
				print '-c imageName fileName newName'
				exit()
			else:
				tehWings = wings()
				tehWings.combine(sys.argv[2], sys.argv[3], sys.argv[4])
		elif sys.argv[1] == '-s' or sys.argv[1] == '--split':
			if len(sys.argv) != 3:
				print '-s imageName'
				exit
			else:
				tehWings = wings()
				tehWings.split(sys.argv[2])

		else:
			print """[Wings]
Simple utility to hide files inside of jpegs. Written with the power of python and boredom
Author: Posiden
-c imageName fileName newName
-s imageName"""
			exit()
	else:
		print """[Wings]
Simple utility to hide files inside of jpegs. Written with the power of python and boredom
Author: Posiden
-c imageName fileName newName
-s imageName"""
		exit()
