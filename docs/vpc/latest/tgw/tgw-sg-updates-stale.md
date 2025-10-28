# Remove stale AWS Transit Gateway security group rules

A stale security group rule is a rule that references a deleted security group in
the same VPC or in VPC attached to the same transit gateway. When a security group rule becomes
stale, it's not automatically removed from your security group—you must manually
remove it.

You can view and delete the stale security group rules for a VPC using the Amazon VPC
console.

###### To view and delete stale security group rules

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Security groups**.
3. Choose **Actions**, **Manage stale rules**.
4. For **VPC**, choose the VPC with the stale rules.
5. Choose **Edit**.
6. Choose the **Delete** button next to the rule that you want to delete.
   Choose **Preview changes**, **Save
   rules**.

###### To describe your stale security group rules using the command line

- [describe-stale-security-groups](../../../cli/latest/reference/ec2/describe-stale-security-groups.md "../../../cli/latest/reference/ec2/describe-stale-security-groups.md") (AWS CLI)
- [Get-EC2StaleSecurityGroup](../../../powershell/latest/reference/items/Get-EC2StaleSecurityGroup.md "../../../powershell/latest/reference/items/Get-EC2StaleSecurityGroup.md") (AWS Tools for Windows PowerShell)
  After you've identified the stale security group rules, you can delete them using
  the [revoke-security-group-ingress](../../../cli/latest/reference/ec2/revoke-security-group-ingress.md "../../../cli/latest/reference/ec2/revoke-security-group-ingress.md") or [revoke-security-group-egress](../../../cli/latest/reference/ec2/revoke-security-group-egress.md "../../../cli/latest/reference/ec2/revoke-security-group-egress.md") commands.
