# Helper files for using Amazon S3 Storage Lens

Use the following JSON files and its key inputs for your examples.


## S3 Storage Lens example configuration in JSON


###### Example `config.json`

The `config.json` file contains the details of a S3 Storage Lens
 Organizations-level *advanced metrics and recommendations* configuration. To use the following
 example, replace the ``user input placeholders`` with
 your own information.

###### Note

Additional charges apply for advanced metrics and recommendations. For more information, see [advanced metrics and recommendations](storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection "storage_lens_basics_metrics_recommendations.md#storage_lens_basics_metrics_selection").


```
{
  "Id": "`SampleS3StorageLensConfiguration`", //Use this property to identify your S3 Storage Lens configuration.
  "AwsOrg": { //Use this property when enabling S3 Storage Lens for AWS Organizations.
    "Arn": "arn:aws:organizations::`123456789012`:organization/`o-abcdefgh`"
  },
  "AccountLevel": {
    "ActivityMetrics": {
      "IsEnabled":`true`
    },
    "AdvancedCostOptimizationMetrics": {
      "IsEnabled":`true`
    },
    "AdvancedDataProtectionMetrics": {
      "IsEnabled":`true`
    },
    "DetailedStatusCodesMetrics": {
      "IsEnabled":`true`
    },
    "BucketLevel": {
      "ActivityMetrics": {
        "IsEnabled":`true`
      },
      "AdvancedDataProtectionMetrics": {
      "IsEnabled":`true`
      },
      "AdvancedCostOptimizationMetrics": {
        "IsEnabled":`true`
      },
      "DetailedStatusCodesMetrics": {
        "IsEnabled":`true`
      },
      "PrefixLevel":{
        "StorageMetrics":{
          "IsEnabled":`true`,
          "SelectionCriteria":{
            "MaxDepth":`5`,
            "MinStorageBytesPercentage":`1.25`,
            "Delimiter":"`/`"
          }
        }
      }
    }
  },
  "Exclude": { //Replace with "Include" if you prefer to include Regions.
    "Regions": [
      "`eu-west-1`"
    ],
    "Buckets": [ //This attribute is not supported for AWS Organizations-level configurations.
      "arn:aws:s3:::``amzn-s3-demo-source-bucket``"
    ]
  },
  "IsEnabled": true, //Whether the configuration is enabled
  "DataExport": { //Details about the metrics export
    "S3BucketDestination": {
      "OutputSchemaVersion": "`V_1`",
      "Format": "`CSV`", //You can add "Parquet" if you prefer.
      "AccountId": "`111122223333`",
      "Arn": "arn:aws:s3:::``amzn-s3-demo-destination-bucket``", // The destination bucket for your metrics export must be in the same Region as your S3 Storage Lens configuration. 
      "Prefix": "`prefix-for-your-export-destination`",
      "Encryption": {
        "SSES3": {}
      }
    },
    "CloudWatchMetrics": {
      "IsEnabled": `true`
    }
  }
}
```

## S3 Storage Lens example configuration with Storage Lens groups in JSON


###### Example `config.json`


The `config.json` file contains the details that you want to apply to your
 Storage Lens configuration when using Storage Lens groups. To use the example, replace the ``user
 input placeholders`` with your own information.


To attach all Storage Lens groups to your dashboard, update your Storage Lens
 configuration with the following syntax:



```
{
  "Id": "ExampleS3StorageLensConfiguration",
  "AccountLevel": {
    "ActivityMetrics": {
      "IsEnabled":`true`
    },
    "AdvancedCostOptimizationMetrics": {
      "IsEnabled":`true`
    },
    "AdvancedDataProtectionMetrics": {
      "IsEnabled":true
    },
    "BucketLevel": {
      "ActivityMetrics": {
      "IsEnabled":`true`
      },
    "StorageLensGroupLevel": {},
  "IsEnabled": `true`
}
```

To include only two Storage Lens groups in your Storage Lens dashboard configuration
 (`slg-1` and `slg-2`), use the following
 syntax:



```
{
  "Id": "`ExampleS3StorageLensConfiguration`",
  "AccountLevel": {
    "ActivityMetrics": {
      "IsEnabled":`true`
    },
    "AdvancedCostOptimizationMetrics": {
      "IsEnabled":`true`
    },
    "AdvancedDataProtectionMetrics": {
      "IsEnabled":`true`
    },
    "BucketLevel": {
      "ActivityMetrics": {
      "IsEnabled":`true`
      },
   "StorageLensGroupLevel": {
        "SelectionCriteria": {
            "Include": [
                "arn:aws:s3:`us-east-1`:`111122223333`:storage-lens-group/`slg-1`",
                "arn:aws:s3:`us-east-1`:`444455556666`:storage-lens-group/`slg-2`"
            ]
    },
  "IsEnabled": `true`
}
```

To exclude only certain Storage Lens groups from being attached to your dashboard
 configuration, use the following syntax:



```
{
  "Id": "`ExampleS3StorageLensConfiguration`",
  "AccountLevel": {
    "ActivityMetrics": {
      "IsEnabled":`true`
    },
    "AdvancedCostOptimizationMetrics": {
      "IsEnabled":`true`
    },
    "AdvancedDataProtectionMetrics": {
      "IsEnabled":`true`
    },
    "BucketLevel": {
      "ActivityMetrics": {
      "IsEnabled":`true`
      },
   "StorageLensGroupLevel": {
        "SelectionCriteria": {
            "Exclude": [
                "arn:aws:s3:`us-east-1`:`111122223333`:storage-lens-group/`slg-1`",
                "arn:aws:s3:`us-east-1`:`444455556666`:storage-lens-group/`slg-2`"
            ]
    },
  "IsEnabled": `true`
}
```

## S3 Storage Lens example tags configuration in JSON


###### Example `tags.json`

The `tags.json` file contains the tags that you want to apply to your
 S3 Storage Lens configuration. To use this example, replace the ``user input
 placeholders`` with your own information.


```
[
    {
        "Key": "`key1`",
        "Value": "`value1`"
    },
    {
        "Key": "`key2`",
        "Value": "`value2`"
    }
]
```

## S3 Storage Lens example
 configuration IAM permissions


###### Example `permissions.json` – Specific dashboard name

This example policy shows an S3 Storage Lens IAM `permissions.json` file
 with a specific dashboard name specified. Replace
 ``value1``,
 ``us-east-1``,
 ``your-dashboard-name``, and
 ``example-account-id`` with your own
 values.


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetStorageLensConfiguration",
 "s3:DeleteStorageLensConfiguration",
 "s3:PutStorageLensConfiguration"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/key1": "`value1`"
 }
 },
 "Resource": "arn:aws:s3:`us-east-1`:`111122223333`:storage-lens/`your-dashboard-name`"
 }
 ]
}`

```





###### Example `permissions.json` – No specific dashboard name

This example policy shows an S3 Storage Lens IAM `permissions.json` file
 without a specific dashboard name specified. Replace
 ``value1``,
 ``us-east-1``, and
 ``example-account-id`` with your own
 values.


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetStorageLensConfiguration",
 "s3:DeleteStorageLensConfiguration",
 "s3:PutStorageLensConfiguration"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/key1": "`value1`"
 }
 },
 "Resource": "arn:aws:s3:`us-east-1`:`111122223333`:storage-lens/*"
 }
 ]
}`

```
