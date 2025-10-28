End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Creating a dataset using images

stored on your local computer

You can create a dataset by using images that are loaded directly from your
computer. You can upload up to 30 images at a time. In this procedure, you can
create a single dataset project, or a project with separate training and test
datasets.

###### Note

If you've just completed [Creating your project](model-create-project.md "model-create-project.md"), the console should show your project
dashboard and you don't need to do steps 1 - 3.

###### To create a dataset using images on a local computer (console)

1. Open the Amazon Lookout for Vision console at [https://console.aws.amazon.com/lookoutvision/](https://console.aws.amazon.com/lookoutvision/ " https://console.aws.amazon.com/lookoutvision/").
2. In the left navigation pane, choose **Projects**.
3. In the **Projects** page, choose the project to which you
   want to add a dataset.
4. On the project details page, choose **Create
   dataset**.
5. Choose the **Single dataset** tab or the
   **Separate training and test datasets** tab and follow
   the steps.

Single dataset

    1. In the **Dataset configuration**
     section, choose **Create a single
     dataset**.
    2. In the **Image source configuration**
     section, choose **Upload images from your
     computer**.
    3. Choose **Create dataset**.
    4. On the dataset page, choose **Add
     images**.
    5. Choose the images you want to upload into the dataset
     from your computer files. You can drag the images or
     choose the images that you want to upload from your
     local computer.
    6. Choose **Upload images**.

Separate training and test datasets

    1. In the **Dataset configuration**
     section, choose **Create a training dataset and
     a test dataset**.
    2. In the **Training dataset details**
     section, choose **Upload images from your
     computer**.
    3. In the **Test dataset details**
     section, choose **Upload images from your
     computer**.


    ###### Note

    Your training and test datasets can have different
     image sources.
    4. Choose **Create dataset**. A dataset
     page appears with a **Training** tab
     and a **Test** tab for the respective
     datasets.
    5. Choose **Actions** and then choose
     **Add images to training
     dataset**.
    6. Choose the images you want to upload to the dataset.
     You can drag the images or choose the images that you
     want to upload from your local computer.
    7. Choose **Upload images**.
    8. Repeat steps 5e - 5g. For step 5e, choose
     **Actions** and then choose
     **Add images to test
     dataset**.

6. Follow the steps in [Labeling images](model-labelling-overview.md "model-labelling-overview.md") to label your images.
7. Follow the steps in [Training your model](model-train.md "model-train.md") to train your model.
