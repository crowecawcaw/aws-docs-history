# imagebuilder-imagerecipe-ebs-volumes-encrypted

Checks that all Amazon EBS volumes in EC2 Image Builder image recipe block device mappings have encryption enabled. The rule is NON_COMPLIANT if not all EBS volumes have encryption enabled, or if there are no block device mappings defined.

**Identifier:** IMAGEBUILDER_IMAGERECIPE_EBS_VOLUMES_ENCRYPTED

**Resource Types:** AWS::ImageBuilder::ImageRecipe

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
