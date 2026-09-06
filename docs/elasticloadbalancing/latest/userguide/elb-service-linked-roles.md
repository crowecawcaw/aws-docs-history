

# Elastic Load Balancing service-linked role
<a name="elb-service-linked-roles"></a>

Elastic Load Balancing uses a service-linked role for the permissions that it requires to call other AWS services on your behalf. For more information, see [Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html) in the *IAM User Guide*.

## Permissions granted by the service-linked role
<a name="service-linked-role-permissions"></a>

Elastic Load Balancing uses the service-linked role named AWSServiceRoleForElasticLoadBalancing to call other AWS services on your behalf.

AWSServiceRoleForElasticLoadBalancing trusts the `elasticloadbalancing.amazonaws.com` service to assume the role.

The role permissions policy is AWSElasticLoadBalancingServiceRolePolicy. To view the permissions for this policy, see [AWSElasticLoadBalancingServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticLoadBalancingServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## Create the service-linked role
<a name="create-service-linked-role"></a>

You don't need to manually create the AWSServiceRoleForElasticLoadBalancing role. Elastic Load Balancing creates this role for you when you create a load balancer or a target group.

For Elastic Load Balancing to create a service-linked role on your behalf, you must have the required permissions. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#service-linked-role-permissions) in the *IAM User Guide*.

## Edit the service-linked role
<a name="edit-service-linked-role"></a>

You can edit the description of AWSServiceRoleForElasticLoadBalancing using IAM. For more information, see [Edit a service-linked role description](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-service-linked-role.html#edit-service-linked-role-iam-console) in the *IAM User Guide*.

## Delete the service-linked role
<a name="delete-service-linked-role"></a>

If you no longer need to use Elastic Load Balancing, we recommend that you delete AWSServiceRoleForElasticLoadBalancing.

You can delete this service-linked role only after you delete all load balancers in your AWS account. This ensures that you can't inadvertently remove permission to access your load balancers. For more information, see [Delete an Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-delete.html), [Delete a Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-delete.html), and [Delete a Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-getting-started.html#delete-load-balancer).

You can use the IAM console, the IAM CLI, or the IAM API to delete service-linked roles. For more information, see [Delete a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#id_roles_manage_delete_slr) in the *IAM User Guide*.

After you delete AWSServiceRoleForElasticLoadBalancing, Elastic Load Balancing creates the role again if you create a load balancer.