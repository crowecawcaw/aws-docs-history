

# Identify AWS Transit Gateway referenced security groups
<a name="tgw-sg-updates-identify"></a>

To determine if your security group is being referenced in the rules of a security group in a VPC attached to the same transit gateway, use one of the following commands.
+ [describe-security-group-references](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-security-group-references.html) (AWS CLI)
+ [Get-EC2SecurityGroupReference](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2SecurityGroupReference.html) (AWS Tools for Windows PowerShell)