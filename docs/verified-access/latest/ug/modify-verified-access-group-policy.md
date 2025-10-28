# Modify a Verified Access group policy

AWS Verified Access allows access to your applications based on the access policies
that you create. The Verified Access policy that you attach to a group is inherited by all
endpoints in the group. You can optionally attach application-specific policies
to specific endpoints.

Use the following procedure to modify the policy for a Verified Access group. After you
make the changes, it takes several minutes before they take effect.

###### To modify a Verified Access group policy using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Verified Access groups**.
3. Select the group.
4. Choose **Actions**, **Modify Verified Access group policy**.
5. (Optional) Turn on or off **Enable policy** as needed.
6. (Optional) For **Policy**, enter the Verified Access policy to apply to the
   group.
7. Choose **Modify Verified Access group policy**.

###### To modify a Verified Access group policy using the AWS CLI

Use the [modify-verified-access-group-policy](../../../cli/latest/reference/ec2/modify-verified-access-group-policy.md "../../../cli/latest/reference/ec2/modify-verified-access-group-policy.md") command.
