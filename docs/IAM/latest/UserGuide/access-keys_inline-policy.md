# Control the use of access keys by attaching an

inline policy to an IAM user

As a best practice we recommend that [workloads
use temporary credentials with IAM roles](best-practices.md#bp-workloads-use-roles "best-practices.md#bp-workloads-use-roles") to access AWS. IAM users with
access keys should be assigned least privilege access and have [multi-factor authentication (MFA)](id_credentials_mfa.md "id_credentials_mfa.md") enabled. For more
information about assuming IAM roles, see [Methods to assume a role](id_roles_manage-assume.md "id_roles_manage-assume.md").

However, if you're creating a proof of concept test of a service automation or other
short-term use case, and you choose to run workloads using an IAM user with access keys
we recommend that you [use policies conditions to
further restrict access](best-practices.md#use-policy-conditions "best-practices.md#use-policy-conditions") of their IAM user credentials.

In this situation you can either create a time-bound policy that expires the credentials
after the specified time or, if you are running a workload from a secure network, you can
use an IP restriction policy.

For both these use cases, you can use an inline policy that's attached to the IAM user
that has access keys.

###### To configure a time-bound policy for an IAM user

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users** and then select the user
   for the short-term use case. If you haven't created the user yet, you can [create the user](getting-started-workloads.md "getting-started-workloads.md") now.
3. On the user **Details** page, choose the
   **Permissions** tab.
4. Choose **Add permissions** and then select **Create
   inline policy**.
5. In the **Policy editor** section, select
   **JSON** to display the JSON editor.
6. In the JSON editor, enter the following policy, replacing the value for the
   `aws:CurrentTime` timestamp with your desired expiration date and
   time:

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "DateGreaterThan": {
 "aws:CurrentTime": "2025-03-01T00:12:00Z"
 }
 }
 }
 ]
}`

```

This policy uses the `Deny` effect to restrict all actions on all
resources after the specified date. The `DateGreaterThan` condition
compares the current time with the timestamp you set. 7. Select **Next** to proceed to the **Review and
create** page. In **Policy** details, under
**Policy name** enter a name for the policy and then choose
**Create policy**.
After the policy is created, it's displayed on the **Permissions** tab
for the user. When the current time is greater than or equal to the time specified in the
policy, the user will no longer have access to AWS resources. Make sure to inform
workload developers of the expiration date you specified for these access keys.

###### To configure an IP restriction policy for an IAM user

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users** and then select the user
   that will run the workload from the secure network. If you haven't created the user
   yet, you can [create the user](getting-started-workloads.md "getting-started-workloads.md")
   now.
3. On the user **Details** page, choose the
   **Permissions** tab.
4. Choose **Add permissions** and then select **Create
   inline policy**.
5. In the **Policy editor** section, select
   **JSON** to display the JSON editor.
6. Copy the following IAM policy into the JSON editor, and change the public IPv4
   or IPv6 addresses, or ranges to your needs. You can use [https://checkip.amazonaws.com/](https://checkip.amazonaws.com/ "https://checkip.amazonaws.com/") to
   determine your current public IP address. You can specify individual IP addresses, or
   ranges of IP addresses using slash notation. For more information, see [aws:SourceIp](reference_policies_condition-keys.md#condition-keys-sourceip "reference_policies_condition-keys.md#condition-keys-sourceip").

###### Note

The IP addresses must not be obfuscated by a VPN or a proxy server.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid":"IpRestrictionIAMPolicyForIAMUser",
 "Effect": "Deny",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "NotIpAddress": {
 "aws:SourceIp": [
 "203.0.113.0/24",
 "2001:DB8:1234:5678::/64",
 "203.0.114.1"
 ]
 },
 "BoolIfExists": {
 "aws:ViaAWSService": "false"
 }
 }
 }
 ]
}`

```

This policy example denies the use of an IAM user’s access keys with this policy
applied, unless the request originated from the networks (specified in CIDR notation)
“203.0.113.0/24”, “2001:DB8:1234:5678::/64”, or the specific IP address “203.0.114.1” 7. Select **Next** to proceed to the **Review and
create** page. In **Policy** details, under
**Policy name** enter a name for the policy and then choose
**Create policy**.
After the policy is created, it's displayed on the **Permissions** tab
for the user.

You could also apply this policy as a service control policy (SCP) across multiple AWS
accounts in AWS Organizations, we recommend using an additional condition,
`aws:PrincipalArn` to make this policy statement only apply to IAM users
within the AWS accounts subject to this SCP. The following policy is includes that
update:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IpRestrictionServiceControlPolicyForIAMUsers",
 "Effect": "Deny",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "NotIpAddress": {
 "aws:SourceIp": [
 "203.0.113.0/24",
 "2001:DB8:1234:5678::/64",
 "203.0.114.1"
 ]
 },
 "BoolIfExists": {
 "aws:ViaAWSService": "false"
 },
 "ArnLike": {
 "aws:PrincipalArn": "arn:aws:iam::*:user/*"
 }
 }
 }
 ]
}`

```
