# Storing and retaining sensitive data

discovery results

When you run a sensitive data discovery job or Amazon Macie performs automated sensitive data discovery, Macie creates an analysis
record for each Amazon Simple Storage Service (Amazon S3) object that's included in the scope of the analysis. These
records, referred to as a _sensitive data discovery results_, log details about
the analysis that Macie performs on individual S3 objects. This includes objects that Macie
doesn't detect sensitive data in, and therefore don't produce findings, and objects that
Macie can't analyze due to errors or issues. If Macie detects sensitive data in an object,
the record includes data from the corresponding finding as well as additional information.
Sensitive data discovery results provide you with analysis records that can be helpful for
data privacy and protection audits or investigations.

Macie stores your sensitive data discovery results for only 90 days. To access your results and enable
long-term storage and retention of them, configure Macie to encrypt the results with an
AWS Key Management Service (AWS KMS) key and store them in an S3 bucket. The bucket can serve as a definitive,
long-term repository for all of your sensitive data discovery results. You can then optionally access and query
the results in that repository.

This topic guides you through the process of using the AWS Management Console to configure a
repository for your sensitive data discovery results. The configuration is a combination of an AWS KMS key
that encrypts the results, an S3 general purpose bucket that stores the results, and Macie
settings that specify which key and bucket to use. If you prefer to configure the Macie
settings programmatically, you can use the [PutClassificationExportConfiguration](../APIReference/classification-export-configuration.md "../APIReference/classification-export-configuration.md") operation of the Amazon Macie API.

When you configure the settings in Macie, your choices apply only to the current
AWS Region. If you're the Macie administrator for an organization, your choices apply only to your
account. They don't apply to any associated member accounts. If you enable automated sensitive data discovery or run
sensitive data discovery jobs to analyze data for member accounts, Macie stores the sensitive data discovery results in the
repository for your administrator account.

If you use Macie in multiple AWS Regions, configure the repository settings for each
Region in which you use Macie. You can optionally store sensitive data discovery results for multiple Regions in
the same S3 bucket. However, note the following requirements:

- To store the results for a Region that AWS enables by default for
  AWS accounts, such as the US East (N. Virginia) Region, you have to choose a bucket in a Region
  that's enabled by default. The results can't be stored in a bucket in an opt-in
  Region (Region that's disabled by default).
- To store the results for an opt-in Region, such as the Middle East (Bahrain) Region, you have
  to choose a bucket in that same Region or a Region that's enabled by default. The
  results can't be stored in a bucket in a different opt-in Region.
  To determine whether a Region is enabled by default, see [Enable or disable AWS Regions in your account](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the _AWS Account Management User Guide_. In addition to the preceding requirements, also
  consider whether you want to [retrieve samples of
  sensitive data](findings-retrieve-sd.md "findings-retrieve-sd.md") that Macie reports in individual findings. To retrieve sensitive
  data samples from an affected S3 object, all of the following resources and data must be
  stored in the same Region: the affected object, the applicable finding, and the
  corresponding sensitive data discovery result.

###### Tasks

- [Before you begin: Learn key
  concepts](#discovery-results-repository-s3-overview "#discovery-results-repository-s3-overview")
- [Step 1: Verify your
  permissions](#discovery-results-repository-s3-permissions "#discovery-results-repository-s3-permissions")
- [Step 2: Configure an
  AWS KMS key](#discovery-results-repository-s3-key-policy "#discovery-results-repository-s3-key-policy")
- [Step 3: Choose an S3
  bucket](#discovery-results-repository-s3-choose-bucket "#discovery-results-repository-s3-choose-bucket")

## Before you begin: Learn key

concepts

Amazon Macie automatically creates a sensitive data discovery result for each Amazon S3 object that it analyzes or
attempts to analyze when you run a sensitive data discovery job or it performs automated sensitive data discovery. This
includes:

- Objects that Macie detects sensitive data in, and therefore also produce
  sensitive data findings.
- Objects that Macie doesn't detect sensitive data in, and therefore don't
  produce sensitive data findings.
- Objects that Macie can't analyze due to errors or issues such as permissions
  settings or use of an unsupported file or storage format.

If Macie detects sensitive data in an S3 object, the sensitive data discovery result includes data from the
corresponding sensitive data finding. It provides additional information too, such as
the location of as many as 1,000 occurrences of each type of sensitive data that Macie
found in the object. For example:

- The column and row number for a cell or field in a Microsoft Excel workbook,
  CSV file, or TSV file
- The path to a field or array in a JSON or JSON Lines file
- The line number for a line in a non-binary text file other than a CSV, JSON,
  JSON Lines, or TSV file—for example, an HTML, TXT, or XML file
- The page number for a page in an Adobe Portable Document Format (PDF)
  file
- The record index and the path to a field in a record in an Apache Avro object
  container or Apache Parquet file

If the affected S3 object is an archive file, such as a .tar or .zip file, the sensitive data discovery result
also provides detailed location data for occurrences of sensitive data in individual
files that Macie extracted from the archive. Macie doesn’t include this information in
sensitive data findings for archive files. To report location data, sensitive data discovery results use a
[standardized JSON schema](findings-locate-sd-schema.md "findings-locate-sd-schema.md").

A sensitive data discovery result doesn't include the sensitive data that Macie found. Instead, it provides you
with an analysis record that can be helpful for audits or investigations.

Macie stores your sensitive data discovery results for 90 days. You can’t access them directly on the
Amazon Macie console or with the Amazon Macie API. Instead, follow the steps in this topic to
configure Macie to encrypt your results with an AWS KMS key that you specify, and
store the results in an S3 general purpose bucket that you also specify. Macie then
writes the results to JSON Lines (.jsonl) files, adds the files to the bucket as GNU Zip
(.gz) files, and encrypts the data using SSE-KMS encryption. As of November 8, 2023,
Macie also signs the resulting S3 objects with a Hash-based Message Authentication Code
(HMAC) AWS KMS key.

After you configure Macie to store your sensitive data discovery results in an S3 bucket, the bucket can
serve as a definitive, long-term repository for the results. You can then optionally
access and query the results in that repository.

###### Tips

For a detailed, instructional example of how you might query and use sensitive data discovery results
to analyze and report potential data security risks, see the following blog post on
the _AWS Security Blog_: [How to query and visualize Macie sensitive data discovery results with Amazon Athena and
Amazon Quick Suite](https://aws.amazon.com/blogs/security/how-to-query-and-visualize-macie-sensitive-data-discovery-results-with-athena-and-quicksight/ "https://aws.amazon.com/blogs/security/how-to-query-and-visualize-macie-sensitive-data-discovery-results-with-athena-and-quicksight/").

For samples of Amazon Athena queries that you can use to analyze sensitive data discovery results, visit
the [Amazon Macie Results Analytics repository](https://github.com/aws-samples/amazon-macie-results-analytics "https://github.com/aws-samples/amazon-macie-results-analytics") on GitHub. This repository also
provides instructions for configuring Athena to retrieve and decrypt your results,
and scripts for creating tables for the results.

## Step 1: Verify your

permissions

Before you configure a repository for your sensitive data discovery results, verify that you have the
permissions that you need to encrypt and store the results. To verify your permissions,
use AWS Identity and Access Management (IAM) to review the IAM policies that are attached to your IAM
identity. Then compare the information in those policies to the following list of
actions that you must be allowed to perform to configure the repository.

Amazon Macie

For Macie, verify that you're allowed to perform the following
action:

`macie2:PutClassificationExportConfiguration`

This action allows you to add or change the repository settings in
Macie.

Amazon S3

For Amazon S3, verify that you're allowed to perform the following
actions:

- `s3:CreateBucket`
- `s3:GetBucketLocation`
- `s3:ListAllMyBuckets`
- `s3:PutBucketAcl`
- `s3:PutBucketPolicy`
- `s3:PutBucketPublicAccessBlock`
- `s3:PutObject`

These actions allow you to access and configure an S3 general purpose
bucket that can serve as the repository.

AWS KMS

To use the Amazon Macie console to add or change the repository settings,
also verify that you're allowed to perform the following AWS KMS
actions:

- `kms:DescribeKey`
- `kms:ListAliases`

These actions allow you to retrieve and display information about the
AWS KMS keys for your account. You can then choose one of these keys to
encrypt your sensitive data discovery results.

If you plan to create a new AWS KMS key to encrypt the data, you also
need to be allowed to perform the following actions:
`kms:CreateKey`, `kms:GetKeyPolicy`, and
`kms:PutKeyPolicy`.

If you're not allowed to perform the requisite actions, ask your AWS administrator
for assistance before you proceed to the next step.

## Step 2: Configure an

AWS KMS key

After you verify your permissions, determine which AWS KMS key you want Macie to
use to encrypt your sensitive data discovery results. The key must be a customer managed, symmetric
encryption KMS key that's enabled in the same AWS Region as the S3 bucket where you
want to store the results.

The key can be an existing AWS KMS key from your own account, or an existing
AWS KMS key that another account owns. If you want to use a new KMS key, create the
key before proceeding. If you want to use an existing key that another account owns,
obtain the Amazon Resource Name (ARN) of the key. You'll need to enter this ARN when you
configure the repository settings in Macie. For information about creating and reviewing
the settings for KMS keys, see the [AWS Key Management Service Developer Guide](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").

###### Note

The key can be an AWS KMS key in an external key store. However, the key might
then be slower and less reliable than a key that’s managed entirely within AWS KMS.
You can reduce this risk by storing your sensitive data discovery results in an S3 bucket that’s
configured to use the key as an S3 Bucket Key. Doing so reduces the number of AWS KMS
requests that must be made to encrypt your sensitive data discovery results.

For information about using KMS keys in external key stores, see [External key stores](../../../kms/latest/developerguide/keystore-external.md "../../../kms/latest/developerguide/keystore-external.md") in the _AWS Key Management Service Developer
Guide_. For information about using S3 Bucket Keys, see [Reducing
the cost of SSE-KMS with Amazon S3 Bucket Keys](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md") in the _Amazon Simple Storage Service User Guide_.

After you determine which KMS key you want Macie to use, give Macie permission to
use the key. Otherwise, Macie won't be able to encrypt or store your results in the
repository. To give Macie permission to use the key, update the key policy for the key.
For detailed information about key policies and managing access to KMS keys, see
[Key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
_AWS Key Management Service Developer Guide_.

###### To update the key policy

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. Choose the key that you want Macie to use to encrypt your sensitive data discovery results.
4. On the **Key policy** tab, choose
   **Edit**.
5. Copy the following statement to your clipboard, and then add it to the
   policy:

```
{
    "Sid": "Allow Macie to use the key",
    "Effect": "Allow",
    "Principal": {
        "Service": "macie.amazonaws.com"
    },
    "Action": [
        "kms:GenerateDataKey",
        "kms:Encrypt"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "`111122223333`"
         },
         "ArnLike": {
             "aws:SourceArn": [
                 "arn:aws:macie2:`us-east-1`:`111122223333`:export-configuration:*",
                 "arn:aws:macie2:`us-east-1`:`111122223333`:classification-job/*"
             ]
         }
    }
}
```

###### Note

When you add the statement to the policy, make sure that the syntax is valid. Policies use
JSON format. This means that you need to also add a comma before or after
the statement, depending on where you add the statement to the policy. If
you add the statement as the last statement, add a comma after the closing
curly brace for the preceding statement. If you add it as the first
statement or between two existing statements, add a comma after the closing
curly brace for the statement. 6. Update the statement with the correct values for your environment:

    * In the `Condition` fields, replace the placeholder values,
     where:




    	+ `111122223333` is the
    	 account ID for your AWS account.
    	+ `us-east-1` is the Region code for
    	 the AWS Region in which you're using Macie and want to allow
    	 Macie to use the key.


    	If you use Macie in multiple Regions and want to allow Macie
    	 to use the key in additional Regions, add
    	 `aws:SourceArn` conditions for each additional
    	 Region. For example:



    	```
    	"aws:SourceArn": [
    	    "arn:aws:macie2:us-east-1:111122223333:export-configuration:*",
    	    "arn:aws:macie2:us-east-1:111122223333:classification-job/*",
    	    "arn:aws:macie2:us-west-2:111122223333:export-configuration:*",
    	    "arn:aws:macie2:us-west-2:111122223333:classification-job/*"
    	]
    	```

    	Alternatively, you can allow Macie to use the key in all
    	 Regions. To do this, replace the placeholder value with the
    	 wildcard character (`*`). For example:



    	```
    	"aws:SourceArn": [
    	    "arn:aws:macie2:*:111122223333:export-configuration:*",
    	    "arn:aws:macie2:*:111122223333:classification-job/*"
    	]
    	```
    * If you're using Macie in an opt-in Region, add the appropriate Region
     code to the value for the `Service` field. For example, if
     you're using Macie in the Middle East (Bahrain) Region, which has the Region code
     *me-south-1*,
     replace `macie.amazonaws.com` with
     `macie.me-south-1.amazonaws.com`.


    For a list of Regions where Macie is currently available and the
     Region code for each one, see [Amazon Macie endpoints and quotas](../../../general/latest/gr/macie.md "../../../general/latest/gr/macie.md") in the *AWS General Reference*.

Note that the `Condition` fields use two IAM global condition
keys:

    * [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") – This condition allows Macie to
     perform the specified actions only for your account. More specifically,
     it determines which account can perform the specified actions for the
     resources and actions specified by the `aws:SourceArn`
     condition.


    To allow Macie to perform the specified actions for additional
     accounts, add the account ID for each additional account to this
     condition. For example:



    ```
    "aws:SourceAccount": [111122223333,444455556666]
    ```
    * [aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") – This condition prevents other
     AWS services from performing the specified actions. It also prevents
     Macie from using the key while performing other actions for your
     account. In other words, it allows Macie to encrypt S3 objects with the
     key only if: the objects are sensitive data discovery results, and the
     results are for automated sensitive data discovery or sensitive data discovery jobs created by
     the specified account in the specified Region.


    To allow Macie to perform the specified actions for additional
     accounts, add ARNs for each additional account to this condition. For
     example:



    ```
    "aws:SourceArn": [
        "arn:aws:macie2:us-east-1:111122223333:export-configuration:*",
        "arn:aws:macie2:us-east-1:111122223333:classification-job/*",
        "arn:aws:macie2:us-east-1:444455556666:export-configuration:*",
        "arn:aws:macie2:us-east-1:444455556666:classification-job/*"
    ]
    ```

The accounts specified by the `aws:SourceAccount` and
`aws:SourceArn` conditions should match.

These conditions help prevent Macie from being used as a [confused deputy](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") during transactions with AWS KMS. Although we don’t
recommend it, you can remove these conditions from the statement. 7. When you finish adding and updating the statement, choose **Save
changes**.

## Step 3: Choose an S3

bucket

After you verify your permissions and configure the AWS KMS key, you're ready to
specify which S3 bucket you want to use as the repository for your sensitive data discovery results. You
have two options:

- **Use a new S3 bucket that Macie creates**
  – If you choose this option, Macie automatically creates a new S3 general
  purpose bucket in the current AWS Region for your discovery results. Macie
  also applies a bucket policy to the bucket. The policy allows Macie to add
  objects to the bucket. It also requires the objects to be encrypted with the
  AWS KMS key that you specify, using SSE-KMS encryption. To review the policy,
  choose **View policy** on the Amazon Macie console after you
  specify a name for the bucket and the KMS key to use.
- **Use an existing S3 bucket that you create**
  – If you prefer to store your discovery results in a particular S3 bucket
  that you create, create the bucket before you proceed. The bucket must be a
  general purpose bucket. In addition, the bucket's settings and policy must allow
  Macie to add objects to the bucket. This topic explains which settings to check
  and how to update the policy. It also provides examples of the statements to add
  to the policy.

The following sections provide instructions for each option. Choose the section for
the option that you want.

If you prefer to use a new S3 bucket that Macie creates for you, the final
step in the process is to configure the repository settings in Macie.

###### To configure the repository settings in Macie

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, under **Settings**, choose
   **Discovery results**.
3. Under **Repository for sensitive data discovery
   results**, choose **Create
   bucket**.
4. In the **Create a bucket** box, enter a name for the
   bucket.

The name must be unique across all S3 buckets. In addition, the name
can consist only of lowercase letters, numbers, dots (.), and hyphens
(-). For additional naming requirements, see [Bucket naming
rules](../../../AmazonS3/latest/userguide/bucketnamingrules.md "../../../AmazonS3/latest/userguide/bucketnamingrules.md") in the _Amazon Simple Storage Service User
Guide_. 5. Expand the **Advanced** section. 6. (Optional) To specify a prefix to use in the path to a location in the
bucket, enter the prefix in the **Data discovery result
prefix** box.

When you enter a value, Macie updates the example below the box to
show the path to the bucket location where it will store your discovery
results. 7. For **Block all public access**, choose
**Yes** to enable all block public access settings
for the bucket.

For information about these settings, see [Blocking public access to your Amazon S3 storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md") in the
_Amazon Simple Storage Service User Guide_. 8. Under **Encryption settings**, specify the
AWS KMS key that you want Macie to use to encrypt the results:

    * To use a key from your own account, choose **Select a
     key from your account**. Then, in the
     **AWS KMS key** list, choose the key to
     use. The list displays customer managed, symmetric encryption
     KMS keys for your account.
    * To use a key that another account owns, choose **Enter
     the ARN of a key from another account**. Then, in
     the **AWS KMS key ARN** box, enter the
     Amazon Resource Name (ARN) of the key to use—for example,
     ``arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``.

9. When you finish entering the settings, choose
   **Save**.

Macie tests the settings to verify that they're correct. If any
settings are incorrect, Macie displays an error message to help you
address the issue.
After you save the repository settings, Macie adds existing discovery results
for the preceding 90 days to the repository. Macie also starts adding new
discovery results to the repository.

If you prefer to store your sensitive data discovery results in a particular S3 bucket that you
create, create and configure the bucket before you configure the settings in
Macie. When you create the bucket, note the following requirements:

- The bucket must be a general purpose bucket. It can't be another type
  of bucket, such as a directory bucket.
- To store your discovery results for a Region that's enabled by default
  for AWS accounts, such as the US East (N. Virginia) Region, the bucket has to be in
  a Region that's enabled by default. The results can't be stored in a
  bucket in an opt-in Region (Region that's disabled by default).
- To store your discovery results for an opt-in Region, such as the
  Middle East (Bahrain) Region, the bucket has to be in the same Region or a Region
  that's enabled by default. The results can't be stored in a bucket in a
  different opt-in Region.
  To determine whether a Region is enabled by default, see [Enable or disable
  AWS Regions in your account](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the _AWS Account Management User Guide_.

After you create the bucket, update the bucket's policy to allow Macie to
retrieve information about the bucket and add objects to the bucket. You can
then configure the settings in Macie.

###### To update the bucket policy for the bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the bucket that you want to store your discovery results
   in.
3. Choose the **Permissions** tab.
4. In the **Bucket policy** section, choose
   **Edit**.
5. Copy the following example policy to your clipboard:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow Macie to use the GetBucketLocation operation",
 "Effect": "Allow",
 "Principal": {
 "Service": "macie.amazonaws.com"
 },
 "Action": "s3:GetBucketLocation",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:macie2:`us-east-1`:`111122223333`:export-configuration:*",
 "arn:aws:macie2:`us-east-1`:`111122223333`:classification-job/*"
 ]
 }
 }
 },
 {
 "Sid": "Allow Macie to add objects to the bucket",
 "Effect": "Allow",
 "Principal": {
 "Service": "macie.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`[optional prefix/]`*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:macie2:`us-east-1`:`111122223333`:export-configuration:*",
 "arn:aws:macie2:`us-east-1`:`111122223333`:classification-job/*"
 ]
 }
 }
 },
 {
 "Sid": "Deny unencrypted object uploads. This is optional",
 "Effect": "Deny",
 "Principal": {
 "Service": "macie.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`[optional prefix/]`*",
 "Condition": {
 "StringNotEquals": {
 "s3:x-amz-server-side-encryption": "aws:kms"
 }
 }
 },
 {
 "Sid": "Deny incorrect encryption headers. This is optional",
 "Effect": "Deny",
 "Principal": {
 "Service": "macie.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`[optional prefix/]`*",
 "Condition": {
 "StringNotEquals": {
 "s3:x-amz-server-side-encryption-aws-kms-key-id": "`arn:aws:kms:us-east-1:`111122223333`:key/KMSKeyId`"
 }
 }
 },
 {
 "Sid": "Deny non-HTTPS access",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "false"
 }
 }
 }
 ]
}`

```

6.  Paste the example policy in the **Bucket policy**
    editor on the Amazon S3 console.
7.  Update the example policy with the correct values for your
    environment:

        * In the optional statement that denies incorrect encryption
         headers:




        	+ Replace `amzn-s3-demo-bucket`
        	 with the name of the bucket. To also specify a prefix
        	 for a path to a location in the bucket, replace
        	 `[optional prefix/]` with
        	 the prefix. Otherwise, remove the `[optional
        	 prefix/]` placeholder value.
        	+ In the `StringNotEquals` condition, replace
        	 `arn:aws:kms:us-east-1:111122223333:key/KMSKeyId`
        	 with the Amazon Resource Name (ARN) of the
        	 AWS KMS key to use for encryption of your discovery
        	 results.
        * In all other statements, replace the placeholder values,
         where:




        	+ `amzn-s3-demo-bucket` is the
        	 name of the bucket.
        	+ `[optional prefix/]` is the
        	 prefix for a path to a location in the bucket. Remove
        	 this placeholder value if you don't want to specify a
        	 prefix.
        	+ `111122223333` is
        	 the account ID for your AWS account.
        	+ `us-east-1` is the Region
        	 code for the AWS Region in which you're using Macie
        	 and want to allow Macie to add discovery results to the
        	 bucket.


        	If you use Macie in multiple Regions and want to allow
        	 Macie to add results to the bucket for additional
        	 Regions, add `aws:SourceArn` conditions for
        	 each additional Region. For example:



        	```
        	"aws:SourceArn": [
        	    "arn:aws:macie2:us-east-1:111122223333:export-configuration:*",
        	    "arn:aws:macie2:us-east-1:111122223333:classification-job/*",
        	    "arn:aws:macie2:us-west-2:111122223333:export-configuration:*",
        	    "arn:aws:macie2:us-west-2:111122223333:classification-job/*"
        	]
        	```

        	Alternatively, you can allow Macie to add results to
        	 the bucket for all Regions in which you use Macie. To do
        	 this, replace the placeholder value with the wildcard
        	 character (`*`). For example:



        	```
        	"aws:SourceArn": [
        	    "arn:aws:macie2:*:111122223333:export-configuration:*",
        	    "arn:aws:macie2:*:111122223333:classification-job/*"
        	]
        	```
        * If you're using Macie in an opt-in Region, add the appropriate
         Region code to the value for the `Service` field in
         each statement that specifies the Macie service principal. For
         example, if you're using Macie in the Middle East (Bahrain) Region, which has
         the Region code *me-south-1*, replace
         `macie.amazonaws.com` with
         `macie.me-south-1.amazonaws.com` in each
         applicable statement.


        For a list of Regions where Macie is currently available and
         the Region code for each one, see [Amazon Macie endpoints and
         quotas](../../../general/latest/gr/macie.md "../../../general/latest/gr/macie.md") in the *AWS General Reference*.

    Note that the example policy includes statements that allow Macie to
    determine which Region the bucket resides in
    (`GetBucketLocation`) and add objects to the bucket
    (`PutObject`). These statements define conditions that
    use two IAM global condition keys:

        * [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") – This condition allows
         Macie to add sensitive data discovery results to the bucket only
         for your account. It prevents Macie from adding discovery
         results for other accounts to the bucket. More specifically, the
         condition specifies which account can use the bucket for the
         resources and actions specified by the
         `aws:SourceArn` condition.


        To store results for additional accounts in the bucket, add
         the account ID for each additional account to this condition.
         For example:



        ```
        "aws:SourceAccount": [111122223333,444455556666]
        ```
        * [aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") – This condition restricts
         access to the bucket based on the source of the objects that are
         being added to the bucket. It prevents other AWS services from
         adding objects to the bucket. It also prevents Macie from adding
         objects to the bucket while performing other actions for your
         account. More specifically, the condition allows Macie to add
         objects to the bucket only if: the objects are sensitive data
         discovery results, and the results are for automated sensitive data discovery or
         sensitive data discovery jobs created by the specified account
         in the specified Region.


        To allow Macie to perform the specified actions for additional
         accounts, add ARNs for each additional account to this
         condition. For example:



        ```
        "aws:SourceArn": [
            "arn:aws:macie2:us-east-1:111122223333:export-configuration:*",
            "arn:aws:macie2:us-east-1:111122223333:classification-job/*",
            "arn:aws:macie2:us-east-1:444455556666:export-configuration:*",
            "arn:aws:macie2:us-east-1:444455556666:classification-job/*"
        ]
        ```

    The accounts specified by the `aws:SourceAccount` and
    `aws:SourceArn` conditions should match.

Both conditions help prevent Macie from being used as a [confused deputy](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") during transactions with Amazon S3. Although we
don’t recommend it, you can remove these conditions from the bucket
policy. 8. When you finish updating the bucket policy, choose **Save
changes**.
You can now configure the repository settings in Macie.

###### To configure the repository settings in Macie

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. In the navigation pane, under **Settings**, choose
   **Discovery results**.
3. Under **Repository for sensitive data discovery
   results**, choose **Existing
   bucket**.
4. For **Choose a bucket**, select the bucket that you
   want to store your discovery results in.
5. To specify a prefix for a path to a location in the bucket, expand the
   **Advanced** section. Then, for **Data
   discovery result prefix**, enter the prefix.

When you enter a value, Macie updates the example below the box to
show the path to the bucket location where it will store your discovery
results. 6. Under **Encryption settings**, specify the
AWS KMS key that you want Macie to use to encrypt the results:

    * To use a key from your own account, choose **Select a
     key from your account**. Then, in the
     **AWS KMS key** list, choose the key to
     use. The list displays customer managed, symmetric encryption
     KMS keys for your account.
    * To use a key that another account owns, choose **Enter
     the ARN of a key from another account**. Then, in
     the **AWS KMS key ARN** box, enter the ARN
     of the key to use—for example,
     `arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.

7. When you finish entering the settings, choose
   **Save**.

Macie tests the settings to verify that they're correct. If any
settings are incorrect, Macie displays an error message to help you
address the issue.
After you save the repository settings, Macie adds existing discovery results
for the preceding 90 days to the repository. Macie also starts adding new
discovery results to the repository.

###### Note

If you subsequently change the **Data discovery result
prefix** setting, also update the bucket policy in Amazon S3. Policy
statements that specify the previous prefix must specify the new prefix.
Otherwise, Macie won't be allowed to add your discovery results to the
bucket.

###### Tip

To reduce server-side encryption costs, also configure the S3 bucket to use an S3
Bucket Key, and specify the AWS KMS key that you configured for encryption of
your sensitive data discovery results. Use of an S3 Bucket Key reduces the number of calls to AWS KMS,
which can reduce AWS KMS request costs. If the KMS key is in an external key store,
use of an S3 Bucket Key can also minimize the performance impact of using the key.
To learn more, see [Reducing the cost of SSE-KMS
with Amazon S3 Bucket Keys](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md") in the _Amazon Simple Storage Service User
Guide_.
