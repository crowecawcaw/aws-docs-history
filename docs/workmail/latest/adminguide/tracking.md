# Enabling email event logging

You enable email event logging in the Amazon WorkMail console in order to track email
messages for your organization. Email event logging uses an AWS Identity and Access Management service-linked
role (SLR) to grant permissions to publish the email event logs to Amazon CloudWatch. For more
information about IAM service-linked roles, see [Using service-linked roles for
Amazon WorkMail](using-service-linked-roles.md "using-service-linked-roles.md").

In the CloudWatch event logs, you can use CloudWatch search tools and metrics to track messages
and troubleshoot email issues. For more information about the event logs that Amazon WorkMail sends
to CloudWatch, see [Monitoring Amazon WorkMail email event logs](cw-events.md "cw-events.md"). For more information
about CloudWatch Logs, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").

###### Topics

- [Turning on email event logging](#enable-tracking "#enable-tracking")
- [Creating a custom log group and IAM role
  for email event logging](#custom-tracking-role "#custom-tracking-role")
- [Turning off email event logging](#turn-off-tracking "#turn-off-tracking")
- [Cross-service confused
  deputy prevention](#cross-service-confused-deputy-prevention "#cross-service-confused-deputy-prevention")

## Turning on email event logging

The following occurs when you turn on email event logging using the default
settings, Amazon WorkMail:

- Creates an AWS Identity and Access Management service-linked role –
  `AmazonWorkMailEvents`.
- Creates a CloudWatch log group –
  `/aws/workmail/emailevents/`organization-alias``.
- Sets CloudWatch log retention to 30 days.

###### To turn on email event logging

1. Open the Amazon WorkMail console at
   [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/ "https://console.aws.amazon.com/workmail/").

If necessary, change the AWS Region. In the bar at the top of the
console window, open the **Select a Region** list and
choose a Region. For more information, see [Regions
and endpoints](../../../general/latest/gr/index.md "../../../general/latest/gr/index.md") in the
_Amazon Web Services General Reference_. 2. In the navigation pane, choose **Organizations**, then
choose the name of your organization. 3. In the navigation pane, choose **Logging
settings**. 4. Choose the **Email flow log settings** tab. 5. In the **Email flow log settings** section, choose
**Edit**. 6. Move the **Enable mail events** slider to the
**on** position. 7. Do one of the following:

    * (Recommended) Choose **Use default
     settings**.
    * (Optional) Clear the **Use default settings**,
     and select a **Destination Log Group** and
     **IAM Role** from the lists that appear.


    ###### Note

    Choose this option only if you have already created a log
     group and custom IAM role using the AWS CLI. For more
     information, see [Creating a custom log group and IAM role
     for email event logging](#custom-tracking-role "#custom-tracking-role").

8. Select **I authorize Amazon WorkMail to publish logs in my account using this
   configuration**.
9. Choose **Save**.

## Creating a custom log group and IAM role

for email event logging

We recommend using the default settings when enabling email event logging for
Amazon WorkMail. If you require a custom monitoring configuration, you can use the AWS CLI to
create a dedicated log group and custom IAM role for email event logging.

###### To create a custom log group and IAM role for email event logging

1. Use the following AWS CLI command to create a log group in the same AWS
   Region as your Amazon WorkMail organization. For more information, see [create-log-group](../../../cli/latest/reference/logs/create-log-group.md "../../../cli/latest/reference/logs/create-log-group.md") in the
   _AWS CLI Command Reference_.

```
aws –-region `us-east-1` logs create-log-group --log-group-name `workmail-monitoring`
```

2. Create a file containing the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "events.workmail.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

3. Use the following AWS CLI command to create an IAM role and attach this
   file as the role policy document. For more information, see [create-role](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") in the _AWS CLI Command Reference_.

```
aws iam create-role --role-name `workmail-monitoring-role` --assume-role-policy-document file://`trustpolicyforworkmail.json`
```

###### Note

If you're a `WorkMailFullAccess` managed policy user, you
must include the term `workmail` in the role name. This
managed policy only allows you to configure email event logging using
roles with `workmail` in the name. For more information, see
[Granting a
user permissions to pass a role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") in the
_IAM User Guide_. 4. Create a file containing the policy for the IAM role that you created in
the previous step. At minimum, the policy must grant permissions to the role
to create log streams and put log events into the log group that you created
in step 1.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:logs:`us-east-1`:`111122223333`:log-group:`example-log-group`*"
 }
 ]
}`

```

5. Use the following AWS CLI command to attach the policy file to the IAM
   role. For more information, see [put-role-policy](../../../cli/latest/reference/iam/put-role-policy.md "../../../cli/latest/reference/iam/put-role-policy.md") in the
   _AWS CLI Command Reference_.

```
aws iam put-role-policy --role-name `workmail-monitoring-role` --policy-name `workmail-permissions` --policy-document file://`rolepolicy.json`
```

## Turning off email event logging

Turn off email event logging from the Amazon WorkMail console. If you no longer need to use
email event logging, we recommend that you delete the related CloudWatch log group and
service-linked role as well. For more information, see [Deleting a service-linked role for
Amazon WorkMail](using-service-linked-roles.md#delete-slr "using-service-linked-roles.md#delete-slr").

###### To turn off email event logging

1. Open the Amazon WorkMail console at
   [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/ "https://console.aws.amazon.com/workmail/").

If necessary, change the AWS Region. In the bar at the top of the
console window, open the **Select a Region** list and
choose a Region. For more information, see [Regions
and endpoints](../../../general/latest/gr/index.md "../../../general/latest/gr/index.md") in the
_Amazon Web Services General Reference_. 2. In the navigation pane, choose **Organizations**, then
choose the name of your organization. 3. In the navigation pane, choose **Monitoring**. 4. In the **Log settings** section, choose
**Edit**. 5. Move the **Enable mail events** slider to the off
position. 6. Choose **Save**.

## Cross-service confused

deputy prevention

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the
action. In AWS, cross-service impersonation can result in the confused deputy
problem. Cross-service impersonation can occur when one service (the
_calling service_) calls another service (the
_called service_).

The calling service can be manipulated to use its permissions to act on another
customer’s resources it wouldn’t otherwise have permission to access.

To prevent this, AWS provides tools that help you protect your data for all
services with service principals that have been given access to resources in your
account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in
resource policies to limit the permissions that CloudWatch Logs and Amazon S3 give to the services
that are generating logs. If you use both global condition context keys, the values
must use the same account ID when used in the same policy statement.

The values of `aws:SourceArn` must be the ARNs of the delivery sources
that are generating logs.

The most effective way to protect against the confused deputy problem is to use
the `aws:SourceArn` global condition context key with the full ARN of the
resource. If you don't know the full ARN of the resource or if you're specifying
multiple resources, use the `aws:SourceArn` global context condition key
with wildcards (`*`) for the unknown portions of the ARN.
