

# Modify a Verified Access endpoint policy

Use the following procedures to modify the policy for a Verified Access endpoint. After you make the changes, it takes several minutes before they take effect.

**Note**  
If you create an endpoint in a Verified Access group that another account shared with you, the owner of the group can also view, modify, and turn off the endpoint policy. For more information, see [Share a Verified Access group with another AWS account](sharing-groups.md).

**To modify a Verified Access endpoint policy using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access endpoints**.

1. Select the endpoint.

1. Choose **Actions**, **Modify Verified Access endpoint policy**.

1. (Optional) Turn on or off **Enable policy** as needed.

1. (Optional) For **Policy**, enter the Verified Access policy to apply to the endpoint.

1. Choose **Modify Verified Access endpoint policy**.

**To modify a Verified Access endpoint policy using the AWS CLI**  
Use the [modify-verified-access-endpoint-policy](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-verified-access-endpoint-policy.html) command.