# Requesting a new application account

You must have a multi-account AWS Managed Services (AMS) environment set up with core accounts,
before requesting a new application account. For information about setting up a multi-account
environment with core accounts, see [MALZ: Core account onboarding](core-acc.md "core-acc.md").

You can choose one of the following Amazon VPC types for the initial VPC in the application
account:

- Private: This VPC has no Internet gateway attached. This is suitable for private
  applications that require no access to/from the Internet.
- Public: This VPC has an Internet gateway attached and has public and private subnets.
  This is suitable for public applications that require access to/from the Internet.
  You can request a new application account by submitting a Deployment | Managed landing
  zone | Management account | Create application account (with VPC) (ct-1zdasmc2ewzrs) RFC and
  providing the following values in the RFC:

- Account Name: A custom name for the account. Note that the Account Name has a maximum
  length of 50 characters.
- Account Email: The distribution list email for the account. This email ID is used for
  creating the AWS account.
- Support level: The AWS Support level, Premium or Plus.
- VPC Name: A name for the VPC.
- Number of Availability Zones (AZs): 2 or 3.
- VPC CIDR: The CIDR block for the VPC.
- Route Type: This can be either `routable` or `isolated`.
  `Routable` means that application VPCs associated with the Transit Gateway
  (TGW) application route table can connect to this VPC. `Isolated` means that
  application VPCs associated with the TGW application route table cannot connect to this
  VPC. The default is `routable`.
- Transit Gateway Application Route Table: The Transit Gateway route table to which the
  application account VPC has to be associated with. If no value is provided,
  the default `defaultAppRouteDomain` is used, which means that this account will be able to communicate with all
  other accounts under the same route table.
- PublicSubnetAZ`<1-3>`CIDRCIDR for public subnet in AZ 1:
  The CIDR for public subnet in Availability Zone 1.
- PrivateSubnet`<1-10>`AZ`<I-3>`CIDRCIDR
  for public subnet in AZ 1: The CIDR for public subnet in Availability Zone 1.
  At this point, AMS deploys a new application account into your AMS management account,
  with the specified VPC configuration.
