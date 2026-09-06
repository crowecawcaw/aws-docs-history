

# Shared subnet prerequisites
<a name="vpc-share-prerequisites"></a>

This section contains prerequisites for working with shared subnets:
+ The accounts for the VPC owner and participant must be managed by AWS Organizations.
+ You must enable resource sharing in the AWS RAM console from the management account for your organization. For more information, see [Enable resource sharing within AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS RAM User Guide*.
+ You must create a resource share. You can specify the subnets to share when you create the resource share, or add the subnets to the resource share later on using the procedure in the next section. For more information, see [Create a resource share](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-create) in the *AWS RAM User Guide*.