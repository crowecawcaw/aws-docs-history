# Assigning image-level labels to an image

You use image-level labels to train models that classify images into categories. An image-level label indicates
that an image contains an object, scene or concept.
For example, the following image shows a river. If your model classifies images as containing rivers, you would
add a _river_ image-level label. For more information, see [Purposing datasets](md-dataset-purpose.md "md-dataset-purpose.md").

![Lake reflecting mountains and clouds in still water at sunset or sunrise.](images/pateros.jpg)
A dataset that contains image-level labels, needs at least two labels defined.
Each image needs at least one assigned label that identifies the object, scene, or
concept in the image.

###### To assign image-level labels to an image (console)

1. Open the Amazon Rekognition console at
   [https://console.aws.amazon.com/rekognition/](https://console.aws.amazon.com/rekognition/ "https://console.aws.amazon.com/rekognition/").
2. Choose **Use Custom Labels**.
3. Choose **Get started**.
4. In the left navigation pane, choose **Projects**.
5. In the **Projects** page, choose the project that you want to use.
   The details page for your project is displayed.
6. In the left navigation pane, choose **Dataset**.
7. If you want to add labels to your training dataset, choose the **Training** tab.
   Otherwise choose the **Test** tab to add labels to the test dataset.
8. Choose **Start labeling** to enter labeling mode.
9. In the image gallery, select one or more images that you want to add labels to. You can only
   select images on a single page at a time. To select a contiguous range of
   images on a page:
   1. Select the first image in the range.
   2. Press and hold the shift key.
   3. Select the last image range. The images between the first and second image are also selected.
   4. Release the shift key.

10. Choose **Assign image-level labels**.
11. In the **Assign image-level label to selected images** dialog box, select a label that you
    want to assign to the image or images.
12. Choose **Assign** to assign label to the image.
13. Repeat labeling until every image is annotated with the required labels.
14. Choose **Save changes** to save your changes.

## Assign image-level labels (SDK)

You can use the `UpdateDatasetEntries` API to add or update the image-level labels that
are assigned to an image.
`UpdateDatasetEntries` takes one or more JSON lines. Each JSON Line represents a single image.
For an image with an image-level label, the JSON Line looks similar to the following.

```
{"source-ref":"s3://custom-labels-console-us-east-1-nnnnnnnnnn/gt-job/manifest/IMG_1133.png","TestCLConsoleBucket":0,"TestCLConsoleBucket-metadata":{"confidence":0.95,"job-name":"labeling-job/testclconsolebucket","class-name":"Echo Dot","human-annotated":"yes","creation-date":"2020-04-15T20:17:23.433061","type":"groundtruth/image-classification"}}

```

The `source-ref` field indicates the location of the image. The JSON line also includes the image-level labels assigned to the image.
For more information, see [Importing
image-level labels in manifest files](md-create-manifest-file-classification.md "md-create-manifest-file-classification.md").

###### To assign image-level labels to an image

1. Get the get JSON Line for the existing image by using the `ListDatasetEntries`. For the `source-ref` field, specify
   the location of the image that you want to assign the label to. For more information, see [Listing dataset entries (SDK)](md-listing-dataset-entries-sdk.md "md-listing-dataset-entries-sdk.md").
2. Update the JSON Line returned in the previous step using the information at [Importing
   image-level labels in manifest files](md-create-manifest-file-classification.md "md-create-manifest-file-classification.md").
3. Call `UpdateDatasetEntries` to update the image. For more information, see [Adding more images to a dataset](md-add-images.md "md-add-images.md").
