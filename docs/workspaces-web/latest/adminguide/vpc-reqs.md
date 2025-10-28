# VPC requirements for Amazon WorkSpaces Secure Browser

During WorkSpaces Secure Browser portal creation, you'll select a VPC in your account. You'll also choose at
least two subnets in two different Availability Zones. These VPCs and subnets must meet
following requirements:

- The VPC must have default tenancy. VPCs with dedicated tenancy are not
  supported.
- For availability consideration, we require at least two subnets created in two
  different Availability Zones. Your subnets must have sufficient IP addresses to support
  the expected WorkSpaces Secure Browser traffic. Configure each of your subnets with a subnet mask that
  allows for enough client IP addresses to account for the maximum number of concurrent
  sessions. For more information, see [Creating a new VPC for Amazon WorkSpaces Secure Browser](create-vpc.md "create-vpc.md").
- All subnets must have a stable connection to any internal content, either located in
  the AWS Cloud or on premises, that users will access with WorkSpaces Secure Browser.
  We recommend you choose three subnets in different Availability Zones for availability
  and scaling consideration. For more information, see [Creating a new VPC for Amazon WorkSpaces Secure Browser](create-vpc.md "create-vpc.md").

WorkSpaces Secure Browser doesn't assign any public IP address to streaming instances to enable internet
access. This would make your streaming instances accessible from the internet. Therefore,
any streaming instance connected to your public subnet won’t have internet access. If you
want your WorkSpaces Secure Browser portal to have access to both public internet content and private VPC
content, complete the steps in [Enabling unrestricted internet browsing for Amazon WorkSpaces Secure Browser
(recommended)](unrestricted-internet-browsing.md "unrestricted-internet-browsing.md").
