AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Creating and managing an object lifecycle

configuration using the AWS CLI

You can use Amazon S3 Lifecycle to optimize storage capacity for
Amazon S3 compatible storage on Snowball Edge. You can create lifecycle rules to expire objects as they age or are
replaced by newer versions. You can create, enable, disable, or delete a lifecycle
rule. For more information about Amazon S3 Lifecycle, see [Managing your storage
lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md").

###### Note

The AWS account that creates the bucket owns it and is the only one that can
create, enable, disable, or delete a lifecycle rule.

To create and manage a lifecycle configuration for an Amazon S3 compatible storage on Snowball Edge bucket using the
AWS Command Line Interface (AWS CLI), see the following examples.

## PUT a lifecycle configuration on a

Snowball Edge bucket

The following AWS CLI example puts a lifecycle configuration policy on a
Snowball Edge bucket. This policy specifies that all objects that have the
flagged prefix (`myprefix`) and tags expire after 10
days. To use this example, replace each user input placeholder with your own
information.

First, save the lifecycle configuration policy to a JSON file. For this
example, the file is named `lifecycle-example.json`.

```
{
    "Rules": [{
        "ID": "id-1",
        "Filter": {
            "And": {
                "Prefix": "myprefix",
                "Tags": [{
                        "Value": "mytagvalue1",
                        "Key": "mytagkey1"
                    },
                    {
                        "Value": "mytagvalue2",
                        "Key": "mytagkey2"
                    }
                ]
            }
        },
        "Status": "Enabled",
        "Expiration": {
            "Days": 10
        }
    }]
}
```

After you save the file, submit the JSON file as part of the
`put-bucket-lifecycle-configuration` command. To use this
command, replace each user input placeholder with your own information.

###### Example of `put-bucket-lifecycle` command

s3api syntax

```

aws s3api put-bucket-lifecycle-configuration --bucket `example-snow-bucket`  \\
    --lifecycle-configuration file://`lifecycle-example.json` --endpoint-url https://`s3api-endpoint-ip` --profile `your-profile`

```

For more information about this command, see [put-bucket-lifecycle-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-lifecycle-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-lifecycle-configuration.html") in the AWS CLI Command Reference.

s3control syntax

```

aws s3control put-bucket-lifecycle-configuration --bucket `example-snow-bucket` \\
    --lifecycle-configuration file://`lifecycle-example.json` \\
    --endpoint-url https://`s3ctrlapi-endpoint-ip` --profile `your-profile`
```

For more information about this command, see [put-bucket-lifecycle-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-bucket-lifecycle-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-bucket-lifecycle-configuration.html") in the AWS CLI Command Reference.
