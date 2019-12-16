#Loading all the Libraries needed
import numpy as np
import cv2 as cv
from PIL import Image
import glob
###############################################################################
class Augmentation:
    def __init__(self,path):
        self.counter = 0
        self.image_list = []
        self.path = path

    # Functions to be used  for Augmentation of Training images
    def Translation_images(self, image_index, orientation_index, command_index):
        img = self.image_list[image_index]
        height, width = img.shape[:2]
        orientation = orientation_index
        percentage = translation_command_list[command_index]
        Translation_Width = int((percentage*width)/100)

        if (orientation == 0):
            # North
            M = np.float32([[1, 0, 0], [0, 1, -Translation_Width]])
        elif (orientation == 1):
            # West
            M = np.float32([[1, 0, -Translation_Width], [0, 1, 0]])
        elif (orientation == 2):
            # East
            M = np.float32([[1, 0, Translation_Width], [0, 1, 0]])
        elif (orientation == 3):
            # South
            M = np.float32([[1, 0, 0], [0, 1, Translation_Width]])
        elif (orientation == 4):
            # SouthEast
            M = np.float32([[1, 0, Translation_Width], [0, 1, Translation_Width]])
        elif (orientation == 5):
            # NorthEast
            M = np.float32([[1, 0, Translation_Width], [0, 1, -Translation_Width]])
        elif (orientation == 6):
            # SouthWest
            M = np.float32([[1, 0, -Translation_Width], [0, 1, Translation_Width]])
        elif (orientation == 7):
            # NorthWest
            M = np.float32([[1, 0, -Translation_Width], [0, 1, -Translation_Width]])

        translated = cv.warpAffine(img, M, (width, height), borderMode=cv.BORDER_REPLICATE)

        return translated


    def Rotation_Images(self, image_index, orientation_index, command_index  ):
        img = self.image_list[image_index]
        height, width = img.shape[:2]
        Rotational_Angle = rot_command_list[command_index]
        dir = orientation_index

        if (dir == 0):
            # CW
            M = cv.getRotationMatrix2D(((width - 1) / 2.0, (height - 1) / 2.0), 360 - Rotational_Angle, 1)
        elif (dir == 1):
            # CCW
            M = cv.getRotationMatrix2D(((width - 1) / 2.0, (height - 1) / 2.0), Rotational_Angle, 1)

        rotated = cv.warpAffine(img, M, (width, height), borderMode=cv.BORDER_REPLICATE)
        return rotated


    def ZoomIn_Images(self, image_index, command_index):
        img = self.image_list[image_index]
        height, width = img.shape[:2]
        percentage = zoom_command_list[command_index]
        #capping the max Zoom to 30 Percent
        if(percentage  > 30):
            percentage = 30
        croppedOutSizeW = int((percentage*width)/100)
        croppedOutSizeH = int((percentage*height)/100)
        
        cropped_img = img[croppedOutSizeH:(height - croppedOutSizeH), croppedOutSizeW:(width - croppedOutSizeW)]
        resized = cv.resize(cropped_img, (width, height), fx=1, fy=1)
        return resized

    def run_augmentation (self):
        for filename in glob.glob(self.path):
            im = Image.open(filename)
            self.image_list.append(np.array(im))
        for i in range(len(self.image_list)):
            for loop in range(len(translation_command_list)):
                for inner in range(MAX_ORIENTATIONS_FOR_TRANSLATION):
                    self.counter = self.counter +1
                    im = Image.fromarray(self.Translation_images(i,inner,loop))
                    im.save("output/image-"+ str(i)+ "-" + str(self.counter) + ".jpg")
                    # 8 x 5 Images = 40

            for loop2 in range(len(zoom_command_list)):
                self.counter = self.counter +1
                im = Image.fromarray(self.ZoomIn_Images(i, loop2))
                im.save("output/image-"+ str(i)+ "-" + str(self.counter) + ".jpg")
                # 5 x1 =5

            for loop3 in range(len(rot_command_list)):
                self.counter = self.counter +1
                im = Image.fromarray(self.Rotation_Images(i, 0, loop3))
                im.save("output/image-"+ str(i)+ "-" + str(self.counter) + ".jpg")
                self.counter = self.counter +1
                im = Image.fromarray(self.Rotation_Images(i, 1, loop3))
                im.save("output/image-"+ str(i)+ "-" + str(self.counter) + ".jpg")
                #5 x 2 =10

            self.counter = 0

##############################################################################################
MAX_ORIENTATIONS_FOR_TRANSLATION = 8
translation_command_list = [10, 15, 20, 25, 30]
zoom_command_list = [10, 15, 20, 25, 30]
rot_command_list = [4, 6, 8, 10, 12]
brightness_contrast_control = [[1,10],[1,20],[2,10],[2,20],[3,50]]
path = 'input/image-*.jpg'
p1 = Augmentation(path)
p1.run_augmentation()
###############################################################################################