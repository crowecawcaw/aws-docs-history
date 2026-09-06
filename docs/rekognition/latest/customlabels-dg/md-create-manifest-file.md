

# Creating a manifest file
<a name="md-create-manifest-file"></a>

You can create a test or training dataset by importing a SageMaker AI Ground Truth format manifest file. If your images are labeled in a format that isn't a SageMaker AI Ground Truth manifest file, use the following information to create a SageMaker AI Ground Truth format manifest file. 

Manifest files are in [JSON lines](http://jsonlines.org) format where each line is a complete JSON object representing the labeling information for an image. Amazon Rekognition Custom Labels supports SageMaker AI Ground Truth manifests with JSON lines in the following formats:
+ [Classification Job Output](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-output.html#sms-output-class) – Use to add image-level labels to an image. An image-level label defines the class of scene, concept, or object (if object location information isn't needed) that's on an image. An image can have more that one image-level label. For more information, see [Importing image-level labels in manifest files](md-create-manifest-file-classification.md).
+ [Bounding Box Job Output](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data-output.html#sms-output-box) – Use to label the class and location of one or more objects on an image. For more information, see [Object localization in manifest files](md-create-manifest-file-object-detection.md).

Image-level and localization (bounding-box) JSON lines can be chained together in the same manifest file. 

**Note**  
The JSON line examples in this section are formatted for readability. 

When you import a manifest file, Amazon Rekognition Custom Labels applies validation rules for limits, syntax, and semantics. For more information, see [Validation rules for manifest files](md-create-manifest-file-validation-rules.md). 

The images referenced by a manifest file must be located in the same Amazon S3 bucket. The manifest file can be located in a different Amazon S3 bucket than the Amazon S3 bucket that stores the images. You specify the location of an image in the `source-ref` field of a JSON line. 

Amazon Rekognition needs permissions to access the Amazon S3 bucket where your images are stored. If you are using the console bucket set up for you by Amazon Rekognition Custom Labels, the required permissions are already set up. If you are not using the console bucket, see [Accessing external Amazon S3 Buckets](su-console-policy.md#su-external-buckets).

**Topics**
+ [Creating a manifest file](#md-create-manifest-file-console)

## Creating a manifest file
<a name="md-create-manifest-file-console"></a>

The following procedure creates a project with a training and test dataset. The datasets are created from training and test manifest files that you create.

<a name="create-dataset-procedure-manifest-file"></a>

**To create a dataset using a SageMaker AI Ground Truth format manifest file (console)**

1. In the console bucket, [create a folder](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-folder.html) to hold your manifest files. 

1. In the console bucket, create a folder to hold your images.

1. Upload your images to the folder you just created.

1. Create a SageMaker AI Ground Truth format manifest file for your training dataset. For more information, see [Importing image-level labels in manifest files](md-create-manifest-file-classification.md) and [Object localization in manifest files](md-create-manifest-file-object-detection.md).
**Important**  
The `source-ref` field value in each JSON line must map to an image that you uploaded.

1. Create an SageMaker AI Ground Truth format manifest file for your test dataset. 

1. [Upload your manifest files](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) to the folder that you just created.

1. Note the location of the manifest file.

1. Follow the instructions at [Creating a dataset with a SageMaker AI Ground Truth manifest file (Console)](md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-console) to create a dataset with the uploaded manifest file. For step 8, in **.manifest file location**, enter the Amazon S3 URL for the location you noted in the previous step. If you are using the AWS SDK, do [Creating a dataset with a SageMaker AI Ground Truth manifest file (SDK)](md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-sdk).