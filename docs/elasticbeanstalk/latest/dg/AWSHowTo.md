# Using Elastic Beanstalk with Amazon S3

This topic explains how Elastic Beanstalk utilizes Amazon Simple Storage Service (Amazon S3) and the types of objects that it stores in S3 buckets. It also notes which objects you must
delete manually after you terminate your Elastic Beanstalk environment and provides instructions to do so.

## The Elastic Beanstalk Amazon S3 customer account bucket

Elastic Beanstalk creates an encrypted Amazon S3 bucket named `elasticbeanstalk-`region`-`account-id`` for
each region in which you create environments. Your AWS account owns this bucket. Elastic Beanstalk stores temporary configuration files and other objects for the proper operation of your
application in this bucket. Elastic Beanstalk requires enabled ACLs for service-managed buckets and therefore enables this bucket's Access Control List (ACL).

Be aware that Amazon S3 disables bucket Access Control Lists (ACLs) by default. Furthermore, the [ACL overview](../../../AmazonS3/latest/userguide/acl-overview.md "../../../AmazonS3/latest/userguide/acl-overview.md") topic in the _Amazon S3 User Guide_ recommends that you
keep ACLs disabled, except for specific use cases. The Elastic Beanstalk service-managed buckets fall into a use case that requires enabled ACLs. To maintain
security Elastic Beanstalk deployments enforce that this bucket is owned by the account running the application.

Elastic Beanstalk retains the default encryption provided by Amazon S3 buckets. For more information about bucket encryption, see [Amazon S3 default encryption](../../../AmazonS3/latest/userguide/bucket-encryption.md "../../../AmazonS3/latest/userguide/bucket-encryption.md") in the _Amazon Simple Storage Service User Guide_.

## Contents of the Elastic Beanstalk Amazon S3 customer account bucket

The following table lists some objects that Elastic Beanstalk stores in your customer account bucket. The table also shows which objects have to be deleted
manually. To avoid unnecessary storage costs, and to ensure that personal information isn't retained, be sure to manually delete these objects when you no
longer need them.

| **Object**                                                                                                  | **When stored?**                                                                                                                                                                                                                                          | **When deleted?**                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Application versions](applications-versions.md "applications-versions.md")                                 | When you create an environment or deploy your application code to an existing environment, Elastic Beanstalk stores an application version in Amazon S3 and<br>associates it with the environment.                                                        | During application deletion, and according to [Version lifecycle](applications-lifecycle.md "applications-lifecycle.md").                                                                                                                                           |
| [Source bundles](applications-versions.md "applications-versions.md")                                       | When you upload a new application version using the Elastic Beanstalk console or the EB CLI, Elastic Beanstalk stores a copy of it in Amazon S3, and sets it as your<br>environment's source bundle.                                                      | _Manually.<br>• When you delete an application version, you can choose \*\*Delete versions from Amazon S3_<br>• to<br>also delete the related source bundle. For details, see [Managing application versions](applications-versions.md "applications-versions.md"). |
| **Custom platforms**                                                                                        | When you create a custom platform, Elastic Beanstalk temporarily stores related data in Amazon S3.                                                                                                                                                        | Upon successful completion of the custom platform's creation.                                                                                                                                                                                                       |
| [Log files](using-features.md "using-features.md")                                                          | You can request Elastic Beanstalk to retrieve instance log files (tail or bundle logs) and store them in Amazon S3. You can also enable log rotation and<br>configure your environment to publish logs automatically to Amazon S3 after they are rotated. | Tail and bundle logs: 15 minutes after they are created.<br>Rotated logs: _Manually._                                                                                                                                                                               |
| [Saved configurations](environment-configuration-savedconfig.md "environment-configuration-savedconfig.md") | _Manually._                                                                                                                                                                                                                                               | _Manually._                                                                                                                                                                                                                                                         |

## Deleting objects in the Elastic Beanstalk Amazon S3 bucket

When you terminate an environment or delete an application, Elastic Beanstalk deletes most related objects from Amazon S3. To minimize storage costs of a running
application, routinely delete objects that your application doesn't need. In addition, pay attention to objects that you have to delete manually, as
listed in [Contents of the Elastic Beanstalk Amazon S3 customer account bucket](#AWSHowTo.S3.content "#AWSHowTo.S3.content"). To ensure that private information isn't unnecessarily retained,
delete these objects when you don't need them anymore.

- Delete application versions that you don't expect to use in your application anymore. When you delete an application version, you can select
  **Delete versions from Amazon S3** to also delete the related source bundle—a copy of your application's source code and
  configurations files, which Elastic Beanstalk uploaded to Amazon S3 when you deployed an application or uploaded an application version. To learn how to delete an
  application version, see [Managing application versions](applications-versions.md "applications-versions.md").
- Delete rotated logs that you don't need. Alternatively, download them or move them to Amazon Glacier for further analysis.
- Delete saved configurations that you aren't going to use in any environment anymore.

## Deleting the Elastic Beanstalk Amazon S3 bucket

When Elastic Beanstalk creates a bucket it also creates a bucket policy that it applies to the new bucket. This policy servers two purposes:

- To allow environments to write to the bucket.
- To prevent accidental deletion of the bucket.

Due to the policy that Elastic Beanstalk applies to the buckets that it creates for your environments, you're not be allowed to delete these buckets, unless you
deliberately delete the bucket policy first. You can delete the bucket policy from the **Permissions** section of the bucket properties
in the Amazon S3 console.

###### Warning

**We recommend that you delete specific unnecessary objects from your Elastic Beanstalk Amazon S3 bucket, instead of deleting the entire
bucket.**

If you delete a bucket that Elastic Beanstalk created in your account, and you still have existing applications and running environments in the corresponding
region, your applications might stop working correctly. For example:

- When an environment scales out, Elastic Beanstalk should be able to find the environment's application version in the Amazon S3 bucket and use it to start new
  Amazon EC2 instances.
- When you create a custom platform, Elastic Beanstalk uses temporary Amazon S3 storage during the creation process.
  For more information about the implications of deleting an S3 bucket, see the considerations listed in [Deleting a bucket](../../../AmazonS3/latest/userguide/delete-bucket.md "../../../AmazonS3/latest/userguide/delete-bucket.md") in the _Amazon S3 User Guide_.

###### To delete an Elastic Beanstalk storage bucket (console)

The general procedure to delete an S3 bucket is also described in [Deleting a bucket](../../../AmazonS3/latest/userguide/delete-bucket.md "../../../AmazonS3/latest/userguide/delete-bucket.md") in the _Amazon S3 User Guide_. Since we're deleting a bucket created by Elastic Beanstalk in the following
procedure, we include additional steps to delete the bucket policy first.

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3 "https://console.aws.amazon.com/s3").
2. Open the Elastic Beanstalk storage bucket's page by choosing the bucket name.
3. Choose the **Permissions** tab.
4. Choose **Bucket Policy**.
5. Choose **Delete**.
6. Go back to the Amazon S3 console's main page, and then select the Elastic Beanstalk storage bucket.
7. Choose **Delete Bucket**.
8. Confirm that you want to delete the bucket by entering the bucket name into the text field, and then choose **Delete
   bucket**.
