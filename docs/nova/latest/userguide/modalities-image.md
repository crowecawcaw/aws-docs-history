# Image understanding

Amazon Nova models allow you to include multiple images in the payload with a total payload limit of 25 MB. However, you can specify an Amazon S3 URI that contains your images for image understanding.
This approach allows you to leverage the model for larger images and more images without being constrained by the 25 MB payload limitation. Amazon Nova models can analyze the passed images and answer
questions, classify images, and summarize images based on your provided instructions.

## Image size information

To provide the best possible results, Amazon Nova automatically rescales input images up
or down depending on their aspect ratio and original resolution. For each image,
Amazon Nova first identifies the closest aspect ratio from 1:1, 1:2, 1:3, 1:4, 1:5, 1:6,
1:7, 1:8, 1:9 2:3, 2:4 and their transposes. Then the image is rescaled so that at least
one side of the image is greater than 896px or the length of shorter side of the
original image, while maintaining the closest aspect ratio. There's a maximum resolution
of 8,000x8,000 pixels

## Bounding box detection

The Amazon Nova Lite and Amazon Nova Pro models are trained to precisely detect bounding boxes within images. This capability can be valuable when the
objective is to obtain the coordinates of a specific object of interest. The bounding box detection functionality of the Amazon Nova model makes it a
suitable candidate for image grounding tasks, thereby enabling enhanced understanding of screen shots. The Amazon Nova model outputs bounding boxes on
a scale of [0, 1000), and after these coordinates are obtained, they can be resized based on the image dimensions as a post-processing step.

## Image to tokens conversion

As previously discussed, images are resized to maximize information extraction, while
still maintaining the aspect ratio. What follows are some examples of sample image
dimensions and approximate token calculations.

| image_resolution (HxW or WxH) | 900 x 450 | 900 x 900 | 1400 x 900 | 1.8K x 900 | 1.3Kx1.3K |
| ----------------------------- | --------- | --------- | ---------- | ---------- | --------- |
| Estimated token count         | ~800      | ~1300     | ~1800      | ~2400      | ~2600     |

So for example, consider an example image that is 800x400 in size, and you want to
estimate the token count for this image. Based on the dimensions, to maintain an aspect
ratio of 1:2, the closest resolution is 900x450. Therefore, the approximate token count
for this image is about 800 tokens.
