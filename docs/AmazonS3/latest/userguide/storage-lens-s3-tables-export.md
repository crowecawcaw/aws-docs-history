# Exporting S3 Storage Lens metrics to S3 Tables

You can configure Amazon S3 Storage Lens to export your storage analytics and insights to S3 Tables. When you enable S3 Tables export, your metrics are automatically stored in read-only Apache Iceberg tables in the AWS-managed `aws-s3` table bucket, making them queryable using SQL with AWS analytics services like Amazon Athena, Amazon Redshift, and Amazon EMR.

###### Note

There is no additional charge for exporting S3 Storage Lens metrics to AWS-managed S3 Tables. Standard charges apply for table storage, table management, and requests on the tables. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing "https://aws.amazon.com/s3/pricing").

## Enable S3 Tables export using the console

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Storage Lens**, and then choose **Storage Lens Dashboards**.
3. In **Storage Lens Dashboards** list, choose the dashboard that you want to edit.
4. Choose **Edit**.
5. On the **Dashboard** page, navigate to **Metrics export and publishing** section.
6. To enable Table Export for **Default metrics report**, select **Table bucket** in the Bucket type.
7. To enable Table Export for **Expanded prefixes metrics report**, select **Table bucket** in the Bucket type.
8. Review dashboard config and choose **Submit**.

###### Note

After you enable S3 Tables export, it can take up to 48 hours for the first data to be available in the tables.

###### Note

There is no additional charge for exporting S3 Storage Lens metrics to AWS-managed S3 Tables. Standard charges apply for table storage, table management, requests on the tables, and monitoring. You can enable or disable export to S3 Tables by using the Amazon S3 console, Amazon S3 API, the AWS CLI, or AWS SDKs.

###### Note

By default, records in your S3 tables don't expire. To help minimize storage costs for your tables, you can enable and configure record expiration for the tables. With this option, Amazon S3 automatically removes records from a table when the records expire. For more information, see [Record expiration for tables](s3-tables-record-expiration.md "s3-tables-record-expiration.md").

## Enable S3 Tables export using the AWS CLI

###### Note

Before running the following commands, make sure that you have an up to date CLI version. See [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

The following example enables S3 Tables export for an S3 Storage Lens configuration "Default metrics report" using the AWS CLI. To use this example, replace the `user input placeholders` with your own information.

```
aws s3control put-storage-lens-configuration --account-id=`555555555555` --config-id=`your-configuration-id` --storage-lens-configuration '{
   "Id":"`your-configuration-id`",
   "AccountLevel":{
      "ActivityMetrics":{
        "IsEnabled":true
      },
      "BucketLevel":{
         "ActivityMetrics":{
            "IsEnabled":true
         }
      }
   },
   "DataExport":{
      "S3BucketDestination":{
         "OutputSchemaVersion":"V_1",
         "Format":"CSV",
         "AccountId":"`555555555555`",
         "Arn":"`arn:aws:s3:::my-export-bucket`",
         "Prefix":"`storage-lens-exports/`"
      },
      "StorageLensTableDestination":{
         "IsEnabled":true
      }
   },
   "IsEnabled":true
}'

```

## Enable S3 Tables export using the AWS SDKs

The following example enables S3 Tables export for an S3 Storage Lens configuration "Default metrics report" using the AWS SDK for Python (Boto3). To use this example, replace the `user input placeholders` with your own information.

```
import boto3

s3control = boto3.client('s3control')

response = s3control.put_storage_lens_configuration( AccountId='`555555555555`', ConfigId='`your-configuration-id`', StorageLensConfiguration={
        'Id': '`your-configuration-id`',
        'AccountLevel': {
            'ActivityMetrics': {
              'IsEnabled': True
            },
            'BucketLevel': {
                'ActivityMetrics': {
                    'IsEnabled': True
                }
            }
        },
        'DataExport': {
            'S3BucketDestination': {
                'OutputSchemaVersion': 'V_1',
                'Format': 'CSV',
                'AccountId': '`555555555555`',
                'Arn': '`arn:aws:s3:::my-export-bucket`',
                'Prefix': '`storage-lens-exports/`'
            },
            'StorageLensTableDestination': {
                'IsEnabled': True
            }
        },
        'IsEnabled': True
    }
)

```

For more information about using the AWS SDKs, see [AWS SDKs and tools](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").

## Next steps

After enabling S3 Tables export, you can:

- Learn about [Table naming for S3 Storage Lens export to S3 Tables](storage-lens-s3-tables-naming.md "storage-lens-s3-tables-naming.md")
- Learn about [Understanding S3 Storage Lens table schemas](storage-lens-s3-tables-schemas.md "storage-lens-s3-tables-schemas.md")
