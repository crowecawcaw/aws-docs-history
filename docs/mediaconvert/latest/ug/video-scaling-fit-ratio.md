# Configuring fit scaling

If you choose **Fit** for your **Scaling behavior**,
MediaConvert scales your input image until it fits inside the dimensions of your output
resolution, without exceeding the dimensions of your output resolution.

For example, if your input file is `200` pixels by `200` pixels
and you want an output resolution that is `300` pixels by `400`
pixels, MediaConvert increases the image to `300` pixels by `300` pixels.
MediaConvert does not add padding to your output when you choose
**Fit**.

**Key**

The following key graphic shows input and output image width, height, cropping, and
padding. In this key graphic, input dimensions (on the top and left) are in blue and
output dimensions (on the right and bottom) are in red.

![Aspect Ratio Key](/images/mediaconvert/latest/ug/images/key.png)
The following table shows example image scaling behavior when your input and output
resolutions differ. For details about to read the images, reference the previous key
graphic.

| Condition                                                                        | Input                                                                                  | Output                                                                                            |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Input width less than output width<br>Input height less than output height       | Blue user icon with dimensions labeled: 200x200 inner square, 300x400 outer rectangle. | Blue figure icon with size dimensions labeled around it: 400 width, 300 height, 200 top and left. |
| Input width less than output width<br>Input height greater than output height    | Blue pawn-shaped figure on a checkered background with red measurement lines.          | Diagram showing a blue figure centered in a 400x200 pixel area with surrounding measurements.     |
| Input width greater than output width<br>Input height less than output height    | Blue user icon centered within a rectangular frame with dimensions labeled.            | Diagram showing a rectangle with dimensions 400x300 inside a larger 500x200 area.                 |
| Input width greater than output width<br>Input height greater than output height | Blue silhouette icon of a person within a red square frame on a grid background.       | Blue 3D figure resembling a snowman or stacked spheres centered in a square frame.                |
