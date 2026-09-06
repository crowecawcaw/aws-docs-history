

# Modify a Verified Access group policy
<a name="modify-verified-access-group-policy"></a>

AWS Verified Access allows access to your applications based on the access policies that you create. The Verified Access policy that you attach to a group is inherited by all endpoints in the group. You can optionally attach application-specific policies to specific endpoints.

Use the following procedure to modify the policy for a Verified Access group. After you make the changes, it takes several minutes before they take effect.

**To modify a Verified Access group policy using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access groups**.

1. Select the group.

1. Choose **Actions**, **Modify Verified Access group policy**.

1. (Optional) Turn on or off **Enable policy** as needed.

1. (Optional) For **Policy**, enter the Verified Access policy to apply to the group.

1. Choose **Modify Verified Access group policy**.

**To modify a Verified Access group policy using the AWS CLI**  
Use the [modify-verified-access-group-policy](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-verified-access-group-policy.html) command.