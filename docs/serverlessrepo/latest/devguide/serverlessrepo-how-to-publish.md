# How to Publish Applications

This section provides you with procedures for publishing your serverless application to
the AWS Serverless Application Repository by using the AWS SAM CLI or the AWS Management Console. It also shows you how to share your
application to allow others to deploy it, and deleting your application from the
AWS Serverless Application Repository.

###### Important

The information that you enter when you publish an application isn't encrypted. This
information includes data such as the author name. If you have personally identifiable
information that you don't want to be stored or made public, we recommend that you
don't enter this information when publishing your application.

## Publishing an Application

(AWS CLI)

The easiest way to publish an application to the AWS Serverless Application Repository is to use a set of AWS SAM CLI
commands. For more information, see [Publishing an Application Using the AWS SAM CLI](../../../serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.md "../../../serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.md") in the _AWS Serverless Application Model
(AWS SAM) Developer Guide_.

## Publishing a New Application

(Console)

This section shows you how to use the AWS Management Console to publish a new application to the
AWS Serverless Application Repository. For instructions on publishing a new version of an existing application, see
[Publishing a New Version of
an Existing Application](serverlessrepo-how-to-publish-new-version.md "serverlessrepo-how-to-publish-new-version.md").

### Prerequisites

Before you publish an application to the AWS Serverless Application Repository, you need the following:

- A valid AWS account.
- A valid AWS Serverless Application Model (AWS SAM) template that defines the AWS resources that are
  used. For more information about AWS SAM templates, see [AWS SAM Template Basics](../../../serverless-application-model/latest/developerguide/serverless-sam-template-basics.md "../../../serverless-application-model/latest/developerguide/serverless-sam-template-basics.md").
- A package for your application that you created by using the AWS CloudFormation
  `package` command for the AWS CLI. This command packages the
  local artifacts (local paths) that your AWS SAM template references. For more
  details, see [package](../../../cli/latest/reference/cloudformation/package.md "../../../cli/latest/reference/cloudformation/package.md") in the CloudFormation documentation.
- A URL that points to your application's source code, in case you want
  to publish your application publicly.
- A readme.txt file. This file should describe how customers can use your
  application, and how to configure it before deploying it in their own AWS
  accounts.
- A license.txt file or a valid license identifier from the [SPDX website](https://spdx.org/licenses/ "https://spdx.org/licenses/"). Note that a
  license is only required if you want to share your application publicly. If
  you're going to keep your application private or only share it privately,
  you don't need to specify a license.
- A valid Amazon S3 bucket policy that grants the service read permissions for
  artifacts that were uploaded to Amazon S3 when you packaged your application. To
  set this policy, follow these steps:
  1.  Open the Amazon S3 console at
      [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
  2.  Choose the Amazon S3 bucket that you used to package your
      application.
  3.  Choose the **Permissions** tab.
  4.  Choose the **Bucket Policy** button.
  5.  Paste the following policy statement into the **Bucket
      policy editor**. Make sure to substitute your bucket
      name in the `Resource` element, and your AWS account ID
      in the `Condition` element. The expression in the
      `Condition` element ensure AWS Serverless Application Repository only has permission
      to access applications from the specified AWS account. For more
      information about policy statements, see [IAM JSON policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
      _IAM User Guide_.

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Effect": "Allow",
   "Principal": {
   "Service": "serverlessrepo.amazonaws.com"
   },
   "Action": "s3:GetObject",
   "Resource": "arn:aws:s3:::`bucketname`/*",
   "Condition" : {
   "StringEquals": {
   "aws:SourceAccount": "`123456789012`"
   }
   }
   }
   ]
  }`

  ```

  6.  Choose the **Save** button.

### Procedure

Create a new application in the AWS Serverless Application Repository by using the following procedure.

###### To create a new application in the AWS Serverless Application Repository

1. Open the [AWS Serverless Application Repository
   console](https://console.aws.amazon.com/serverlessrepo/home "https://console.aws.amazon.com/serverlessrepo/home") and choose **Publish
   applications**.
2. On the **Publish an application** page, enter the
   following application information, and then choose **Publish
   application**:

| Property                          | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| **Application name**              | TRUE     | The name of the application.<br>Minimum length=1. Maximum length=140.<br>Pattern: "[a-zA-Z0-9\\-]+";                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Author**                        | TRUE     | The name of the author publishing the application.<br>Minimum length=1. Maximum length=127.<br>Pattern: "^[a-z0-9](([a-z0-9]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | -(?!-))\*[a-z0-9])?$"; |
| **Home page**                     | FALSE    | A URL with more information about the application—for example, the<br>location of your GitHub repository for the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Description**                   | TRUE     | The description of the application.<br>Minimum length=1. Maximum length=256.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Labels**                        | FALSE    | The labels that improve the discovery of applications in search<br>results.<br>Minimum length=1. Maximum length=127. Maximum number of labels: 10.<br>Pattern: "^[a-zA-Z0-9+\\-\_:\\/@]+$";                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Spdx license (drop-down list)** | FALSE    | Choose a valid license identifier from the drop-down that contains licenses<br>that are available on the [SPDX<br>website](https://spdx.org/licenses/ "https://spdx.org/licenses/"). Choosing an item in the drop-down populates the<br>**License\*<br>• text box below it. Note: Choosing a license in<br>the drop-down replaces the contents of the **License\*<br>• text<br>box, and discards any manual edits that you have made.                                                                                                                                                                                                               |
| **License**                       | FALSE    | Upload a .txt license file, or choose a license from the **Spdx<br>license\*<br>• drop-down described in the previous row. Choosing a<br>license from the **Spdx license*<br>• drop-down automatically<br>populates the \*\*License*<br>• text box. You can manually edit<br>the contents of this text box after uploading a license file or choosing one<br>from the **Spdx license\*<br>• drop-down. However, if another<br>**Spdx license\*<br>• is chosen from the drop-down, any<br>manual edits that you have made are discarded.<br>This is an optional field, but you must provide a license in order to share<br>the application publicly. |
| **Readme**                        | FALSE    | Upload the contents of the Readme file, which can be in text or markdown<br>format. These contents are displayed on the application's detail page in the<br>AWS Serverless Application Repository. You can manually edit the contents of this text box after uploading a<br>file.                                                                                                                                                                                                                                                                                                                                                                   |
| **Semantic version**              | FALSE    | The semantic version of the application. For more information, see the<br>[Semantic Versioning<br>website](https://semver.org/ "https://semver.org/").<br>You must provide a value for this property in order to make your<br>application public.                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Source code Url**               | FALSE    | A link to a public repository for the source code of your<br>application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **SAM template**                  | TRUE     | A valid AWS Serverless Application Model (AWS SAM) template that defines the AWS resources that are<br>used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Sharing an Application

Published applications can have permissions set in one of the three following
categories:

- **Private (default)** – Applications that
  were created with the same account, and haven't been shared with any other AWS
  account. Only consumers that share your AWS account have permission to deploy
  private applications.
- **Privately shared** – Applications that
  the publisher has explicitly shared with a specific set of AWS accounts, or with
  AWS accounts in an AWS Organization. Consumers have permission to deploy
  applications that have been shared with their AWS account or AWS Organization.
  For more information about AWS Organizations, see the
  _[AWS Organizations User Guide](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md")_.
- **Publicly shared** – Applications that
  the publisher has shared with everyone. All consumers have permission to deploy
  any publicly shared application.

After you have published an application to the AWS Serverless Application Repository, by default it is set to
**private**. This section shows you how to share an
application privately with specific AWS accounts or an AWS Organization, or share it
publicly with everyone.

### Sharing an Application Through the

Console

You have two options for sharing your application with others: 1) Share it with
specific AWS accounts or the AWS accounts within your AWS organization, or 2) Share
it publicly with everyone. For more information about AWS Organizations, see the
_[AWS Organizations User Guide](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md")_.

###### Option 1: To share your application with specific AWS account(s) or accounts

within your AWS organization

1. Open the [AWS Serverless Application Repository
   console](https://console.aws.amazon.com/serverlessrepo/home "https://console.aws.amazon.com/serverlessrepo/home").
2. On the navigation pane, choose **Published Applications**
   to bring up the list of applications that you've created.
3. Choose the application that you want to share.
4. Choose the **Sharing** tab.
5. In the **Application policy statements** section, choose
   the **Create Statement** button.
6. In the **Statement Configuration** window fill out the
   fields based on how you want to share your application.

###### Note

If you are sharing with an organization, you can only specify the
organization that your AWS account is a member of. If you try to specify
an AWS Organization that you are not a member of, an error will
result.

To share your application with your AWS Organization, you must
acknowledge that the `UnshareApplication` action will be
added to your policy statement, in case the sharing needs to be revoked
in the future. 7. Choose the **Save** button.

###### Option 2: To share your application publicly with everyone

1. Open the [AWS Serverless Application Repository
   console](https://console.aws.amazon.com/serverlessrepo/home "https://console.aws.amazon.com/serverlessrepo/home").
2. On the navigation pane, choose **Published Applications**
   to bring up the list of applications that you've created.
3. Choose the application that you want to share.
4. Choose the **Sharing** tab.
5. In the **Public Sharing** section, choose the
   **Edit** button.
6. Under **Public sharing** choose the
   **Enabled** radio button.
7. In the text box type the name of your application, then choose the
   **Save** button.

###### Note

In order to share an application publicly, it must have both the
`SemanticVersion` and `LicenseUrl` properties
set.

### Sharing an Application Through the

AWS CLI

To share an application using the AWS CLI you grant permissions using the
`put-application-policy` command to specify the AWS account(s)
you want to share with as principals.

For more information about sharing your application by using the AWS CLI, see
[AWS Serverless Application Repository
Application Policy Examples](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md").

## Unsharing an Application

There are two options for unsharing an application from an AWS Organization:

1. The publisher of the application can remove permissions using the `put-application-policy` command.
2. A user from the _management account_ of an AWS Organization can
   perform an [unshare application](applications-applicationid-unshare.md "applications-applicationid-unshare.md") operation on any application shared with the
   organization, even if the application was published by a user from a different
   account.

###### Note

When an application is unshared from an AWS Organization with the "unshare
application" operation, it cannot be shared with AWS Organization
again.

For more information about AWS Organizations, see the
_[AWS Organizations User Guide](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md")_.

### Publisher Removing

Permissions

#### Publisher Removing

Permissions Through the Console

To unshare an application through the AWS Management Console, you remove the policy
statement that shares it with other AWS accounts. To do this, follow these
steps:

1. Open the [AWS Serverless Application Repository console](https://console.aws.amazon.com/serverlessrepo/home "https://console.aws.amazon.com/serverlessrepo/home").
2. Choose **Available Applications** in the left
   navigation pane.
3. Choose the application that you want to unshare.
4. Choose the **Sharing** tab.
5. In the **Application policy statements** section,
   select the policy statement that is sharing the application with the
   accounts that you want to unshare from.
6. Choose **Delete**.
7. A confirmation message will appear. Choose **Delete**
   again.

#### Publisher Removing

Permissions Through the AWS CLI

To unshare an application through the AWS CLI, the publisher can remove or
otherwise change permissions using the `put-application-policy` command to make the application
private, or share with a different set of AWS accounts.

For more information about changing permissions using the AWS CLI, see [AWS Serverless Application Repository
Application Policy Examples](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md").

### Management account unsharing an

application

#### Management account unsharing an

application from an AWS Organization through the console

To unshare an application from an AWS Organization through the AWS Management Console, a
user from the _management account_ can do the following:

1. Open the [AWS Serverless Application Repository console](https://console.aws.amazon.com/serverlessrepo/home "https://console.aws.amazon.com/serverlessrepo/home").
2. Choose **Available Applications** in the left
   navigation pane.
3. In the application's tile, choose **Unshare**.
4. In the unshare message box, confirm you want to unshare the
   application by entering the Organization ID and application name, then
   choosing **Save**.

#### Management account unsharing an

application from an AWS Organization Through the AWS CLI

To unshare an application from an AWS Organization, a user from the
_management account_ can run the
`aws
 serverlessrepo unshare-application` command.

The following command unshares an application from an AWS Organization, where
`application-id` is the Amazon Resource Name (ARN)
of the application, and `organization-id` is the AWS
Organization ID:

```
aws serverlessrepo unshare-application --application-id `application-id` --organization-id `organization-id`
```

## Deleting an Application

You can delete applications from the AWS Serverless Application Repository by using either the AWS Management Console or the AWS SAM
CLI.

### Deleting an Application

(Console)

To delete a published application through the AWS Management Console, do the following.

1. Open the [AWS Serverless Application Repository
   console](https://console.aws.amazon.com/serverlessrepo/home "https://console.aws.amazon.com/serverlessrepo/home").
2. For **My Applications**, choose the application that you
   want to delete.
3. In the application's detail page, choose **Delete
   application**.
4. Choose **Delete application** to complete the
   deletion.

### Deleting an Application

(AWS CLI)

To delete a published application using the AWS CLI, run the `aws serverlessrepo
 delete-application` command.

The following command deletes an application, where
`application-id` is the Amazon
Resource Name (ARN) of the application:

```
aws serverlessrepo delete-application --application-id `application-id`
```
