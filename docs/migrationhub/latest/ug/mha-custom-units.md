AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Custom AWS Migration Hub automation units

###### Note

The AWS Migration Hub Automation feature is in preview release. It is available in
US East (N. Virginia). To use this feature, you must set your AWS Region to US East (N. Virginia).
You must also set the AWS Migration Hub home Region to US East (N. Virginia). For instructions on how to
set the AWS Migration Hub home Region, see [Managing your AWS Migration Hub home Region](home-region.md "home-region.md").

This is pre-release documentation. Both the AWS Migration Hub Automation feature and the
documentation are subject to change.

This topic describes how to create a custom automation unit. For information about how to
run an automation unit, see [Automation runs in AWS Migration Hub](mha-runs.md "mha-runs.md").

###### To create a custom automation unit

1. Sign in to the AWS Management Console and open
   the Migration Hub console at
   [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the left navigation pane, under **Automation**, choose
   **Automation units**.
3. Choose **Create custom unit**.
4. Enter a unique name for the unit.
5. For the runtime target, specify the ARN of one of the following:
   - An AWS-owned Systems Manager automation document. For information, see [Systems Manager Automation runbook reference](../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md").
   - Your own Systems Manager automation. For information, see [Authoring
     Automation runbooks](../../../systems-manager/latest/userguide/automation-authoring-runbooks.md "../../../systems-manager/latest/userguide/automation-authoring-runbooks.md").
   - A Lambda function. For information, see [Create your first Lambda
     function](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md").

6. AWS does not use the values that you enter for the optional fields **Runtime
   services**, **Description**, and
   **Prerequisites** other than for display purposes. The purpose of these
   three fields is to allow you to document your custom automation unit. After you create the
   unit, you can see the values that you entered for these three fields in the unit's details
   page.
7. Choose **Next**.
8. To add an input to the automation unit, choose **Add input**.
   1. Specify a name and a type for this input. Optionally, you can also enter a
      description and a format in the form of a regular expression.
   2. The default is for the new input to be required. To make this input optional, clear
      the **This input is required** checkbox.

9. To specify more inputs for the custom unit, choose **Add input**
   again, and then follow the previous steps for each additional input.
10. In the **IAM role - _optional_**
    section, specify an IAM role that has the trust policy that Migration Hub needs to run the unit,
    and the permissions policy that your custom unit needs to perform its actions. To learn how
    to create such a role, see [IAM role and policies for custom
    automation units](mha-iam-roles.md#iam-custom-automation-units "mha-iam-roles.md#iam-custom-automation-units").
11. Review the details that you entered for the unit, and then choose **Create
    automation unit**.
