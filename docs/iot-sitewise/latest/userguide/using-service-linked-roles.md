# Use service-linked roles for AWS IoT SiteWise

AWS IoT SiteWise uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md"). A service-linked role is a unique type of IAM role that is
linked directly to AWS IoT SiteWise. service-linked roles are predefined by AWS IoT SiteWise and
include all the permissions that the service requires to call other AWS services on your
behalf.

Service-linked roles simplify the configuration of AWS IoT SiteWise by automatically including all
necessary permissions. AWS IoT SiteWise defines the permissions of its service-linked roles, and
unless defined otherwise, only AWS IoT SiteWise can assume its roles. The defined permissions
include the trust policy and the permissions policy. And that permissions policy can't be
attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your AWS IoT SiteWise resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked Role** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

###### Topics

- [Service-linked role permissions](service-linked-role-permissions.md "service-linked-role-permissions.md")
- [Create a service-linked role](create-service-linked-role.md "create-service-linked-role.md")
- [Update a service-linked role](edit-service-linked-role.md "edit-service-linked-role.md")
- [Delete a service-linked role](delete-service-linked-role.md "delete-service-linked-role.md")
- [Supported regions](#slr-regions "#slr-regions")
- [Use service roles for SiteWise Monitor](monitor-service-role.md "monitor-service-role.md")

## Supported Regions for AWS IoT SiteWise service-linked roles

AWS IoT SiteWise supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS IoT SiteWise Endpoints and Quotas](../../../general/latest/gr/iot-sitewise.md "../../../general/latest/gr/iot-sitewise.md").
