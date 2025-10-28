# Set up Connector for SCEP

The procedures in this section help you get started with Connector for SCEP. It assumes that you've already created an AWS account. After you complete the steps on this page, you can proceed with creating a connector for SCEP.

###### Topics

- [Step 1: Create an AWS Identity and Access Management policy](#scep-prequisite-iam "#scep-prequisite-iam")
- [Step 2: Create a private CA](#scep-prequisite-pca "#scep-prequisite-pca")
- [Step 3: Create a resource share using AWS Resource Access Manager](#scep-prequisite-ram-share-pca "#scep-prequisite-ram-share-pca")

## Step 1: Create an AWS Identity and Access Management policy

To create a connector for SCEP, you need to create an IAM policy that grants Connector for SCEP the ability to create and manage resources needed by the connector, and to issue certificates on your behalf. For more information about IAM see [What is IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") in the _IAM User Guide_.

The following example is a customer managed policy that you can use for Connector for SCEP.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "pca-connector-scep:*",
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
 "acm-pca:TemplateArn": "arn:aws:acm-pca:::template/BlankEndEntityCertificate_APICSRPassthrough/V*"
 },
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": "pca-connector-scep.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ram:CreateResourceShare",
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

## Step 2: Create a private CA

To use Connector for SCEP you need to associate a private CA from AWS Private Certificate Authority to the connector. We recommend that you use a private CA that's only for the connector, due to inherent security vulnerabilities that are present in the SCEP protocol.

The private CA must meet the following requirements:

- It must be in an active state and use the general-purpose operating mode.
- You must own the private CA. You can't use a private CA that was shared with you through cross-account sharing.

Be aware of the following considerations when configuring your private CA to use with Connector for SCEP:

- **DNS name constrains** – Consider using DNS name constraints as a way to control which domains are allowed or prohibited in the certificates issued for your SCEP devices. For more information, see [How to enforce DNS name constraints in AWS Private Certificate Authority](https://aws.amazon.com/blogs/security/how-to-enforce-dns-name-constraints-in-aws-private-ca/ "https://aws.amazon.com/blogs/security/how-to-enforce-dns-name-constraints-in-aws-private-ca/").
- **Revocation** – Enable OCSP or CRLs on your private CA to allow for revocation. For more information, see [Plan your AWS Private CA certificate revocation method](revocation-setup.md "revocation-setup.md").
- **PII** – We advise that you do not add personally identifiable information (PII) or other confidential or sensitive information in your CA certificates. In the event of a security exploit, this helps to limit exposure of sensitive information.
- **Store root certificates in trust stores** – Store your root CA certificates in your device trust stores, so that you can verify certificates and the return values of [GetCertificateAuthorityCertificate](../APIReference/API_GetCertificateAuthorityCertificate.md "../APIReference/API_GetCertificateAuthorityCertificate.md"). For information about trust stores as they relate to AWS Private CA, see [Root CA](PcaTerms.md#terms-rootca "PcaTerms.md#terms-rootca") .

For information about how to create a private CA, see [Create a private CA in AWS Private CA](create-CA.md "create-CA.md").

## Step 3: Create a resource share using AWS Resource Access Manager

If you're using Connector for SCEP programmatically using the AWS Command Line Interface, AWS SDK, or Connector for SCEP
API, you need to share your private CA with Connector for SCEP by using AWS Resource Access Manager service
principal sharing. This gives Connector for SCEP shared access to your private CA. When you create
a connector in the AWS console, we automatically create the resource share for you.
For information about resource sharing, see [Create a resource share](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-create") in the _AWS RAM User Guide_.

To create a resource share using the AWS CLI, you can use the AWS RAM **create-resource-share** command. The following command creates a resource share. Specify the ARN of the private CA that you want to share as the value of `resource-arns`.

```
`$`  `aws ram create-resource-share \
--region `us-east-1` \
--name `MyPcaConnectorScepResourceShare` \
--permission-arns arn:aws:ram::aws:permission/AWSRAMBlankEndEntityCertificateAPICSRPassthroughIssuanceCertificateAuthority \
--resource-arns arn:aws:acm-pca:`Region`:`account`:certificate-authority/`CA_ID` \
--principals pca-connector-scep.amazonaws.com \
--sources `account``
```

The service principal that calls `CreateConnector` has certificate issuance permissions on the private CA. To prevent service principals that use
Connector for SCEP from having general access to your AWS Private CA resources, restrict their permissions using `CalledVia`.
