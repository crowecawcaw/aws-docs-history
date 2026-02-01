# Configuring an SFTP, FTPS, or FTP server

endpoint

This topic provides details for creating and using AWS Transfer Family server endpoints that use one
or more of the SFTP, FTPS, and FTP protocols.

###### Topics

- [Identity provider options](#identity-provider-details "#identity-provider-details")
- [AWS Transfer Family endpoint type matrix](#endpoint-matrix "#endpoint-matrix")
- [Configuring an SFTP, FTPS, or FTP server
  endpoint](tf-server-endpoint.md "tf-server-endpoint.md")
- [FTP and FTPS Network Load Balancer
  considerations](#ftp-ftps-nlb-considerations "#ftp-ftps-nlb-considerations")
- [Transferring files over a server endpoint using a
  client](transfer-file.md "transfer-file.md")
- [Managing users for server endpoints](create-user.md "create-user.md")
- [Using logical directories to simplify your Transfer Family
  directory structures](logical-dir-mappings.md "logical-dir-mappings.md")
- [Access your FSx for NetApp ONTAP file systems with Transfer Family](fsx-s3-access-points.md "fsx-s3-access-points.md")

## Identity provider options

AWS Transfer Family provides several methods for authenticating and managing
users. The following table compares the available identity providers that you can use
with Transfer Family.

| Action                                             | AWS Transfer Family service managed | AWS Managed Microsoft AD | Amazon API Gateway | AWS Lambda      |
| -------------------------------------------------- | ----------------------------------- | ------------------------ | ------------------ | --------------- |
| Supported protocols                                | SFTP                                | SFTP, FTPS, FTP          | SFTP, FTPS, FTP    | SFTP, FTPS, FTP |
| Key-based authentication                           | Yes                                 | No                       | Yes                | Yes             |
| Password authentication                            | No                                  | Yes                      | Yes                | Yes             |
| AWS Identity and Access Management (IAM) and POSIX | Yes                                 | Yes                      | Yes                | Yes             |
| Logical home directory                             | Yes                                 | Yes                      | Yes                | Yes             |
| Parameterized access (username-based)              | Yes                                 | Yes                      | Yes                | Yes             |
| Ad hoc access structure                            | Yes                                 | No                       | Yes                | Yes             |
| AWS WAF                                            | No                                  | No                       | Yes                | No              |

Notes:

- IAM is used to control access for Amazon S3 backing storage, and POSIX is used
  for Amazon EFS.
- _Ad hoc_ refers to the ability to send the user profile at
  runtime. For example, you can land users in their home directories by passing
  the username as a variable.
- For details about AWS WAF, see [Add a web application firewall](web-application-firewall.md "web-application-firewall.md").
- There is a blog post that describes using a Lambda function integrated with
  Microsoft Entra ID (formerly Azure AD) as your Transfer Family identity provider. For
  details, see [Authenticating to AWS Transfer Family with Azure Active Directory and
  AWS Lambda](https://aws.amazon.com/blogs/storage/authenticating-to-aws-transfer-family-with-azure-active-directory-and-aws-lambda/ "https://aws.amazon.com/blogs/storage/authenticating-to-aws-transfer-family-with-azure-active-directory-and-aws-lambda/").
- We provide several CloudFormation templates to help you quickly deploy a Transfer Family server
  that uses a custom identity provider. For details, see [Lambda function templates](custom-lambda-idp.md#lambda-idp-templates "custom-lambda-idp.md#lambda-idp-templates").

In the following procedures, you can create an SFTP-enabled server, FTPS-enabled
server, FTP-enabled server, or AS2-enabled server.

Next step

- [Create an SFTP-enabled server](create-server-sftp.md "create-server-sftp.md")
- [Create an FTPS-enabled server](create-server-ftps.md "create-server-ftps.md")
- [Create an FTP-enabled server](create-server-ftp.md "create-server-ftp.md")
- [Configuring AS2](create-b2b-server.md "create-b2b-server.md")

## AWS Transfer Family endpoint type matrix

When you create a Transfer Family server, you choose the type of endpoint to use. The following
table describes characteristics for each type of endpoint.

| Endpoint type matrix       | Characteristic                                                                                                                                                                                                                                                                            | Public                                                                                                                                                                                                                                                                                                                                                                                      | VPC<br>• Internet                                                                                                                                                                                           | VPC<br>• Internal                                                                                                                                                         | VPC_Endpoint (deprecated) |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| Supported protocols        | SFTP                                                                                                                                                                                                                                                                                      | SFTP, FTPS, AS2                                                                                                                                                                                                                                                                                                                                                                             | SFTP, FTP, FTPS, AS2                                                                                                                                                                                        | SFTP                                                                                                                                                                      |
| Access                     | From over the internet. This endpoint type doesn't require any<br>special configuration in your VPC.                                                                                                                                                                                      | Over the internet and from within VPC and VPC-connected environments,<br>such as an on-premises data center over Direct Connect or VPN.                                                                                                                                                                                                                                                     | From within VPC and VPC-connected environments, such as an<br>on-premises data center over Direct Connect or VPN.                                                                                           | From within VPC and VPC-connected environments, such as an<br>on-premises data center over Direct Connect or VPN.                                                         |
| Static IP address          | You can’t attach a static IP address. AWS provides IP addresses<br>that are subject to change.                                                                                                                                                                                            | You can attach Elastic IP addresses to the endpoint. These can be<br>AWS-owned IP addresses or your own IP addresses ([Bring your own IP<br>addresses](../../../AWSEC2/latest/UserGuide/ec2-byoip.md "../../../AWSEC2/latest/UserGuide/ec2-byoip.md")). Elastic IP addresses attached to the<br>endpoint don't change.<br>Private IP addresses attached to the server also don't<br>change. | Private IP addresses attached to the endpoint don't change.                                                                                                                                                 | Private IP addresses attached to the endpoint don't change.                                                                                                               |
| Source IP allow list       | This endpoint type does not support allow lists by source IP<br>addresses.<br>The endpoint is publicly accessible and listens for traffic over<br>port 22.<br>NoteFor VPC-hosted endpoints, SFTP Transfer Family servers can operate over<br>port 22 (the default), 2222, 2223, or 22000. | To allow access by source IP address, you can use security groups<br>attached to the server endpoints and network ACLs attached to the<br>subnet that the endpoint is in.                                                                                                                                                                                                                   | To allow access by source IP address, you can use security groups<br>attached to the server endpoints and network access control lists<br>(network ACLs) attached to the subnet that the endpoint is<br>in. | To allow access by source IP address, you can use security groups<br>attached to the server endpoints and network ACLs attached to the<br>subnet that the endpoint is in. |
| Client firewall allow list | You must allow the DNS name of the server.<br>Because IP addresses are subject to change, avoid using IP<br>addresses for your client firewall allow list.                                                                                                                                | You can allow the DNS name of the server or the Elastic IP<br>addresses attached to the server.                                                                                                                                                                                                                                                                                             | You can allow the private IP addresses or the DNS name of the<br>endpoints.                                                                                                                                 | You can allow the private IP addresses or the DNS name of the<br>endpoints.                                                                                               |
| IP address type            | IPv4 (default) or dual-stack (IPv4 and IPv6)                                                                                                                                                                                                                                              | IPv4 only (dual-stack not supported)                                                                                                                                                                                                                                                                                                                                                        | IPv4 (default) or dual-stack (IPv4 and IPv6)                                                                                                                                                                | IPv4 only (dual-stack not supported)                                                                                                                                      |

###### Note

The `VPC_ENDPOINT` endpoint type is now deprecated and cannot be used
to create new servers. Instead of using `EndpointType=VPC_ENDPOINT`, use
the VPC endpoint type (`EndpointType=VPC`), which you can use as either
**Internal** or **Internet Facing**, as
described in the preceding table.

- For details about the deprecation, see [Discontinuing the use of VPC_ENDPOINT](create-server-in-vpc.md#deprecate-vpc-endpoint "create-server-in-vpc.md#deprecate-vpc-endpoint").
- For information about managing VPC endpoint permissions, see [Limiting VPC endpoint access for Transfer Family
  servers](create-server-in-vpc.md#limit-vpc-endpoint-access "create-server-in-vpc.md#limit-vpc-endpoint-access").

Consider the following options to increase the security posture of your AWS Transfer Family
server:

- Use a VPC endpoint with internal access, so that the server is accessible only
  to clients within your VPC or VPC-connected environments such as an on-premises
  data center over Direct Connect or VPN.
- To allow clients to access the endpoint over the internet and protect your
  server, use a VPC endpoint with internet-facing access. Then, modify the VPC's
  security groups to allow traffic only from certain IP addresses that host your
  users' clients.
- If you require password-based authentication and you use a custom identity
  provider with your server, it's a best practice that your password policy
  prevents users from creating weak passwords and limits the number of failed
  login attempts.
- AWS Transfer Family is a managed service, and so it doesn't provide shell access. You cannot
  directly access the underlying SFTP server to run OS native commands on Transfer Family
  servers.
- Use a Network Load Balancer in front of a VPC endpoint with internal access.
  Change the listener port on the load balancer from port 22 to a different port.
  This can reduce, but not eliminate, the risk of port scanners and bots probing
  your server, because port 22 is most commonly used for scanning. For details,
  see the blog post [Network
  Load Balancers now support Security groups](https://aws.amazon.com/blogs/containers/network-load-balancers-now-support-security-groups/ "https://aws.amazon.com/blogs/containers/network-load-balancers-now-support-security-groups/").

###### Note

If you use a Network Load Balancer, the AWS Transfer Family CloudWatch logs show the IP
address for the NLB, rather than the actual client IP address.

## FTP and FTPS Network Load Balancer

considerations

Although we recommend avoiding Network Load Balancers in front of AWS Transfer Family servers, if
your FTP or FTPS implementation requires an NLB or NAT in the communication route from
the client, follow these recommendations:

- For an NLB, use port 21 for health checks, instead of ports 8192-8200.
- For the AWS Transfer Family server, enable TLS session resumption by setting
  `TlsSessionResumptionMode = ENFORCED`.

###### Note

This is the recommended mode, as it provides enhanced security:

    + Requires clients to use TLS session resumption for subsequent
     connections.
    + Provides stronger security guarantees by ensuring consistent
     encryption parameters.
    + Helps prevent potential downgrade attacks.
    + Maintains compliance with security standards while optimizing
     performance.

- If possible, migrate away from using an NLB to take full advantage of AWS Transfer Family
  performance and connection limits.

For additional guidance on NLB alternatives, contact the AWS Transfer Family Product Management
team through AWS Support. For more information about improving your security posture,
see the blog post [Six tips to improve the security of your AWS Transfer Family server](https://aws.amazon.com/blogs/security/six-tips-to-improve-the-security-of-your-aws-transfer-family-server/ "https://aws.amazon.com/blogs/security/six-tips-to-improve-the-security-of-your-aws-transfer-family-server/").

Security guidance for NLBs is provided in [Avoid placing NLBs and NATs in front of AWS Transfer Family
servers](infrastructure-security.md#nlb-considerations "infrastructure-security.md#nlb-considerations").
