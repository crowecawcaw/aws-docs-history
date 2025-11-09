# Configuring fill scaling

If you choose **Fill** for your **Scaling
behavior**, MediaConvert scales your input image until it fills the dimensions of your
output resolution, and crops anything that exceeds the dimensions of your output
resolution.

For example, if your input file is `200` pixels by `200` pixels
and you want an output resolution that is `300` pixels by `400`
pixels, MediaConvert increases the size of your input image to `400` pixels by
`400` pixels, crops off the top and bottom `50` pixels, and
returns a `300` pixel by `400` pixel file. MediaConvert does not add
padding to your output when you choose **Fill**.

**Key**

The following key graphic shows input and output image width, height, cropping, and
padding. In this key graphic, input dimensions (on the top and left) are in blue and
output dimensions (on the right and bottom) are in red.

![Aspect Ratio Key](images/key.png)
The following table shows example image scaling behavior when your input and output
resolutions differ. For details about to read the images, reference the previous key
graphic.

| Condition                                                                        | Input                                                                                  | Output                                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Input width less than output width<br>Input height less than output height       | Blue user icon with dimensions labeled: 200x200 inner square, 300x400 outer rectangle. | Blue figure icon with dimensions and sizing information overlaid on a checkered background. |
| Input width less than output width<br>Input height greater than output height    | Blue pawn-shaped figure on a checkered background with red measurement lines.          | Diagram showing a blue figure with dimensions: 200 height, 300 width, 400 total height.     |
| Input width greater than output width<br>Input height less than output height    | Blue user icon centered within a rectangular frame with dimensions labeled.            | Blue hourglass-shaped icon with numerical values indicating dimensions around it.           |
| Input width greater than output width<br>Input height greater than output height | Blue silhouette icon of a person within a red square frame on a grid background.       | Blue 3D figure centered in a square frame with measurement indicators on the sides.         |
