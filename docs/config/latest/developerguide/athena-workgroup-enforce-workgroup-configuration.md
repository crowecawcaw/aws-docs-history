

# athena-workgroup-enforce-workgroup-configuration
<a name="athena-workgroup-enforce-workgroup-configuration"></a>

Checks if Amazon Athena workgroups using Athena engine enforce workgroup configuration to override client-side settings. The rule is NON\_COMPLIANT if configuration.WorkGroupConfiguration.EnforceWorkGroupConfiguration is false. 



**Identifier:** ATHENA\_WORKGROUP\_ENFORCE\_WORKGROUP\_CONFIGURATION

**Resource Types:** AWS::Athena::WorkGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d209c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).