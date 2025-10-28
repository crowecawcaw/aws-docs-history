Defect Detection App is in preview release and is subject to change.

# Creating your datasets

Datasets manage images and labels assigned to those images. Training a model requires a
training dataset (trains the model) and a test dataset (evaluates the trained model). To train a
model with Defect Detection App, you must create a training dataset, and optionally you can create a test
dataset. If you only create a training dataset, Defect Detection Station App, trains the model by
splitting the training dataset to create a test dataset. If you want control over the images
that Defect Detection App uses to evaluate a model, you can create a test
dataset. For example, you might want to use a set of benchmark images to
compare evaluation results between different models thjat you train.

You create a dataset by using the Defect Detection App Console. During dataset creation you upload the
images that you want to use to train the model. You can choose to automatically classify the
images as normal or anomaly. This saves you from having to classify the images in the image gallery.
After you create the dataset, you label the
images according to the type of model that you want to create (image classification or image
segmentation). You can add more images to the dataset, as you need them. For example, if the
training evaluation results are poor, you can improve the model by adding more images to the
dataset. Note that you can't delete images from a dataset.

The following procedure shows how to create a training dataset and optionally a test dataset.

###### To create your datasets

1. [Sign in](dda-signin-dda-web-app.md "dda-signin-dda-web-app.md") to the Defect Detection App Console.
2. In the top navigation pane, choose **Projects**.
3. On the projects page, choose the project for the dataset.
4. The **Training dataset** tab displays the dataset details. Initially,
   the dataset contains no images.
5. In the **Images** panel, choose **Add images**.
6. In the **Add images to dataset** page, choose a classification method for
   the images that you upload. You can classify the images as normal, anomaly, no classification,
   or use a file prefix to classify the image. If you choose to use a file prefix, images without
   the matching prefixes are added to the dataset, but you will need to classify
   them. To use a file prefix, do the following:
   1. Enter the file prefix for normal
      images in **Normal prefix**.
   2. Enter the file prefix for anomalous images in **Anomaly prefix**.

7. Choose **Upload files** and choose the images that you want to use.
   Alternatively, drag and drop the image files to the page. If you used the Station App to capture
   images, the images are in the folder you noted in step 6 of [Capturing images (Station App)](dda-collect-images.md#dda-capture-images-console "dda-collect-images.md#dda-capture-images-console"). You can
   upload up to 30 images at a time.
8. Choose **Save** to finish uploading the images.
9. Repeat the **Add images** step until you have added all the images you need to create the
   dataset. To guide you, note the training requirements for the training dataset (and test requirements, if
   you're creating a test dataset).
10. (Optional) Create a test dataset by doing the following:
    1. On the project details page, choose the **Test dataset** tab.
    2. Choose **Create test dataset**.
    3. Repeat steps 6 - 9 to add images to your test dataset.

11. Next step: [Annotating dataset images](dda-label-dataset-images.md "dda-label-dataset-images.md").
