Defect Detection App is in preview release and is subject to change.

# Collecting images for your datasets

You need a collection of images to create a dataset. Your images must be PNG or JPEG format
files.

## Single dataset

To create an image classification model or a heatmap model, you need the following to start training:

- At least 20 images of normal objects.
- At least 10 images of anomalous objects.

To create an image segmentation model, you need the following to start training:

- At least 20 images of each anomaly type.
- Each anomalous image (image with anomaly types present) must have only one type of anomaly.
- At least 20 images of normal objects.

## Separate training and test datasets

To create an image classification model or a heatmap model, you need the following:

- At least 10 images of normal objects in the training dataset.
- At least 10 images of normal objects in the test dataset.
- At least 10 images of anomalous objects in the test dataset.

To create an image
segmentation model, you need the following:

- Each dataset needs at least 10 images of each anomaly type.
- Each anomalous image (image with anomaly types present) must contain only one type of anomaly.
- Each dataset must have at least 10 images of normal objects.

To create a higher quality model, use more than the minimum number of images. If you are
creating a segmentation model, we recommend including images with multiple anomaly types, but
these don't count towards the minimum that Defect Detection App needs to start training.

Your images should be of a single type of object. Also, you should have consistent image
capture conditions, such as camera positioning, lighting, and object pose.

All images in a project must have the same dimensions.

All training images must be unique images, preferably of unique objects. Normal images
should capture the normal variations of the object being analyzed. Anomalous images should
capture a diverse sampling of anomalies.

To collect images for your dataset, you can use the Defect Detection Station App. The application saves
images the images to a folder on your station. You then import the images to a dataset that
you create.

After you create the dataset, consider backing up the images. The Station App doesn't
automatically delete images, and you might need to delete images to free up disk space.

## Capturing images (Station App)

You can capture images by using the Station App. Before you start, you must first create
a image source for the camera.

The Station App shows a preview image from the image source. The preview image refreshes every
500 milliseconds.

###### To capture images with the Station App

1. If you haven't already, do the following:
   1. Create an image source for the camera that's attached to the station. For more
      information, see [Adding an image source](dda-configure-image-source.md "dda-configure-image-source.md").
   2. Configure the camera. For more information, see [Configuring the camera](dda-set-up-camera-position.md "dda-set-up-camera-position.md").

2. Open the Station App on your edge device by opening a browser and navigating to
   `x.x.x.x`:3000. For `x.x.x.x`, use the IP address of
   your edge device.
3. On the left menu of the application, choose
   **Management** and then **Image
   sources**.
4. In **Image sources** select the image source that
   you want use to capture images.
5. On the image source page, choose the **Image capture** tab.
6. In the **Image preview** section, turn off **Live preview**.
7. In the **Image preview** section, note the folder path in
   **Capture path**. This is the location where the Station App saves captured images. You
   need the location to upload images to your dataset.
8. If the image in the **Image preview** section is acceptable for your dataset, do the following:
   1. (Optional) In **File prefix** add a prefix to the file name that used
      for the image. A prefix is useful if you want to identify a captured image as normal or
      anomalous.
   2. Choose **Capture image** to save the image.

9. (Optional). You can see up to the last 12 captured images in the **Last {Number} captured images** section.
   If you don't need an image, choose **Delete image** to delete the image.
10. Repeat steps 7 and 8 until you have enough images for your dataset.
11. Next step: [Creating a project](dda-create-project.md "dda-create-project.md").
