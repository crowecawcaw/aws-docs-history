

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Data perimeters in AWS Systems Manager
<a name="data-perimeters"></a>

A data perimeter is a set of preventive guardrails in your AWS environment that help make sure your data can only be accessed by trusted identities from expected networks and resources. When you implement data perimeter controls, you might need to include exceptions for AWS service-owned resources that Systems Manager accesses on your behalf.

**Example scenario: SSM document categories S3 bucket**  
Systems Manager accesses an AWS managed S3 bucket to retrieve document category information for [AWS Systems Manager Documents](documents.md). This bucket contains metadata about document categories that help organize and classify SSM Documents in the console.

Resource ARN pattern  
`arn:aws:s3:::ssm-document-categories-{{region}}`  
Regional examples:  
+ `arn:aws:s3:::ssm-document-categories-us-east-1`
+ `arn:aws:s3:::ssm-document-categories-us-west-2`
+ `arn:aws:s3:::ssm-document-categories-eu-west-1`
+ `arn:aws:s3:::ssm-document-categories-ap-northeast-1`

When accessed  
This resource is accessed when you view SSM Documents in the Systems Manager console or when using APIs that retrieve document metadata and categories.

Data stored  
The bucket contains JSON files with document category definitions and metadata. This data is read-only and does not contain customer-specific information.

Identity used  
Systems Manager accesses this resource using AWS service credentials on behalf of your requests.

Required permissions  
`s3:GetObject` on the bucket contents.

**Data perimeter policy considerations**  
When implementing data perimeter controls using Service Control Policies (SCPs) or VPC endpoint policies with conditions like `aws:ResourceOrgID`, you need to create exceptions for the AWS service-owned resources that Systems Manager requires.

For example, if you're using an SCP with `aws:ResourceOrgID` to restrict access to resources outside your organization, you would need to add an exception for the SSM Document categories bucket.

The policy would need to access to resources outside your organization but include an exception for the appropriate S3 buckets, allowing Systems Manager to continue functioning properly.

Similarly, if you're using VPC endpoint policies to restrict S3 access, you would need to make sure that the SSM document categories buckets are accessible through your VPC endpoints.

**Example scenario: Hybrid node registration APIs**  
Hybrid nodes don't natively belong to an AWS account – they are registered to one. Because of this, the `ssm:RegisterManagedInstance`, `ssm:RequestManagedInstanceRoleToken`, and `ssm:UpdateManagedInstancePublicKey` APIs don't use AWS Signature Version 4 (SigV4) when authenticating hybrid nodes.

As a result, policy evaluation can't access an AWS principal identity or global context keys such as `aws:PrincipalOrgId`, `aws:PrincipalAccount`, and `aws:SourceAccount`. Service control policies (SCPs) and VPC endpoint policies that rely on these global keys or on AWS principal identity might block these three APIs when hybrid nodes attempt to register. This can prevent hybrid nodes from completing registration.

To restrict access to these APIs based on account or organization membership, use the following Systems Manager condition keys, which resolve consistently for both Amazon EC2 instances and hybrid nodes:
+ `ssm:NodeAccountId` – Resolves to the account in which an Amazon EC2 instance exists, or the account to which a hybrid node is registered.
+ `ssm:NodeOrgId` – Resolves to the organization that owns the Amazon EC2 instance's account, or the organization of the account to which a hybrid node is registered.

**More information**  
For more information about data perimeters in AWS, see the following topics:
+ [Data perimeters on AWS](https://aws.amazon.com/identity/data-perimeters-on-aws/).
+ [Establish permissions guardrails using data perimeters](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_data-perimeters.html) in the *IAM User Guide*
+ [Service-specific guidance: AWS Systems Manager](https://github.com/aws-samples/data-perimeter-policy-examples/blob/main/service_specific_guidance/ssm-specific-guidance.md) and [Service-owned resources](https://github.com/aws-samples/data-perimeter-policy-examples/blob/main/service_owned_resources.md) in the *AWS Samples* repository on GitHub