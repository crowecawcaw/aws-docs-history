# Update AWS Transit Gateway security group inbound rules

You can update any of the inbound security group rules associated with a transit gateway. You can update security group rules using either the Amazon VPC Console console or by using the command-line or API. For more
information about security group referencing, see [Security group referencing](tgw-vpc-attachments.md#vpc-attachment-security "tgw-vpc-attachments.md#vpc-attachment-security").

###### To update your security group rules using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Security groups**.
3. Select the security group, and choose **Actions**,
   **Edit inbound rules** to modify the inbound rules.
4. To add a rule, choose **Add rule** and specify the type,
   protocol, and port range. For **Source** (inbound rule),
   enter the ID of the security group in the VPC connected to the transit
   gateway.

###### Note

Security groups in a VPC connected to the transit gateway are not automatically displayed. 5. To edit an existing rule, change its values (for example, the source or the description). 6. To delete a rule, choose **Delete** next to the rule. 7. Choose **Save rules**.

###### To update inbound rules using the command line

- [authorize-security-group-ingress](../../../cli/latest/reference/ec2/authorize-security-group-ingress.md "../../../cli/latest/reference/ec2/authorize-security-group-ingress.md") (AWS CLI)
- [Grant-EC2SecurityGroupIngress](../../../powershell/latest/reference/items/Grant-EC2SecurityGroupIngress.md "../../../powershell/latest/reference/items/Grant-EC2SecurityGroupIngress.md") (AWS Tools for Windows PowerShell)
- [Revoke-EC2SecurityGroupIngress](../../../powershell/latest/reference/items/Revoke-EC2SecurityGroupIngress.md "../../../powershell/latest/reference/items/Revoke-EC2SecurityGroupIngress.md") (AWS Tools for Windows PowerShell)
- [revoke-security-group-ingress](../../../cli/latest/reference/ec2/revoke-security-group-ingress.md "../../../cli/latest/reference/ec2/revoke-security-group-ingress.md") (AWS CLI)
