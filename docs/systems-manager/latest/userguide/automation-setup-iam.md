# Create the service roles for Automation using

the console

If you need to create a service role for Automation, a tool in AWS Systems Manager, complete
the following tasks. For more information about when a service role is required for
Automation, see [Setting up Automation](automation-setup.md "automation-setup.md").

###### Tasks

- [Task 1: Create a service role for
  Automation](#create-service-role "#create-service-role")
- [Task 2: Attach the iam:PassRole policy
  to your Automation role](#attach-passrole-policy "#attach-passrole-policy")

## Task 1: Create a service role for

Automation

Use the following procedure to create a service role (or _assume
role_) for Systems Manager Automation.

###### Note

You can also use this role in runbooks, such as the
`AWS-CreateManagedLinuxInstance` runbook. Using this role, or
the Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role, in runbooks
allows Automation to perform actions in your environment, such as launch new
instances and perform actions on your behalf.

###### To create an IAM role and allow Automation to assume it

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**, and then
   choose **Create role**.
3. Under **Select type of trusted entity**, choose
   **AWS service**.
4. In the **Choose a use case** section, choose
   **Systems Manager**, and then choose **Next:
   Permissions**.
5. On the **Attached permissions policy** page, search
   for the **AmazonSSMAutomationRole** policy, choose it,
   and then choose **Next: Review**.
6. On the **Review** page, enter a name in the
   **Role name** box, and then enter a
   description.
7. Choose **Create role**. The system returns you to the
   **Roles** page.
8. On the **Roles** page, choose the role you just
   created to open the **Summary** page. Note the
   **Role Name** and **Role ARN**.
   You will specify the role ARN when you attach the
   **iam:PassRole** policy to your IAM account in
   the next procedure. You can also specify the role name and the ARN in
   runbooks.

###### Note

The `AmazonSSMAutomationRole` policy assigns the Automation
role permission to a subset of AWS Lambda functions within your account.
These functions begin with "Automation". If you plan to use Automation with
Lambda functions, the Lambda ARN must use the following format:

`"arn:aws:lambda:*:*:**function:Automation\***"`

If you have existing Lambda functions whose ARNs don't use this format,
then you must also attach an additional Lambda policy to your automation
role, such as the **AWSLambdaRole** policy. The additional
policy or role must provide broader access to Lambda functions within the
AWS account.

After creating your service role, we recommend editing the trust policy to
help prevent the cross-service confused deputy problem. The _confused deputy problem_ is a security issue where
an entity that doesn't have permission to perform an action can coerce a
more-privileged entity to perform the action. In AWS, cross-service
impersonation can result in the confused deputy problem. Cross-service
impersonation can occur when one service (the _calling
service_) calls another service (the _called
service_). The calling service can be manipulated to use its
permissions to act on another customer's resources in a way it should not
otherwise have permission to access. To prevent this, AWS provides tools that
help you protect your data for all services with service principals that have
been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in
resource policies to limit the permissions that Automation gives another service
to the resource. If the `aws:SourceArn` value doesn't contain the
account ID, such as an Amazon S3 bucket ARN, you must use both global condition
context keys to limit permissions. If you use both global condition context keys
and the `aws:SourceArn` value contains the account ID, the
`aws:SourceAccount` value and the account in the
`aws:SourceArn` value must use the same account ID when used in
the same policy statement. Use `aws:SourceArn` if you want only one
resource to be associated with the cross-service access. Use
`aws:SourceAccount` if you want to allow any resource in that
account to be associated with the cross-service use. The value of
`aws:SourceArn` must be the ARN for automation executions. If you
don't know the full ARN of the resource or if you're specifying multiple
resources, use the `aws:SourceArn` global context condition key with
wildcards (`*`) for the unknown portions of the ARN. For example,
`arn:aws:ssm:*:123456789012:automation-execution/*`.

The following example shows how you can use the `aws:SourceArn` and
`aws:SourceAccount` global condition context keys for Automation
to prevent the confused deputy problem.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "ssm.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "123456789012"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:ssm:*:123456789012:automation-execution/*"
 }
 }
 }
 ]
}`

```

###### To modify the role's trust policy

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. In the list of roles in your account, choose the name of your
   Automation service role.
4. Choose the **Trust relationships** tab, and then
   choose **Edit trust relationship**.
5. Edit the trust policy using the `aws:SourceArn` and
   `aws:SourceAccount` global condition context keys for
   Automation to prevent the confused deputy problem.
6. Choose **Update Trust Policy** to save your
   changes.

### (Optional) Add an Automation inline

policy or customer managed policy to invoke other AWS services

If you run an automation that invokes other AWS services by using an
IAM service role, the service role must be configured with permission to
invoke those services. This requirement applies to all AWS Automation
runbooks (`AWS-*` runbooks) such as the
`AWS-ConfigureS3BucketLogging`,
`AWS-CreateDynamoDBBackup`, and
`AWS-RestartEC2Instance` runbooks, to name a few. This
requirement also applies to any custom runbooks you create that invoke other
AWS services by using actions that call other services. For example, if
you use the `aws:executeAwsApi`, `aws:CreateStack`, or
`aws:copyImage` actions, to name a few, then you must
configure the service role with permission to invoke those services. You can
give permissions to other AWS services by adding an IAM inline policy or
customer managed policy to the role.

###### To embed an inline policy for a service role (IAM console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. In the list, choose the name of the role that you want to
   edit.
4. Choose the **Permissions** tab.
5. In the **Add permissions** dropdown, choose
   **Attach policies** or **Create inline
   policy**.
6. If you choose **Attach policies**, select the
   check box next to the policy you want to add and choose
   **Add permissions**.
7. If you choose **Create inline policy**, choose
   the **JSON** tab.
8. Enter a JSON Policy document for the AWS services you want to
   invoke. Here are two example JSON Policy documents.

**Amazon S3 PutObject and GetObject
Example**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
 }
 ]
}`

```

**Amazon EC2 CreateSnapshot and DescribeSnapShots
Example**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":"ec2:CreateSnapshot",
 "Resource":"*"
 },
 {
 "Effect":"Allow",
 "Action":"ec2:DescribeSnapshots",
 "Resource":"*"
 }
 ]
}`

```

For details about the IAM policy language, see [IAM JSON
Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the
_IAM User Guide_. 9. When you're finished, choose **Review policy**.
The [Policy Validator](../../../IAM/latest/UserGuide/access_policies_policy-validator.md "../../../IAM/latest/UserGuide/access_policies_policy-validator.md") reports any syntax errors. 10. On the **Review policy** page, enter a
**Name** for the policy that you're creating.
Review the policy **Summary** to see the
permissions that are granted by your policy. Then choose
**Create policy** to save your work. 11. After you create an inline policy, it's automatically embedded in
your role.

## Task 2: Attach the iam:PassRole policy

to your Automation role

Use the following procedure to attach the `iam:PassRole` policy to
your Automation service role. This allows the Automation service to pass the
role to other services or Systems Manager tools when running automations.

###### To attach the iam:PassRole policy to your Automation role

1. In the **Summary** page for the role you just
   created, choose the **Permissions** tab.
2. Choose **Add inline policy**.
3. On the **Create policy** page, choose the
   **Visual editor** tab.
4. Choose **Service**, and then choose
   **IAM**.
5. Choose **Select actions**.
6. In the **Filter actions** text box, type
   `PassRole`, and then choose the
   **PassRole** option.
7. Choose **Resources**. Verify that
   **Specific** is selected, and then choose
   **Add ARN**.
8. In the **Specify ARN for role** field, paste the
   Automation role ARN that you copied at the end of Task 1. The system
   populates the **Account** and **Role name with
   path** fields.

###### Note

If you want the Automation service role to attach an IAM
instance profile role to an EC2 instance, then you must add the ARN
of the IAM instance profile role. This allows the Automation
service role to pass the IAM instance profile role to the target
EC2 instance. 9. Choose **Add**. 10. Choose **Review policy**. 11. On the **Review Policy** page, enter a name and then
choose **Create Policy**.
