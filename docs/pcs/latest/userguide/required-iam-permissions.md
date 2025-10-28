# Required IAM permissions for AWS PCS

The IAM security
principal that you're using must have permissions to work with AWS PCS IAM roles, service
linked roles, AWS CloudFormation, a VPC, and related resources. For more information, see [Identity and Access Management for AWS Parallel Computing Service](security-iam.md "security-iam.md"), and [Create a service-linked
role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md") in the _AWS Identity and Access Management User Guide_. You must complete all steps in
this guide as the same user. To check the current user, run the following command:

```
aws sts get-caller-identity
```
