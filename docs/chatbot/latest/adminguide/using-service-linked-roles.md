AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Using Service-Linked Roles for

Amazon Q Developer in chat applications

A [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is a type of IAM role that links directly to an AWS service.
It gives AWS services the permissions to access resources in other services to complete
actions on your behalf.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column.
Choose any **Yes** entry with a link to view the service-linked role
documentation for that service.

When you create an Amazon Q Developer in chat applications resource in the Amazon Q Developer in chat applications console, you can also choose to provide a list of
one or more SNS topics to associate with the new resource. Amazon Q Developer in chat applications automatically uses the
**AWSServiceRoleForAWSChatbot** service-linked role to add or remove subscriptions to the Amazon Q Developer in chat applications global Amazon SNS subscription endpoint.

The service-linked role makes setting up Amazon Q Developer in chat applications easier because you don’t have to manually add
the necessary permissions. Amazon Q Developer in chat applications defines the permissions for the service-linked role and only
Amazon Q Developer in chat applications can assume that role. The permissions include a trust policy and a permissions policy,
which apply only to the Amazon Q Developer in chat applications service.

###### Topics

- [Amazon Q Developer in chat applications Service-linked role for performing operations on Amazon SNS topics and CloudWatch Logs](slr-permissions.md "slr-permissions.md")
