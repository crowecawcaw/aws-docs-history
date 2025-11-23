# Setting up AWS AppConfig

If you haven't already done so, sign up for an AWS account and create an
administrative user.

## Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

## Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Grant programmatic

access

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                                  | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM                                                          | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Login for AWS local development](../../../cli/latest/userguide/cli-configure-sign-in.md "../../../cli/latest/userguide/cli-configure-sign-in.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs, see [Login for AWS local development](../../../sdkref/latest/guide/access-login.md "../../../sdkref/latest/guide/access-login.md") in the<br>_AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                                                             |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

## Configure permissions for automatic rollback

You can configure AWS AppConfig to roll back to a previous version of a configuration in
response to one or more Amazon CloudWatch alarms. When you configure a deployment to respond to
CloudWatch alarms, you specify an AWS Identity and Access Management (IAM) role. AWS AppConfig requires this role so that it
can monitor CloudWatch alarms. This procedure is optional, but highly recommended.

###### Note

Note the following information.

- The IAM role must belong to the current account. By default, AWS AppConfig can
  only monitor alarms owned by the current account.
- For information about metrics to monitor and how to configure AWS AppConfig for
  automatic rollback, see [Monitoring deployments for automatic rollback](monitoring-deployments.md "monitoring-deployments.md").

Use the following procedures to create an IAM role that enables AWS AppConfig to rollback
based on CloudWatch alarms. This section includes the following procedures.

1. [Step 1: Create the permission policy for rollback based on CloudWatch alarms](#getting-started-with-appconfig-cloudwatch-alarms-permissions-policy "#getting-started-with-appconfig-cloudwatch-alarms-permissions-policy")
2. [Step 2: Create the IAM role for rollback based on CloudWatch alarms](#getting-started-with-appconfig-cloudwatch-alarms-permissions-role "#getting-started-with-appconfig-cloudwatch-alarms-permissions-role")
3. [Step 3: Add a trust relationship](#getting-started-with-appconfig-cloudwatch-alarms-permissions-trust "#getting-started-with-appconfig-cloudwatch-alarms-permissions-trust")

### Step 1: Create the permission policy for rollback based on CloudWatch alarms

Use the following procedure to create an IAM policy that gives AWS AppConfig permission
to call the `DescribeAlarms` API action.

###### To create an IAM permission policy for rollback based on CloudWatch

alarms

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**, and then
   choose **Create policy**.
3. On the **Create policy** page, choose the
   **JSON** tab.
4. Replace the default content on the JSON tab with the following permission
   policy, and then choose **Next: Tags**.

###### Note

To return information about CloudWatch composite alarms, the [DescribeAlarms](../../../AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.md "../../../AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.md") API operation must be assigned
`*` permissions, as shown here. You can't return
information about composite alarms if `DescribeAlarms` has a
narrower scope.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:DescribeAlarms"
 ],
 "Resource": "*"
 }
 ]
 }`

```

5. Enter tags for this role, and then choose **Next:
   Review**.
6. On the **Review** page, enter
   `SSMCloudWatchAlarmDiscoveryPolicy` in the
   **Name** field.
7. Choose **Create policy**. The system returns you to the
   **Policies** page.

### Step 2: Create the IAM role for rollback based on CloudWatch alarms

Use the following procedure to create an IAM role and assign the policy you
created in the previous procedure to it.

###### To create an IAM role for rollback based on CloudWatch alarms

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**, and then choose
   **Create role**.
3. Under **Select type of trusted entity**, choose
   **AWS service**.
4. Immediately under **Choose the service that will use this
   role**, choose **EC2: Allows EC2 instances to call
   AWS services on your behalf**, and then choose
   **Next: Permissions**.
5. On the **Attached permissions policy** page, search for
   **SSMCloudWatchAlarmDiscoveryPolicy**.
6. Choose this policy and then choose **Next: Tags**.
7. Enter tags for this role, and then choose **Next:
   Review**.
8. On the **Create role** page, enter
   `SSMCloudWatchAlarmDiscoveryRole` in the
   **Role name** field, and then choose **Create
   role**.
9. On the **Roles** page, choose the role you just created.
   The **Summary** page opens.

### Step 3: Add a trust relationship

Use the following procedure to configure the role you just created to trust
AWS AppConfig.

###### To add a trust relationship for AWS AppConfig

1. In the **Summary** page for the role you just created,
   choose the **Trust Relationships** tab, and then choose
   **Edit Trust Relationship**.
2. Edit the policy to include only "`appconfig.amazonaws.com`", as
   shown in the following example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "appconfig.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

3. Choose **Update Trust Policy**.
