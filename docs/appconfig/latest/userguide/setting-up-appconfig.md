# Setting up AWS AppConfig

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

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

###### To create an IAM permission policy for rollback based on CloudWatch alarms

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
