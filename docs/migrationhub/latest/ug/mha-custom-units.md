

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Custom AWS Migration Hub automation units
<a name="mha-custom-units"></a>

**Note**  
The AWS Migration Hub Automation feature is in preview release. It is available in US East (N. Virginia). To use this feature, you must set your AWS Region to US East (N. Virginia). You must also set the AWS Migration Hub home Region to US East (N. Virginia). For instructions on how to set the AWS Migration Hub home Region, see [Managing your AWS Migration Hub home Region](home-region.md).  
This is pre-release documentation. Both the AWS Migration Hub Automation feature and the documentation are subject to change.

This topic describes how to create a custom automation unit. For information about how to run an automation unit, see [Automation runs in AWS Migration Hub](mha-runs.md).

**To create a custom automation unit**

1. Sign in to the AWS Management Console and open the Migration Hub console at [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/). 

1. In the left navigation pane, under **Automation**, choose **Automation units**.

1. Choose **Create custom unit**.

1. Enter a unique name for the unit.

1. For the runtime target, specify the ARN of one of the following:
   + An AWS-owned Systems Manager automation document. For information, see [Systems Manager Automation runbook reference](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.html).
   + Your own Systems Manager automation. For information, see [Authoring Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-authoring-runbooks.html).
   + A Lambda function. For information, see [Create your first Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html).

1. AWS does not use the values that you enter for the optional fields **Runtime services**, **Description**, and **Prerequisites** other than for display purposes. The purpose of these three fields is to allow you to document your custom automation unit. After you create the unit, you can see the values that you entered for these three fields in the unit's details page.

1. Choose **Next**.

1. To add an input to the automation unit, choose **Add input**.

   1. Specify a name and a type for this input. Optionally, you can also enter a description and a format in the form of a regular expression.

   1. The default is for the new input to be required. To make this input optional, clear the **This input is required** checkbox.

1. To specify more inputs for the custom unit, choose **Add input** again, and then follow the previous steps for each additional input.

1. In the **IAM role - *optional*** section, specify an IAM role that has the trust policy that Migration Hub needs to run the unit, and the permissions policy that your custom unit needs to perform its actions. To learn how to create such a role, see [IAM role and policies for custom automation units](mha-iam-roles.md#iam-custom-automation-units).

1. Review the details that you entered for the unit, and then choose **Create automation unit**.