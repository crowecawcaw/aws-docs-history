# Serverless endpoint creation

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

To create a serverless endpoint, you can use the Amazon SageMaker AI console, the APIs, or the AWS CLI.
You can create a serverless endpoint using a similar process as a [real-time endpoint](realtime-endpoints.md "realtime-endpoints.md").

###### Topics

- [Create a model](serverless-endpoints-create-model.md "serverless-endpoints-create-model.md")
- [Create an endpoint configuration](serverless-endpoints-create-config.md "serverless-endpoints-create-config.md")
- [Create an endpoint](serverless-endpoints-create-endpoint.md "serverless-endpoints-create-endpoint.md")
