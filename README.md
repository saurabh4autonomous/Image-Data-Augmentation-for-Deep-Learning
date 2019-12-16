# Image-Data-Augmentation-for-Deep-Learning

This Repository covers the basic methods to augment image data for Deep Learning
---

## Introduction
Since the degree of model overfitting is determined by both its power and the amount of training it receives, providing a convolutional
network with more training examples can reduce overfitting. Since these networks are usually trained with all available data, one approach
is to either generate new data from scratch (if possible) or Augment existing data to create new ones. For example, input images could be
asymmetrically cropped by a few percent to create new examples with the same label as the original
So for making our model more robust, following Augmentation techniques can be used:

## Types of Augmentation Used here
* Image Scaling : Zooming to a maximum of 30%
Percentage of scaling can be entered in  the `zoom_command_list`
number of images created per image = num of elements in `zoom_command_list`
* Image Translation : Percentage of Translation,orientation must be entered in  the `translation_command_list`
Here are all the listed methods (orientations) used for translation:
    1. North Direction
    2. South Direction
    3. East Direction
    4. West Direction
    5. North-East Direction
    6. South-East Direction
    7. North-West Direction
    8. South-West Direction
The number of elements enetered here shall create images as per this count:
number of images created per image = num of elements in `translation_command_list` x 8 
* Image Rotation : Enter the degrees for rotation and the Direction [clockwise,Anticlockwise]
    1. Clockwise Rotation
    2. Counter-Clockwise Rotation
Rotation command must be entered in  the `rot_command_list`
The number of elements enetered here shall create images as per this count:
number of images created per image = num of elements in `rot_command_list`

## Output
    ![output-1](./writeup_images/output_thumbnail_for_image-1.jpg)
    ![output-2](./writeup_images/output_thumbnail_for_image-2.jpg)
## Python Libraries used    
* numpy
* opencv
* Image from PIL
* glob
