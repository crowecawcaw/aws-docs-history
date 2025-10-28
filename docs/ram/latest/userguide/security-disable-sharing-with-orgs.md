# Disabling resource sharing with

AWS Organizations

If you previously enabled sharing with AWS Organizations and you no longer need to share resources
with your entire organization or organizational units (OUs), you can disable sharing. When
you disable sharing with AWS Organizations, all organizations or OUs are removed from the resource shares that
you have created and they lose access to the shared resources. External accounts (accounts added to the resource share via
invitation) will not be impacted, and will continue to be associated with the resource share.

###### To disable sharing with AWS Organizations

1. Disable trusted access to AWS Organizations using the AWS Organizations [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md") AWS CLI command.

```
`$`  aws organizations disable-aws-service-access --service-principal ram.amazonaws.com
```

###### Important

When you disable trusted access to AWS Organizations, principals within your
organizations are removed from all resource shares and lose access to those shared
resources. 2. Use the IAM console, the AWS CLI, or the IAM API operations to delete the
**AWSServiceRoleForResourceAccessManager** service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.
