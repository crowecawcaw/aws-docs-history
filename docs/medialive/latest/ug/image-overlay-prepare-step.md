# Preparing the static image overlay

file

You must prepare each image overlay that you want to use in your MediaLive channel, and store
it in a suitable location, such as an Amazon S3 bucket. You can prepare the images at any time,
either before you start the channel, or while the channel is running.

###### To prepare the overlay file

1.  Determine the size (width and height in pixels) of the file you need. You might need
    several instances of one image, each in a different size. For more information, see the
    guidelines after this procedure.
2.  Create files with the following characteristics:
    - 32-bit bmp, png, or tga format

    - If you use a graphics program that outputs channels, set up to output the alpha
      channel. This ensures that the image overlay doesn't appear in a black or white
      box.

3.  Place the prepared file in a location that is accessible to the MediaLive. Make a note of
    the location and of any user credentials that users need to access the file. You can
    specify the location in one of these ways:

        * Amazon S3 bucket, using SSL. For example:


        `s3ssl://amzn-s3-demo-bucket/company-overlays/overlay.png`


        With MediaLive, the Amazon S3 bucket name mustn't use dot notation, which means it mustn't
         use . (dot) between the words in the bucket name.
        * A location that supports HTTP or HTTPS. For example:



        `https://203.0.113.0/corporate-logos/large.bmp`

    **Determining the image size if you are using the global
    option**

Keep in mind that with the global insertion option, MediaLive inserts the image on the output
video frame _before_ it sets the output video resolution.
This means that the image will be resized with the output video.

Follow these guidelines:

- Determine the size of the image relative to the _source_ video. For example, you might want an image to take up 10% of a
  1280×720 source video frame. In this case, the image height should be approximately 72
  pixels.
- You can prepare a new file that is the desired size. Or you can use an existing file
  and resize it when you prepare the insert action. MediaLive resizes the image before
  overlaying it on the video. Keep in mind that resizing might decrease the quality.
- If the channel has sources with different resolutions, you have two options:
  - You can optimize the image for one source.
  - Or you can create multiple versions of the same file, with each file in a
    different size. When you create an action to switch to a different input (with a
    different resolution), create a new insert image action, to insert the image that has
    the appropriate size.

- If the image is bigger than the source video frame, MediaLive trims off the excess.
  **Determining the image size if you are using the per-output
  option**

Keep in mind that with the per-output insertion option, MediaLive inserts the image on the
output video frame _after_ it sets the output video
resolution. This means that the image will be resized with the output video.

Follow these guidelines:

- Determine how many sizes you need of each image. For example, if you will insert the
  image on outputs that have three different resolutions, you need three different
  sizes.

You can obtain the different sizes in either of these ways:

    + You can create multiple versions of the same file, with each file in a different
     size. Create separate actions for each size. In each action, specify all the outputs
     where the image will be inserted.
    + You can resize the image when you create the insert action. Create separate
     actions for each size. In each action, resize the image by setting a height and width.
     Specify all the outputs where the resized image will be inserted.

- If the image is bigger than the output video frame, MediaLive trims off the excess.
