

# Connect Studio JupyterLab notebooks to Amazon S3 Access Grants with trusted identity propagation enabled
<a name="trustedidentitypropagation-s3-access-grants"></a>

You can use [Amazon S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants.html) to flexibly grant identity-based fine-grain access control to Amazon S3 locations. These grant Amazon S3 buckets access directly to your corporate users and groups. The following pages provides information and instructions on how to use Amazon S3 Access Grants with trusted identity propagation for SageMaker AI.

## Prerequisites
<a name="s3-access-grants-prerequisites"></a>

To connect Studio to Lake Formation and Athena with trusted identity propagation enabled, ensure you have completed the following prerequisites:
+  [Setting up trusted identity propagation for Studio](trustedidentitypropagation-setup.md) 
+ Follow the [getting started with Amazon S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-get-started.html) to set up Amazon S3 Access Grants for your bucket. See [scaling data access with Amazon S3 Access Grants](https://aws.amazon.com/blogs/storage/scaling-data-access-with-amazon-s3-access-grants/) for more information.
**Note**  
Standard Amazon S3 APIs do not automatically work with Amazon S3 Access Grants. You must explicitly use Amazon S3 Access Grants APIs. See [Managing access with Amazon S3 Access Grants](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants.html) for more information.

**Topics**
+ [Prerequisites](#s3-access-grants-prerequisites)
+ [Connect Amazon S3 Access Grants with Studio JupyterLab notebooks](s3-access-grants-setup.md)
+ [Connect Studio JupyterLab notebooks to Amazon S3 Access Grants with Training and Processing jobs](trustedidentitypropagation-s3-access-grants-jobs.md)