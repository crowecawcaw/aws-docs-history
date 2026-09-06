

# Configuring fit without upscaling scaling
<a name="video-scaling-fit-without-upscaling"></a>

If you choose **Fit without upscaling** for your **Scaling behavior**, MediaConvert decreases the size of your input image until it fits inside the dimensions of your output resolution, without going over any of the dimensions of your output resolution. If your input image is smaller than your output image, MediaConvert does not increase the size of your image.

For example, if your input image is `400` pixels by `400` pixels and you want an output resolution that is `200` pixels by `300` pixels, MediaConvert shrinks your input image to `200` pixels by `200` pixels. MediaConvert does not add padding when you choose **Fit without upscaling**.

**Note**  
You cannot choose **Fit without upscaling** when you enable **Automated ABR** in **Apple HLS**, **DASH**, or **CMAF** output groups.

**Key**

The following key graphic shows input and output image width, height, cropping, and padding. In this key graphic, input dimensions (on the top and left) are in blue and output dimensions (on the right and bottom) are in red. 

![Aspect Ratio Key](http://docs.aws.amazon.com/mediaconvert/latest/ug/images/key.png)


The following table shows example image scaling behavior when your input and output resolutions differ. For details about to read the images, reference the previous key graphic.


|  Condition  |  Input  |  Output  | 
| --- | --- | --- | 
| Input width less than output width<br />Input height less than output height |  ![Blue user icon with dimensions labeled: 200x200 inner square, 300x400 outer rectangle.](http://docs.aws.amazon.com/mediaconvert/latest/ug/images/input1-thumb.png)  |  ![Diagram showing a blue user icon surrounded by numbered dimensions: 200, 300, and 400.](http://docs.aws.amazon.com/mediaconvert/latest/ug/images/keep1-unpadded-thumb.png)  | 
| Input width less than output width<br />Input height greater than output height |  ![Blue pawn-shaped figure on a checkered background with red measurement lines.](http://docs.aws.amazon.com/mediaconvert/latest/ug/images/input2-thumb.png)  |  ![](http://docs.aws.amazon.com/mediaconvert/latest/ug/images/fit2-unpadded-thumb.png)  | 
| Input width greater than output width<br />Input height less than output height |  ![](http://docs.aws.amazon.com/mediaconvert/latest/ug/images/input3-thumb.png)  |  ![](http://docs.aws.amazon.com/mediaconvert/latest/ug/images/fit3-unpadded-thumb.png)  | 
| Input width greater than output width<br />Input height greater than output height |  ![Blue silhouette icon of a person within a red square frame on a grid background.](http://docs.aws.amazon.com/mediaconvert/latest/ug/images/input4-thumb.png)  |  ![Blue 3D figure resembling a snowman or stacked spheres centered in a square frame.](http://docs.aws.amazon.com/mediaconvert/latest/ug/images/fit4-unpadded-thumb.png)  | 