

# efs-mount-target-public-accessible
<a name="efs-mount-target-public-accessible"></a>

Checks if an Amazon Elastic File System (Amazon EFS) is associated with subnets that assign public IP addresses on launch. The rule is NON\_COMPLIANT if the Amazon EFS mount target is associated with subnets that assign public IP addresses on launch. 



**Identifier:** EFS\_MOUNT\_TARGET\_PUBLIC\_ACCESSIBLE

**Resource Types:** AWS::EFS::FileSystem

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China (Beijing), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d709c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).