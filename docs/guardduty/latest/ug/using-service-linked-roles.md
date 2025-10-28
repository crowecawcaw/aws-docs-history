# Using service-linked roles for

Amazon GuardDuty

Amazon GuardDuty uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role (SLR) is a unique type of IAM role
that is linked directly to GuardDuty. Service-linked roles are predefined by GuardDuty and include
all the permissions that GuardDuty requires to call other AWS services on your behalf.

With service-linked role, you can set up GuardDuty without adding the necessary permissions
manually. GuardDuty defines the permissions of its service-linked role, and unless the
permissions are defined otherwise, only GuardDuty can assume the role. The defined permissions
include the trust policy and the permissions policy, and that permissions policy can't be
attached to any other IAM entity.

GuardDuty supports using service-linked roles in all of the Regions where GuardDuty is available.
For more information, see [Regions and endpoints](guardduty_regions.md "guardduty_regions.md").

You can delete the GuardDuty service-linked role only after first disabling GuardDuty in all
Regions where it is enabled. This protects your GuardDuty resources because you can't
inadvertently remove permission to access them.

For information about other services that support service-linked roles, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_ and
look for the services that have **Yes** in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.
