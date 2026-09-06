

# fsx-windows-deployment-type-check
<a name="fsx-windows-deployment-type-check"></a>

Checks if the Amazon FSx for WINDOWS file systems are configured with certain deployment types. The rule is NON\_COMPLIANT if FSx for WINDOWS file systems are not configured with the deployment types you specify. 



**Identifier:** FSX\_WINDOWS\_DEPLOYMENT\_TYPE\_CHECK

**Resource Types:** AWS::FSx::FileSystem

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

deploymentTypesType: CSV  
Comma-separated list of allowed Deployment types for the rule to check. 

## AWS CloudFormation template
<a name="w2aac20c16c17b7d869c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).