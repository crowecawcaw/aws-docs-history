# Update an

infrastructure configuration

This section covers how you can use the Image Builder console or **imagebuilder**
commands in the AWS CLI to update an infrastructure configuration resource. To track your
resources, you can apply tags as follows. Tags are entered as key value pairs.

- _Resource tags_ assign metadata tags to the Amazon EC2 instance that Image Builder launches during
  the build process.
- _Tags_ assign metadata tags to the infrastructure configuration resource that Image Builder
  creates as output.

Console
You can edit the following infrastructure configuration details
from the Image Builder console:

- The **Description** for your
  infrastructure configuration.
- The **IAM role** to associate with the
  instance profile.
- **AWS infrastructure**, including the
  **Instance type** and an
  **SNS topic** for notifications.
- **VPC, subnet, and security groups**.
- **Troubleshooting settings**, including
  **Terminate instance on failure**,
  the **Key pair** for connecting, and
  an optional S3 bucket location for instance logs.

To update an infrastructure configuration resource from the Image Builder console, follow
these steps:

###### Choose an existing Image Builder infrastructure configuration

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. To see a list of the infrastructure configuration resources under your account,
   choose **Infrastructure configuration** from the
   navigation pane.
3. To view details or edit an infrastructure configuration, choose the
   **Configuration name** link. This opens the detail view
   for the infrastructure configuration.

###### Note

You can also select the check box next to the
**Configuration name**, then choose
**View detail**. 4. From the upper right corner of the **Infrastructure details**
panel, choose **Edit** . 5. When you're ready to save updates you've made to your infrastructure configuration,
choose **Save changes**.

AWS CLI
The following example shows how to update the infrastructure configuration for your
image with the Image Builder **[update-infrastructure-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-infrastructure-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-infrastructure-configuration.html")** command in
the AWS CLI.

1. ###### Create a CLI input JSON file

This infrastructure configuration example uses the same settings as the create
example, except that we've updated the
`terminateInstanceOnFailure` setting to
`false`. After we run the
**update-infrastructure-configuration** command,
pipelines that use this infrastructure configuration terminate the
build and test instances when the build fails.

Use a file editing tool to create a JSON file with keys shown in the following
example, plus values that are valid for your environment. This
example uses a file named
`update-infrastructure-configuration.json`:

```
{
"infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-`2:123456789012`:infrastructure-configuration/`my-example-infrastructure-configuration`",
"description": "`An example that will terminate instances of failed builds`",
"instanceTypes": [
    "m5.large", "m5.2xlarge"
],
"instanceProfileName": "`myIAMInstanceProfileName`",
"securityGroupIds": [
    "`sg-12345678`"
],
"subnetId": "sub-12345678",
"logging": {
    "s3Logs": {
        "s3BucketName": "`my-logging-bucket`",
        "s3KeyPrefix": "`my-path`"
    }
},
"terminateInstanceOnFailure": true,
"snsTopicArn": "arn:aws:sns:us-west-``2:123456789012``:`MyTopic`"
}
```

2. ###### Use the file you created as input when you run the following command.

```
aws imagebuilder update-infrastructure-configuration --cli-input-json file://`update-infrastructure-configuration.json`
```
