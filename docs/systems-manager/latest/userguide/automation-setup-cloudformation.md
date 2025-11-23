AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Create service roles for

Automation by using CloudFormation

You can create a service role for Automation, a tool in AWS Systems Manager, from an
AWS CloudFormation template. After you create the service role, you can specify the service
role in runbooks using the parameter `AutomationAssumeRole`.

## Create the service role using

CloudFormation

Use the following procedure to create the required AWS Identity and Access Management (IAM) role for
Systems Manager Automation by using CloudFormation.

###### To create the required IAM role

1. Download and unzip the [`AWS-SystemsManager-AutomationServiceRole.zip`](samples/AWS-SystemsManager-AutomationServiceRole.md "samples/AWS-SystemsManager-AutomationServiceRole.md")
   file. This file includes the
   `AWS-SystemsManager-AutomationServiceRole.yaml` CloudFormation
   template file.
2. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. Choose **Create Stack**.
4. In the **Specify template** section, choose
   **Upload a template file**.
5. Choose **Browse**, and then choose the
   `AWS-SystemsManager-AutomationServiceRole.yaml` CloudFormation
   template file.
6. Choose **Next**.
7. On the **Specify stack details** page, in the
   **Stack name** field, enter a name.
8. On the **Configure stack options** page, you don’t
   need to make any selections. Choose **Next**.
9. On the **Review** page, scroll down and choose the
   **I acknowledge that CloudFormation might create IAM
   resources** option.
10. Choose **Create**.

CloudFormation shows the **CREATE_IN_PROGRESS** status for
approximately three minutes. The status changes to
**CREATE_COMPLETE** after the stack is created and your
roles are ready to use.

###### Important

If you run an automation workflow that invokes other services by using an AWS Identity and Access Management
(IAM) service role, be aware that the service role must be configured with permission
to invoke those services. This requirement applies to all AWS Automation runbooks
(`AWS-*` runbooks) such as the `AWS-ConfigureS3BucketLogging`,
`AWS-CreateDynamoDBBackup`, and `AWS-RestartEC2Instance`
runbooks, to name a few. This requirement also applies to any custom Automation runbooks
you create that invoke other AWS services by using actions that call other services.
For example, if you use the `aws:executeAwsApi`,
`aws:createStack`, or `aws:copyImage` actions, configure the
service role with permission to invoke those services. You can give permissions to other
AWS services by adding an IAM inline policy to the role. For more information, see
[(Optional) Add an Automation inline
policy or customer managed policy to invoke other AWS services](automation-setup-iam.md#add-inline-policy "automation-setup-iam.md#add-inline-policy").

## Copy role information for

Automation

Use the following procedure to copy information about the Automation service
role from the CloudFormation console. You must specify these roles when you use a
runbook.

###### Note

You don't need to copy role information using this procedure if you run
the `AWS-UpdateLinuxAmi` or `AWS-UpdateWindowsAmi`
runbooks. These runbooks already have the required roles specified as
default values. The roles specified in these runbooks use IAM managed
policies.

###### To copy the role names

1. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. Select the Automation **Stack name** you created in
   the previous procedure.
3. Choose the **Resources** tab.
4. Choose the **Physical ID** link for
   **AutomationServiceRole**. The IAM console opens
   to a summary of the Automation service role.
5. Copy the Amazon Resource Name (ARN) next to **Role
   ARN**. The ARN is similar to the following:
   `arn:aws:iam::12345678:role/AutomationServiceRole`
6. Paste the ARN into a text file to use later.

You have finished configuring the service role for Automation. You can now use
the Automation service role ARN in your runbooks.
