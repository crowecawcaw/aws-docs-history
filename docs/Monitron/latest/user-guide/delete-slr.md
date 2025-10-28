Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Deleting a service-linked role for

Amazon Monitron

You don't need to manually delete the AWSServiceRoleForMonitron[\_{SUFFIX}] role. When you
delete a Amazon Monitron project that you created through Amazon Monitron in the AWS Management Console, Amazon Monitron cleans up the
resources and deletes the service-linked role for you.

You can also use the IAM console, the AWS CLI or the AWS API to manually
delete the service-linked role. To do this, you must first manually clean up the
resources for your service-linked role and then you can manually delete
it.

###### Note

If the Amazon Monitron service is using the role when you try to delete the
resources, then the deletion might fail. If that happens, wait for a few
minutes and try the operation again.

###### To delete Amazon Monitron resources used by the AWSServiceRoleForMonitron[\_{SUFFIX}]

- Delete Amazon Monitron projects using this service-linked role.
  **To manually delete the service-linked role using
  IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForMonitron[\_{SUFFIX}]
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.
