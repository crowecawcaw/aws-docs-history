# Infrastructure security in

Amazon Quick

|                                                   |
| ------------------------------------------------- |
| Intended audience:<br>Amazon Quick administrators |

Quick is delivered as a web application, hosted on dedicated Amazon EC2 hosts,
separate from AWS virtual private clouds (VPCs). Instead of deploying Amazon Quick on your
own hosts, you access the Amazon Quick service through Regional public endpoints.
Amazon Quick accesses data sources over a secured internet connection from Regional
endpoints. To access data sources that are located inside a corporate network, configure the
network to allow access from one of the Amazon Quick public IP address blocks. We recommend
that you consider using a VPC (a virtual network dedicated to your AWS account).

For more information, see the following:

- [Global
  Infrastructure: The Most Extensive, Reliable, and Secure Global Cloud
  Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure "https://aws.amazon.com/about-aws/global-infrastructure")
- [AWS
  Regions, websites, IP address ranges, and endpoints](../../../quicksight/latest/user/regions.md "../../../quicksight/latest/user/regions.md")
- [Connecting to a Amazon VPC with Amazon Quick](../../../quicksight/latest/user/working-with-aws-vpc.md "../../../quicksight/latest/user/working-with-aws-vpc.md")
  As a managed service, Quick is protected by the AWS global network security
  procedures that are described in the [Amazon Web Services: Overview of Security Processes](https://tinyurl.com/AWSSecurityPaper "https://tinyurl.com/AWSSecurityPaper") paper.

If you use AWS published API calls to access Amazon Quick through the network, clients
must support Transport Layer Security (TLS) 1.2 or later.
Clients must also support cipher suites with perfect forward secrecy (PFS) such as Ephemeral
Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems
such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret access key
that is associated with an AWS Identity and Access Management (IAM) principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md")
(AWS STS) to generate temporary security credentials to sign requests.

You can call these API operations from any network location, but Amazon Quick does support
resource-based access policies, which can include restrictions based on the source IP
address. You can also use Amazon Quick policies to control access from specific Amazon Virtual Private Cloud
(Amazon VPC) endpoints or specific VPCs. Effectively, this isolates network access to a given
Amazon Quick resource from only the specific VPC within the AWS network. For more
information on using Amazon Quick in a VPC, see [Connecting
to a Amazon VPC with Amazon Quick](../../../quicksight/latest/user/working-with-aws-vpc.md "../../../quicksight/latest/user/working-with-aws-vpc.md").
