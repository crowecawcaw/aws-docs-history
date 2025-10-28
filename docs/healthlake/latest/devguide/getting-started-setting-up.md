# Setting up AWS HealthLake

In this chapter, you use the AWS Management Console to set up the required permissions to start using
AWS HealthLake and create a data store. To set up permissions to create a data store, you create
an IAM user or role that is a data lake administrator and HealthLake administrator. You make
this user a data lake administrator in AWS Lake Formation. The data lake administrator grants Lake Formation
access to resources needed to use Amazon Athena to query a data store. After you create a HealthLake
data store, you can set up permissions for importing and exporting files.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create a user with administrative access](#create-an-admin "#create-an-admin")
- [Configure an IAM user or role to use HealthLake
  (IAM Administrator)](#setting-up-configure-iam "#setting-up-configure-iam")
- [Add a user or role as the Data Lake
  Administrator in Lake Formation (IAM Administrator)](#setting-up-add-lake-formation "#setting-up-add-lake-formation")
- [Create S3 buckets](#setting-up-create-s3-buckets "#setting-up-create-s3-buckets")
- [Create a data store](#setting-up-create-data-store "#setting-up-create-data-store")
- [Setting up permissions for import
  jobs](#setting-up-import-permissions "#setting-up-import-permissions")
- [Setting up permissions for export
  jobs](#setting-up-export-permissions "#setting-up-export-permissions")
- [Install the AWS CLI](#setting-up-install-cli "#setting-up-install-cli")

## Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

## Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Configure an IAM user or role to use HealthLake

(IAM Administrator)

###### Persona: IAM Administrator

A user who can create IAM users and roles, and can add data lake
administrators.

These steps in this topic must be carried out by an IAM administrator.

To connect your HealthLake data store to Athena, you need create an IAM user or role that
is a data lake administrator and a HealthLake administrator. This new user or role grants
access to resources found in a data store via AWS Lake Formation, and has the
`AmazonHealthLakeFullAccess` AWS managed policy added to their user or role.

###### Important

An IAM user or role that is a data lake administrator
_cannot_ create new data lake administrators. To add
additional data lake administrator you must use a IAM user or role which has been
granted `AdministratorAccess` access.

###### To create an administrator

1. Add the `AmazonHealthlakeFullAccess` IAM AWS managed
   policy to a user or role in your organization.

If you're unfamiliar with creating an IAM user, see [Creating an IAM User](../../../IAM/latest/UserGuide/Using_SettingUpUser.md#Using_CreateUser_console "../../../IAM/latest/UserGuide/Using_SettingUpUser.md#Using_CreateUser_console") and [Overview of AWS IAM
Policies](../../../IAM/latest/UserGuide/PoliciesOverview.md "../../../IAM/latest/UserGuide/PoliciesOverview.md") in the _IAM User Guide_. 2. Grant the IAM user or role access to AWS Lake Formation.

    * Add the following IAM AWS managed policy to a user or role in your
     organization: `AWSLakeFormationDataAdmin`


    ###### Note

    The `AWSLakeFormationDataAdmin` policy grants access to
     all AWS Lake Formation resources. We recommend that you always use the
     minimum permissions required to accomplish your task. For more
     information, see [IAM Best
     Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the *IAM User
     Guide*.

3. Add the following inline policy to the user or role. For more information, see
   [Inline policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies") in the
   _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`/*",
 "arn:aws:s3:::`amzn-s3-demo-logging-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ram:GetResourceShareInvitations",
 "ram:AcceptResourceShareInvitation",
 "glue:CreateDatabase",
 "glue:DeleteDatabase"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information on the `AWSLakeFormationDataAdmin` policy, see [Lake Formation Personas and IAM Permissions Reference](../../../index.md "../../../index.md") in
the _AWS Lake Formation Developer Guide_.

## Add a user or role as the Data Lake

Administrator in Lake Formation (IAM Administrator)

###### Note

This step is required if you are integrating [SQL index and query](integrating-athena.md "integrating-athena.md").

Next, the IAM administrator must add the user or role created in the previous step
as a data lake administrator in Lake Formation.

###### To add an IAM user or role as a data lake administrator

1. Open the AWS Lake Formation console: [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/")

###### Note

If this is your first time visiting Lake Formation, a **Welcome to
Lake Formation** dialog box appears asking you to define a Lake Formation
administrator.

![Image of a dialog box asking you to define a lake formation administrator](/images/healthlake/latest/devguide/images/lf-landing-page.png) 2. Assign the new user or role to be a AWS Lake Formation data lake administrator.

    * *Option 1:* If you received the **Welcome
     to Lake Formation** dialog box.



    	1. Choose **Add other AWS users or
    	 roles**.
    	2. Choose the **down arrow (▼)**.
    	3. Choose the HealthLake administrator you would like to also be Lake Formation
    	 administrators.
    	4. Choose **Get started**.
    * *Option 2:* Use the **Navigation pane
     (☰)**.



    	1. Choose the **Navigation pane
    	 (☰)**.
    	2. Under **Permissions**, choose
    	 **Administrative roles and tasks**.
    	3. In the **Data lake administrators** section,
    	 select **Choose administrators** .
    	4. In the **Manage data lake administrators**
    	 dialog box, choose the **down arrow
    	 (▼)**.
    	5. Next, select or search for the HealthLake administrators users or
    	 roles who you also want to be Lake Formation administrators.
    	6. Choose **Save**.

3. Change the default security settings to be managed by Lake Formation. The HealthLake data
   store resources need to be managed by Lake Formation _not_ IAM. To
   update, see [Change the default permission model](../../../lake-formation/latest/dg/getting-started-setup.md#setup-change-cat-settings "../../../lake-formation/latest/dg/getting-started-setup.md#setup-change-cat-settings") in the _AWS Lake Formation
   Developer Guide_.

## Create S3 buckets

To import FHIR R4 data into AWS HealthLake, two Amazon S3 buckets are recommended. The Amazon S3
input bucket holds the FHIR data to be imported and HealthLake reads from this bucket. The
Amazon S3 output bucket stores the processing results of the import job and HealthLake writes
(logs) to this bucket.

###### Note

Due to AWS Identity and Access Management (IAM) policy, your Amazon S3 bucket names must be unique. For more
information, see [Bucket naming
rules](../../../AmazonS3/latest/userguide/bucketnamingrules.md "../../../AmazonS3/latest/userguide/bucketnamingrules.md") in the _Amazon Simple Storage Service User Guide_.

For the purpose of this guide, we specify the following Amazon S3 input and output buckets
when setting up [import permissions](#setting-up-import-permissions "#setting-up-import-permissions")
later in this section.

- Input bucket:
  `arn:aws:s3:::`amzn-s3-demo-source-bucket``
- Output bucket:
  `arn:aws:s3:::`amzn-s3-demo-logging-bucket``

For additional information, see [Creating a
bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.

## Create a data store

A HealthLake data store is a repository of FHIR R4 data that resides within a single
AWS Region. An AWS account can have zero or many data stores. HealthLake supports two
data store authorization
strategies.

###### Important

Before you create a HealthLake data store, review the [Service
control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in your AWS Organization that might restrict
the creation or management of HealthLake resources. SCPs can prevent the successful
creation of HealthLake data stores, even if your IAM permissions are set up
correctly.

A `datastoreID` is generated when you create a HealthLake data store. You
must use the `datastoreID` when setting up [import permissions](#setting-up-import-permissions "#setting-up-import-permissions") later in this
section.

To create a HealthLake data store, see [Creating a HealthLake data store](managing-data-stores-create.md "managing-data-stores-create.md").

## Setting up permissions for import

jobs

Before you import files into a data store, you must grant HealthLake permission to access
your input and output buckets in Amazon S3. To grant HealthLake access, you create an IAM
service role for HealthLake, add a trust policy to the role to grant HealthLake assume role
permissions, and attach a permissions policy to role that grants it to access to your
Amazon S3 buckets.

When you create an import job, you specify the Amazon Resource Name (ARN) of this
role for the `DataAccessRoleArn`. For more information about IAM roles and
trust policies, see [IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md").

After you set up permission, you are ready to import files into your data store with
an import job. For more information, see [Starting a FHIR import job](importing-fhir-data-start.md "importing-fhir-data-start.md").

###### To set up import permissions

1. If haven't already, create a destination Amazon S3 bucket for output log files. The
   Amazon S3 bucket must be in the same AWS Region as the service, and Block Public
   Access must be turned on for all options. To learn more, see [Using
   Amazon S3 block public access](../../../AmazonS3/latest/dev/access-control-block-public-access.md "../../../AmazonS3/latest/dev/access-control-block-public-access.md"). An Amazon-owned or customer-owned KMS
   key must also be used for encryption. To learn more about using KMS keys, see
   [Amazon Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").
2. Create a data access service role for HealthLake and give the HealthLake service
   permission to assume it with the following trust policy. HealthLake uses this to
   write the output Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "healthlake.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`accountID`"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:healthlake:us-west-2:`111122223333`:datastore/fhir/`datastoreID`"
 }
 }
 }
 ]
}`

```

3. Add a permissions policy to the data access role that allows it to access the
   Amazon S3 bucket. Replace `amzn-s3-demo-bucket` with your bucket's
   name.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketPublicAccessBlock",
 "s3:GetEncryptionConfiguration"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`"
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
 },
 {
 "Action": [
 "kms:DescribeKey",
 "kms:GenerateDataKey*"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:012345678910:key/d330e7fc-b56c-4216-a250-f4c43ef46e83"
 ],
 "Effect": "Allow"
 }]
}`

```

## Setting up permissions for export

jobs

Before you export files from a data store, you must grant HealthLake permission to access
your output bucket in Amazon S3. To grant HealthLake access, you create an IAM service role for
HealthLake, add a trust policy to the role to grant HealthLake assume role permissions, and attach
a permissions policy to role that grants it to access to your Amazon S3 bucket.

If you already created a role for HealthLake, you can reuse it and grant it the additional
permissions for your export Amazon S3 bucket listed in this topic. To learn more about IAM
roles and trust policies, see [IAM
Policies and Permissions](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md").

###### Important

HealthLake supports both [native SDK export
requests](exporting-fhir-data.md "exporting-fhir-data.md") and the [FHIR R4
$export](reference-fhir-operations-export.md "reference-fhir-operations-export.md") operation. Separate IAM actions must be
provided depending on which export API you decide to use. This allows you to handle
`allow` and `deny` permissions separately. If you want to
restrict both HealthLake SDK and FHIR REST API exports, you must apply deny permissions
to the separate IAM actions. IAM user permission changes are not required if you
give users full access to HealthLake.

###### Using AWS CLI and AWS SDKs:

The following native HealthLake actions are available for exporting data from a data store
using the AWS CLI and AWS SDKs:

- `StartFHIRExportJob`
- `DescribeFHIRExportJob`
- `ListFHIRExportJobs`

###### Using FHIR APIs:

The following IAM actions are available for exporting data from a HealthLake data
store and for cancelling (deleting) an export job using the FHIR `$export` operation:

`POST`:

- `StartFHIRExportJobWithPost`
  `GET`:

- `StartFHIRExportJobWithGet`
- `DescribeFHIRExportJobWithGet`
- `GetExportedFile`
  `DELETE`:

- `CancelFHIRExportJobWithDelete`

The user or role that sets up permissions must have permission to create roles, create
policies, and attach policies to roles. The following IAM policy grants these
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "iam:CreateRole",
 "iam:CreatePolicy",
 "iam:AttachRolePolicy"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "iam:PassRole",
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "healthlake.amazonaws.com"
 }
 }
 }
 ]
}`

```

###### To set up export permissions

1. If haven't already, create a destination Amazon S3 bucket for the data you will
   export from your data store. The Amazon S3 bucket must be in the same AWS Region as
   the service, and Block Public Access must be turned on for all options. To learn
   more, see [Using
   Amazon S3 block public access](../../../AmazonS3/latest/dev/access-control-block-public-access.md "../../../AmazonS3/latest/dev/access-control-block-public-access.md"). An Amazon-owned or customer-owned KMS
   key must also be used for encryption. To learn more about using KMS keys, see
   [Amazon Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").
2. If you haven't already, create a data access service role for HealthLake and give
   the HealthLake service permission to assume it with the following trust policy. HealthLake
   uses this to write the output Amazon S3 bucket. If you already created one in [Setting up permissions for import
   jobs](#setting-up-import-permissions "#setting-up-import-permissions"), you can reuse it and grant
   it permissions for your Amazon S3 bucket in the next step.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "healthlake.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`accountID`"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:healthlake:us-west-2:`111122223333`:datastore/fhir/`data store ID`"
 }
 }
 }
 ]
}`

```

3. Add a permissions policy to the data access role that allows it to access your
   output Amazon S3 bucket. Replace `amzn-s3-demo-bucket` with your bucket's
   name.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketPublicAccessBlock",
 "s3:GetEncryptionConfiguration"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`"
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
 },
 {
 "Action": [
 "kms:DescribeKey",
 "kms:GenerateDataKey*"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:012345678910:key/d330e7fc-b56c-4216-a250-f4c43ef46e83"
 ],
 "Effect": "Allow"
 }]
}`

```

## Install the AWS CLI

The AWS CLI is required to describe and list HealthLake import and export job properties. You
can also request this information using HealthLake SDKs.

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
aws healthlake help
```

If the AWS CLI is configured correctly, you see a brief description of AWS HealthLake
and a list of available commands.
