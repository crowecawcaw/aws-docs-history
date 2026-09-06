

# Connecting to private APIs in other AWS accounts
<a name="connection-private-cross-region"></a>

EventBridge supports connections to private APIs across accounts in the same Region. 

For you to create a connection to a private API in another AWS account, the owner of that account must first share a VPC Lattice resource configuration for that private API with you. To do this, they share the resource with you in AWS Resource Access Manager. AWS RAM enables secure sharing of resources across AWS accounts, within organizational units (OUs), and integrates with AWS Identity and Access Management roles and users. Once you've accepted the resource share in AWS RAM you can specify the shared VPC Lattice resource configuration when creating a connection.

For more information on AWS RAM, see the following topics in the *AWS Resource Access Manager User Guide*:
+ [Benefits of AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html#what-is-features)
+ [How resource sharing works](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html#what-is-how)
+ [Access AWS resources shared with you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-invitations.html)

EventBridge does not support connections to private APIs across Regions. However, to target a private API in a different Region from your event bus:, you can:

1. Define an event bus rule that targets a second event bus that does reside in the same Region as the desired private API.

1. Create a connection for the second event bus to target the private API.

For more information, see [Sending and receiving events between AWS Regions in Amazon EventBridge](eb-cross-region.md).