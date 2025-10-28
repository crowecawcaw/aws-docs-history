# Configuring IAM permissions for

AWS Glue

You use AWS Identity and Access Management (IAM) to define policies and roles that AWS Glue uses to
access resources. The following steps lead you through various options for setting up the
permissions for AWS Glue. Depending on your business needs, you might have to add or reduce
access to your resources.

###### Note

To get started with basic IAM permissions for AWS Glue instead, see [Setting up IAM permissions for AWS Glue](set-up-iam.md "set-up-iam.md").

1. [Create an IAM policy for the AWS Glue service](create-service-policy.md "create-service-policy.md"):
   Create a service policy that allows access to AWS Glue resources.
2. [Create an IAM role for AWS Glue](create-an-iam-role.md "create-an-iam-role.md"): Create an IAM
   role, and attach the AWS Glue service policy and a policy for your Amazon Simple Storage Service (Amazon S3)
   resources that are used by AWS Glue.
3. [Attach a policy to users or groups that access
   AWS Glue](attach-policy-iam-user.md "attach-policy-iam-user.md"): Attach policies to any users or groups that sign in to the AWS Glue
   console.
4. [Create an IAM policy for notebooks](create-notebook-policy.md "create-notebook-policy.md"): Create a
   notebook server policy to use in the creation of notebook servers on development
   endpoints.
5. [Create an IAM role for notebooks](create-an-iam-role-notebook.md "create-an-iam-role-notebook.md"): Create
   an IAM role and attach the notebook server policy.
6. [Create an IAM policy for
   Amazon SageMaker AI notebooks](create-sagemaker-notebook-policy.md "create-sagemaker-notebook-policy.md"): Create an IAM policy to use when creating Amazon SageMaker AI
   notebooks on development endpoints.
7. [Create an IAM role for
   Amazon SageMaker AI notebooks](create-an-iam-role-sagemaker-notebook.md "create-an-iam-role-sagemaker-notebook.md"): Create an IAM role and attach the policy to grant
   permissions when creating Amazon SageMaker AI notebooks on development endpoints.
