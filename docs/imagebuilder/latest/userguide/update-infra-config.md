

# Update an infrastructure configuration
<a name="update-infra-config"></a>

This section covers how to update an infrastructure configuration resource. You can use the Image Builder console, **imagebuilder** commands in the AWS CLI, or AWS Tools for PowerShell. To track your resources, you can apply tags as follows. Enter tags as key-value pairs.
+ *Resource tags* assign metadata tags to the Amazon EC2 instance that Image Builder launches during the build process.
+ *Tags* assign metadata tags to the infrastructure configuration resource that Image Builder creates as output.

**Note**  
We recommend that you configure all EC2 instances that Image Builder launches from a pipeline build to use IMDSv2 so that instance metadata retrieval requests require a signed token header.

------
#### [ Console ]

You can edit the following infrastructure configuration details from the Image Builder console:
+ The **Description** for your infrastructure configuration.
+ The **IAM role** to associate with the instance profile.
+ **AWS infrastructure**, including the **Instance type** and an **SNS topic** for notifications.
+ **VPC, subnet, and security groups**.
+ **Troubleshooting settings**, including **Terminate instance on failure**, the **Key pair** for connecting, and an optional S3 bucket location for instance logs.

To update an infrastructure configuration resource from the Image Builder console, follow these steps:

**Choose an existing Image Builder infrastructure configuration**

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. To see a list of the infrastructure configuration resources under your account, choose **Infrastructure configuration** from the navigation pane.

1. To view details or edit an infrastructure configuration, choose the **Configuration name** link. This opens the detail view for the infrastructure configuration.
**Note**  
You can also select the check box next to the **Configuration name**, then choose **View detail**.

1. From the upper right corner of the **Infrastructure details** panel, choose **Edit** .

1. When you're ready to save updates you've made to your infrastructure configuration, choose **Save changes**.

------
#### [ AWS CLI ]

The following example shows how to update the infrastructure configuration for your image with the Image Builder [update-infrastructure-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-infrastructure-configuration.html) command in the AWS CLI.

1. 

**Create a CLI input JSON file**

   This example is based on the first example in [Create an infrastructure configuration](create-infra-config.md). It sets `terminateInstanceOnFailure` to `true`, so pipelines that use this infrastructure configuration terminate the build and test instances when a build fails.

   The following example sets common infrastructure fields. To require IMDSv2 tokens on the build and test instances, add an `instanceMetadataOptions` block with `httpTokens` set to `required`.

   Use a file editing tool to create a JSON file with keys shown in the following example, plus values that are valid for your environment. This example uses a file named `update-infrastructure-configuration.json`:

   ```
   {
       "infrastructureConfigurationArn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:infrastructure-configuration/{{my-example-infrastructure-configuration}}",
       "description": "{{An example that will terminate instances of failed builds}}",
       "instanceTypes": [
           "m7i.large", "m7i.2xlarge"
       ],
       "instanceProfileName": "{{my-iam-instance-profile-name}}",
       "securityGroupIds": [
           "sg-{{12345678}}"
       ],
       "subnetId": "subnet-{{12345678}}",
       "logging": {
           "s3Logs": {
               "s3BucketName": "{{amzn-s3-demo-logging-bucket}}",
               "s3KeyPrefix": "{{my-path}}"
           }
       },
       "terminateInstanceOnFailure": true,
       "snsTopicArn": "arn:aws:sns:{{us-west-2}}:{{111122223333}}:{{my-topic}}"
   }
   ```

1. 

**Use the file you created as input when you run the following command.**

   ```
   aws imagebuilder update-infrastructure-configuration --cli-input-json file://{{update-infrastructure-configuration.json}}
   ```

------
#### [ PowerShell ]

The following example shows how to use the [Update-EC2IBInfrastructureConfiguration](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-EC2IBInfrastructureConfiguration.html) cmdlet to update an infrastructure configuration. This example is based on the first example in [Create an infrastructure configuration](create-infra-config.md). It sets the `TerminateInstanceOnFailure` parameter to `$true`, so pipelines that use this infrastructure configuration terminate the build and test instances when a build fails.

The following example sets common infrastructure fields. To require IMDSv2 tokens on the build and test instances, set the `InstanceMetadataOptions_HttpToken` parameter to `required`.

To update the infrastructure configuration, run the `Update-EC2IBInfrastructureConfiguration` cmdlet:

```
Update-EC2IBInfrastructureConfiguration -InfrastructureConfigurationArn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:infrastructure-configuration/{{my-example-infrastructure-configuration}} `
    -Description "{{An example that will terminate instances of failed builds}}" `
    -InstanceType m7i.large, m7i.2xlarge `
    -InstanceProfileName {{my-iam-instance-profile-name}} `
    -SecurityGroupId sg-{{12345678}} `
    -SubnetId subnet-{{12345678}} `
    -S3Logs_S3BucketName {{amzn-s3-demo-logging-bucket}} `
    -S3Logs_S3KeyPrefix {{my-path}} `
    -TerminateInstanceOnFailure $true `
    -SnsTopicArn arn:aws:sns:{{us-west-2}}:{{111122223333}}:{{my-topic}}
```

------