# Using service-linked roles for

AWS Batch

AWS Batch uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS Batch. Service-linked roles are predefined by AWS Batch and
include all the permissions that the service requires to call other AWS services on your
behalf.

AWS Batch uses two different service-linked roles:

- [AWSServiceRoleForBatch](using-service-linked-roles-batch-general.md "using-service-linked-roles-batch-general.md") - For
  AWS Batch operations including compute environments.
- [AWSServiceRoleForAWSBatchWithSagemaker](using-service-linked-roles-batch-sagemaker.md "using-service-linked-roles-batch-sagemaker.md") - For SageMaker AI workload management and queuing.

###### Topics

- [Using roles for AWS Batch](using-service-linked-roles-batch-general.md "using-service-linked-roles-batch-general.md")
- [Using roles for AWS Batch with SageMaker AI](using-service-linked-roles-batch-sagemaker.md "using-service-linked-roles-batch-sagemaker.md")
