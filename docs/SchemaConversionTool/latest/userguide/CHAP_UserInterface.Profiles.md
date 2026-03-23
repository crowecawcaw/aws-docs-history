# Managing Profiles in the AWS Schema Conversion Tool

You can store your AWS credentials in AWS SCT.
AWS SCT uses your credentials
when you use features that integrate with AWS services.
For example, AWS SCT integrates with Amazon S3,
AWS Lambda, Amazon Relational Database Service (Amazon RDS), and AWS Database Migration Service (AWS DMS).

AWS SCT asks you for your AWS credentials
when you access a feature that requires them.
You can store your credentials
in the global application settings.
When AWS SCT asks for your credentials,
you can select the stored credentials.

You can store different sets of AWS credentials in the global application settings. For
example, you can store one set of credentials that you use in test scenarios, and a
different set of credentials that you use in production scenarios. You can also store
different credentials for different AWS Regions.

## Storing AWS credentials

Use the following procedure to store AWS credentials globally.

###### To store AWS credentials

1. Start the AWS Schema Conversion Tool.
2. Open the **Settings** menu, and then choose **Global
   settings**. The **Global settings** dialog box
   appears.
3. Choose **AWS service profiles**, and then
   choose **Add a new AWS service profile**.
4. Enter your AWS information as follows.

| AWS SCT option              | Action                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Profile name**            | Enter a name for your profile.                                                                                                                                                                                                                                                                                                             |
| **AWS access key**          | Enter your AWS access key.                                                                                                                                                                                                                                                                                                                 |
| **AWS secret key**          | Enter your AWS secret access key. For more information<br>about AWS access keys, see [Managing access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_.                                                                            |
| **Region**                  | Choose the AWS Region for your profile.                                                                                                                                                                                                                                                                                                    |
| **Amazon S3 bucket folder** | Choose the Amazon S3 bucket for your profile. You need to specify<br>a bucket only if you are using a feature that connects to Amazon S3. For more information<br>about the required privileges, see [Permissions for using the AWS service profile](#CHAP_UserInterface.Profiles.Permissions "#CHAP_UserInterface.Profiles.Permissions"). |

Choose **Use FIPS endpoint for S3** if you need to comply with the security
requirements for the Federal Information Processing Standard (FIPS). FIPS endpoints are available
in the following AWS Regions:

    * US East (N. Virginia) Region
    * US East (Ohio) Region
    * US West (N. California) Region
    * US West (Oregon) Region

5. Choose **Test connection**
   to verify that your credentials are correct and active.

The **Test connection** dialog box appears.
You can see the status for each of the services connected to your profile.
**Pass** indicates that the profile can successfully access the service.

![The Test connection dialog box](images/AWSServiceProfileSettings-Test.png) 6. After you have configured your profile, choose **Save** to
save your profile or **Cancel** to cancel your changes. 7. Choose **OK**
to close the **Global settings** dialog box.

## Setting the default profile for a project

You can set the default profile for an AWS SCT project.
Doing this associates the AWS credentials stored in the profile with the project.
With your project open, use the following procedure to set the default profile.

###### To set the default profile for a project

1. Start the AWS Schema Conversion Tool and create a new project.
2. On the **Settings** menu,
   choose **Project settings**.
   The **Project settings** dialog box appears.
3. Choose the **Project environment** tab.
4. Choose **Add a new AWS service profile** to add a new profile.
   Then for **AWS service profile**,
   choose the profile that you want to associate with the project.
5. Choose **OK**
   to close the **Project settings** dialog box.
   You can also choose **Cancel** to cancel your changes.

## Permissions for using the AWS service profile

The following permissions are required for accessing your Amazon S3 bucket from
your AWS service profile:

- `s3:PutObject` – to add objects in your Amazon S3 bucket.
- `s3:DeleteObject` – to remove the null version of an object and insert a delete
  marker, which becomes the current version of the object.
- `s3:ListBucket` – to return up to 1,000 objects from your
  Amazon S3 bucket.
- `s3:GetObject` – to retrieve objects from your Amazon S3 bucket.

The following code example shows you how to grant these permissions to your user.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:DeleteObject",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:PutObject"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
