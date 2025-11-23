# Amazon S3 integration

With Amazon S3 integration in Amazon Quick Suite, you can create knowledge bases from documents
stored in S3 buckets. This integration supports data ingestion capabilities for indexing and
searching S3 content. Amazon S3 actions are only supported for Quick Automate.

Amazon Quick Suite supports source attribution with citations. If you specify the \_source_uri metadata field when you add metadata to your Amazon S3 bucket,
the source attribution links returned by Amazon Quick Suite in the chat results will direct users to the configured URL. If you don't specify a \_source_uri,
users can still access the source documents through clickable citation links that will download the file at query time.
This allows users to verify information even when no source URI is configured.
To learn how to add metadata for your Amazon S3 connector, see [Adding document metadata in Amazon S3](#s3-metadata "#s3-metadata").

## What you can do

Amazon S3 users can ask questions about content stored in their Amazon S3 buckets. For
example, users can inquire about key findings from documents, search for specific
information across multiple file types, or analyze data patterns. The integration
enables users to quickly access and understand information from their Amazon S3 content,
regardless of file location or type, while providing contextual details such as
modification dates, and file metadata —all contributing to more
efficient information discovery and better-informed decision making.

###### Note

This guide covers Amazon S3 data ingestion integration for knowledge base creation. For Amazon S3 action connectors that perform Amazon S3
operations (upload, download, delete files), these must be created through the admin console. For more information, see [AWS service action connectors](builtin-services-integration.md "builtin-services-integration.md").

## Before you begin

Before you set up Amazon S3 integration, make sure you have the following:

- AWS account with Amazon S3 access.
- Amazon S3 bucket with documents to index.
- Amazon Quick Suite Enterprise subscription.
- Necessary permissions to create Amazon S3 integrations.

If you need to access Amazon S3 buckets in a different AWS account, verify that cross-account access has been enabled by your administrator.

###### Note

Cross-account Amazon S3 access is only supported within the same AWS region.

## Enable cross-account access (administrators only)

If you need to enable cross-account Amazon S3 access for your organization, complete the following steps.

###### To enable cross-account Amazon S3 access

1. Open the Amazon Quick Suite Admin console.
2. Choose **AWS resource page**, and then choose **Amazon S3 configuration**.
3. Select **Choose accessible buckets from other AWS accounts**.

## Prepare IAM role and policy setup

Before setting up the integration in Amazon Quick Suite, prepare your IAM role and policy configuration. Amazon S3 integration uses AWS authentication to access your Amazon S3 buckets.

### Required IAM permissions

Make sure your AWS account has the following minimum permissions for the Amazon S3 bucket:

- `s3:GetObject` - Read objects from the bucket.
- `s3:ListBucket` - List bucket contents.
- `s3:GetBucketLocation` - Get bucket region information.
- `s3:GetObjectVersion` - Get object versions.
- `s3:ListBucketVersions` - List bucket versions.

### Configure Amazon S3 bucket permissions for cross-account access

If you're accessing Amazon S3 buckets in a different AWS account, you must configure IAM policies in the source AWS account.

###### To configure Amazon S3 bucket permissions for cross-account access

1. Sign in to the AWS Management Console for the account that contains the Amazon S3 bucket.
2. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
3. Choose the bucket that you want to grant access to.
4. Choose **Permissions**, and then choose **Bucket Policy**.
5. Add a bucket policy with the following elements:
   - `Version` – Set to "2012-10-17"
   - `Statement` – Array containing policy statements with:
     - `Sid` – "AllowQuickSuiteS3Access"
     - `Effect` – "Allow"
     - `Principal` – AWS ARN for the Amazon Quick Suite service role in your account. For
       example, the principal should look like this:`"Principal": { "AWS":
"arn:aws:iam::<quick_account_id>:role/service-role/aws-quicksight-service-role-v0"
}`
     - `Action` – Array of Amazon S3 permissions: s3:GetObject, s3:ListBucket, s3:GetBucketLocation, s3:GetObjectVersion, s3:ListBucketVersions
     - `Resource` – "\*" (applies to the current key), the Amazon S3 bucket path should look like
       the following: `"Resource": [
"arn:aws:s3:::bucket_name"]`

6. Choose **Save changes**.

### Configure KMS key permissions (if your bucket uses encryption)

If your Amazon S3 bucket uses AWS KMS encryption, complete the following steps.

1. Open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. Choose the KMS key that is used to encrypt your Amazon S3 bucket.
3. Choose **Key policy**, and then choose **Edit**.
4. Add a statement to the key policy with the following structural
   elements:
   - `Sid` – "AllowQuickSuiteKMSAccess"
   - `Effect` – "Allow"
   - `Principal` – AWS ARN for the Amazon Quick Suite service role in your account. For
     example, the principal should look like this:`"Principal": { "AWS":
"arn:aws:iam::<quick_account_id>:role/service-role/aws-quicksight-service-role-v0"
}`
   - `Action` – Array of KMS permissions: kms:Decrypt, kms:DescribeKey
   - `Resource` – "\*" (applies to the current key), the Amazon S3 bucket path should look like
     the following: `"Resource": [
"arn:aws:s3:::bucket_name"]`

5. Choose **Save changes**.
6. Wait 2-3 minutes for the policy changes to propagate.

During the integration setup, you will need to:

- Verify the connection and bucket access.

## Configure VPC access for Amazon S3 Connector in Amazon Quick Suite

VPC permissions ensure Amazon Quick Suite can only access your Amazon S3 bucket through secure VPC or VPC endpoint connections.

### Required policy change

Add this statement to your bucket access policy to allow Amazon Quick Suite to access your bucket through VPC endpoints:

```
{
  "Sid": "Allow-Quick-access"		 	 	 ,
  "Principal": "arn:aws:iam::Quick Account:role/service-role/aws-quicksight-service-role-v0",
  "Action": "s3:*",
  "Effect": "Allow",
  "Resource": [
    "arn:aws:s3:::amzn-s3-demo-bucket",
    "arn:aws:s3:::amzn-s3-demo-bucket/*"
  ],
  "Condition": {
    "Null": {
      "aws:SourceVpce": "false"
    }
  }
}
```

- Replace `amzn-s3-demo-bucket` with your bucket name.
- Replace `Quick Account` with your Amazon Quick Suite account.

The `"aws:SourceVpce": "false"` condition ensures Amazon Quick Suite can only access your bucket through VPC endpoints, maintaining your security requirements.

### Deny policies

If your bucket has a policy that restricts traffic to a specific VPC or VPC endpoint via Deny Policy, this policy needs to be reversed because deny policies take precedence over allow policies.

For example:

```
{
   "Version":"2012-10-17"		 	 	 ,
   "Id": "Policy1415115909152",
   "Statement": [
     {
       "Sid": "Access-to-specific-VPCE-only",
       "Principal": "*",
       "Action": "s3:*",
       "Effect": "Deny",
       "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket",
                    "arn:aws:s3:::amzn-s3-demo-bucket/*"],
       "Condition": {
         "StringNotEquals": {
           "aws:SourceVpce": "vpce-0abcdef1234567890"
         }
       }
     }
   ]
}
```

Should be reversed into:

```
{
   "Version":"2012-10-17"		 	 	 ,
   "Id": "Policy1415115909152",
   "Statement": [
     {
       "Sid": "Access-to-specific-VPCE-only",
       "Principal": "*",
       "Action": "s3:*",
       "Effect": "Allow",
       "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket",
                    "arn:aws:s3:::amzn-s3-demo-bucket/*"],
       "Condition": {
         "StringEquals": {
           "aws:SourceVpce": "vpce-0abcdef1234567890"
         }
       }
     }
   ]
}
```

### Best practices

**Restrict access to your Amazon Quick Suite role**

Access policies should enforce that the caller is your Amazon Quick Suite role ARN or, at minimum, your Amazon Quick Suite account. This ensures that despite allowing VPC traffic, calls come only from expected sources.

### Security recommendations

- Restrict policies to your Amazon Quick Suite role for most secure traffic
- Review your bucket policies regularly to ensure they follow the principle of least privilege

## Set up Amazon S3 integration

After preparing your IAM role and policy configuration, follow these steps to create your Amazon S3 integration:

1. In the Amazon Quick Suite console, choose **Integrations**.
2. Choose **Add** (the plus **+** button).
3. Choose your AWS account option:
   - **Default Account** – Use this option to access Amazon S3 buckets in the same AWS account where Amazon Quick Suite is enabled. This option is selected by default.
   - **Other AWS Account** – Use this option to access Amazon S3 buckets in a different AWS account.

###### Note

If order for **Other AWS Account** to be used, your
adming must enable the feature.

###### Important

Cross-account Amazon S3 access is only supported within the same AWS
region. 4. If you selected **Other AWS Account**, enter the AWS account ID that contains the Amazon S3 bucket. 5. Fill in the integration details:

    * **Name** - Descriptive name for your Amazon S3 integration.
    * **Amazon S3 bucket URL** - The Amazon S3 bucket path containing your documents. Your Amazon S3 bucket should be i the same region as your Amazon Quick Suite region.
    * **Metadata Folder** - Specific folder within the
     bucket (optional).

6. Select **Create and continue**. The system validates your
   configuration. If errors occur, review the error message for specific
   remediation steps. You can use the Amazon S3 policy details specified above and copy them into your S3 bucket.
7. On the **Add files or folders** page, select the files to place in your
   knowledge base. You select the files you want Amazon Quick Suite to sync with using a
   point-and-click experience.
8. Complete the knowledge base details:
   - **Name** - Enter a descriptive name for your knowledge base.
   - **Description** - Describe the purpose of this knowledge base.

9. Select **Create**.

After clicking create, the data sync is started automatically.

## Manage knowledge bases

After setting up your Amazon S3 integration, you can create and manage knowledge bases from your Amazon S3 content.

### Edit existing knowledge bases

You can modify your existing Amazon S3 knowledge bases:

1. In the Amazon Quick Suite console, choose **Knowledge bases**.
2. Select your Amazon S3 knowledge base from the list.
3. Choose the three-dot icon under **Actions**, then choose
   **Edit knowledge base**.
4. Update your configuration settings as needed and choose **Save**.

### Create additional knowledge bases

You can create multiple knowledge bases from the same Amazon S3 integration:

1. In the Amazon Quick Suite console, choose **Integrations**, and
   then select the **Data** tab.
2. Choose your existing Amazon S3 integration from the list.
3. Choose the three-dot icon under **Actions**, then choose
   **Create knowledge base**.
4. Configure your knowledge base settings and choose **Create**.

For detailed information about knowledge base configuration options, see [Common configuration settings](knowledge-base-integrations.md#common-configuration-settings "knowledge-base-integrations.md#common-configuration-settings").

###### Note

Amazon Quick Suite doesn't sync ACLs from data sources. When you create a knowledge base in Amazon Quick Suite,
by default only you can get insights from the knowledge base.
For shared content, you can provide access to different users and groups by updating the knowledge base permissions.

## Adding document metadata in Amazon S3

To customize chat results for your end users, you can add metadata or document attributes to documents in an Amazon S3 bucket by using a metadata file. Metadata is additional information about a document, such as its title and the date and time it was created.

Amazon Quick Suite supports source attribution with citations. If you specify the `_source_uri` metadata field when you add metadata to your Amazon S3 bucket, the source attribution links returned by Amazon Quick Suite in the chat results will direct users to the configured URL. If you don't specify a `_source_uri`, users can still access the source documents through clickable citation links that will download the file at query time. This allows users to verify information even when no source URI is configured.

### Document metadata location

In Amazon S3, each metadata file can be associated with an indexed document. Your metadata files must be stored in the same Amazon S3 bucket as your indexed files. You can specify a location within the Amazon S3 bucket for your metadata files when configuring your Amazon S3 integration in Amazon Quick Suite.

If you don't specify an Amazon S3 prefix, your metadata files must be stored in the same location as your indexed documents. If you specify an Amazon S3 prefix for your metadata files, they must be in a directory structure parallel to your indexed documents. Amazon Quick Suite looks only in the specified directory for your metadata. If the metadata isn't read, check that the directory location matches the location of your metadata.

The following examples show how the indexed document location maps to the metadata file location. The document's Amazon S3 key is appended to the metadata's Amazon S3 prefix and then suffixed with `.metadata.json` to form the metadata file's Amazon S3 path.

###### Note

The combined Amazon S3 key, the metadata's Amazon S3 prefix, and the `.metadata.json` suffix must be no more than a total of 1,024 characters. We recommend that your Amazon S3 key is less than 1,000 characters to account for additional characters when combining your key with the prefix and suffix.

###### Example 1: No metadata path specified

```

Bucket name:
     s3://bucketName
Document path:
     documents
Metadata path:
     none
File mapping
     s3://bucketName/documents/file.txt ->
        s3://bucketName/documents/file.txt.metadata.json

```

###### Example 2: Metadata path specified

```

Bucket name:
     s3://bucketName
Document path:
     documents/legal
Metadata path:
     metadata
File mapping
     s3://bucketName/documents/legal/file.txt ->
        s3://bucketName/metadata/documents/legal/file.txt.metadata.json

```

### Document metadata structure

You define your document metadata itself in a JSON file. The file must be a UTF-8 text file without a BOM marker. The file name of the JSON file must be `<document>.<extension>.metadata.json`. In this example, `document` is the name of the document that the metadata applies to and `extension` is the file extension for the document. The document ID must be unique in `<document>.<extension>.metadata.json`.

The content of the JSON file uses the following template:

```
{
    "DocumentId": "document ID",
    "Attributes": {
        "_authors": ["author of the document"],
        "_category": "document category",
        "_created_at": "ISO 8601 encoded string",
        "_last_updated_at": "ISO 8601 encoded string",
        "_source_uri": "document URI",
        "_version": "file version",
        "_view_count": number of times document has been viewed
    },
    "Title": "document title",
    "ContentType": "PDF | HTML | MS_WORD | PLAIN_TEXT | PPT | RTF | XML | XSLT | MS_EXCEL | CSV | JSON | MD"
}

```

If you provide a metadata path, make sure that directory structure inside the metadata directory exactly matches the directory structure of data file.

For example, if the data file location is at `s3://bucketName/documents/legal/file.txt`, the metadata file location should be at `s3://bucketName/metadata/documents/legal/file.txt.metadata.json`.

All of the attributes and fields are optional, so it's not necessary to include all attributes. However, you must provide a value for each attribute that you want to include; the value can't be empty.

The `_created_at` and `_last_updated_at` metadata fields are ISO 8601 encoded dates. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25, 2012, at 12:30PM (plus 10 seconds) in the Central European Time time zone.

## Troubleshooting Amazon S3 integration issues

If you encounter issues connecting to your Amazon S3 bucket, review the following common causes and solutions.

### Cross-account access not configured

**Issue:** Your administrator hasn't granted access to use Amazon S3 buckets from other AWS accounts in Amazon Quick Suite.

**Solution for administrators:**

1. Navigate to Amazon Quick Suite Admin settings → Manage Amazon Quick Suite → Manage AWS resources.
2. Under **Allow access and autodiscovery for these resources**, choose **Select Amazon S3 Bucket** and enable **Amazon S3 Buckets You Can Access Across AWS**.
3. Select **Choose accessible buckets from AWS account**.

Contact your administrator to confirm cross-account access has been properly configured.

### Bucket not in approved list

If your admin is only allowing certain buckets to be accessed, check with your
admin to make sure your bucket is in the approved list.

**Issue:** The bucket you're trying to access hasn't been authorized by your administrator.

**Solution:**

- Confirm the bucket name is spelled correctly.
- Verify with your administrator that the bucket is included in the approved list.
- Request your administrator to add the bucket to the authorized buckets list if needed.

### Insufficient IAM permissions

**Issue:** Your IAM role or user lacks the necessary permissions to access the Amazon S3 bucket.

**Solution:**

- Verify your IAM policy includes the required Amazon S3 permissions:
  - `s3:GetObject`
  - `s3:ListBucket`
  - `s3:GetBucketLocation`
  - `s3:GetObjectVersion`
  - `s3:ListBucketVersions`

- Check your own buckets for any explicit Deny statements that might be blocking access.

###### Note

The ARN `arn:aws:iam::account-id:role/service-role/aws-quicksight-service-role-v0` is the default service role used when no custom role has been created. If a custom service role exists, contact your administrator to obtain the custom service role ARN and use it instead of the default.

### Cross-region restrictions

**Issue:** The Amazon S3 bucket is located in a different AWS region than your Amazon Quick Suite account or service.

**Solution:**

- Verify the bucket region matches your Amazon Quick Suite service region.
- Check bucket region using AWS CLI: `aws s3api get-bucket-location --bucket bucket-name`
- Use a bucket in the same region as your service.

### Additional troubleshooting steps

- **Test bucket accessibility** using AWS CLI:

```
aws s3 ls s3://bucket-name --profile your-profile
```

- **Review CloudTrail logs** for AccessDenied errors to identify the specific permission issue.
- **Check Amazon S3 Block Public Access settings** - while these typically don't affect authenticated access,
  verify they're not interfering with your specific use case.
- **Verify bucket ownership** - ensure the bucket exists and you have the correct bucket name.

## Limitations

When using Amazon S3 integrations in Amazon Quick Suite, be aware of the following
limitations:

- The Amazon S3 bucket must be in the same AWS Region as your Amazon Quick Suite application.
