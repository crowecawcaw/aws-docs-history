

# Viewing details about an Amazon S3 table
<a name="s3-tables-table-details"></a>

You can view the general details of a table in a table bucket, such creation details, format and type, in the console or programmatically. You can view table encryption settings, and maintenance settings programmatically by using the S3 Tables REST API, AWS CLI or AWS SDKs.

## Viewing table details
<a name="table-details-view"></a>

### Using the AWS CLI
<a name="table-details-CLI"></a>

This example shows how to get details about a table by using the AWS CLI. To use this example, replace the {{user input placeholders}} with your own information.

```
aws s3tables get-table --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/amzn-s3-demo-table-bucket --namespace {{my-namespace}} --name {{my-table}}
```

### Using the S3 console
<a name="table-details-console"></a>

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Table buckets**.

1. Select your table bucket, then select your table.

1. Select the **Properties** tab.

1. (Optional) For information about the permission policy attached to the table, select **Permissions**.

## Previewing table data
<a name="table-preview-data"></a>

### Using the S3 console
<a name="table-preview-data-console"></a>

You can preview the data in your table directly from the Amazon S3 console using the following procedure.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the left navigation pane, choose **Table buckets**.

1. On the **Table buckets** page, choose the bucket that contains the table that you want to query.

1. Select the table you want to preview then, choose **Preview**.

**Note**  
The preview shows the first 10 rows and up to 25 columns of your table. Tables over 50mb cannot be previewed.

## Encryption details
<a name="table-encryption-view"></a>

For more information about table bucket encryption, see [Using server-side encryption with AWS KMS keys (SSE-KMS) in table buckets](s3-tables-kms-encryption.md).

### Using the AWS CLI
<a name="table-encryption-view-CLI"></a>

This example shows how to get details about encryption settings for a table by using the AWS CLI. To use this example, replace the {{user input placeholders}} with your own information.

```
aws s3tables get-table-encryption --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/amzn-s3-demo-table-bucket --namespace {{my-namespace}} --name {{my-table}}
```

## Maintenance details
<a name="table-maintenance-view"></a>

For information about maintenance settings, see [Maintenance for table buckets](s3-table-buckets-maintenance.md) 

### Using the AWS CLI
<a name="table-maintenance-view-CLI"></a>

This example shows how to get details about maintenance configuration settings for a table by using the AWS CLI. To use this example, replace the {{user input placeholders}} with your own information.

```
aws s3tables get-table-maintenance-configuration --table-bucket-arn arn:aws:s3tables:{{us-east-1}}:{{111122223333}}:bucket/amzn-s3-demo-table-bucket --namespace {{my-namespace}} --name {{my-table}}
```