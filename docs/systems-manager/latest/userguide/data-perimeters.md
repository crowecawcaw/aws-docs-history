• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Data perimeters in AWS Systems Manager

A data perimeter is a set of preventive guardrails in your AWS environment that help
ensure your data can only be accessed by trusted identities from expected networks and
resources. When you implement data perimeter controls, you might need to include
exceptions for AWS service-owned resources that Systems Manager accesses on your behalf.

###### Example scenario: SSM document categories S3 bucket

Systems Manager accesses an AWS managed S3 bucket to retrieve document category
information for [AWS Systems Manager Documents](documents.md "documents.md"). This bucket
contains metadata about document categories that help organize and classify SSM
Documents in the console.

Resource ARN pattern

`arn:aws:s3:::ssm-document-categories-`region``

Regional examples:

- `arn:aws:s3:::ssm-document-categories-us-east-1`
- `arn:aws:s3:::ssm-document-categories-us-west-2`
- `arn:aws:s3:::ssm-document-categories-eu-west-1`
- `arn:aws:s3:::ssm-document-categories-ap-northeast-1`

When accessed

This resource is accessed when you view SSM Documents in the Systems Manager console
or when using APIs that retrieve document metadata and categories.

Data stored

The bucket contains JSON files with document category definitions and
metadata. This data is read-only and does not contain customer-specific
information.

Identity used

Systems Manager accesses this resource using AWS service credentials on behalf of
your requests.

Required permissions

`s3:GetObject` on the bucket contents.

###### Data perimeter policy considerations

When implementing data perimeter controls using Service Control Policies (SCPs) or
VPC endpoint policies with conditions like `aws:ResourceOrgID`, you need
to create exceptions for the AWS service-owned resources that Systems Manager
requires.

For example, if you're using an SCP with `aws:ResourceOrgID` to restrict
access to resources outside your organization, you would need to add an exception for
the SSM Document categories bucket.

The policy would need to access to resources outside your organization but include an
exception for the appropriate S3 buckets, allowing Systems Manager to continue functioning
properly.

Similarly, if you're using VPC endpoint policies to restrict S3 access, you would need
to ensure that the SSM document categories buckets are accessible through your VPC
endpoints.

###### More information

For more information about data perimeters in AWS, see the following
topics:

- [Data perimeters
  on AWS](https://aws.amazon.com/identity/data-perimeters-on-aws/ "https://aws.amazon.com/identity/data-perimeters-on-aws/").
- [Establish
  permissions guardrails using data perimeters](../../../IAM/latest/UserGuide/access_policies_data-perimeters.md "../../../IAM/latest/UserGuide/access_policies_data-perimeters.md") in the
  _IAM User Guide_
- [Service-specific guidance: AWS Systems Manager](https://github.com/aws-samples/data-perimeter-policy-examples/blob/main/service_specific_guidance/ssm-specific-guidance.md "https://github.com/aws-samples/data-perimeter-policy-examples/blob/main/service_specific_guidance/ssm-specific-guidance.md") and [Service-owned resources](https://github.com/aws-samples/data-perimeter-policy-examples/blob/main/service_owned_resources.md "https://github.com/aws-samples/data-perimeter-policy-examples/blob/main/service_owned_resources.md") in the _AWS Samples_
  repository on GitHub
