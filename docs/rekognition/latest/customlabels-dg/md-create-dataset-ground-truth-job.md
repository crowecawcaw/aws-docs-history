

# Labeling images with an Amazon SageMaker AI Ground Truth job
<a name="md-create-dataset-ground-truth-job"></a>

With Amazon SageMaker AI Ground Truth, you can use workers from either Amazon Mechanical Turk, a vendor company that you choose, or an internal, private workforce along with machine learning that allows you to create a labeled set of images. Amazon Rekognition Custom Labels imports SageMaker AI Ground Truth manifest files from an Amazon S3 bucket that you specify.

Amazon Rekognition Custom Labels supports the following SageMaker AI Ground Truth tasks.
+ [Image Classification](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-image-classification.html)
+ [Bounding Box](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-bounding-box.html)

The files you import are the images and a manifest file. The manifest file contains label and bounding box information for the images you import.

Amazon Rekognition needs permissions to access the Amazon S3 bucket where your images are stored. If you are using the console bucket set up for you by Amazon Rekognition Custom Labels, the required permissions are already set up. If you are not using the console bucket, see [Accessing external Amazon S3 Buckets](su-console-policy.md#su-external-buckets).

## Creating a manifest file with a SageMaker AI Ground Truth job (Console)
<a name="md-create-dataset-ground-truth-job-console"></a>

The following procedure shows you how to create a dataset by using images labeled by a SageMaker AI Ground Truth job. The job output files are stored in your Amazon Rekognition Custom Labels console bucket.<a name="create-dataset-procedure-ground-truth"></a>

**To create a dataset using images labeled by a SageMaker AI Ground Truth job (console)**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the console bucket, [create a folder](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-folder.html) to hold your training images. 
**Note**  
The console bucket is created when you first open the Amazon Rekognition Custom Labels console in an AWS Region. For more information, see [Managing an Amazon Rekognition Custom Labels project](managing-project.md).

1. [Upload your images](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) to the folder that you just created.

1. In the console bucket, create a folder to hold the output of the Ground Truth job.

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. Create a Ground Truth labeling job. You'll need the Amazon S3 URLs for the folders you created in step 2 and step 4. For more information, see [Use Amazon SageMaker Ground Truth for Data Labeling](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html). 

1. Note the location of the `output.manifest` file in the folder you created in step 4. It should be in the sub-folder `{{Ground-Truth-Job-Name}}/manifests/output`.

1. Follow the instructions at [Creating a dataset with a SageMaker AI Ground Truth manifest file (Console)](md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-console) to create a dataset with the uploaded manifest file. For step 8, in **.manifest file location**, enter the Amazon S3 URL for the location you noted in the previous step. If you are using the AWS SDK, do [Creating a dataset with a SageMaker AI Ground Truth manifest file (SDK)](md-create-dataset-ground-truth.md#md-create-dataset-ground-truth-sdk).

1. Repeat steps 1 - 6 to create SageMaker AI Ground Truth job for your test dataset.