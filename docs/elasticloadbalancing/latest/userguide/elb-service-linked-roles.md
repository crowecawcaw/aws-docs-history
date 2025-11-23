# ELB service-linked role

ELB uses a service-linked role for the permissions that it requires to call other
AWS services on your behalf. For more information, see [Service-linked
roles](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md") in the _IAM User Guide_.

## Permissions granted by the

service-linked role

ELB uses the service-linked role named
AWSServiceRoleForElasticLoadBalancing to call other AWS
services on your behalf.

AWSServiceRoleForElasticLoadBalancing trusts the
`elasticloadbalancing.amazonaws.com` service to assume the
role.

The role permissions policy is AWSElasticLoadBalancingServiceRolePolicy.
To view the permissions for this policy, see [AWSElasticLoadBalancingServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSElasticLoadBalancingServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSElasticLoadBalancingServiceRolePolicy.md") in the _AWS Managed Policy Reference_.

## Create the service-linked role

You don't need to manually create the
AWSServiceRoleForElasticLoadBalancing role. ELB creates
this role for you when you create a load balancer or a target group.

For ELB to create a service-linked role on your behalf, you must have the
required permissions. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Edit the service-linked role

You can edit the description of
AWSServiceRoleForElasticLoadBalancing using IAM. For more
information, see [Edit a service-linked role description](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console") in the
_IAM User Guide_.

## Delete the service-linked role

If you no longer need to use ELB, we recommend that you delete
AWSServiceRoleForElasticLoadBalancing.

You can delete this service-linked role only after you delete all load balancers
in your AWS account. This ensures that you can't inadvertently remove permission
to access your load balancers. For more information, see [Delete an Application Load Balancer](../application/load-balancer-delete.md "../application/load-balancer-delete.md"), [Delete a Network Load Balancer](../network/load-balancer-delete.md "../network/load-balancer-delete.md"), and [Delete a
Classic Load Balancer](../classic/elb-getting-started.md#delete-load-balancer "../classic/elb-getting-started.md#delete-load-balancer").

You can use the IAM console, the IAM CLI, or the IAM API to delete
service-linked roles. For more information, see [Delete a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the
_IAM User Guide_.

After you delete AWSServiceRoleForElasticLoadBalancing, ELB
creates the role again if you create a load balancer.
