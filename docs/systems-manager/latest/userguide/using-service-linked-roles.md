AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Using service-linked roles for

Systems Manager

AWS Systems Manager uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role
that is linked directly to Systems Manager. Service-linked roles are predefined by
Systems Manager and include all the permissions that the service requires to call other
AWS services on your behalf.

###### Note

A _service role_ role differs from a service-linked role. A
service role is a type of AWS Identity and Access Management (IAM) role that grants permissions to an
AWS service so that the service can access AWS resources. Only a few Systems Manager
scenarios require a service role. When you create a service role for Systems Manager, you
choose the permissions to grant so that it can access or interact with other AWS
resources.

A service-linked role makes setting up Systems Manager easier because you don’t have to
manually add the necessary permissions. Systems Manager defines the permissions of its
service-linked roles, and unless defined otherwise, only Systems Manager can assume its
roles. The defined permissions include the trust policy and the permissions policy, and
that permissions policy can't be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related
resources. This protects your Systems Manager resources because you can't inadvertently
remove permission to access the resources.

###### Note

For non-EC2 nodes in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment , you need an additional IAM role
that allows those machines to communicate with the Systems Manager service. This is
the IAM service role for Systems Manager. This role grants AWS Security Token Service (AWS STS)
_AssumeRole_ trust to the Systems Manager
service. The `AssumeRole` action returns a set of temporary security
credentials (consisting of an access key ID, a secret access key, and a security
token). You use these temporary credentials to access AWS resources that you might
not normally have access to. For more information, see [Create the IAM service role required for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md "hybrid-multicloud-service-role.md") and [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the
_[AWS Security Token Service API Reference](../../../STS/latest/APIReference.md "../../../STS/latest/APIReference.md")_.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have
**Yes** in the **Service-linked
roles** column. Choose a **Yes** with a link
to view the service-linked role documentation for that service.

###### Topics

- [Using roles to collect inventory and view OpsData](using-service-linked-roles-service-action-1.md "using-service-linked-roles-service-action-1.md")
- [Using roles to collect AWS account information for OpsCenter and Explorer](using-service-linked-roles-service-action-2.md "using-service-linked-roles-service-action-2.md")
- [Using roles to create OpsData and OpsItems for Explorer](using-service-linked-roles-service-action-3.md "using-service-linked-roles-service-action-3.md")
- [Using roles to create operational insight OpsItems in Systems Manager OpsCenter](using-service-linked-roles-service-action-4.md "using-service-linked-roles-service-action-4.md")
- [Using roles to maintain Quick Setup-provisioned resource health and consistency](using-service-linked-roles-service-action-5.md "using-service-linked-roles-service-action-5.md")
- [Using roles to export Explorer OpsData](using-service-linked-roles-service-action-6.md "using-service-linked-roles-service-action-6.md")
- [Using roles to enable just-in-time node access](using-service-linked-roles-service-action-8.md "using-service-linked-roles-service-action-8.md")
- [Using roles to send just-in-time node access request notifications](using-service-linked-roles-service-action-9.md "using-service-linked-roles-service-action-9.md")
