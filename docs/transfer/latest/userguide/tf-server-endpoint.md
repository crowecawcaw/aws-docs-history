# Configuring an SFTP, FTPS, or FTP server

endpoint

You can create a file transfer server by using the AWS Transfer Family service. The following
file transfer protocols are available:

- Secure Shell (SSH) File Transfer Protocol (SFTP) – File transfer over
  SSH. For details, see [Create an SFTP-enabled server](create-server-sftp.md "create-server-sftp.md").

###### Note

We provide an AWS CDK example for creating an SFTP Transfer Family server. The example uses TypeScript, and is available on GitHub [here](https://github.com/aws-samples/aws-cdk-examples/tree/master/typescript/aws-transfer-sftp-server "https://github.com/aws-samples/aws-cdk-examples/tree/master/typescript/aws-transfer-sftp-server").

- File Transfer Protocol Secure (FTPS) – File transfer with TLS
  encryption. For details, see [Create an FTPS-enabled server](create-server-ftps.md "create-server-ftps.md").
- File Transfer Protocol (FTP) – Unencrypted file transfer. For details,
  see [Create an FTP-enabled server](create-server-ftp.md "create-server-ftp.md").
- Applicability Statement 2 (AS2) – File transfer for transporting
  structured business-to-business data. For details, see [Configuring AS2](create-b2b-server.md "create-b2b-server.md"). For AS2, you can quickly create an AWS CloudFormation stack for demonstration purposes. This procedure is
  described in [Use a template to create a demo Transfer Family AS2
  stack](create-as2-transfer-server.md#as2-cfn-demo-template "create-as2-transfer-server.md#as2-cfn-demo-template").
  You can create a server with multiple protocols.

###### Note

If you have multiple protocols enabled for the same server endpoint and you want
to provide access by using the same username over multiple protocols, you can do so
as long as the credentials specific to the protocol have been set up in your
identity provider. For FTP, we recommend maintaining separate credentials from SFTP
and FTPS. This is because, unlike SFTP and FTPS, FTP transmits credentials in clear
text. By isolating FTP credentials from SFTP or FTPS, if FTP credentials are shared
or exposed, your workloads using SFTP or FTPS remain secure.

When you create a server, you choose a specific AWS Region to perform the file
operation requests of users who are assigned to that server. Along with assigning the
server one or more protocols, you also assign one of the following identity provider
types:

- **Service managed by using SSH keys**. For
  details, see [Working with service-managed users](service-managed-users.md "service-managed-users.md").
- **AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD)**. This method
  allows you integrate your Microsoft Active Directory groups to provide access to
  your Transfer Family servers. For details, see [Using AWS Directory Service for Microsoft
  Active Directory](directory-services-users.md "directory-services-users.md").
- **A custom identity provider**. Transfer Family offers
  several options for using a custom identity provider, as described in the [Working with custom identity providers](custom-idp-intro.md "custom-idp-intro.md") topic.
  You also assign the server an endpoint type (publicly accessible or VPC hosted) and a
  hostname by using the default server endpoint, or a custom hostname by using the
  Amazon Route 53 service or by using a Domain Name System (DNS) service of your choice. A
  server hostname must be unique in the AWS Region where it's created.

Additionally, you can assign an Amazon CloudWatch logging role to push events to your CloudWatch
logs, choose a security policy that contains the cryptographic algorithms that are
enabled for use by your server, and add metadata to the server in the form of tags that
are key-value pairs.

###### Important

You incur costs for instantiated servers and for data transfer. For information
about pricing and to use AWS Pricing Calculator to get an estimate of the cost to use Transfer Family, see
[AWS Transfer Family
pricing](https://aws.amazon.com/aws-transfer-family/pricing/ "https://aws.amazon.com/aws-transfer-family/pricing/").
