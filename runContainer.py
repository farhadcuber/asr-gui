import docker
import sys, os

def runContainer(pathToSpeech):
	if not os.path.isfile(pathToSpeech):
		raise Exception('%s doesn\'t exists.' % pathToSpeech)

	folder, fileName = tuple(pathToSpeech.rsplit('/', 1))
		
	imageName = 'jrottenberg/ffmpeg'
	folderInDocker = '/tmp'

	command = '-i %s/%s' % (folderInDocker, fileName) 
	volumes = {folder:{'bind':folderInDocker, 'mode':'rw'}}

	client = docker.from_env()
	result = client.containers.run(imageName, command, volumes=volumes)
	print(result)

if __name__ == '__main__':
	runContainer(sys.argv[1])
