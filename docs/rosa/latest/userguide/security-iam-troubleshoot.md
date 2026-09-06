

# Troubleshooting ROSA identity and access
<a name="security-iam-troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with ROSA and IAM.

## AWS Organizations service control policy denies required AWS Marketplace permissions
<a name="error-aws-orgs-scp-denies-permissions"></a>

If your AWS Organizations service control policy (SCP) doesn’t allow the required AWS Marketplace subscription permissions when you attempt to enable ROSA, the following console error occurs.

```
An error occurred while enabling ROSA, because a service control policy (SCP) is denying required permissions. Contact your management account administrator, and consult the documentation for troubleshooting.
```

If you receive this error, then you must contact your administrator for assistance. Your administrator is the person that manages the accounts for your organization. Ask that person to do the following:

1. Configure the SCP to allow `aws-marketplace:Subscribe`, `aws-marketplace:Unsubscribe`, and `aws-marketplace:ViewSubscriptions` permissions. For more information, see [Updating an SCP](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_create.html#update_policy) in the * AWS Organizations User Guide*.

1. Enable ROSA in the organization’s management account.

1. Share the ROSA subscription to member accounts that require access within the organization. For more information, see [Sharing subscriptions in an organization](https://docs.aws.amazon.com/marketplace/latest/buyerguide/organizations-sharing.html) in the * AWS Marketplace Buyer Guide*.

## User or role does not have the required AWS Marketplace permissions
<a name="error-iam-lacks-permissions"></a>

If your IAM principal doesn’t have the required AWS Marketplace subscription permissions when you attempt to enable ROSA, the following console error occurs.

```
An error occurred while enabling ROSA, because your user or role does not have the required permissions.
```

To resolve this issue, follow these steps:

1. Go to the [IAM console](https://console.aws.amazon.com/iam) and attach the AWS managed policy `ROSAManageSubscription` to your IAM identity. For more information, see [ROSAManageSubscription](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ROSAManageSubscription.html) in the * AWS Managed Policy Reference Guide*.

1. Follow the procedure in [Enable ROSA and configure AWS prerequisites](set-up.md#enable-rosa).

If you don’t have permission to view or update your permission set in IAM or you receive an error, then you must contact your administrator for assistance. Ask that person to attach `ROSAManageSubscription` to your IAM identity and follow the procedure in [Enable ROSA and configure AWS prerequisites](set-up.md#enable-rosa). When an administrator performs this action, it enables ROSA by updating the permission set for all IAM identities under the AWS account.

## Required AWS Marketplace permissions blocked by an administrator
<a name="error-admin-blocked-iam-permissions"></a>

If your account administrator blocked the required AWS Marketplace subscription permissions, the following console error occurs when you attempt to enable ROSA.

```
An error occurred while enabling ROSA because required permissions have been blocked by an administrator. ROSAManageSubscription includes the permissions required to enable ROSA. Consult the documentation and try again.
```

If you receive this error, then you must contact your administrator for assistance. Ask that person to do the following:

1. Go to the [ROSA console](https://console.aws.amazon.com/rosa) and attach the AWS managed policy `ROSAManageSubscription` to your IAM identity. For more information, see [ROSAManageSubscription](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ROSAManageSubscription.html) in the * AWS Managed Policy Reference Guide*.

1. Follow the procedure in [Enable ROSA and configure AWS prerequisites](set-up.md#enable-rosa) to enable ROSA. This procedure enables ROSA by updating the permission set for all IAM identities under the AWS account.

## Error creating load balancer: AccessDenied
<a name="elb-role-missing-error"></a>

If you haven’t created a load balancer, the `AWSServiceRoleForElasticLoadBalacing` service-linked role may not exist in your account. The following error occurs if you attempt to create a ROSA cluster without the `AWSServiceRoleForElasticLoadBalacing` role in your account.

```
Error creating network Load Balancer: AccessDenied
```

To resolve this issue, follow these steps:

1. Check if your account has the `AWSServiceRoleForElasticLoadBalancing` role.

   ```
   aws iam get-role --role-name "AWSServiceRoleForElasticLoadBalancing"
   ```

1. If you don’t have this role, follow the instructions to create the role found in [Create the service-linked role](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/elb-service-linked-roles.html) in the * Elastic Load Balancing User Guide*.