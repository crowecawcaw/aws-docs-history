# Shared subnet prerequisites

This section contains prerequisites for working with shared subnets:

- The accounts for the VPC owner and participant must be managed by AWS Organizations.
- You must enable resource sharing in the AWS RAM console from the management account
  for your organization. For more information, see [Enable
  resource sharing within AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS RAM User Guide_.
- You must create a resource share. You can specify the subnets to share when you
  create the resource share, or add the subnets to the resource share later on using
  the procedure in the next section. For more information, see
  [Create a resource share](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create") in the _AWS RAM User Guide_.
