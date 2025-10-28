Defect Detection App is in preview release and is subject to change.

# Adding an image source

Your [workflows](dda-components.md#dda-component-workflow "dda-components.md#dda-component-workflow") need an image source that makes
images available for analysis with your model. An image source can be a camera on the
same network as your edge device, or a folder on the edge device.
If the image source is a camera, you can also specify the gain, exposure, and Gstreamer pipeline settings for the camera.

If you intend to use the Station App to capture images for your dataset, you need to add
an image source for the camera attached to the station. For more information, see [Collecting images for your datasets](dda-collect-images.md "dda-collect-images.md").

###### To add an image source (Station App)

1. Open the Station App on your edge device by opening a browser and navigating to
   `x.x.x.x`:3000. For `x.x.x.x`, use the IP address of
   your edge device.
2. On the left menu panel of the application, choose **Management** and then **Image sources**.
3. Choose **Add image source**.
4. Do one of the following:
   - ###### To use a camera as an image source
     1. In **Type**, choose **Camera**.
     2. In the **Cameras discovered** section,
        select the camera that you want to use. If you don't see any
        cameras listed, make sure your cameras are correctly installed
        and choose **Rediscover
        cameras** to try again. For more information, see [Installing the cameras on the edge device](dda-set-up-device-station.md#dda-set-up-camera "dda-set-up-device-station.md#dda-set-up-camera").

   - ###### To use a folder
     1. In **Type**, choose **Folder**.
     2. In **Folder path**, enter the folder path for the folder that provides images for the image source.
        The path you enter is relative to the `/aws_dda/` folder on the edge device.

5. In **Image source details** enter an image source name and description for the image source.
6. Choose **Save**.
7. If you created a camera image source, and you want to change the camera settings, do [Configuring the camera](dda-set-up-camera-position.md "dda-set-up-camera-position.md").
