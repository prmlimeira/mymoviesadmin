import os
import sys

#DETECTING IF ARGUMENTS ARE VALID
MOVIES_ROOT_DIR = sys.argv[1]
CHOSEN_LANGUAGE_VERSION = sys.argv[2]
TARGET = sys.argv[3]

if ( not os.access(MOVIES_ROOT_DIR, "F_OK") ):
	print "The chosen movie source dir "+MOVIES_ROOT_DIR+" does not exists."
	exit()
if ( not os.access(MOVIES_ROOT_DIR, "R_OK") ):
	print "Permission to read chosen movie source dir "+MOVIES_ROOT_DIR+" is not granted."
	exit()
if ( not os.access(TARGET, "F_OK") ):
	print "The chosen target dir "+TARGET+" does not exists."
	exit()
if ( not os.access(TARGET, "W_OK") ):
	print "Permission to write target dir "+TARGET+" does not exists."
	exit()
if ( not CHOSEN_LANGUAGE_VERSION == "PT" or not CHOSEN_LANGUAGE_VERSION == "EN" ):
	print "Invalid language version argument "+CHOSEN_LANGUAGE_VERSION+"."
	exit()

#DECLARING FUNCTIONS TO BE IMPLEMENTED USING CRAWLERS
#def detectLanguageVersionOfMovieTitle(movie):
#def getMovieTitleInChosenLanguageVersion(movie):
#def getMovieTitleGenre(movieTitle):


#STARTING SCRIPT EXECUTION FOR PROPER MANAGEMENT
MOVIE_FOLDERS = os.listdir(MOVIES_ROOT_DIR)

for movieTitle in MOVIE_FOLDERS:

	if ( os.path.isfile(MOVIES_ROOT_DIR+"/"+movieTitle) ):
		#TODO deal with possible *FILES* listed
		continue

	os.chdir(MOVIES_ROOT_DIR)

	languageVersion = detectLanguageVersionOfMovieTitle(movieTitle)
	if ( not languageVersion == CHOSEN_LANGUAGE_VERSION ):
		movieTitle = getMovieTitleInChosenLanguageVersion(movieTitle)

	os.chdir(TARGET)

	genre = getMovieTitleGenre(movieTitle)

	genreFolderPath = TARGET+"/"+genre
	if ( not os.access(genreFolderPath, "F_OK") ):
		os.mkdir(genreFolderPath, 0744)
	os.chdir(genreFolderPath)

	if ( not os.access(genreFolderPath+"/"+movieTitle, "F_OK") ):

		os.mkdir(genreFolderPath+"/"+movieTitle, 0744)

		movieFiles = os.listdir(MOVIES_ROOT_DIR+"/"+movieTitle)
		for movieFile in movieFiles:

			if ( os.path.isdir(MOVIES_ROOT_DIR+"/"+movieTitle+"/"+movieFile) ):
				#TODO deal with possible *FOLDERS* listed
				continue

			originalMovieFile = open(MOVIES_ROOT_DIR+"/"+movieTitle+"/"+movieFile, "r")
			copiedMovieFile = open(genreFolderPath+"/"+movieTitle+"/"+movieFile, "w")
			copiedMovieFile.write(originalMovieFile.read())
			originalMovieFile.close()
			copiedMovieFile.close()
