# Creating a canary

###### Important

Ensure that you use Synthetics canaries to monitor only endpoints and APIs where you have
ownership or permissions. Depending on the canary frequency settings, these endpoints might
experience increased traffic.

When you use the CloudWatch console to create a canary, you can use a blueprint provided by CloudWatch to
create your canary or you can write your own
script. For more information, see [Using canary blueprints](CloudWatch_Synthetics_Canaries_Blueprints.md "CloudWatch_Synthetics_Canaries_Blueprints.md").

You can also create a canary using CloudFormation if you are using your own script for the canary.
For more information, see [AWS::Synthetics::Canary](../../../AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.md") in the _AWS CloudFormation User Guide_.

If you are writing your own script, you can use several functions that
CloudWatch Synthetics has built into a library. For more information, see
[Synthetics runtime versions](CloudWatch_Synthetics_Canaries_Library.md "CloudWatch_Synthetics_Canaries_Library.md").

###### Note

When you create a canary, one of the layers created is a Synthetics layer prepended with `Synthetics`. This layer is owned by the Synthetics service account and contains the runtime code.

###### To create a canary

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**, **Synthetics Canaries**.
3. Choose **Create Canary**.
4. Choose one of the following:
   - To base your canary on a blueprint script, choose **Use a
     blueprint**, and then choose the type of canary you want to create. For
     more information about what each type of blueprint does, see [Using canary blueprints](CloudWatch_Synthetics_Canaries_Blueprints.md "CloudWatch_Synthetics_Canaries_Blueprints.md").
   - To upload your own Node.js script to create a custom canary, choose **Upload a script**.

   You can then drag your script into the **Script** area or choose
   **Browse files** to navigate to the script in your file
   system.
   - To import your script from an S3 bucket, choose **Import from
     S3**. Under **Source location**, enter the complete path
     to your canary or choose **Browse S3**.

   You must have `s3:GetObject` and `s3:GetObjectVersion`
   permissions for the S3 bucket that you use. The bucket must be in the same AWS Region
   where you are creating the canary.

5. Under **Name**, enter a name for your canary. The name is used on many pages,
   so we recommend that you give it a descriptive name that distinguishes it from other
   canaries.
6. Under **Application or endpoint URL**, enter the URL that you want the canary
   to test. This URL must include the protocol (such as https://).

If you want the canary to test an endpoint on a VPC, you must also enter information
about your VPC later in this procedure. 7. If you are using your own script for the canary, under **Lambda handler**,
enter the entry point where you want the canary to start. For information on Lambda handler format, see [Synthetics runtime versions](CloudWatch_Synthetics_Canaries_Library.md "CloudWatch_Synthetics_Canaries_Library.md") . 8. Under **Script editor**, **Runtime version**, select a synthetics runtime version to execute the canary. For information on synthetics runtime versions, see [Synthetics runtime versions](CloudWatch_Synthetics_Canaries_Library.md "CloudWatch_Synthetics_Canaries_Library.md") .

Under **Browser configuration**, you can enable the browser to test the canary. You must select at least one browser. 9. If you are using environment variables in your script, choose
**Environment variables** and then specify a value for each
environment variable defined in your script. For more information,
see [Environment variables](CloudWatch_Synthetics_Canaries_WritingCanary_Nodejs_Pup.md#CloudWatch_Synthetics_Environment_Variables "CloudWatch_Synthetics_Canaries_WritingCanary_Nodejs_Pup.md#CloudWatch_Synthetics_Environment_Variables"). 10. Under **Schedule**, choose whether to run this canary just once, run it continuously
using a rate expression, or schedule it using a cron expression.

    * When you use the CloudWatch console
     to create a canary that runs continuously, you can choose a rate anywhere between once a minute and once an hour.


    * For more information about writing a cron expression for canary scheduling, see
     [Scheduling canary runs using cron](CloudWatch_Synthetics_Canaries_cron.md "CloudWatch_Synthetics_Canaries_cron.md").

11. (Optional) To set a timeout value for the canary, choose **Additional configuration**
    and then specify the timeout value. Make it no shorter than
    15 seconds to allow for Lambda cold starts and the time it takes to boot up the canary
    instrumentation.
12. Under **Data retention**, specify how long to retain information about both failed and successful canary runs.
    The range is 1-455 days.

This setting affects the range of information returned by [GetCanaryRuns](../../../AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.md "../../../AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.md") operations, as well as the range of
information displayed in the Synthetics console.

It does not
affect the data stored in your Amazon S3 buckets, or logs or metrics that are published by the canary.

Regardless of the canary's data retention period, the range of information displayed
in console has certain limits. In the Synthetics console home view,
the relative and absolute time range are limited to seven days. In the Synthetics
console view for a specific canary, the relative time range is limited to seven
days and the absolute time range is limited to 30 days. 13. Under **Data Storage**, select the Amazon S3 bucket to use to
store the data from
the canary runs. The bucket name can't contain a period (.). If you leave this blank, a default Amazon S3 bucket is used or created. 14. (Optional) By default, canaries store their artifacts on Amazon S3, and the artifacts are encrypted at rest
using an AWS-managed AWS KMS key. You can use a different encryption option by choosing
**Additional configuration** in the **Data Storage** section. You can
then choose the type of key to use for encryption. For more information, see [Encrypting canary artifacts](CloudWatch_Synthetics_artifact_encryption.md "CloudWatch_Synthetics_artifact_encryption.md"). 15. Under **Access permissions**, choose whether to create an IAM role to run
the canary or use an existing one.

If you have CloudWatch Synthetics create the role, it automatically includes all the necessary permissions.
If you want to create the role yourself, see
[Required roles and permissions for canaries](CloudWatch_Synthetics_Canaries_CanaryPermissions.md "CloudWatch_Synthetics_Canaries_CanaryPermissions.md") for information about the necessary permissions.

If you use the CloudWatch console to create a role for a canary when
you create the canary, you can't re-use the role for other canaries, because
these roles are specific to just one canary. If you have manually created a role
that works for multiple canaries, you can use that existing role.

To use an existing role, you must have the `iam:PassRole` permission to
pass that role to Synthetics and Lambda. You must also have the `iam:GetRole`
permission. 16. (Optional) Under **Alarms**, choose whether you want default CloudWatch alarms to
be created for this canary. If you choose to create alarms, they are created with the following
name convention:`Synthetics-Alarm-`canaryName`-`index``

`index` is a number representing each different alarm created for this canary. The first alarm
has an index of 1, the second alarm has an index of 2, and so on. 17. (Optional) To have this canary test an endpoint that is on a VPC, choose **VPC
settings**, and then do the following:

    1. Select the VPC that hosts the endpoint.
    2. Select one or more subnets on your VPC. You must select a private subnet because a Lambda
     instance can't be configured to run in a public subnet when an IP address can't be
     assigned to the Lambda instance during execution. For more information, see [Configuring a Lambda Function to Access
     Resources in a VPC](../../../lambda/latest/dg/configuration-vpc.md "../../../lambda/latest/dg/configuration-vpc.md").
    3. Select one or more security groups on your VPC.
    4. To allow outbound IPv6 traffic for this canary, select **Allow IPv6 Traffic for dual-stack subnets**. This enables the canary to
     monitor IPv6-only and dual stack enabled endpoints over IPv6.


    You can monitor endpoints external to your VPC by giving
     the canary internet access and configuring the VPC subnets appropriately. For more information, see [Running a canary on a VPC](CloudWatch_Synthetics_Canaries_VPC.md "CloudWatch_Synthetics_Canaries_VPC.md").If the endpoint

is on a VPC, you must enable your canary to send information to CloudWatch and Amazon S3. For more information,
see [Running a canary on a VPC](CloudWatch_Synthetics_Canaries_VPC.md "CloudWatch_Synthetics_Canaries_VPC.md"). 18. (Optional) Under **Tags**, add one or more key-value pairs as tags for this
canary. Tags can help you identify and organize your AWS resources and track your AWS
costs. For more information, see [Tagging your Amazon CloudWatch resources](CloudWatch-Tagging.md "CloudWatch-Tagging.md").

If you want the tags that you apply to the canary to also be applied to the Lambda function that the canary uses,
choose **Lambda function** under **Tag Replication**. If you choose this option, CloudWatch Synthetics
will keep the tags on the canary and the Lambda function synchronized:

    * Synthetics will apply the same tags that you specify here to both your canary and your Lambda function.
    * If you later update the canary's tags and keep this option selected, Synthetics modifies the tags on your Lambda function to remain in sync with the canary.

19. (Optional) Under **Active tracing**, choose whether to
    enable active X-Ray tracing for this canary. Active tracing is only available for Puppeteer and Java runtimes.
    For more information, see [Canaries and X-Ray tracing](CloudWatch_Synthetics_Canaries_tracing.md "CloudWatch_Synthetics_Canaries_tracing.md").

## Resources that are created for canaries

When you create a canary, the following resources are created:

- An IAM role with the name
  `CloudWatchSyntheticsRole-`canary-name`-`uuid``
  (if you use CloudWatch console to create the canary and specify for a new role to be created for the canary)
- An IAM policy with the name
  `CloudWatchSyntheticsPolicy-`canary-name`-`uuid``.
- An S3 bucket with the name
  `cw-syn-results-`accountID`-`region``.
- Alarms with the name
  `Synthetics-Alarm-`MyCanaryName``, if you want
  alarms to be created for the canary.
- Lambda functions and layers, if you use a blueprint to create the canary. These
  resources have the prefix
  `cwsyn-`MyCanaryName``.
- CloudWatch Logs log groups with the name
  `/aws/lambda/cwsyn-`MyCanaryName`-`randomId``.
