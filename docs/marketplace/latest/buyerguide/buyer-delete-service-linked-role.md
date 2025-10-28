# Deleting a service-linked role

for AWS Marketplace

If you no longer need to use a feature or service that requires a service-linked
role, we recommend that you delete that role. That way you don’t have an unused
entity that is not actively monitored or maintained. However, you must clean up the
resources for your service-linked role before you can manually delete it.

###### Note

If the AWS Marketplace service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try
the operation again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the
`AWSServiceRoleForMarketplaceLicenseManagement`
service-linked role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_ .
