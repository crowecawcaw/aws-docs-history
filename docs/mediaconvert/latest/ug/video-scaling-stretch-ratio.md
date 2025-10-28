# Configuring stretch to output scaling

If you choose **Stretch to output** for your **Scaling
behavior**, MediaConvert stretches or shrinks your video image to your output
resolution.

For example, if your input image is `200` pixels by `200` pixels
and you want an output resolution that is `300` pixels by `400`
pixels, MediaConvert increases the size of your input image to `300` pixels by
`400` pixels, distorting the proportions of your output image. MediaConvert does
not use padding or cropping for the **Stretch to output** scaling
behavior.

###### Important

If your input resolution has a different aspect ratio than your output resolution,
your output image will be distorted when compared to your input image.

**Key**

The following key graphic shows input and output image width, height, cropping, and
padding. In this key graphic, input dimensions (on the top and left) are in blue and
output dimensions (on the right and bottom) are in red.

![Aspect Ratio Key](images/key.png)
The following table shows example image scaling behavior when your input and output
resolutions differ. For details about to read the images, reference the previous key
graphic.

| Condition                                                                     | Input                                                                                  | Output                                                                                           |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Input width less than output width Input height less than output height       | Blue user icon with dimensions labeled: 200x200 inner square, 300x400 outer rectangle. | Blue 3D object resembling a chess pawn piece with dimensions labeled around it.                  |
| Input width less than output width Input height greater than output height    | Blue pawn-shaped figure on a checkered background with red measurement lines.          | Diagram showing dimensions of a blue cylindrical object on a checkered background.               |
| Input width greater than output width Input height less than output height    | Blue user icon centered within a rectangular frame with dimensions labeled.            | Diagram showing a blue bowling pin shape centered within nested rectangles and numerical labels. |
| Input width greater than output width Input height greater than output height | Blue silhouette icon of a person within a red square frame on a grid background.       | Blue 3D figure resembling a snowman or stacked spheres centered in a square frame.               |
