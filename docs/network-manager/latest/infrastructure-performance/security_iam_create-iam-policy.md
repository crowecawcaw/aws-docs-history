# Allow IAM users or groups to access

Infrastructure Performance

Any user user that signs in to the AWS Management Console or AWS Command Line Interface (AWS CLI) must have permissions to
access specific resources. You provide those permissions by using AWS Identity and Access Management (IAM), through
policies.

The following procedure shows you how to attach an IAM policy to a user or group that
allows full access to Infrastructure Performance.

###### Note

We recommend creating a new IAM policy that grants only the permissions necessary to
use Infrastructure Performance.

## Create an IAM policy

Create a policy that provides users full access to Infrastructure Performance. Then attach the policy to
a user or group.

###### To create and attach an IAM policy using the console

1. Sign in to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") with administrator
   credentials.
2. In the navigation pane, choose **Policies**.
3. In the content pane, choose **Create policy**.
4. Choose the **JSON** tab.
5. Paste the following JSON policy document in the text field.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DisableAwsNetworkPerformanceMetricSubscription",
 "ec2:DescribeAwsNetworkPerformanceMetricSubscriptions",
 "ec2:EnableAwsNetworkPerformanceMetricSubscription",
 "ec2:GetAwsNetworkPerformanceData"
 ],
 "Resource": "*"
 }
 ]
}`

```

When you are finished, choose **Review policy**. 6. On the **Review** page, enter a name for the policy, for example,
`InfrastructurePerformancePolicy`. Optionally, enter a description for
**Description**. 7. In **Summary**, review the policy to see the permissions that it
grants, and then choose **Create policy**. 8. Attach the new policy to your user or group.

For information on attaching a policy to a user, see [Changing permissions for
an IAM user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md") in the _IAM User Guide_. For information on
attaching a policy to a group, see [Attaching a policy to
an IAM Group](../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md "../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md") in the _IAM User Guide_.
