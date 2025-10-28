End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Creating a dataset with a manifest

file (console)

The following procedure shows you how to create a training or test dataset by
importing an SageMaker AI format manifest file that is stored in an Amazon S3 bucket.

After you create the dataset, you can add more images to the dataset, or add
labels to images. For more information, see [Adding images to your dataset](edit-dataset.md "edit-dataset.md").

###### To create a dataset

using an SageMaker AI Ground Truth format manifest file (console)

1. Create, or use an existing, Amazon Lookout for Vision compatible SageMaker AI Ground Truth
   format manifest file. For more information, see [Creating a manifest file](manifest-files.md "manifest-files.md").
2. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
3. In an Amazon S3 bucket, [create
   a folder](../../../AmazonS3/latest/userguide/create-folder.md "../../../AmazonS3/latest/userguide/create-folder.md") to hold your manifest file.
4. [Upload your manifest
   file](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") to the folder that you just created.
5. In the Amazon S3 bucket, create a folder to store your images.
6. Upload your images to the folder you just created.

###### Important

The `source-ref` field value in each JSON line must map
to images in the folder. 7. Open the Amazon Lookout for Vision console at [https://console.aws.amazon.com/lookoutvision/](https://console.aws.amazon.com/lookoutvision/ " https://console.aws.amazon.com/lookoutvision/"). 8. Choose **Get started**. 9. In the left navigation pane, choose
**Projects**. 10. Choose the project that you want to add to use with the manifest
file. 11. In the **How it works** section, choose
**Create dataset**. 12. Choose the **Single dataset** tab or the
**Separate training and test datasets** tab and
follow the steps.

Single dataset

    1. Choose **Create a single
     dataset**.
    2. In the **Image source
     configuration** section, choose
     **Import images labeled by SageMaker
     Ground Truth**.
    3. For **.manifest file location**,
     enter the location of your manifest file.

Separate training and test datasets

    1. Choose **Create a training dataset and a
     test dataset**.
    2. In the **Training dataset
     details** section, choose
     **Import images labeled by SageMaker
     Ground Truth**.
    3. In **.manifest file location**,
     enter the location of your training manifest
     file.
    4. In the **Test dataset details**
     section, choose **Import images labeled by
     SageMaker Ground Truth**.
    5. In **.manifest file location**,
     enter the location of your test manifest
     file.


    ###### Note

    Your training and test datasets can have
     different image sources.

13. Choose **Submit**.
14. Follow the steps in [Training your model](model-train.md "model-train.md") to train your model.
    Amazon Lookout for Vision creates a dataset in the Amazon S3 bucket `datasets` folder.
    Your original `.manifest` file remains unchanged.
