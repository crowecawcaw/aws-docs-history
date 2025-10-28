# Importing images from an Amazon S3 bucket

The images are imported from an Amazon S3 bucket. You can use the console bucket, or another Amazon S3 bucket in your AWS account.
If you are using the console bucket, the required permissions are already set up. If you are not using the console bucket, see
[Accessing external Amazon S3 Buckets](su-console-policy.md#su-external-buckets "su-console-policy.md#su-external-buckets").

###### Note

You can't use the AWS SDK to create a dataset directly from images in an Amazon S3 bucket. Instead, create a
manifest file that references the source locations of the images. For more information, see
[Using a manifest file to import
images](md-create-dataset-ground-truth.md "md-create-dataset-ground-truth.md")

During dataset creation, you can choose to assign label names to images based on the
name of the folder that contains the images. The folder(s) must be a child of the Amazon S3 folder path that you specify in
**S3 folder location** during dataset creation. To create a dataset, see [Creating a dataset by importing images from an S3 bucket](#cd-procedure "#cd-procedure").

For example, assume the following folder structure in an Amazon S3 bucket. If you specify the Amazon S3 folder location as
_S3-bucket/alexa-devices_, the images in the folder _echo_ are assigned the label
_echo_. Similarly, images in the folder _echo-dot_ are assigned the
label _echo-dot_. The names of deeper child folders aren't used to label images. Instead, the appropriate
child folder of the Amazon S3 folder location is used. For example, images in the folder _white-echo-dots_ are assigned the label
_echo-dot_. Images at the level of the S3 folder location (_alexa-devices_) don't have labels assigned to them.

Folders deeper in the folder structure can be used to label images by specifying a deeper S3 folder location. For example,
If you specify _S3-bucket/alexa-devices/echo-dot_, Images in the folder _white-echo-dot_
are labeled _white-echo-dot_. Images outside the specified s3 folder location, such as _echo_, aren't imported.

```
S3-bucket
└── alexa-devices
    ├── echo
    │   ├── echo-image-1.png
    │   └── echo-image-2.png
    │   ├── .
    │   └── .
    └── echo-dot
        ├── white-echo-dot
        │   ├── white-echo-dot-image-1.png
        │   ├── white-echo-dot-image-2.png
        │
        ├── echo-dot-image-1.png
        ├── echo-dot-image-2.png
        ├── .
        └── .

```

We recommend that you use the Amazon S3 bucket (console bucket) created for you by Amazon Rekognition when you first
opened the console in the current AWS region. If the Amazon S3 bucket that you are using is
different (external) to the console bucket, the console prompts you to
set up appropriate permissions during dataset creation. For more information, see [Step 2: Set up Amazon Rekognition Custom Labels console permissions](su-console-policy.md "su-console-policy.md").

## Creating a dataset by importing images from an S3 bucket

The following procedure shows you how to create a dataset using images stored in the Console S3 bucket.
The images are automatically labeled with the name of the folder in which they are stored.

After you have imported your images, you can add more images, assign labels, and add bounding boxes from a dataset's
gallery page. For more information, see [Labeling images](md-labeling-images.md "md-labeling-images.md").

###### Upload your images to an Amazon Simple Storage Service bucket

1. Create a folder on your local file system. Use a folder name such as _alexa-devices_.
2. Within the folder you just created, create folders named after each label that you want to
   use. For example, _echo_ and
   _echo-dot_. The folder structure should be
   similar to the following.

```
alexa-devices
├── echo
│   ├── echo-image-1.png
│   ├── echo-image-2.png
│   ├── .
│   └── .
└── echo-dot
    ├── echo-dot-image-1.png
    ├── echo-dot-image-2.png
    ├── .
    └── .
```

3. Place the images that correspond to a label into the folder with the same label name.
4. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
5. [Add the folder](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md") you created in step 1 to the Amazon S3 bucket (console bucket)
   created for you by Amazon Rekognition Custom Labels during _First Time Set Up_. For more information, see [Managing an Amazon Rekognition Custom Labels project](managing-project.md "managing-project.md").
6. Open the Amazon Rekognition console at
   [https://console.aws.amazon.com/rekognition/](https://console.aws.amazon.com/rekognition/ "https://console.aws.amazon.com/rekognition/").
7. Choose **Use Custom Labels**.
8. Choose **Get started**.
9. In the left navigation pane, choose **Projects**.
10. In the **Projects** page, choose the project to which you want to add a dataset.
    The details page for your project is displayed.
11. Choose **Create dataset**. The **Create dataset** page is
    shown.
12. In **Starting configuration**, choose either **Start with a single dataset**
    or **Start with a training dataset**. To create a higher quality model, we recommend starting with separate
    training and test datasets.

Single dataset

    1. In the **Training dataset details**
     section, choose **Import images from S3 bucket**.
    2. In the **Training dataset details** section,
     Enter the information for steps 13 - 15 in the **Image source configuration** section.

Separate training and test datasets

    1. In the **Training dataset details**
     section, choose **Import images from S3 bucket**.
    2. In the **Training dataset details** section, enter the information for steps
     13 - 15 in the **Image source
     configuration** section.
    3. In the **Test dataset details**
     section, choose **Import images from S3 bucket**.
    4. In the **Test dataset details** section, enter the information for steps 13 -
     15 in the **Image source
     configuration** section.

13. Choose **Import images from Amazon S3 bucket**.
14. In **S3 URI**, enter the Amazon S3 bucket location and folder path.
15. Choose **Automatically attach labels to images based on the folder**.
16. Choose **Create Datasets**. The datasets page for your project opens.
17. If you need to add or change labels, do [Labeling images](md-labeling-images.md "md-labeling-images.md").
18. Follow the steps in [Training a model (Console)](training-model.md#tm-console "training-model.md#tm-console") to train your model.
