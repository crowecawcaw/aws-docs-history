

# codebuild-project-envvar-awscred-check
<a name="codebuild-project-envvar-awscred-check"></a>

Checks if the project contains environment variables AWS\_ACCESS\_KEY\_ID and AWS\_SECRET\_ACCESS\_KEY. The rule is NON\_COMPLIANT when the project environment variables contains plaintext credentials. 



**Identifier:** CODEBUILD\_PROJECT\_ENVVAR\_AWSCRED\_CHECK

**Resource Types:** AWS::CodeBuild::Project

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Jakarta), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7d377c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).