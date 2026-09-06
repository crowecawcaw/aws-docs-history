

# sagemaker-notebook-instance-platform-version
<a name="sagemaker-notebook-instance-platform-version"></a>

Checks if a Sagemaker Notebook Instance is configured to use a supported platform identifier version. The rule is NON\_COMPLIANT if a Notebook Instance is not using the specified supported platform identifier version as specified in the parameter. 



**Identifier:** SAGEMAKER\_NOTEBOOK\_INSTANCE\_PLATFORM\_VERSION

**Resource Types:** AWS::SageMaker::NotebookInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

supportedPlatformIdentifierVersionsType: CSV  
Comma-separated list of the supported platform identifier version for the rule to check.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1497c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).