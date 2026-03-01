# Control access to a REST API with API Gateway resource policies

Amazon API Gateway _resource policies_ are JSON policy documents that you attach to an API to control
whether a specified principal (typically an IAM role or group) can invoke the API. You can use API Gateway
resource policies to allow your API to be securely invoked by:

- Users from a specified AWS account.
- Specified source IP address ranges or CIDR blocks.
- Specified virtual private clouds (VPCs) or VPC endpoints (in any account).
  You can attach a resource
  policy for any API endpoint type in API Gateway by using the AWS Management Console, AWS CLI, or AWS SDKs. For [private
  APIs](apigateway-private-apis.md "apigateway-private-apis.md"), you can use resource policies together with VPC endpoint policies to control
  which principals have access to which resources and actions. For more information, see [Use VPC endpoint policies for private APIs in API Gateway](apigateway-vpc-endpoint-policies.md "apigateway-vpc-endpoint-policies.md").

API Gateway resource policies are different from IAM identity-based policies. IAM identity-based policies are
attached to IAM users, groups, or roles and define what actions those identities are capable of doing on which
resources. API Gateway resource policies are attached to resources. You can use API Gateway resource policies together with IAM
policies. For more information,
see [Identity-Based Policies and Resource-Based
Policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md").

###### Topics

- [Access policy language overview for Amazon API Gateway](apigateway-control-access-policy-language-overview.md "apigateway-control-access-policy-language-overview.md")
- [How API Gateway resource policies affect authorization workflow](apigateway-authorization-flow.md "apigateway-authorization-flow.md")
- [API Gateway resource policy examples](apigateway-resource-policies-examples.md "apigateway-resource-policies-examples.md")
- [Create and attach an API Gateway resource policy to an API](apigateway-resource-policies-create-attach.md "apigateway-resource-policies-create-attach.md")
- [AWS condition keys that can be used in API Gateway resource policies](apigateway-resource-policies-aws-condition-keys.md "apigateway-resource-policies-aws-condition-keys.md")
