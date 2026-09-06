

# Using service-linked roles for MediaTailor
<a name="using-service-linked-roles"></a>

AWS Elemental MediaTailor uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to MediaTailor. Service-linked roles are predefined by MediaTailor and include all the permissions that the service requires to call other AWS services on your behalf. 

A service-linked role makes setting up MediaTailor easier because you don’t have to manually add the necessary permissions. MediaTailor defines the permissions of its service-linked roles, and unless defined otherwise, only MediaTailor can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your MediaTailor resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes **in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Supported Regions for MediaTailor service-linked roles
<a name="slr-regions"></a>

MediaTailor supports using service-linked roles in all of the regions where the service is available. For more information, see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/mediatailor.html#mediatailor_region).

**Topics**
+ [Supported Regions for MediaTailor service-linked roles](#slr-regions)
+ [Service-linked role permissions for MediaTailor](slr-permissions.md)
+ [Creating a service-linked role for MediaTailor](create-slr.md)
+ [Editing a service-linked role for MediaTailor](edit-slr.md)
+ [Deleting a service-linked role for MediaTailor](delete-slr.md)