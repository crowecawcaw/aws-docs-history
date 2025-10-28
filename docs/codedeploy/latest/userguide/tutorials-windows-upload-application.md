# Step 3: Upload your "hello, world!"

application to Amazon S3

Now you will prepare and upload your source content to a location from which CodeDeploy can
deploy it. The following instructions show you how to provision an Amazon S3 bucket, prepare the
application revision's files for the bucket, bundle the revision's files, and then push the
revision to the bucket.

###### Note

Although it's not covered in this tutorial, you can use CodeDeploy to deploy applications from
GitHub repositories to instances. For more information, see [Integrating CodeDeploy with GitHub](integrations-partners-github.md "integrations-partners-github.md").

###### Topics

- [Provision an Amazon S3
  bucket](#tutorials-windows-upload-application-create-s3-bucket "#tutorials-windows-upload-application-create-s3-bucket")
- [Prepare the
  application's files for the bucket](#tutorials-windows-upload-application-prepare-application-files "#tutorials-windows-upload-application-prepare-application-files")
- [Bundle the
  application's files into a single archive file and push the archive file](#tutorials-windows-upload-application-bundle-and-push-archive "#tutorials-windows-upload-application-bundle-and-push-archive")

## Provision an Amazon S3

bucket

Create a storage container or _bucket_ in Amazon S3—or use an existing
bucket. Make sure you can upload the revision to the bucket and that Amazon EC2 instances used in
deployments can download the revision from the bucket.

You can use the AWS CLI, the Amazon S3 console, or the Amazon S3 APIs to create an Amazon S3 bucket. After
you create the bucket, make sure to give access permissions to the bucket and your CodeDeploy
user.

###### Note

Bucket names must be unique across Amazon S3 for all AWS accounts. If you aren't able to
use `amzn-s3-demo-bucket`, try a different bucket name,
such as `amzn-s3-demo-bucket` followed by a dash and your
initials or some other unique identifier. Then be sure to substitute your bucket name for
`amzn-s3-demo-bucket` wherever you see it throughout this
tutorial.

The Amazon S3 bucket must be created in the same AWS region in which your target Amazon EC2
instances are launched. For example, if you create the bucket in the US East (N. Virginia) Region, then
your target Amazon EC2 instances must be launched in the US East (N. Virginia) Region.

###### Topics

- [To create an
  Amazon S3 bucket (CLI)](#tutorials-windows-upload-application-create-s3-bucket-cli "#tutorials-windows-upload-application-create-s3-bucket-cli")
- [To create an
  Amazon S3 bucket (console)](#tutorials-windows-upload-application-create-s3-bucket-console "#tutorials-windows-upload-application-create-s3-bucket-console")
- [Give permissions to the Amazon S3 bucket and your AWS account](#tutorials-windows-upload-application-create-s3-bucket-grant-permission "#tutorials-windows-upload-application-create-s3-bucket-grant-permission")

### To create an

Amazon S3 bucket (CLI)

Call the **mb** command to create an Amazon S3 bucket named
`amzn-s3-demo-bucket`:

```
aws s3 mb s3://amzn-s3-demo-bucket --region `region`
```

### To create an

Amazon S3 bucket (console)

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the Amazon S3 console, choose **Create bucket**.
3. In the **Bucket name** box, type a name for the bucket.
4. In the **Region** list, choose the target region, and then choose
   **Create**.

### Give permissions to the Amazon S3 bucket and your AWS account

You must have permissions to upload to the Amazon S3 bucket. You can specify these permissions
through an Amazon S3 bucket policy. For example, in the following Amazon S3 bucket policy, using the
wildcard character (\*) allows AWS account `111122223333` to upload
files to any directory in the Amazon S3 bucket named
`amzn-s3-demo-bucket`:

```
{
    "Statement": [
        {
            "Action": [
                "s3:PutObject"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
            "Principal": {
                "AWS": [
                    "111122223333"
                ]
            }
        }
    ]
}
```

To view your AWS account ID, see [Finding Your AWS account
ID](../../../IAM/latest/UserGuide/console_account-alias.md#FindingYourAWSId "../../../IAM/latest/UserGuide/console_account-alias.md#FindingYourAWSId").

Now is a good time to verify the Amazon S3 bucket will allow download requests from each
participating Amazon EC2 instance. You can specify this through an Amazon S3 bucket policy. For
example, in the following Amazon S3 bucket policy, using the wildcard character (\*) allows any
Amazon EC2 instance with an attached IAM instance profile containing the ARN
`arn:aws:iam::444455556666:role/CodeDeployDemo` to download files from any directory in the Amazon S3 bucket
named `amzn-s3-demo-bucket`:

```
{
    "Statement": [
        {
            "Action": [
                "s3:Get*",
                "s3:List*"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::444455556666:role/CodeDeployDemo"
                ]
            }
        }
    ]
}
```

For information about how to generate and attach an Amazon S3 bucket policy, see [Bucket policy examples](../../../AmazonS3/latest/userguide/example-bucket-policies.md "../../../AmazonS3/latest/userguide/example-bucket-policies.md").

The CodeDeploy adminstrative user that you created in [Step 1: Setting up](getting-started-setting-up.md "getting-started-setting-up.md") must
also have permission to upload the revision to the Amazon S3 bucket. One way to specify this is
through an IAM policy, which you add to the user's permission set, or to an IAM role
(which you allow the user to assume). The following IAM policy allows the user to upload
revisions anywhere in the Amazon S3 bucket named
`amzn-s3-demo-bucket`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":["s3:PutObject"],
 "Resource":"arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 }
 ]
}`

```

For information about how to create an IAM policy, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in
the _IAM User Guide_. For information on adding a policy to a
permission set, see [Create a permission
set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

## Prepare the

application's files for the bucket

Make sure the web page, the AppSpec file, and the script are organized on your
development machine like this:

````
c:\
|-- temp\
|--HelloWorldApp\
|-- appspec.yml
|-- before-install.bat
|-- index.html ``` ## Bundle the application's files into a single archive file and push the archive file Bundle the files into an archive file (known as an application *revision*). ###### Note You may be charged for storing objects in a bucket and for transferring application revisions into and out of a bucket. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/"). 1. On the development machine, switch to the folder where the files are stored: ``` cd c:\temp\HelloWorldApp ``` ###### Note If you don't switch to this folder, then the file bundling will start at your current folder. For example, if your current folder is `c:\temp` instead of `c:\temp\HelloWorldApp`, the bundling will start with files and subfolders in the `c:\temp` folder, which may include more than the `HelloWorldApp` subfolder. 2. Call the **create-application** command to register a new application named `HelloWorld_App` with CodeDeploy: ``` aws deploy create-application --application-name HelloWorld_App ``` 3. Call the CodeDeploy [push](../../../cli/latest/reference/deploy/push.md "../../../cli/latest/reference/deploy/push.md") command to bundle the files together, upload the revisions to Amazon S3, and register information with CodeDeploy about the uploaded revision, all in one action. ``` aws deploy push --application-name HelloWorld_App --s3-location s3://amzn-s3-demo-bucket/HelloWorld_App.zip --ignore-hidden-files ``` This command bundles the files from the current directory (excluding any hidden files) into a single archive file named `HelloWorld_App.zip`, uploads the revision to the `amzn-s3-demo-bucket` bucket, and registers information with CodeDeploy about the uploaded revision.
````
