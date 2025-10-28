# Configuring fit without upscaling scaling

If you choose **Fit without upscaling** for your **Scaling
behavior**, MediaConvert decreases the size of your input image until it fits
inside the dimensions of your output resolution, without going over any of the
dimensions of your output resolution. If your input image is smaller than your output
image, MediaConvert does not increase the size of your image.

For example, if your input image is `400` pixels by `400` pixels
and you want an output resolution that is `200` pixels by `300`
pixels, MediaConvert shrinks your input image to `200` pixels by `200`
pixels. MediaConvert does not add padding when you choose **Fit without
upscaling**.

###### Note

You cannot choose **Fit without upscaling** when you enable
**Automated ABR** in **Apple HLS**,
**DASH**, or **CMAF** output groups.

**Key**

The following key graphic shows input and output image width, height, cropping, and
padding. In this key graphic, input dimensions (on the top and left) are in blue and
output dimensions (on the right and bottom) are in red.

![Aspect Ratio Key](images/key.png)
The following table shows example image scaling behavior when your input and output
resolutions differ. For details about to read the images, reference the previous key
graphic.

| Condition                                                                     | Input                                                                                  | Output                                                                                        |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Input width less than output width Input height less than output height       | Blue user icon with dimensions labeled: 200x200 inner square, 300x400 outer rectangle. | Diagram showing a blue user icon surrounded by numbered dimensions: 200, 300, and 400.        |
| Input width less than output width Input height greater than output height    | Blue pawn-shaped figure on a checkered background with red measurement lines.          | Diagram showing a blue figure centered in a 400x200 pixel area with surrounding measurements. |
| Input width greater than output width Input height less than output height    | Blue user icon centered within a rectangular frame with dimensions labeled.            | Diagram showing a rectangle with dimensions 400x300 inside a larger 500x200 area.             |
| Input width greater than output width Input height greater than output height | Blue silhouette icon of a person within a red square frame on a grid background.       | Blue 3D figure resembling a snowman or stacked spheres centered in a square frame.            |
