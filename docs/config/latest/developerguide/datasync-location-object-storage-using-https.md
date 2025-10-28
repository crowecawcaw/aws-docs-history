# datasync-location-object-storage-using-https

Checks if AWS DataSync location object storage servers use the HTTPS protocol to communicate. The rule is NON_COMPLIANT if configuration.ServerProtocol is not 'HTTPS'.

**Identifier:** DATASYNC_LOCATION_OBJECT_STORAGE_USING_HTTPS

**Resource Types:** AWS::DataSync::LocationObjectStorage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
