# Setting up AWS HealthImaging

You must set up your AWS environment before using AWS HealthImaging. The following topics are
prerequisites for the [tutorial](getting-started-tutorial.md "getting-started-tutorial.md") located in
the next section.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create S3 buckets](#setting-up-create-s3-buckets "#setting-up-create-s3-buckets")
- [Create a data store](#setting-up-create-data-store "#setting-up-create-data-store")
- [Create an IAM user with HealthImaging full access permission](#setting-up-create-iam-user "#setting-up-create-iam-user")
- [Create an IAM role for import](#setting-up-create-iam-role-import "#setting-up-create-iam-role-import")
- [Install the AWS CLI (optional)](#setting-up-install-cli "#setting-up-install-cli")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Create S3 buckets

To import DICOM P10 data into AWS HealthImaging, two Amazon S3 buckets are recommended. The Amazon S3
input bucket stores the DICOM P10 data to be imported and HealthImaging reads from this bucket.
The Amazon S3 output bucket stores the processing results of the import job and HealthImaging writes
to this bucket. For a visual representation of this, see the diagram at [Understanding import jobs](understanding-import-jobs.md "understanding-import-jobs.md").

###### Note

Due to AWS Identity and Access Management (IAM) policy, your Amazon S3 bucket names must be unique. For more
information, see [Bucket naming
rules](../../../AmazonS3/latest/userguide/bucketnamingrules.md "../../../AmazonS3/latest/userguide/bucketnamingrules.md") in the _Amazon Simple Storage Service User Guide_.

For the purpose of this guide, we specify the following Amazon S3 input and output buckets
in the [IAM role for
import](#setting-up-create-iam-role-import "#setting-up-create-iam-role-import").

- Input bucket:
  `arn:aws:s3:::`amzn-s3-demo-source-bucket``
- Output bucket:
  `arn:aws:s3:::`amzn-s3-demo-logging-bucket``

For additional information, see [Creating a
bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.

## Create a data store

When you import your medical imaging data, the AWS HealthImaging [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store") holds the results of your transformed
DICOM P10 files, which are called [image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set").
For a visual representation of this, see the diagram at [Understanding import jobs](understanding-import-jobs.md "understanding-import-jobs.md").

###### Tip

A `datastoreID` is generated when you create a data store. You must use
the `datastoreID` when completing the [trust relationship](#anchor-trust-relationship "#anchor-trust-relationship") for import
later in this section.

To create a data store, see [Creating a data store](create-data-store.md "create-data-store.md").

## Create an IAM user with HealthImaging full access permission

###### Best practice

We suggest you create separate IAM users for different needs such as importing,
data access, and data management. This aligns with [Grant least privilege access](../../../wellarchitected/latest/framework/sec_permissions_least_privileges.md "../../../wellarchitected/latest/framework/sec_permissions_least_privileges.md") in the _AWS Well-Architected
Framework_.

For the purposes of the [Tutorial](getting-started-tutorial.md "getting-started-tutorial.md")
in the next section, you will be using a single IAM user.

###### To create an IAM user

1. Follow the instructions for [Creating an IAM user in
   your AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") in the _IAM User Guide_.
   Consider naming the user `ahiadmin` (or similar) for clarification
   purposes.
2. Assign the `AWSHealthImagingFullAccess` managed policy to the IAM
   user. For more information, see [AWS managed policy: AWSHealthImagingFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSHealthImagingFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSHealthImagingFullAccess").

###### Note

IAM permissions can be narrowed. For more information, see [AWS managed policies for AWS HealthImaging](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Create an IAM role for import

###### Note

The following instructions refer to an AWS Identity and Access Management (IAM) role that grants read and
write access to Amazon S3 buckets for importing your DICOM data. Although the role is
required for the [tutorial](getting-started-tutorial.md "getting-started-tutorial.md") in the
next section, we recommend you add IAM permissions to users, groups, and roles
using [AWS managed policies for AWS HealthImaging](security-iam-awsmanpol.md "security-iam-awsmanpol.md"), because they are easier to use than writing policies yourself.

An IAM role is an IAM identity that you can create in your account that has
specific permissions. To start an import job, the IAM role that calls the
`StartDICOMImportJob` action must be attached to a user policy that
grants access to the Amazon S3 buckets used for reading your DICOM P10 data and storing the
import job processing results. It must also be assigned a trust relationship (policy)
that enables AWS HealthImaging to assume the role.

###### To create an IAM role for import purposes

1. Using the [IAM Console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam"), create a role
   named `ImportJobDataAccessRole`. You use this role for the [tutorial](getting-started-tutorial.md "getting-started-tutorial.md") in the next section. For
   more information, see [Creating IAM roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md")
   in the _IAM User Guide_.

###### Tip

For the purposes of this guide, the code examples in [Starting an import job](start-dicom-import-job.md "start-dicom-import-job.md") reference the `ImportJobDataAccessRole` IAM role. 2. Attach an IAM permission policy to the IAM role. This permission policy
grants access to the Amazon S3 input and output buckets. Attach the following
permission policy to the IAM role `ImportJobDataAccessRole`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-logging-bucket`"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`/*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-logging-bucket`/*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

3. Attach
   the following trust relationship (policy) to the
   `ImportJobDataAccessRole` IAM role. The trust policy requires
   the `datastoreId` that was generated when you completed the section
   [Create a data store](#setting-up-create-data-store "#setting-up-create-data-store"). The [tutorial](getting-started-tutorial.md "getting-started-tutorial.md") following this topic
   assumes you are using one AWS HealthImaging data store, but with data store-specific
   Amazon S3 buckets, IAM roles, and trust policies.

###### Note

The `Condition` block in this trust policy helps prevent the
confused deputy problem by ensuring that only your specific AWS HealthImaging data
store can be accessed. For more information about this security measure, see
[Cross-service confused deputy prevention in HealthImaging](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "medical-imaging.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

To learn more about creating and using IAM policies with AWS HealthImaging, see [Identity and Access Management for AWS HealthImaging](security-iam.md "security-iam.md").

To learn more about IAM roles in general, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the
_IAM User Guide_. To learn more about IAM policies and
permissions in general, see [IAM Policies and
Permissions](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.

## Install the AWS CLI (optional)

The following procedure is required if you are using the AWS Command Line Interface. If you're using
the AWS Management Console or AWS SDKs, you can skip the following procedure.

###### To set up the AWS CLI

1. Download and configure the AWS CLI. For instructions, see the following topics
   in the _AWS Command Line Interface User Guide_.

   - [Installing
     or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
   - [Getting
     started with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md")

2. In the AWS CLI `config` file, add a named profile for the
   administrator. You use this profile when running the AWS CLI commands. Under the
   security principle of least privilege, we recommend you create a separate IAM
   role with privileges specific to the tasks being performed. For more information
   about named profiles, see [Configuration and
   credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") in the
   _AWS Command Line Interface User Guide_.

```
[default]
aws_access_key_id = `default access key ID`
aws_secret_access_key = `default secret access key`
region = `region`

```

3. Verify the setup using the following `help` command.

```
aws medical-imaging help
```

If the AWS CLI is configured correctly, you see a brief description of AWS HealthImaging
and a list of available commands.
