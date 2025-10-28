# Service role requirements for model evaluation jobs

To create a model evaluation job, you must specify a service role.

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

The required IAM actions and resource depend on the type of model evaluation job you are creating. Use the following sections to learn more about the required Amazon Bedrock,Amazon SageMaker AI, and Amazon S3 IAM actions, service principals, and resources. You can optionally choose to encrypt your data using AWS Key Management Service.

###### Topics

- [Service role requirements for automatic model evaluation jobs](automatic-service-roles.md "automatic-service-roles.md")
- [Service role requirements for human-based model evaluation jobs](model-eval-service-roles.md "model-eval-service-roles.md")
- [Required service role permissions for creating a model evaluation job that uses a judge model](judge-service-roles.md "judge-service-roles.md")
- [Service role requirements for knowledge base
  evaluation jobs](rag-eval-service-roles.md "rag-eval-service-roles.md")
