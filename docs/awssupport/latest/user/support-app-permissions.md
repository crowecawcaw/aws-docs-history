# Managing access to the AWS Support App

After you have permissions to the AWS Support App widget, you must also create an AWS Identity and Access Management
(IAM) role. This role performs actions from other AWS services for you, such as the
AWS Support API and Service Quotas.

You then attach an IAM policy to this role so that the role has the required permissions
to complete these actions. You choose this role when you create your Slack channel
configuration in the Support Center Console.

Users in your Slack channel have the same permissions that you grant to the IAM role.
For example, if you specify read-only access to your support cases, then users in your Slack
channel can view your support cases, but can't update them.

###### Important

When you request a live chat with a support agent and choose new private channel as
your live chat channel preference, the AWS Support App creates a separate Slack channel.
This Slack channel has the same permissions as the channel where you
created the case or initiated the chat.

If you change the IAM role or the IAM policy, your changes apply to the Slack
channel that you configured and to any new live chat Slack channels that the AWS Support App
creates for you.

Follow these procedures to create your IAM role and policy.

###### Topics

- [Use an AWS managed policy or create a
  customer managed policy](#create-iam-role-support-app "#create-iam-role-support-app")
- [Create an IAM role](#creating-an-iam-role-for-support-app "#creating-an-iam-role-for-support-app")
- [Troubleshooting](#troubleshooting-permissions-for-support-app "#troubleshooting-permissions-for-support-app")

## Use an AWS managed policy or create a

customer managed policy

To grant your role permissions, you can use either an AWS managed policy or a
customer managed policy.

###### Tip

If you don't want to create a policy manually, we recommend that you use an AWS
managed policy instead and skip this procedure. Managed policies automatically have
the required permissions for the AWS Support App. You don't need to update the policies
manually. For more information, see [AWS managed policies for
AWS Support App in Slack](support-app-managed-policies.md "support-app-managed-policies.md").

Follow this procedure to create a customer managed policy for your role. This
procedure uses the JSON policy editor in the IAM console.

###### To create a customer managed policy for the AWS Support App

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. Choose **Create policy**.
4. Choose the **JSON** tab.
5. Enter your JSON, and then replace the default JSON in the editor. You can use
   the [example policy](#example-support-app-policy "#example-support-app-policy").
6. Choose **Next: Tags**.
7. (Optional) You can use tags as key–value pairs to add metadata to the
   policy.
8. Choose **Next: Review**.
9. On the **Review policy** page, enter a
   **Name**, such as
   `AWSSupportAppRolePolicy`, and a
   **Description** (optional).
10. Review the **Summary** page to see the permissions that the
    policy allows and then choose **Create policy**.

This policy defines the actions that the role can take. For more information, see
[Creating IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

### Example IAM policy

You can attach the following example policy to your IAM role. This policy allows
the role to have full permissions to all required actions for the AWS Support App. After
you configure a Slack channel with the role, any user in your channel has the same
permissions.

###### Note

For a list of AWS managed policies, see [AWS managed policies for
AWS Support App in Slack](support-app-managed-policies.md "support-app-managed-policies.md").

You can update the policy to remove a permission from the AWS Support App.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "supportapp:GetSlackOauthParameters",
 "supportapp:RedeemSlackOauthCode",
 "supportapp:DescribeSlackChannels",
 "supportapp:ListSlackWorkspaceConfigurations",
 "supportapp:ListSlackChannelConfigurations",
 "supportapp:CreateSlackChannelConfiguration",
 "supportapp:DeleteSlackChannelConfiguration",
 "supportapp:DeleteSlackWorkspaceConfiguration",
 "supportapp:GetAccountAlias",
 "supportapp:PutAccountAlias",
 "supportapp:DeleteAccountAlias",
 "supportapp:UpdateSlackChannelConfiguration",
 "iam:ListRoles"
 ],
 "Resource": "*"
 }
 ]
}`

```

For descriptions for each action, see the following topics in the
_Service Authorization Reference_:

- [Actions, resources, and condition keys for
  AWS Support](../../../service-authorization/latest/reference/list_awssupport.md "../../../service-authorization/latest/reference/list_awssupport.md")
- [Actions, resources, and condition keys for
  Service Quotas](../../../service-authorization/latest/reference/list_servicequotas.md "../../../service-authorization/latest/reference/list_servicequotas.md")
- [Actions, resources, and condition keys for AWS Identity and Access Management](../../../service-authorization/latest/reference/list_identityandaccessmanagement.md "../../../service-authorization/latest/reference/list_identityandaccessmanagement.md")

## Create an IAM role

After you have your policy, you must create an IAM role, and then attach the policy
to that role. You choose this role when you create a Slack channel configuration in the
Support Center Console.

###### To create a role for the AWS Support App

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**, and then choose
   **Create role**.
3. For **Select trusted entity**, choose
   **AWS service**.
4. Choose **AWS Support App**.
5. Choose **Next: Permissions**.
6. Enter the policy name. You can choose the AWS managed policy or choose a
   customer managed policy that you created, such as
   `AWSSupportAppRolePolicy`. Then
   select the check box next to the policy.
7. Choose **Next: Tags**.
8. (Optional) You can use tags as key–value pairs to add metadata to the
   role.
9. Choose **Next: Review**.
10. For **Role name**, enter a name, such as
    `AWSSupportAppRole`.
11. (Optional) For **Role description**, enter a description for
    the role.
12. Review the role and then choose **Create role**. You can now
    choose this role when you configure a Slack channel in the Support Center Console. See
    [Configuring a Slack channel](add-your-slack-channel.md "add-your-slack-channel.md").

For more information, see [Creating a role for an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console "../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console") in the
_IAM User Guide_.

## Troubleshooting

See the following topics to manage access to the AWS Support App.

###### Contents

- [I want to restrict specific users in my
  Slack channel from specific actions](support-app-permissions.md#restrict-channel-users "support-app-permissions.md#restrict-channel-users")
- [When I configure a Slack channel, I don't see the
  IAM role that I created](support-app-permissions.md#missing-iam-role "support-app-permissions.md#missing-iam-role")
- [My IAM role is missing a
  permission](support-app-permissions.md#missing-permissions-slack "support-app-permissions.md#missing-permissions-slack")
- [A Slack error says that my IAM
  role isn't valid](support-app-permissions.md#find-the-configured-iam-role "support-app-permissions.md#find-the-configured-iam-role")
- [The AWS Support App says that I'm missing an
  IAM role for Service Quotas](support-app-permissions.md#missing-service-quota-role "support-app-permissions.md#missing-service-quota-role")

### I want to restrict specific users in my

Slack channel from specific actions

By default, users in your Slack channel have the same permissions specified in the
IAM policy that you attach to the IAM role that you create. This means anyone in
the channel has read or write access to your support cases, whether or not they have
an AWS account or an IAM user.

We recommend the following best practices:

- Configure private Slack channels with the AWS Support App
- Only invite users to your channel who need access to your support
  cases
- Use an IAM policy that has the minimum required permissions to the
  AWS Support App. See [AWS managed policies for
  AWS Support App in Slack](support-app-managed-policies.md "support-app-managed-policies.md").

### When I configure a Slack channel, I don't see the

IAM role that I created

If your IAM role doesn't appear in the **IAM role for the
AWS Support App** list, this means that the role doesn't have the AWS Support App as
a trusted entity, or that the role was deleted. You can update the existing role, or
create another one. See [Create an IAM role](#creating-an-iam-role-for-support-app "#creating-an-iam-role-for-support-app").

### My IAM role is missing a

permission

The IAM role that you create for your Slack channel needs permissions to perform
the actions that you want. For example, if you want your users in Slack to create
support cases, the role must have the `support:CreateCase` permission.
The AWS Support App assumes this role to perform these actions for you.

If you receive an error about a missing permission from the AWS Support App, verify that
the policy attached to your role has the required permission.

See the previous [Example IAM policy](#example-support-app-policy "#example-support-app-policy").

### A Slack error says that my IAM

role isn't valid

Verify that you chose the correct role for your channel configuration.

###### To verify your role

1. Sign in to the AWS Support Center Console at [https://console.aws.amazon.com/support/app#/config](https://console.aws.amazon.com/support/app#/config "https://console.aws.amazon.com/support/app#/config") page.
2. Choose the channel that you configured with the AWS Support App.
3. From the **Permissions** section, find the IAM role
   name that you chose.
   - To change the role, choose **Edit**, choose
     another role, and then choose **Save**.
   - To update the role or the policy attached to the role, sign in to
     the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").

### The AWS Support App says that I'm missing an

IAM role for Service Quotas

You must have the `AWSServiceRoleForServiceQuotas` role in your account
to request quota increases from Service Quotas. If you receive an error about a missing
resource, complete one of the following steps:

- Use the [Service Quotas](https://console.aws.amazon.com/servicequotas "https://console.aws.amazon.com/servicequotas") console to
  request a quota increase. After you make a successful request, Service Quotas creates
  this role for you automatically. Then, you can use the AWS Support App to request
  quota increases in Slack. For more information, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md").
- Update the IAM policy attached to your role. This grants the role
  permission to Service Quotas. The following section in the [Example IAM policy](#example-support-app-policy "#example-support-app-policy") allows the AWS Support App to create the
  Service Quotas role for you.

```
{
    "Effect": "Allow",
    "Action": "iam:CreateServiceLinkedRole",
    "Resource": "*",
    "Condition": {
        "StringEquals": {"iam:AWSServiceName": "servicequotas.amazonaws.com"}
     }
}
```

If you delete the IAM role that you configure for your channel, you must
manually create the role or update the IAM policy to allow the AWS Support App to create
one for you.
