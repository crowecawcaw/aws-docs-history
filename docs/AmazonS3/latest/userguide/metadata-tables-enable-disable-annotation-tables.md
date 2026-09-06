

# Enabling or disabling annotation tables
<a name="metadata-tables-enable-disable-annotation-tables"></a>

By default, your metadata table configuration contains a *journal table*, which records the events that occur for the objects in your bucket. The journal table is required for each metadata table configuration. 

Optionally, you can add an *annotation table* to your metadata table configuration. The annotation table tracks all annotations on objects in your bucket so that you can query annotation data at scale.

The annotation table contains the latest annotations for all objects in your bucket. You can use this table to simplify and speed up business workflows and big data jobs by identifying objects based on their annotations. For example, you can query the annotation table to do the following: 
+ Find all objects with a specific annotation key or value.
+ Create a distribution of annotation keys across objects in your bucket.
+ Find all objects that have annotations applied by a specific principal.

If you chose to enable an annotation table for your metadata table configuration, the table goes through a process known as *backfilling*, during which Amazon S3 scans your general purpose bucket to retrieve and populate annotations for all objects that exist in the bucket. Depending on the number of objects in your bucket, this process can take minutes to hours. When the backfilling process is finished, the status of your annotation table changes from **Backfilling** to **Active**. After backfilling is completed, updates to your objects are typically reflected in the annotation table within one hour.

**Note**  
You're charged for backfilling your annotation table. For more information, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/).
You can't pause updates to your annotation table and then resume them. However, you can disable the annotation table configuration. Disabling the annotation table doesn't delete it. The annotation table is retained for your records until you decide to delete it.   
If you've disabled your annotation table and later want to re-enable it, you must first delete the old annotation table from your AWS managed table bucket. When you re-enable the annotation table configuration, Amazon S3 creates a new annotation table, and you're charged again for backfilling the new annotation table.

You can enable or disable annotation tables by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the AWS SDKs, or the Amazon S3 REST API.

**Prerequisites**  
If you've disabled your annotation table and now want to re-enable it, you must first manually delete the old annotation table from your AWS managed table bucket. Otherwise, re-enabling the annotation table fails because an annotation table already exists in the table bucket. To delete your annotation table, see [Delete a metadata table](metadata-tables-delete-table.md#delete-metadata-table-procedure). 

When you re-enable the annotation table configuration, Amazon S3 creates a new annotation table, and you're charged again for backfilling the new annotation table. 

## Annotation table IAM role
<a name="annotation-table-iam-role-section"></a>

The annotation table requires an IAM role that grants Amazon S3 Metadata permission to read annotations from your bucket. Use the following trust and permissions policies when you create this role.

**Trust policy**  
The following trust policy identifies Amazon S3 Metadata as the service principal that can assume the role.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "metadata.s3.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{123456789012}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
                }
            }
        }
    ]
}
```

**Permissions policy**  
The following permissions policy grants the IAM role the minimum permissions required to read annotations.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PermissionForGetAnnotation",
      "Effect": "Allow",
      "Action": [
        "s3:GetObjectAnnotation",
        "s3:GetObjectVersionAnnotation"
      ],
      "Resource": ["arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"]
    },
    {
      "Sid": "PermissionsForListBucket",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:ListBucketVersions"
      ],
      "Resource": ["arn:aws:s3:::{{amzn-s3-demo-bucket}}"]
    },
    {
      "Sid": "PermissionsForDecryptAnnotation",
      "Effect": "Allow",
      "Action": ["kms:Decrypt"],
      "Resource": ["*"]
    }
  ]
}
```

If your objects use SSE-KMS encryption, the `kms:Decrypt` permission covers decryption for the AWS KMS key used to encrypt the objects. You also need `iam:PassRole` permission to assign the role to the annotation table configuration.

## Enable or disable annotation tables
<a name="metadata-tables-enable-disable-annotation-tables-procedure"></a>

### Using the S3 console
<a name="metadata-tables-enable-disable-annotation-tables-console"></a>

**To enable or disable annotation tables**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **General purpose buckets**.

1. Choose the general purpose bucket with the metadata table configuration that you want to enable or disable an annotation table for.

1. On the bucket's details page, choose the **Metadata** tab. 

1. On the **Metadata** tab, choose **Edit**, then choose **Edit annotation table configuration**.

1. On the **Edit annotation table configuration** page, choose **Enabled** or **Disabled** under **Annotation table**.
**Note**  
Before you choose **Enabled**, make sure that you've reviewed and met the [prerequisites](#annotation-table-config-prereqs). 
   + If you chose **Enabled**, under **IAM role**, choose one of the following IAM role selection methods:
     + **Create new IAM role** – Amazon S3 creates a new IAM role with the required permissions for the annotation table.
     + **Choose from existing IAM roles** – Select an existing IAM role from the **IAM role** dropdown. The role must have the required permissions to read annotations from your bucket.
     + **Enter IAM role ARN** – Enter the ARN of an existing IAM role that has the required permissions.

     For more information about the required permissions for the annotation table IAM role, see [Annotation table IAM role](#annotation-table-iam-role-section).

     You can also choose whether to encrypt your table with server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS). By default, annotation tables are encrypted with server-side encryption using Amazon S3 managed keys (SSE-S3).

     If you choose to use SSE-KMS, you must provide a customer managed KMS key in the same Region as your general purpose bucket. 
**Important**  
You can set the encryption type for your metadata tables only during table creation. After an AWS managed table is created, you can't change its encryption setting.
     + To encrypt your annotation table with SSE-S3 (the default), choose **Don't specify encryption type**. 
     + To encrypt your annotation table with SSE-KMS, choose **Specify encryption type**. Under **Encryption type**, choose **Server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS)**. Under **AWS KMS key**, either choose from your existing KMS keys, or enter your KMS key ARN. If you don't already have a KMS key, choose **Enter KMS key ARN**, and then choose **Create a KMS key**.
   + If you chose **Disabled**, under **After the annotation table is disabled, the table will no longer be updated, and updates can't be resumed**, select the checkbox.

1. Choose **Save changes**.

### Using the AWS CLI
<a name="metadata-tables-enable-disable-annotation-tables-cli"></a>

To run the following commands, you must have the AWS CLI installed and configured. If you don't have the AWS CLI installed, see [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.

Alternatively, you can run AWS CLI commands from the console by using AWS CloudShell. AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console. For more information, see [What is CloudShell?](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) and [Getting started with AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/getting-started.html) in the *AWS CloudShell User Guide*.

**To enable or disable annotation tables by using the AWS CLI**

To use the following example commands, replace the `{{user input placeholders}}` with your own information. 
**Note**  
Before enabling an annotation configuration, make sure that you've reviewed and met the [prerequisites](#annotation-table-config-prereqs). 

1. Create a JSON file that contains your annotation table configuration, and save it (for example, `annotation-config.json`). The following is a sample configuration to enable a new annotation table.

   If you're enabling an annotation table, you can optionally specify an encryption configuration. By default, metadata tables are encrypted with server-side encryption using Amazon S3 managed keys (SSE-S3), which you can specify by setting `SseAlgorithm` to `AES256`.

   To encrypt your annotation table with server-side encryption using AWS Key Management Service (AWS KMS) keys (SSE-KMS), set `SseAlgorithm` to `aws:kms`. You must also set `KmsKeyArn` to the ARN of a customer managed KMS key in the same Region where your general purpose bucket is located.

   ```
   {
     "ConfigurationState": "ENABLED",
     "Role": "arn:aws:iam::{{account-id}}:role/{{annotation-table-role}}",
     "EncryptionConfiguration": {
       "SseAlgorithm": "aws:kms",
       "KmsKeyArn": "arn:aws:kms:{{us-east-2}}:{{account-id}}:key/{{key-id}}"
     }
   }
   ```

   The `Role` field is required when enabling an annotation table for the first time or when changing the IAM role. The role must grant Amazon S3 Metadata permission to read annotations from your bucket. For more information, see [Annotation table IAM role](#annotation-table-iam-role-section).

   If you want to disable an existing annotation table, use the following configuration: 

   ```
   {
     "ConfigurationState": "DISABLED"  }
   ```

1. Use the following command to update the annotation table configuration for your general purpose bucket (for example, `{{amzn-s3-demo-bucket}}`):

   ```
   aws s3api update-bucket-metadata-annotation-table-configuration \
   --bucket {{amzn-s3-demo-bucket}} \
   --annotation-table-configuration file://./{{annotation-config}}.json \
   --region {{us-east-2}}
   ```

### Using the REST API
<a name="metadata-tables-enable-disable-annotation-tables-rest-api"></a>

You can send REST requests to enable or disable annotation tables. For more information, see [UpdateBucketMetadataAnnotationTableConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataAnnotationTableConfiguration.html).

### Using the AWS SDKs
<a name="metadata-tables-enable-disable-annotation-tables-sdk"></a>

You can use the AWS SDKs to enable or disable annotation tables in Amazon S3. For information, see the [list of supported SDKs](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataAnnotationTableConfiguration.html#API_UpdateBucketMetadataAnnotationTableConfiguration_SeeAlso).