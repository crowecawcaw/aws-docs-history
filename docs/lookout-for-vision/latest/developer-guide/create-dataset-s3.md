End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Creating a dataset using images stored in an

Amazon S3 bucket

You can create a dataset using images stored in an Amazon S3 bucket. With this option,
you can use the folder structure in your Amazon S3 bucket to automatically classify your
images. You can store the images in the console bucket or another Amazon S3 bucket in
your account.

## Setting up folders for automatic

labeling

During dataset creation, you can choose to assign label names to images based
on the name of the folder that contains the images. The folders must be a child
of the Amazon S3 folder path that you specify in **S3 URI**
when you create the dataset.

The following is the `train` folder for the Getting Started
example images. If you specify the Amazon S3 folder location as
`S3-bucket/circuitboard/train/`, the images in the folder
`normal` are assigned the label
`Normal`. Images in the folder
`anomaly` are assigned the label
`Anomaly`. The names of deeper child folders aren't used
to label images.

```

S3-bucket
  └── circuitboard
    └── train
        ├── anomaly
            ├── train-anomaly_1.jpg
            ├── train-anomaly_2.jpg
            ├── .
            └── .
        └── normal
            ├── train-normal_1.jpg
            ├── train-normal_2.jpg
            ├── .
            └── .

```

## Creating a dataset using images

from an Amazon S3 bucket

The following procedure creates a dataset using the [classification example](example-datasets.md#example-datasets-classification "example-datasets.md#example-datasets-classification")
images stored in an Amazon S3 bucket. To use your own images, create the folder
structure described in [Setting up folders for automatic
labeling](#create-dataset-s3-auto-label "#create-dataset-s3-auto-label").

The procedure also shows how to create a single dataset project, or a project
that uses separate training and test datasets.

If you don't choose to automatically label your images, you need to label the
images after the datasets is created. For more information, see [Classifying images (console)](model-label.md "model-label.md").

###### Note

If you've just completed [Creating your project](model-create-project.md "model-create-project.md"), the console should show your
project dashboard and you don't need to do steps 1 - 4.

###### To create a dataset using images stored in an Amazon S3 bucket

1. If you haven't already done so, upload the getting started images to
   your Amazon S3 bucket. For more information, see [Image classification
   dataset](example-datasets.md#example-datasets-classification "example-datasets.md#example-datasets-classification").
2. Open the Amazon Lookout for Vision console at [https://console.aws.amazon.com/lookoutvision/](https://console.aws.amazon.com/lookoutvision/ " https://console.aws.amazon.com/lookoutvision/").
3. In the left navigation pane, choose
   **Projects**.
4. In the **Projects** page, choose the project to which
   you want to add a dataset. The details page for your project is
   displayed.
5. Choose **Create dataset**. The **Create
   dataset** page is shown.

###### Tip

If you're following the Getting Started instructions, choose
**Create a training dataset and a test
dataset**. 6. Choose the **Single dataset** tab or the
**Separate training and test datasets** tab and
follow the steps.

Single dataset

    1. In the **Dataset configuration**
     section, choose **Create a single
     dataset**.
    2. Enter the information for steps 7 - 9 in the
     **Image source configuration**
     section.

Separate training and test datasets

    1. In the **Dataset configuration**
     section, choose **Create a training dataset
     and a test dataset**.
    2. For your training dataset, enter the information
     for steps 7 - 9 in the **Training dataset
     details** section.
    3. For your test dataset, enter the information for
     steps 7 - 9 in the **Test dataset
     details** section.


    ###### Note

    Your training and test datasets can have
     different image sources.

7. Choose **Import images from Amazon S3 bucket**.
8. In **S3 URI**, enter the Amazon S3 bucket location and
   folder path. Change `bucket` to the name of your Amazon S3
   bucket.
   1. If you're creating a single dataset project or a training
      dataset, enter the
      following:

   ```
   s3://`bucket`/circuitboard/train/
   ```

   2. If you're creating a test dataset enter the following:

   ```
   s3://`bucket`/circuitboard/test/
   ```

9. Choose **Automatically attach labels to images based on the
   folder**.
10. Choose **Create dataset**. A dataset page opens with
    your labeled images.
11. Follow the steps in [Training your model](model-train.md "model-train.md") to train your model.
