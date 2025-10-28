# Using service-linked roles for

Site-to-Site VPN

AWS Site-to-Site VPN uses AWS Identity and Access Management (IAM)
service-linked roles. A service-linked role is a unique type of IAM role that is
linked directly to Site-to-Site VPN. Service-linked roles are predefined by Site-to-Site VPN and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up Site-to-Site VPN easier because you don’t have to
manually add the necessary permissions. Site-to-Site VPN defines the permissions of its
service-linked roles, and unless defined otherwise, only Site-to-Site VPN can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your Site-to-Site VPN resources because you can't inadvertently remove permission to
access the resources.

## Service-linked role permissions for

Site-to-Site VPN

Site-to-Site VPN uses the service-linked role named **AWSServiceRoleForVPCS2SVPN** –
Allow Site-to-Site VPN to create and manage resources related to your VPN connections.

The AWSServiceRoleForVPCS2SVPN service-linked role trusts the following service to assume the role:

- `s2svpn.amazonaws.com`

This service-linked role uses the managed policy AWSVPCS2SVpnServiceRolePolicy to complete the
following actions on the specified resources:

- When using certificate authentication for your VPN connection, AWS Site-to-Site VPN
  exports the VPN tunnel AWS Certificate Manager certificates for use on the VPN tunnel endpoints.
- When using certificate authentication for your VPN connection, AWS Site-to-Site VPN manages the
  renewal of the VPN tunnel AWS Certificate Manager certificates.
- When using SecretsManager pre-shared key storage for your VPN connection, AWS Site-to-Site VPN
  manages the VPN connection’s AWS Secrets Manager s2svpn managed secret.

To view the permissions for this policy, see [AWSVPCS2SVpnServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSVPCS2SVpnServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSVPCS2SVpnServiceRolePolicy.md") in the _AWS Managed Policy
Reference_.

## Create a service-linked role for Site-to-Site VPN

You don't need to manually create a service-linked role. When you
create a customer gateway with an associated ACM private certificate in the AWS Management Console, the AWS CLI, or the AWS API, Site-to-Site VPN
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create a customer gateway with an associated ACM private certificate,
Site-to-Site VPN creates the service-linked role for you again.

## Edit a service-linked role for Site-to-Site VPN

Site-to-Site VPN does not allow you to edit the AWSServiceRoleForVPCS2SVPN service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Edit a service-linked role description](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console") in the _IAM User Guide_.

## Delete a service-linked role for Site-to-Site VPN

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the Site-to-Site VPN service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

###### To delete Site-to-Site VPN resources used by the AWSServiceRoleForVPCS2SVPN

You can delete this service-linked role only after you delete all customer gateways that have an associated ACM private certificate. This ensures that you cannot inadvertently remove permission to access your ACM certificates in use by Site-to-Site VPN connections.

###### To manually delete the service-linked role using IAM

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForVPCS2SVPN
service-linked role. For more information, see [Delete a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the _IAM User Guide_.
