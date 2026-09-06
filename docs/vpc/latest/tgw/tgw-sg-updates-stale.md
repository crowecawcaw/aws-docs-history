

# Remove stale AWS Transit Gateway security group rules
<a name="tgw-sg-updates-stale"></a>

A stale security group rule is a rule that references a deleted security group in the same VPC or in VPC attached to the same transit gateway. When a security group rule becomes stale, it's not automatically removed from your security group—you must manually remove it.

You can view and delete the stale security group rules for a VPC using the Amazon VPC console.

**To view and delete stale security group rules**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security groups**.

1. Choose **Actions**, **Manage stale rules**.

1. For **VPC**, choose the VPC with the stale rules.

1. Choose **Edit**.

1. Choose the **Delete** button next to the rule that you want to delete. Choose **Preview changes**, **Save rules**.

**To describe your stale security group rules using the command line**
+ [describe-stale-security-groups](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-stale-security-groups.html) (AWS CLI)
+ [Get-EC2StaleSecurityGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2StaleSecurityGroup.html) (AWS Tools for Windows PowerShell)

After you've identified the stale security group rules, you can delete them using the [revoke-security-group-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/revoke-security-group-ingress.html) or [revoke-security-group-egress](https://docs.aws.amazon.com/cli/latest/reference/ec2/revoke-security-group-egress.html) commands.