

# encrypted-volumes
<a name="encrypted-volumes"></a>

Checks if attached Amazon EBS volumes are encrypted and optionally are encrypted with a specified KMS key. The rule is NON\_COMPLIANT if attached EBS volumes are unencrypted or are encrypted with a KMS key not in the supplied parameters. 



**Identifier:** ENCRYPTED\_VOLUMES

**Resource Types:** AWS::EC2::Volume

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

kmsId (Optional)Type: String  
ID or ARN of the KMS key that is used to encrypt the volume.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d815c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).