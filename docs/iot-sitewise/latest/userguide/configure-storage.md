# Configure storage settings in AWS IoT SiteWise

You can configure storage settings to opt in to service managed warm tier storage,
and also to replicate data to the cold tier. To learn more about the retention period for the warm
and hot tier, see [Data retention impact](#retention-period "#retention-period").
While configuring the storage settings, do the following:

- **Hot tier retention** — Set a retention period for how long your
  data is stored in the hot tier before it's deleted, and moved to the service managed warm
  tier storage or cold tier storage based on your storage settings. AWS IoT SiteWise will delete any
  data in the hot tier that existed before the retention period ends. If you don't set a
  retention period, your data is stored indefinitely in the hot tier.
- **Warm tier retention** — Set a retention period for how long your
  data is stored in the warm tier before it’s deleted from AWS IoT SiteWise storage and moved to the
  customer managed cold tier storage. AWS IoT SiteWise deletes any data from the warm tier that existed before
  the retention period ends. If a retention period is not set, your data is
  stored indefinitely in the warm tier.

###### Note

To improve query performance, set a hot tier retention period with warm tier
storage.

## Impact of data retention in hot and warm tier storage

- When you decrease the retention period of the hot tier storage, data is
  permanently moved from the hot tier to the warm or cold tier. When you decrease the
  retention period of the warm tier, data is moved to the cold tier, and permanently deleted
  from the warm tier.
- When you increase the retention period of the hot or warm tier storage, the
  change affects data that's sent to AWS IoT SiteWise from then on. AWS IoT SiteWise does not retrieve data
  from the warm or cold storage to populate the hot tier. For example, if the retention
  period of the hot tier storage is initially set for 30 days and then increased to 60
  days, it takes 30 days for the hot tier storage to contain 60 days worth of data.

###### Topics

- [Configure storage settings for warm tier
  (console)](#configure-storage-console-warm "#configure-storage-console-warm")
- [Configure storage settings for warm tier (AWS CLI)](#configure-storage-cli-warm "#configure-storage-cli-warm")
- [Configure storage settings for cold tier (console)](#configure-storage-console "#configure-storage-console")
- [Configure storage settings for cold tier (AWS CLI)](#configure-storage-cli "#configure-storage-cli")

## Configure storage settings for warm tier

(console)

The following procedure shows you how to configure the storage settings to replicate data
to the warm tier in the AWS IoT SiteWise console.

###### To configure storage settings in the console

1.  Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2.  In the navigation pane, under **Settings**, choose
    **Storage**.
3.  In the upper-right corner, choose **Edit**.
4.  On the **Edit storage** page, do the following:
5.  For **Hot tier settings**, do the following:

        * If you want to set a retention period for how long your data is stored in the hot tier before it's deleted,
         and moved to the service managed warm tier storage, choose **Enable retention period**.
        * To configure a retention period, enter a whole number and choose a unit. The retention period must be greater than or equal to 30 days.

    AWS IoT SiteWise deletes any data in the hot tier that's older than the retention period.
    If you don't set a retention period, your data is stored indefinitely.

6.  (Recommended) For **Warm tier settings**, do the following:

        * To opt in to warm tier storage, select **I confirm to the opt-in of
         warm tier storage** to opt in for the warm tier storage.
        * (Optional) To configure a retention period, enter a whole number and choose a unit.
         The retention period must be greater than or equal to 365 days.

    AWS IoT SiteWise deletes data in the warm tier that existed earlier than the retention
    period. If you don't set a retention period, your data is stored indefinitely.

###### Note

    * When you opt in for warm tier, the configuration displays once only.
    * To set hot tier retention, you must have either warm or cold tier storage. For
     cost efficiency and historical data retrieval, AWS IoT SiteWise recommends that you store
     long term data in the warm tier.
    * To set warm tier retention, you must have cold tier storage.

7. Choose **Save** to save your storage settings.

In the **AWS IoT SiteWise storage** section, the
**Warm tier storage** is in one of these states:

- **Enabled** – If your data existed before the hot tier retention period, AWS IoT SiteWise
  moves the data to the warm tier."
- **Disabled** – The warm tier storage is disabled.

## Configure storage settings for warm tier (AWS CLI)

You can configure storage settings to move data to the warm tier by using the AWS CLI and
the following commands.

To prevent overriding the existing configuration, retrieve the current storage
configuration information by running the following command:

```
aws iotsitewise describe-storage-configuration
```

###### Example response without existing cold tier configuration

```
{
          "storageType": "SITEWISE_DEFAULT_STORAGE",
          "disassociatedDataStorage": "ENABLED",
          "configurationStatus": {
              "state": "ACTIVE"
          },
          "lastUpdateDate": "2021-10-14T15:53:35-07:00",
          "warmTier": "DISABLED"
}
```

###### Example response with existing cold tier configuration

```
{
      "storageType": "MULTI_LAYER_STORAGE",
          "multiLayerStorage": {
            "customerManagedS3Storage": {
            "s3ResourceArn": "arn:aws:s3:::amzn-s3-demo-bucket/prefix/",
            "roleArn": "arn:aws:iam::aws-account-id:role/role-name"
            }
          },
      "disassociatedDataStorage": "ENABLED",
      "retentionPeriod": {
      "numberOfDays": `retention-in-days`
      },
       "configurationStatus": {
       "state": "ACTIVE"
      },
      "lastUpdateDate": "2023-10-25T15:59:46-07:00",
      "warmTier": "DISABLED"
}
```

### Configure storage settings for warm tier

with AWS CLI

Run the following command to configure the storage settings. Replace
`file-name` with the name of the file that contains the AWS IoT SiteWise storage
configuration.

```
aws iotsitewise put-storage-configuration --cli-input-json file://file-name.json
```

###### Example AWS IoT SiteWise configuration with hot and warm tier

```
{
             "storageType": "SITEWISE_DEFAULT_STORAGE",
             "disassociatedDataStorage": "ENABLED",
             "warmTier": "ENABLED",
             "retentionPeriod": {
                "numberOfDays": `hot-tier-retention-in-days`
              }

}
```

`hot-tier-retention-in-days` must be a whole number greater than or equal
to 30 days.

###### Example response

```
{
             "storageType": "SITEWISE_DEFAULT_STORAGE",
             "configurationStatus": {
             "state": "UPDATE_IN_PROGRESS"
             }
}
```

If you have cold tier storage enabled, see [Configure storage settings with
AWS CLI and existing cold tier](#configure-storage-cli-existing-cold "#configure-storage-cli-existing-cold").

### Configure storage settings with

AWS CLI and existing cold tier

###### Configure storage settings using AWS CLI with existing cold tier storage

- Run the following command to configure the storage settings. Replace
  `file-name` with the name of the file that contains the
  AWS IoT SiteWise storage configuration.

```
aws iotsitewise put-storage-configuration --cli-input-json file://`file-name`.json
```

###### Example AWS IoT SiteWise storage configuration

    + Replace `amzn-s3-demo-bucket` with your Amazon S3 bucket
     name.
    + Replace `prefix` with your Amazon S3 prefix.
    + Replace `aws-account-id` with your AWS account
     ID.
    + Replace `role-name` with the name of the Amazon S3 access
     role that allows AWS IoT SiteWise to send data to Amazon S3.
    + Replace `hot-tier-retention-in-days` with a whole
     number greater than or equal to 30 days.
    + Replace `warm-tier-retention-in-days` with a whole
     number greater than or equal to 365 days.###### Note

AWS IoT SiteWise will delete any data in the warm tier that's older than the retention
period of the cold tier. If you don't set a retention period, your data is stored
indefinitely.

```
{
      "storageType": "MULTI_LAYER_STORAGE",
        "multiLayerStorage": {
          "customerManagedS3Storage": {
              "s3ResourceArn": "arn:aws:s3:::amzn-s3-demo-bucket/prefix/",
              "roleArn": "arn:aws:iam::aws-account-id:role/role-name"
              }
          },
    "disassociatedDataStorage": "ENABLED",
    "retentionPeriod": {
      "numberOfDays": `hot-tier-retention-in-days`
    },
    "warmTier": "ENABLED",
    "warmTierRetentionPeriod": {
      "numberOfDays": `warm-tier-retention-in-days`
    }
}
```

###### Example response

```
{
      "storageType": "MULTI_LAYER_STORAGE",
      "configurationStatus": {
        "state": "UPDATE_IN_PROGRESS"
       }
}
```

## Configure storage settings for cold tier (console)

The following procedure shows you how to configure the storage settings to replicate data
to the cold tier in the AWS IoT SiteWise console.

###### To configure storage settings in the console

1.  Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2.  In the navigation pane, under **Settings**, choose
    **Storage**.
3.  In the upper-right corner, choose **Edit**.
4.  On the **Edit storage** page, do the following:
    1. For **Storage settings**, choose
       **Enable cold tier storage**. The cold tier storage is
       disabled by default.
    2. For **S3 bucket location**, enter the name of an existing
       Amazon S3 bucket and a prefix.

    ###### Note

        * Amazon S3 uses the prefix as a folder name in the Amazon S3 bucket. The prefix
         must have 1-255 characters and end with a forward slash (/). Your AWS IoT SiteWise
         data is saved in this folder.
        * If you don't have an Amazon S3 bucket, choose **View**, and
         then create one in the Amazon S3 console. For more information, see [Create your first S3 bucket](../../../AmazonS3/latest/userguide/GetStartedWithS3.md#creating-bucket "../../../AmazonS3/latest/userguide/GetStartedWithS3.md#creating-bucket")
         in the *Amazon S3 User Guide*.

    3.  For **S3 access role**, do one of the following:
        - Choose **Create a role from an AWS managed template**,
          AWS automatically creates an IAM role that allows AWS IoT SiteWise to send data to
          Amazon S3.
        - Choose **Use an existing role**, and then choose the role
          that you created from the list.

        ###### Note

            + You must use the same Amazon S3 bucket name for the **S3 bucket
             location** that you used in the previous step and in your
             IAM policy.
            + Make sure that your role has the permissions shown in the following
             example.


            ###### Example permissions policy:


            JSON





            ```
            `{
             "Version":"2012-10-17",
             "Statement": [
             {
             "Effect": "Allow",
             "Action": [
             "s3:PutObject",
             "s3:GetObject",
             "s3:DeleteObject",
             "s3:GetBucketLocation",
             "s3:ListBucket"
             ],
             "Resource": [
             "arn:aws:s3:::amzn-s3-demo-bucket",
             "arn:aws:s3:::amzn-s3-demo-bucket/*"
             ]
             }
             ]
             }`

            ```




            Replace amzn-s3-demo-bucket with the name of
             your Amazon S3 bucket.
            + If the Amazon S3 bucket is encrypted using a customer managed KMS key,
             the KMS key must have an access policy with an IAM role for `kms:Decrypt` and `kms:GenerateDataKey` operations.

    4.  To setup hot tier, see Step 5 in [Configure storage settings for warm tier
        (console)](#configure-storage-console-warm "#configure-storage-console-warm").
    5.  (Optional) For **AWS IoT Analytics integration**, do the following.

    ###### Note

    End of support notice: On December 15, 2025, AWS
    will end support for AWS IoT Analytics. After December 15, 2025, you will no longer be able to access the AWS IoT Analytics console or AWS IoT Analytics resources. For more information, see [AWS IoT Analytics end of support](../../../iotanalytics/latest/userguide/iotanalytics-end-of-support.md "../../../iotanalytics/latest/userguide/iotanalytics-end-of-support.md").

        1. If you want to use AWS IoT Analytics to query your data, choose
         **Enabled AWS IoT Analytics data store**.
        2. AWS IoT SiteWise generates a name for your data store or you can enter a different
         name.AWS IoT SiteWise automatically creates a data store in AWS IoT Analytics to save your data. To query

    the data, you can use AWS IoT Analytics to create datasets. For more information, see [Working with AWS IoT SiteWise data](../../../iotanalytics/latest/userguide/dataset-itsw.md "../../../iotanalytics/latest/userguide/dataset-itsw.md") in the
    _AWS IoT Analytics User Guide_. 6. Choose **Save**.

In the **AWS IoT SiteWise storage** section, the
**Cold tier storage** can be one of the following values:

- **Enabled** – AWS IoT SiteWise replicates your data to the specified
  Amazon S3 bucket.
- **Enabling** – AWS IoT SiteWise is processing your request to enable the cold tier storage.
  This process can take several minutes to complete.
- **Enable_Failed** – AWS IoT SiteWise couldn't process your request to enable the cold tier storage.
  If you enabled AWS IoT SiteWise to send logs to Amazon CloudWatch Logs, you can use these logs to
  troubleshoot issues. For more information, see [Monitor with Amazon CloudWatch Logs](monitor-cloudwatch-logs.md "monitor-cloudwatch-logs.md").
- **Disabled** – The cold tier storage is disabled.

## Configure storage settings for cold tier (AWS CLI)

The following procedure shows you how to configure the storage settings to replicate data
to the cold tier using AWS CLI.

###### To configure storage settings using AWS CLI

1. To export data to an Amazon S3 bucket in your account, run the following command to
   configure the storage settings. Replace `file-name` with the
   name of the file that contains the AWS IoT SiteWise storage configuration.

```
aws iotsitewise put-storage-configuration --cli-input-json file://`file-name`.json
```

###### Example AWS IoT SiteWise storage configuration

    * Replace `amzn-s3-demo-bucket` with your Amazon S3 bucket
     name.
    * Replace `prefix` with your Amazon S3 prefix.
    * Replace `aws-account-id` with your AWS account
     ID.
    * Replace `role-name` with the name of the Amazon S3
     access role that allows AWS IoT SiteWise to send data to Amazon S3.
    * Replace `retention-in-days` with a whole number than is greater than
     or equal to 30 days.

```
{
      "storageType": "MULTI_LAYER_STORAGE",
      "multiLayerStorage": {
          "customerManagedS3Storage": {
              "s3ResourceArn": "arn:aws:s3:::amzn-s3-demo-bucket/`prefix`/",
              "roleArn": "arn:aws:iam::`aws-account-id`:role/`role-name`"
          }
      },
      "retentionPeriod": {
          "numberOfDays": `retention-in-days`,
          "unlimited": false
      }
  }
```

###### Note

    * You must use the same Amazon S3 bucket name in the AWS IoT SiteWise storage configuration
     and IAM policy.
    * Make sure that your role has the permissions shown in the following
     example.


    ###### Example permissions policy:


    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Action": [
     "s3:PutObject",
     "s3:GetObject",
     "s3:DeleteObject",
     "s3:GetBucketLocation",
     "s3:ListBucket"
     ],
     "Resource": [
     "arn:aws:s3:::amzn-s3-demo-bucket",
     "arn:aws:s3:::amzn-s3-demo-bucket/*"
     ]
     }
     ]
     }`

    ```




    Replace amzn-s3-demo-bucket with the name of your Amazon S3
     bucket.
    * If the Amazon S3 bucket is encrypted using a customer managed KMS key,
     the KMS key must have an access policy with an IAM role for `kms:Decrypt` and `kms:GenerateDataKey` operations.

###### Example response

```
{
    "storageType": "MULTI_LAYER_STORAGE",
    "retentionPeriod": {
        "numberOfDays": 100,
        "unlimited": false
    },
    "configurationStatus": {
        "state": "UPDATE_IN_PROGRESS"
    }
}
```

###### Note

It can take a few minutes for AWS IoT SiteWise to update the storage configuration. 2. To retrieve the storage configuration information, run the following
command.

```
aws iotsitewise describe-storage-configuration
```

###### Example response

```
{
      "storageType": "MULTI_LAYER_STORAGE",
      "multiLayerStorage": {
          "customerManagedS3Storage": {
              "s3ResourceArn": "arn:aws:s3:::amzn-s3-demo-bucket/torque/",
              "roleArn": "arn:aws:iam::123456789012:role/SWAccessS3Role"
          }
      },
      "retentionPeriod": {
          "numberOfDays": 100,
          "unlimited": false
      },
      "configurationStatus": {
          "state": "ACTIVE"
      },
      "lastUpdateDate": "2021-03-30T15:54:14-07:00"
  }
```

3. To stop exporting data to the Amazon S3 bucket, run the following command to configure
   storage settings.

```
aws iotsitewise put-storage-configuration --storage-type SITEWISE_DEFAULT_STORAGE
```

###### Note

By default, your data is only stored in the hot tier of AWS IoT SiteWise.

###### Example response

```
{
      "storageType": "SITEWISE_DEFAULT_STORAGE",
      "configurationStatus": {
          "state": "UPDATE_IN_PROGRESS"
      }
  }
```

4. To retrieve the storage configuration information, run the following
   command.

```
aws iotsitewise describe-storage-configuration
```

###### Example response

```
{
      "storageType": "SITEWISE_DEFAULT_STORAGE",
      "configurationStatus": {
          "state": "ACTIVE"
      },
      "lastUpdateDate": "2021-03-30T15:57:14-07:00"
  }
```

### (Optional) Create an AWS IoT Analytics data store

(AWS CLI)

###### Note

End of support notice: On December 15, 2025, AWS
will end support for AWS IoT Analytics. After December 15, 2025, you will no longer be able to access the AWS IoT Analytics console or AWS IoT Analytics resources. For more information, see [AWS IoT Analytics end of support](../../../iotanalytics/latest/userguide/iotanalytics-end-of-support.md "../../../iotanalytics/latest/userguide/iotanalytics-end-of-support.md").

An AWS IoT Analytics data store is a scalable and queryable repository that receives and stores
data. You can use the AWS IoT SiteWise console or AWS IoT Analytics APIs to create an AWS IoT Analytics data store to save
your AWS IoT SiteWise data. To query the data, you create datasets by using AWS IoT Analytics. For more
information, see [Working with AWS IoT SiteWise
data](../../../iotanalytics/latest/userguide/dataset-itsw.md "../../../iotanalytics/latest/userguide/dataset-itsw.md") in the _AWS IoT Analytics User Guide_.

The following steps use AWS CLI to create a data store in AWS IoT Analytics.

To create a data store, run the following command. Replace
`file-name` with the name of the file that contains the data
store configuration.

```
aws iotanalytics create-datastore --cli-input-json file://`file-name`.json
```

###### Note

- You must specify the name of an existing Amazon S3 bucket. If you don't have an Amazon S3
  bucket, create one first. For more information, see [Create your first S3 bucket](../../../AmazonS3/latest/userguide/GetStartedWithS3.md#creating-bucket "../../../AmazonS3/latest/userguide/GetStartedWithS3.md#creating-bucket") in the
  _Amazon S3 User Guide_.
- You must use the same Amazon S3 bucket name in the AWS IoT SiteWise storage configuration,
  IAM policy, and AWS IoT Analytics data store configuration.

###### Example AWS IoT Analytics data store configuration

Replace `data-store-name` and
`amzn-s3-demo-bucket` with your AWS IoT Analytics data store name and Amazon S3
bucket name.

```
{
      "datastoreName": "`data-store-name`",
      "datastoreStorage": {
          "iotSiteWiseMultiLayerStorage": {
              "customerManagedS3Storage": {
                  "bucket": "`amzn-s3-demo-bucket`"
              }
          }
      },
      "retentionPeriod": {
          "numberOfDays": 90
      }
  }
```

###### Example response

```
{
      "datastoreName": "datastore_IoTSiteWise_demo",
      "datastoreArn": "arn:aws:iotanalytics:us-west-2:123456789012:datastore/datastore_IoTSiteWise_demo",
      "retentionPeriod": {
          "numberOfDays": 90,
          "unlimited": false
      }
  }
```
