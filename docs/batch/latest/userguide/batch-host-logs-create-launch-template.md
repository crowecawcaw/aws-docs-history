

# Step 3: Create a launch template and attach it to a compute environment
<a name="batch-host-logs-create-launch-template"></a>

When the instance starts, the user-data script automatically installs Fluent Bit, retrieves the instance ID from IMDSv2, syncs configuration from Amazon S3, and starts the Fluent Bit service. For more information about launch templates, see [Use Amazon EC2 launch templates with AWS Batch](launch-templates.md). For more information about IMDS configuration, see [Instance Metadata Service (IMDS) configuration](imds-compute-environments.md).

For a sample user-data script, see the [companion GitHub repository](https://github.com/aws-samples/sample-batch-host-level-logs). Use the `launch-template-userdata-minimal.txt` file for your launch template. This file excludes comments to reduce user-data size. The `launch-template-userdata.txt` file is a commented version for reference. Replace the following placeholders in the template before use:
+ `<BUCKET_NAME>` – The name of your Amazon S3 bucket.
+ `<FLUENT_BIT_VERSION>` – The Fluent Bit version to install. Leave blank to install the latest available version.
+ [Step 1: Set up the Amazon S3 bucket and Fluent Bit configuration](batch-host-logs-s3-setup.md)
+ [Step 2: Configure IAM permissions on your instance role](batch-host-logs-configure-iam.md)

------
#### [ AWS Console ]

Create the launch template:

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Launch Templates**.

1. Choose **Create launch template**.

1. For **Launch template name**, enter a name such as `{{batch-host-logs}}`.

1. Expand **Advanced details**.

1. For **Metadata version**, choose **V2 only (token required)**.

1. For **Metadata response hop limit**, enter `2`.

1. Scroll to **User data** and paste the user-data script from the [companion GitHub repository](https://github.com/aws-samples/sample-batch-host-level-logs). Replace {{`<BUCKET_NAME>`}} with your bucket name. Replace {{`<FLUENT_BIT_VERSION>`}} with your desired Fluent Bit version, or leave blank for the latest version.

1. Choose **Create launch template**.

Create the compute environment:

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. In the navigation pane, choose **Compute environments**.

1. Choose **Create**.

1. For **Compute environment configuration**, choose **Amazon Elastic Compute Cloud (Amazon EC2)**.

1. For **Orchestration type**, choose **Managed**.

1. For **Name**, enter a name such as `{{my-host-logs-ce}}`.

1. For **Instance role**, choose the instance role you updated or created in Step 2, such as `ecsInstanceRole`.

1. Choose **Next**.

1. Under **Instance configuration**, expand **Launch templates** and select the template you created.

1. Complete the remaining fields and choose **Create compute environment**.

------
#### [ AWS CLI ]

Create the launch template. Save the user-data script from the [companion GitHub repository](https://github.com/aws-samples/sample-batch-host-level-logs) to a file and encode it with base64:

```
aws ec2 create-launch-template \
    --launch-template-name {{batch-host-logs}} \
    --launch-template-data '{
        "MetadataOptions": {
            "HttpTokens": "required",
            "HttpPutResponseHopLimit": 2
        },
        "UserData": "{{BASE64_ENCODED_USER_DATA}}"
    }'
```

Create the compute environment with the launch template:

```
aws batch create-compute-environment \
    --compute-environment-name {{my-host-logs-ce}} \
    --type MANAGED \
    --compute-resources '{
        "type": "EC2",
        "minvCpus": 0,
        "maxvCpus": 256,
        "instanceTypes": ["optimal"],
        "subnets": ["{{subnet-12345678}}"],
        "securityGroupIds": ["{{sg-12345678}}"],
        "instanceRole": "arn:aws:iam::{{111122223333}}:instance-profile/ecsInstanceRole",
        "launchTemplate": {
            "launchTemplateName": "{{batch-host-logs}}",
            "version": "$Latest"
        }
    }'
```

------

**Note**  
The metadata response hop limit is set to `2` in the launch template because applications running in job containers require an extra network hop to reach the IMDSv2 endpoint. Without this setting, IMDSv2 requests from containers fail.