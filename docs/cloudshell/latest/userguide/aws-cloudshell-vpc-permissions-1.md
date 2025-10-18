# Required IAM permissions for creating and
 using CloudShell VPC environments

To create and use CloudShell VPC environments, the IAM administrator must enable
 access to VPC specific Amazon EC2 permissions. This section lists the Amazon EC2
 permissions needed to create and use VPC environments.


 To create VPC environments, the IAM policy assigned to your role must include the following Amazon EC2 permissions:
 


* `ec2:DescribeVpcs`
* `ec2:DescribeSubnets`
* `ec2:DescribeSecurityGroups`
* `ec2:DescribeDhcpOptions`
* `ec2:DescribeNetworkInterfaces`

* `ec2:CreateTags`
* `ec2:CreateNetworkInterface`
* `ec2:CreateNetworkInterfacePermission`
We recommend to include: 


* **ec2:DeleteNetworkInterface**
###### Note

This permission is not mandatory, but this is required for CloudShell to clean up the ENI
 resource (ENIs created for CloudShell VPC environments are tagged with
 **ManagedByCloudShell** key) created by it. If this permission not in
 enabled, you must manually clean up the ENI resource after every CloudShell VPC
 environment use.


## IAM policy granting full
 CloudShell access including access to VPC


The following example displays how to enable full permissions, including access to
 VPC, to CloudShell:



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "AllowCloudShellOperations",
 "Effect": "Allow",
 "Action": [
 "cloudshell:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowDescribeVPC",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeVpcs"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowInspectVPCConfigurationViaCloudShell",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeNetworkInterfaces"
 ],
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "cloudshell.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AllowCreateTagWithCloudShellKeyViaCloudShell",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:*:*:network-interface/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateNetworkInterface"
 },
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "ManagedByCloudShell",
 "aws:CalledVia": "cloudshell.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AllowCreateNetworkInterfaceWithSubnetsAndSGViaCloudShell",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": [
 "arn:aws:ec2:*:*:subnet/*",
 "arn:aws:ec2:*:*:security-group/*"
 ],
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "cloudshell.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AllowCreateNetworkInterfaceWithCloudShellTagViaCloudShell",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface"
 ],
 "Resource": "arn:aws:ec2:*:*:network-interface/*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:TagKeys": "ManagedByCloudShell",
 "aws:CalledVia": "cloudshell.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AllowCreateNetworkInterfacePermissionWithCloudShellTagViaCloudShell",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterfacePermission"
 ],
 "Resource": "arn:aws:ec2:*:*:network-interface/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/ManagedByCloudShell": ""
 },
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "cloudshell.amazonaws.com"
 }
 }
 },
 {
 "Sid": "AllowDeleteNetworkInterfaceWithCloudShellTagViaCloudShell",
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteNetworkInterface"
 ],
 "Resource": "arn:aws:ec2:*:*:network-interface/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/ManagedByCloudShell": ""
 },
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "cloudshell.amazonaws.com"
 }
 }
 }
 ]
}`

```





## Using IAM condition keys for VPC
 environments


You can use CloudShell-specific condition keys for VPC settings to provide
 additional permission controls for your VPC environments. You can also specify the subnets
 and security groups that the VPC environment can and can't use. 


CloudShell supports the following condition keys in IAM policies:



* `CloudShell:VpcIds` – Allow or deny one or more VPCs
* `CloudShell:SubnetIds` – Allow or deny one or more subnets
* `CloudShell:SecurityGroupIds` – Allow or deny one or more security groups

###### Note

If the permissions for users with access to public CloudShell environments are
 modified to add restriction to the `cloudshell:createEnvironment` action, they
 can still access their existing public environment. However, if you want to modify an
 IAM policy with this restriction and disable their access to the existing public
 environment, you must first update the IAM policy with the restriction, and then ensure
 that every CloudShell user in your account manually deletes the existing public
 environment using the CloudShell web user interface (**Actions** →
 **Delete CloudShell environment**).


## Example policies with condition keys for VPC settings


The following examples demonstrate how to use condition keys for VPC settings. After you create a policy statement with the desired restrictions, append the policy statement for the target user or role.


### Ensure that users create only
 VPC environments and deny creation of public environments


To ensure that users can create only VPC environments, use the deny permission as
 shown in the following example: 



```
{
  "Statement": [
    {
      "Sid": "DenyCloudShellNonVpcEnvironments",
      "Action": [
        "cloudshell:CreateEnvironment"
      ],
      "Effect": "Deny",
      "Resource": "*",
      "Condition": {
        "Null": {
          "cloudshell:VpcIds": "true"
        }
      }
    }
  ]
}
```

### Deny users access to specific
 VPCs, subnets, or security groups


To deny users access to specific VPCs, use `StringEquals` to check the
 value of the `cloudshell:VpcIds` condition. The following example denies
 users access to `vpc-1` and `vpc-2`:


To deny users access to specific VPCs, use `StringEquals` to check the value of
 the `cloudshell:SubnetIds` condition. The following example denies users access to
 `subnet-1` and `subnet-2`:


To deny users access to specific VPCs, use `StringEquals` to check the value of
 the `cloudshell:SecurityGroupIds` condition. The following example denies users
 access to `sg-1` and `sg-2`:



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "EnforceOutOfSecurityGroups",
 "Action": [
 "cloudshell:CreateEnvironment"
 ],
 "Effect": "Deny",
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "cloudshell:SecurityGroupIds": [
 "sg-1",
 "sg-2"
 ]
 }
 }
 }
 ]
}`

```





### Allow users to create environments with specific VPC configurations


To allow users access to specific VPCs, use `StringEquals` to check the
 value of the `cloudshell:VpcIds` condition. The following example allows
 users access to `vpc-1` and `vpc-2`:


To allow users access to specific VPCs, use `StringEquals` to check the
 value of the `cloudshell:SubnetIds` condition. The following example allows
 users access to `subnet-1` and `subnet-2`:



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "EnforceStayInSpecificSubnets",
 "Action": [
 "cloudshell:CreateEnvironment"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "ForAllValues:StringEquals": {
 "cloudshell:SubnetIds": [
 "subnet-1",
 "subnet-2"
 ]
 }
 }
 }
 ]
}`

```





To allow users access to specific VPCs, use `StringEquals` to check the
 value of the `cloudshell:SecurityGroupIds` condition. The following example
 allows users access to `sg-1` and `sg-2`:



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "EnforceStayInSpecificSecurityGroup",
 "Action": [
 "cloudshell:CreateEnvironment"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "ForAllValues:StringEquals": {
 "cloudshell:SecurityGroupIds": [
 "sg-1",
 "sg-2"
 ]
 }
 }
 }
 ]
}`

```
