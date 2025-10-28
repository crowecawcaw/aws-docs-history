# Importing images from a local

computer

The images are loaded directly from your computer. You can upload up to
30 images at a time.

The images you upload won't have labels associated with them. For more
information, see [Labeling images](md-labeling-images.md "md-labeling-images.md"). If you have many images to upload,
consider using an Amazon S3 bucket. For more information, see [Importing images from an Amazon S3 bucket](md-create-dataset-s3.md "md-create-dataset-s3.md").

###### Note

You can't use the AWS SDK to create a dataset with local images. Instead, create a
manifest file and upload the images to an Amazon S3 bucket. For more information, see
[Using a manifest file to import
images](md-create-dataset-ground-truth.md "md-create-dataset-ground-truth.md").

###### To create a dataset using images on a local computer (console)

1. Open the Amazon Rekognition console at
   [https://console.aws.amazon.com/rekognition/](https://console.aws.amazon.com/rekognition/ "https://console.aws.amazon.com/rekognition/").
2. Choose **Use Custom Labels**.
3. Choose **Get started**.
4. In the left navigation pane, choose **Projects**.
5. In the **Projects** page, choose the project to which you want to add a dataset.
   The details page for your project is displayed.
6. Choose **Create dataset**. The **Create dataset** page is
   shown.
7. In **Starting configuration**, choose either **Start with a single dataset**
   or **Start with a training dataset**. To create a higher quality model, we recommend starting with separate
   training and test datasets.

Single dataset

    1. In the **Training dataset details section**
     section, choose **Upload images from your
     computer**.
    2. Choose **Create Dataset**.
    3. On the project's dataset page, choose **Add
     images**.
    4. Choose the images you want to upload into the dataset
     from your computer files. You can drag the images or
     choose the images that you want to upload from your
     local computer.
    5. Choose **Upload images**.

Separate training and test datasets

    1. In the **Training dataset details**
     section, choose **Upload images from your
     computer**.
    2. In the **Test dataset details**
     section, choose **Upload images from your
     computer**.


    ###### Note

    Your training and test datasets can have different
     image sources.
    3. Choose **Create Datasets**. Your project's datasets
     page appears with a **Training** tab
     and a **Test** tab for the respective
     datasets.
    4. Choose **Actions** and then choose
     **Add images to training
     dataset**.
    5. Choose the images you want to upload to the dataset.
     You can drag the images or choose the images that you
     want to upload from your local computer.
    6. Choose **Upload images**.
    7. Repeat steps 5e - 5g. For step 5e, choose
     **Actions** and then choose
     **Add images to test
     dataset**.

8. Follow the steps in [Labeling images](md-labeling-images.md "md-labeling-images.md") to label your images.
9. Follow the steps in [Training a model (Console)](training-model.md#tm-console "training-model.md#tm-console") to train your model.
