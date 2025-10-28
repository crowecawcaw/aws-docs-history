Defect Detection App is in preview release and is subject to change.

# Configuring the camera

If an image source is a camera, you can use a live image from the camera in the Defect Detection Station App to position the camera and
make camera setting adjustments.

###### Note

The Station App refreshes the image every 500 milliseconds.

The settings you can change are:

- **gain** — increases the brightness of the images output by the camera. The value
  you enter is the _raw_ gain value for the camera. The default value is `10`.
- **exposure** — The amount of time, in milliseconds, that the image
  sensor is exposed to light when capturing an image. The default value is
  `4000`.
- **gstreamer** — Station App uses the
  gstreamer library to capture images from a camera, and make them available
  for analysis with your model, or for adding to a dataset. The default
  settings are `video/x-bayer, format=bggr ! bayer2rgb ! video/x-raw,
format=RGBA`. For more information, see [gstreamer](https://gstreamer.freedesktop.org/ "https://gstreamer.freedesktop.org/").

###### Topics

- [Configure the camera (Station App)](#dda-confgure-camera-console "#dda-confgure-camera-console")

## Configure the camera (Station App)

###### To configure the camera (Station App)

1. Open the Station App on your edge device by opening a browser and navigating
   to `x.x.x.x`:3000. For `x.x.x.x`, use
   the IP address of your edge device.
2. On the left menu of the application, choose **Management** and
   then **Image sources**.
3. In **Images sources**, choose the image source with the
   camera that you want to configure. If you don't have an image source, do
   [Adding an image source](dda-configure-image-source.md "dda-configure-image-source.md").
4. Choose the **Image capture** tab.
5. In the **Image preview** section, turn on **Live
   preview**. The preview image is updated every 500ms.
6. Decide if the image from the camera is acceptable.

You can use the following commands to pan and zoom the image.

    * Pan image — Choose the pan button (
    ![Pan](images/pan.png)
    ). Click and hold the mouse button and then drag the
     mouse to pan across the image.
    * Zoom image — Zoom in an out of the image with the zoom in button (
    ![Zoom in](images/zoom-in.png)
    ) and the zoom out button
    ![Zoom out](/images/lookout-for-vision/latest/dda-user-guide/images/zoom-out.png)
    . Double-click the image to zoom 2x into to the
     image. Use the mouse scroll wheel to zoom in and out of the image. The
     mouse cursor position is the center position for zooming (in or
     out).
    * Reset image size — Choose the reset button (
    ![Reset image](images/reset.png)
    ) or press Ctrl + 0.

If you need to make changes, choose
**Edit image settings** to make changes. You can adjust
the **Gain** and **Exposure** values.

To make Gstreamer setting changes, do the following:

    1. Choose **Advanced settings**.
    2. In the **Gstreamer pipeline** edit box, enter the
     changes that you want to make.
    3. Choose **Apply** to apply your changes. To reset
     to the default values, choose **Reset**.Changes are immediately saved to the camera. Use the preview image to

confirm that the changes are acceptable.

Choose **Save** to save your changes. 7. Next step: [Collecting images for your datasets](dda-collect-images.md "dda-collect-images.md").
