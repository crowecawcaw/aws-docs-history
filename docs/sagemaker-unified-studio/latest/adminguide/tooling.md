

# Tooling blueprints in Amazon SageMaker Unified Studio
<a name="tooling"></a>

Every Amazon SageMaker Unified Studio project deploys a Tooling environment first. Tooling provisions the project's Amazon S3 storage, the IAM role for project execution, and a collection of default Amazon DataZone connections. Tooling also provisions AWS resources commonly used within projects, such as Amazon Athena workgroups and AWS Lake Formation permissions.

All blueprints in Amazon SageMaker Unified Studio provision an AWS CloudFormation template using an IAM role designated as the provisioning role. After a project becomes active, you need an IAM role designated as the project user role to run the project. The following table gives the name of each role in an IAM-based domain and in an Identity Center-based domain.


| IAM role | IAM-based domain | Identity Center-based domain | 
| --- | --- | --- | 
| Provisioning | AmazonSageMakerAdminIAMExecutionRole | AmazonSageMakerProvisioning-{{accountId}} | 
| Project user | AmazonSageMakerUserIAMExecutionRole | datazone\_usr\_role\_{{projectId}}\_{{environmentId}} | 

Depending on the type of domain, Amazon SageMaker Unified Studio provides AWS managed policies that can be attached to the provisioning or project user roles to grant full permissions. The following table gives the managed policy for each role in an IAM-based domain and in an Identity Center-based domain.


| IAM role | IAM-based domain | Identity Center-based domain | 
| --- | --- | --- | 
| Provisioning | [AWS policy: SageMakerStudioAdminIAMPermissiveExecutionPolicy](security-iam-awsmanpol-SageMakerStudioAdminIAMPermissiveExecutionPolicy.md) | [AWS policy: SageMakerStudioProjectProvisioningRolePolicy](security-iam-awsmanpol-SageMakerStudioProjectProvisioningRolePolicy.md) | 
| Project user | [AWS policy: SageMakerStudioUserIAMPermissiveExecutionPolicy](security-iam-awsmanpol-SageMakerStudioUserIAMPermissiveExecutionPolicy.md) | [AWS policy: SageMakerStudioProjectUserRolePolicy](security-iam-awsmanpol-SageMakerStudioProjectUserRolePolicy.md) | 

Tooling provisions the default connections that every project requires. The set of connections differs between an IAM-based domain and an Identity Center-based domain. The name of each connection differs too.


| Default connection | IAM-based domain | Identity Center-based domain | 
| --- | --- | --- | 
| Amazon Athena (Spark) | serverless.spark | serverless.spark | 
| Amazon Athena (SQL) | default.sql | project.athena | 
| Amazon S3, default folder | default.s3\_project | project.s3\_default\_folder | 
| Amazon S3, root | default.s3 | — | 
| Amazon S3, shared folder | default.s3\_shared | default.s3\_shared | 
| AWS Glue (Spark) | default.spark | project.spark.compatibility, project.spark.fineGrained | 
| AWS IAM | default.iam | project.iam | 
| Data catalog | default.catalog | project.default\_lakehouse | 
| Workflows | default.workflow\_serverless | default.workflow\_serverless | 

Enable the managed Tooling blueprint for your domain on the Blueprints page. Tooling has parameters you can set, and a permissions boundary you can apply to the roles it creates. For both, see [Manage Tooling blueprint parameters](manage-tooling-blueprint.md).

**Topics**
+ [Custom blueprints as Tooling](tooling-custom-blueprints.md)
+ [Tooling capabilities](tooling-capabilities.md)
+ [Compatibility with managed blueprints](tooling-managed-compatibility.md)