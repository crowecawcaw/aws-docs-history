# Configuring default scaling (Fit with padding)

If you choose **Default (Fit with padding)** for your
**Scaling behavior**, MediaConvert scales your video image to your output
resolution. Then, if your input resolution has a different aspect ratio than your output
resolution, MediaConvert pads your video image until it matches the dimensions of your output
resolution.

For example, if your input file is `1280` pixels by `720` pixels
and you specify an output resolution that is `640` pixels by `480`
pixels, MediaConvert reduces the image size to `640x360` and then pads the top and
bottom of the image so that the final video resolution is `640x480`.
MediaConvert does not use cropping for the **Default** scaling
behavior.

**Key**

The following key graphic shows input and output image width, height, cropping, and
padding. In this key graphic, input dimensions (on the top and left) are in blue and
output dimensions (on the right and bottom) are in red.

![Aspect Ratio Key](images/key.png)
The following table shows example image scaling behavior when your input and output
resolutions differ. For details about to read the images, reference the previous key
graphic.

| Condition                                                                        | Input                                                                                  | Output                                                                                        |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Input width less than output width<br>Input height less than output height       | Blue user icon with dimensions labeled: 200x200 inner square, 300x400 outer rectangle. | Diagram showing a blue figure icon centered within a frame with dimensions labeled.           |
| Input width less than output width<br>Input height greater than output height    | Blue pawn-shaped figure on a checkered background with red measurement lines.          | Diagram showing a blue figure centered within a white rectangle surrounded by black bars.     |
| Input width greater than output width<br>Input height less than output height    | Blue user icon centered within a rectangular frame with dimensions labeled.            | Diagram showing dimensions of a rectangle: 500 width, 400 height, with inner area of 300x200. |
| Input width greater than output width<br>Input height greater than output height | Blue silhouette icon of a person within a red square frame on a grid background.       | Blue 3D snowman-like figure centered within nested squares on a checkered background.         |
