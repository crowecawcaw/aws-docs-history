# Set up Connector for AD

The steps in this section are prerequisites to using Connector for AD. It assumes that you've already created an AWS account. After you complete the steps on this page, you can get started with creating a connector for AD.

## Step 1: Create a private CA using AWS Private CA

Set up a private certificate authority (CA) for issuing certificates to your directory objects. For
more information, see [Certificate authorities in AWS Private CA](creating-managing.md "creating-managing.md").

The private CA must be in the `Active` state to create a
Connector for AD. The private CA's subject name must include a common name.
Connector creation will fail if you try to create a connector using a private CA without a common name.

## Step 2: Set up an Active Directory

In addition to a private CA, you need an active directory in a virtual
private cloud (VPC). Connector for AD supports the following
directory types offered by AWS Directory Service:

- [AWS
  Managed Microsoft Active Directory](../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md "../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md"): With AWS Directory Service you can run
  Microsoft Active Directory (AD) as a managed service. AWS Directory Service for Microsoft Active Directory
  also referred to as AWS Managed Microsoft AD, is powered by Windows Server 2019.
  With AWS Managed Microsoft AD, you can run directory-aware workloads in the
  AWS Cloud, including Microsoft Sharepoint and custom .Net and SQL
  Server-based applications.
- [Active Directory Connector](../../../directoryservice/latest/admin-guide/directory_ad_connector.md "../../../directoryservice/latest/admin-guide/directory_ad_connector.md"): AD Connector is a directory
  gateway that can redirect directory requests to your on-premises
  Microsoft Active Directory, without caching any information in the
  cloud. AD Connector supports connecting to a domain hosted on
  Amazon EC2

## (Active Directory Connector only) Step 3: Delegate permissions to service account

###### Note

If you are using AWS Managed Microsoft AD the additional permissions are
delegated automatically when you authorize the Connector for AD
service with your directory. You can skip this prerequisite step.

When using the Directory Service AD Connector, you need to delegate additional
permissions to the service account. Set access-control list (ACL) on the service
account to allow the ability:

- Add and remove a Service Principal Name (SPN) to itself
- Create and update certification authorities in the following
  containers:

```
#containers
CN=Public Key Services,CN=Services,CN=Configuration
CN=AIA,CN=Public Key Services,CN=Services,CN=Configuration
CN=Certification Authorities,CN=Public Key Services,CN=Services,CN=Configuration

```

- Create and update a NTAuthCertificates Certification Authority (CA)
  object. Note: if the NTAuthCertificates CA object exists then you must
  delegate permissions for it. If the object does not exist then you must
  delegate the ability to create child objects on the Public Key Services
  container.

```
#objects
CN=NTAuthCertificates,CN=Public Key Services,CN=Services,CN=Configuration

```

The PowerShell script available in the official [Connector for Active Directory repository](https://github.com/aws-samples/sample-aws-privateca-connector-for-active-directory "https://github.com/aws-samples/sample-aws-privateca-connector-for-active-directory") can be used to delegate the additional permissions required for the Directory Service AD Connector service account.

This script creates the NTAuthCertificates certification authority object.

For the latest version of the script and usage details, refer to the README in the [GitHub repository](https://github.com/aws-samples/sample-aws-privateca-connector-for-active-directory "https://github.com/aws-samples/sample-aws-privateca-connector-for-active-directory").

## Step 4: Create IAM Policy

To create a connector for AD, you need an IAM policy that allows you to
create connector resources, share your private CA with the
Connector for AD service, and authorize the
Connector for AD service with your directory.

This is an example a user managed policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "pca-connector-ad:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "acm-pca:DescribeCertificateAuthority",
 "acm-pca:GetCertificate",
 "acm-pca:GetCertificateAuthorityCertificate",
 "acm-pca:ListCertificateAuthorities",
 "acm-pca:ListTags",
 "acm-pca:PutPolicy"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "acm-pca:IssueCertificate",
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "acm-pca:TemplateArn": "arn:aws:acm-pca:::template/BlankEndEntityCertificate_APIPassthrough/V*"
 },
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "pca-connector-ad.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ds:AuthorizeApplication",
 "ds:DescribeDirectories",
 "ds:ListTagsForResource",
 "ds:UnauthorizeApplication",
 "ds:UpdateAuthorizedApplication"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateVpcEndpoint",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeVpcs",
 "ec2:DeleteVpcEndpoints"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeTags",
 "ec2:DeleteTags",
 "ec2:CreateTags"
 ],
 "Resource": "arn:*:ec2:*:*:vpc-endpoint/*"
 }
 ]
}`

```

Connector for AD requires additional AWS RAM permissions, for both
console and command line use.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ram:CreateResourceShare",
 "Resource": "*",
 "Condition": {
 "StringEqualsIfExists": {
 "ram:Principal": "pca-connector-ad.amazonaws.com",
 "ram:RequestedResourceType": "acm-pca:CertificateAuthority"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ram:GetResourcePolicies",
 "ram:GetResourceShareAssociations",
 "ram:GetResourceShares",
 "ram:ListPrincipals",
 "ram:ListResources",
 "ram:ListResourceSharePermissions",
 "ram:ListResourceTypes"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Step 5: Share your private CA with

Connector for AD

You will need to share your private CA with the connectors service by using
AWS Resource Access Manager service principal sharing.

When you create a connector in the AWS console, the resource share is
automatically created for you.

When you create a resource share using the AWS CLI, you will use the AWS RAM
**create-resource-share** command.

The following command creates a resource share:

```
`$`  `aws ram create-resource-share \
 --region `us-east-1` \
 --name `MyPcaConnectorAdResourceShare` \
 --permission-arns arn:aws:ram::aws:permission/AWSRAMBlankEndEntityCertificateAPIPassthroughIssuanceCertificateAuthority \
 --resource-arns arn:aws:acm-pca:`region`:`account`:certificate-authority/`CA_ID` \
 --principals pca-connector-ad.amazonaws.com \
 --sources `account``
```

The service principal that calls CreateConnector has certificate issuance
permissions on the PCA. To prevent service principals that use
Connector for AD from having general access to your AWS Private CA
resources, restrict their permissions using `CalledVia`.

## Step 6: Create directory registration

You authorize the Connector for AD service with your directory so
the connector can communicate with your directory. To authorize the
Connector for AD service, you create a directory registration. For
more information on creating a directory registration, see [Manage directory registrations](directory-registration.md "directory-registration.md")

## Step 7: Configure security groups

Communication between your VPC and the Connector for AD connector
is through AWS PrivateLink, which requires a security group(s) with inbound rules
that open port 443 TCP on your VPC. You will be asked for this security
group when you create a connector. You can specify the source as custom and
select your VPC's CIDR block. You can choose to restrict this further (i.e. IP,
CIDR, and security group ID).

## Step 8: Configure network access for directory objects

Directory objects require public internet access to validate Online Certificate Status Protocol (OCSP) and certificate revocation lists (CRLs) from the following domains:

```
*.windowsupdate.com
*.amazontrust.com
```

Minimum required access rules:

- Required for OCSP and CRL communication:

```
TCP 80: (HTTP) to 0.0.0.0/0
```

- Required for Connector for AD:

```
TCP 443: (HTTPS) to 0.0.0.0/0
```

- Required for Active Directory:

```
TCP 88: (Kerberos) to Domain Controller IP range
TCP/UDP 389/636: (LDAP/LDAPS) to Domain Controller IP range, depending on Domain Controller configuration
TCP/UDP 53: (DNS) to 0.0.0.0/0
```

If the devices do not have public internet access, certificate issuance will fail intermittently with the error code `WS_E_OPERATION_TIMED_OUT.`

###### Note

If you are configuring a security group for an Amazon EC2 instance, it does not have to be the same one in Step 7.
