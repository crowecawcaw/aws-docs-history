

# Update an infrastructure configuration
<a name="update-infra-config"></a>

This section covers how you can use the Image Builder console or **imagebuilder** commands in the AWS CLI to update an infrastructure configuration resource. To track your resources, you can apply tags as follows. Enter tags as key-value pairs.
+ *Resource tags* assign metadata tags to the Amazon EC2 instance that Image Builder launches during the build process.
+ *Tags* assign metadata tags to the infrastructure configuration resource that Image Builder creates as output.

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

The following example shows how to update the infrastructure configuration for your image with the Image Builder **[update-infrastructure-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-infrastructure-configuration.html)** command in the AWS CLI.

1. 

**Create a CLI input JSON file**

   In this example, the settings match the create example, except that `terminateInstanceOnFailure` is set to `true`. After you run the **update-infrastructure-configuration** command, pipelines that use this infrastructure configuration terminate the build and test instances when a build fails.

   The following example sets common infrastructure fields. To require IMDSv2 tokens on the build and test instances, add an `instanceMetadataOptions` block with `httpTokens` set to `required`.
**Note**  
We recommend that you configure all EC2 instances that Image Builder launches from a pipeline build to use IMDSv2 so that instance metadata retrieval requests require a signed token header.

   Use a file editing tool to create a JSON file with keys shown in the following example, plus values that are valid for your environment. This example uses a file named `update-infrastructure-configuration.json`:

   ```
   {
   "infrastructureConfigurationArn": "arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:infrastructure-configuration/{{my-example-infrastructure-configuration}}",
   "description": "{{An example that will terminate instances of failed builds}}",
   "instanceTypes": [
       "m7i.large", "m7i.2xlarge"
   ],
   "instanceProfileName": "{{myIAMInstanceProfileName}}",
   "securityGroupIds": [
       "{{sg-12345678}}"
   ],
   "subnetId": "subnet-{{12345678}}",
   "logging": {
       "s3Logs": {
           "s3BucketName": "{{my-logging-bucket}}",
           "s3KeyPrefix": "{{my-path}}"
       }
   },
   "terminateInstanceOnFailure": true,
   "snsTopicArn": "arn:aws:sns:{{us-west-2}}:{{123456789012}}:{{MyTopic}}"
   }
   ```

1. 

**Use the file you created as input when you run the following command.**

   ```
   aws imagebuilder update-infrastructure-configuration --cli-input-json file://{{update-infrastructure-configuration.json}}
   ```

------