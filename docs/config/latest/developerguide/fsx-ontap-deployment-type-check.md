

# fsx-ontap-deployment-type-check
<a name="fsx-ontap-deployment-type-check"></a>

Checks if Amazon FSx for NetApp ONTAP file systems are configured with certain deployment types. The rule is NON\_COMPLIANT if the Amazon FSx for NetApp ONTAP file systems are not configured with the deployment types you specify. 



**Identifier:** FSX\_ONTAP\_DEPLOYMENT\_TYPE\_CHECK

**Resource Types:** AWS::FSx::FileSystem

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

deploymentTypesType: CSV  
Comma-separated list of allowed Deployment types for the rule to check. 

## AWS CloudFormation template
<a name="w2aac20c16c17b7d859c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).