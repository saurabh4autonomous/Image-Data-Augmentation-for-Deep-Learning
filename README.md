# Image-Data-Augmentation-for-Deep-Learning
This Repository covers the basic methods to augment image data for Deep Learning

Preprocessing the data includes Augmentation and Normalization techniques as described below:
 model have to handle all of these conditions. So, it’s probably better not to truncate our dataset in order to obtain data balance. So for making our model more robust, I included following Augmentation techniques:

* Image Scaling : Zooming of 12.5 %
* Image Translation : In each direction for about 3 Pixels
    1. North Direction
    2. South Direction
    3. East Direction
    4. West Direction
    5. North-East Direction
    6. South-East Direction
    7. North-West Direction
    8. South-West Direction
* Image Rotation : 5 Degrees Rotation
    1. Clockwise Rotation
    2. Counter-Clockwise Rotation
