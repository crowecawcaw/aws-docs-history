# Step 3: Upload your WordPress

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
  bucket](#tutorials-wordpress-upload-application-create-s3-bucket "#tutorials-wordpress-upload-application-create-s3-bucket")
- [Prepare the
  application's files for the bucket](#tutorials-wordpress-upload-application-prepare-application-files "#tutorials-wordpress-upload-application-prepare-application-files")
- [Bundle the
  application's files into a single archive file and push the archive file](#tutorials-wordpress-upload-application-bundle-and-push-archive "#tutorials-wordpress-upload-application-bundle-and-push-archive")

## Provision an Amazon S3

bucket

Create a storage container or _bucket_ in Amazon S3—or use an existing
bucket. Make sure you can upload the revision to the bucket and that Amazon EC2 instances used in
deployments can download the revision from the bucket.

You can use the AWS CLI, the Amazon S3 console, or the Amazon S3 APIs to create an Amazon S3 bucket. After
you create the bucket, make sure to give access permissions to the bucket and your AWS
account.

###### Note

Bucket names must be unique across Amazon S3 for all AWS accounts. If you aren't able to
use `amzn-s3-demo-bucket`, try a different bucket name,
such as `amzn-s3-demo-bucket` followed by a dash and your
initials or some other unique identifier. Then be sure to substitute your bucket name for
`amzn-s3-demo-bucket` wherever you see it throughout this
tutorial.

The Amazon S3 bucket must be created in the same AWS region where your target Amazon EC2
instances are launched. For example, if you create the bucket in the US East (N. Virginia) Region, then
your target Amazon EC2 instances must be launched in the US East (N. Virginia) Region.

###### Topics

- [To create an
  Amazon S3 bucket (CLI)](#tutorials-wordpress-upload-application-create-s3-bucket-cli "#tutorials-wordpress-upload-application-create-s3-bucket-cli")
- [To create
  an Amazon S3 bucket (console)](#tutorials-wordpress-upload-application-create-s3-bucket-console "#tutorials-wordpress-upload-application-create-s3-bucket-console")
- [Give permissions to the Amazon S3 bucket and AWS account](#tutorials-wordpress-upload-application-create-s3-bucket-grant-permissions "#tutorials-wordpress-upload-application-create-s3-bucket-grant-permissions")

### To create an

Amazon S3 bucket (CLI)

Call the **mb** command to create an Amazon S3 bucket named
`amzn-s3-demo-bucket`:

```
aws s3 mb s3://amzn-s3-demo-bucket --region `region`
```

### To create

an Amazon S3 bucket (console)

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the Amazon S3 console, choose **Create bucket**.
3. In the **Bucket name** box, type a name for the bucket.
4. In the **Region** list, choose the target region, and then choose
   **Create**.

### Give permissions to the Amazon S3 bucket and AWS account

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

For information about how to create and attach an IAM policy, see [Working with
policies](../../../IAM/latest/UserGuide/ManagingPolicies.md#AddingPermissions_Console "../../../IAM/latest/UserGuide/ManagingPolicies.md#AddingPermissions_Console").

## Prepare the

application's files for the bucket

Make sure the WordPress application files, the AppSpec file, and the scripts are
organized on your development machine similar to the following:

```
/tmp/
  |--WordPress/
      |-- appspec.yml
      |-- scripts/
      |    |-- change_permissions.sh
      |    |-- create_test_db.sh
      |    |-- install_dependencies.sh
      |    |-- start_server.sh
      |    |-- stop_server.sh
      |-- `wp-admin/`
      |    |-- `(various files...)`
      |-- `wp-content/`
      |    |-- `(various files...)`
      |-- `wp-includes/`
      |    |-- `(various files...)`
      |-- `index.php`
      |-- `license.txt`
      |-- `readme.html`
      |-- `(various files ending with .php...)`
```

## Bundle the

application's files into a single archive file and push the archive file

Bundle the WordPress application files and the AppSpec file into an archive file (known
as an application _revision_).

###### Note

You may be charged for storing objects in a bucket and for transferring application
revisions into and out of a bucket. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

1. On the development machine, switch to the folder where the files are stored:

```
cd /tmp/WordPress
```

###### Note

If you don't switch to this folder, then the file bundling will start at your
current folder. For example, if your current folder is `/tmp` instead
of `/tmp/WordPress`, then the bundling will start with files and
subfolders in the `tmp` folder, which may include more than the
`WordPress` subfolder. 2. Call the **create-application** command to register a new application
named `WordPress_App`:

```
aws deploy create-application --application-name WordPress_App
```

3. Call the CodeDeploy [push](../../../cli/latest/reference/deploy/push.md "../../../cli/latest/reference/deploy/push.md") command to bundle the files together, upload the
   revisions to Amazon S3, and register information with CodeDeploy about the uploaded revision, all in
   one action.

```
aws deploy push \
  --application-name WordPress_App \
  --s3-location s3://amzn-s3-demo-bucket/WordPressApp.zip \
  --ignore-hidden-files
```

This command bundles the files from the current directory (excluding any hidden files)
into a single archive file named
`WordPressApp.zip`, uploads the revision to the
`amzn-s3-demo-bucket` bucket, and registers information
with CodeDeploy about the uploaded revision.
