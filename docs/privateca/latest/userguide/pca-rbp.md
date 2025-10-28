# Resource-based policies

Resource-based policies are permissions policies that you create and manually
attach to a resource (in this case, a private CA) rather than to a user identity or
role. Or, instead of creating your own policies, you can use AWS managed policies
for AWS Private CA. Using AWS RAM to apply a resource-based policy, an AWS Private CA administrator
can share access to a CA with a user in a different AWS account directly or
through AWS Organizations. Alternatively, an AWS Private CA administrator can use the PCA APIs
[PutPolicy](../APIReference/API_PutPolicy.md "../APIReference/API_PutPolicy.md"), [GetPolicy](../APIReference/API_GetPolicy.md "../APIReference/API_GetPolicy.md"), and [DeletePolicy](../APIReference/API_DeletePolicy.md "../APIReference/API_DeletePolicy.md"), or the
corresponding AWS CLI commands [put-policy](../../../cli/latest/reference/acm-pca/put-policy.md "../../../cli/latest/reference/acm-pca/put-policy.md"), [get-policy](../../../cli/latest/reference/acm-pca/get-policy.md "../../../cli/latest/reference/acm-pca/get-policy.md"), and [delete-policy](../../../cli/latest/reference/acm-pca/delete-policy.md "../../../cli/latest/reference/acm-pca/delete-policy.md"), to apply and manage resource-based policies.

For general information about resource-based policies, see [Identity-Based
Policies and Resource-Based Policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") and [Controlling Access Using
Policies](../../../IAM/latest/UserGuide/access_controlling.md "../../../IAM/latest/UserGuide/access_controlling.md").

To view the list of AWS managed resource-based policies for AWS Private CA, navigate to
the [Managed permissions
library](https://console.aws.amazon.com/ram/home#Permissions: "https://console.aws.amazon.com/ram/home#Permissions:") in the AWS Resource Access Manager console, and search for
**CertificateAuthority**. As with any policy, before you apply
it, we recommend applying the policy in a test environment to ensure that it meets
your requirements.

AWS Certificate Manager (ACM) users with cross-account shared access to a private CA can issue
managed certificates that are signed by the CA. Cross-account issuers are constrained
by a resource-based policy and have access only to the
following end-entity certificate templates:

- [EndEntityCertificate/V1](template-definitions.md#EndEntityCertificate-V1 "template-definitions.md#EndEntityCertificate-V1")
- [EndEntityClientAuthCertificate/V1](template-definitions.md#EndEntityClientAuthCertificate-V1 "template-definitions.md#EndEntityClientAuthCertificate-V1")
- [EndEntityServerAuthCertificate/V1](template-definitions.md#EndEntityServerAuthCertificate-V1 "template-definitions.md#EndEntityServerAuthCertificate-V1")
- [BlankEndEntityCertificate_APIPassthrough/V1](template-definitions.md#BlankEndEntityCertificate_APIPassthrough "template-definitions.md#BlankEndEntityCertificate_APIPassthrough")
- [BlankEndEntityCertificate_APICSRPassthrough/V1](template-definitions.md#BlankEndEntityCertificate_APICSRPassthrough "template-definitions.md#BlankEndEntityCertificate_APICSRPassthrough")
- [SubordinateCACertificate_PathLen0/V1](template-definitions.md#SubordinateCACertificate_PathLen0-V1 "template-definitions.md#SubordinateCACertificate_PathLen0-V1")

## Policy examples

This section provides example cross-account policies for various needs. In all
cases, the following command pattern is used to apply a policy:

```
`$` `aws acm-pca put-policy \
 --region `region` \
 --resource-arn arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566` \
 --policy file:///`[path]`/`policy*N*.json``
```

In addition to specifying the ARN of a CA, the administrator provides an AWS
account ID or an AWS Organizations ID that will be granted access to the CA. The JSON of
each of the following polices is formatted as a file for readability, but can
also be supplied as an inline CLI arguments.

###### Note

The structure of the JSON resource-based polices shown below must be
followed precisely. Only the ID fields for the principals (the AWS account
number or the AWS Organizations ID) and the CA ARNs can be configured by
customers.

1. **File: policy1.json – Sharing access to a
   CA with a user in a different account**

Replace `555555555555` with the
AWS account ID that's sharing the CA.

For the resource ARN, replace the following with your own
values:

    * ``aws`` - The AWS
     partition. For example, `aws`,
     `aws-us-gov`, `aws-cn`, etc.
    * ``us-east-1`` - The AWS
     Region that the resource is available in, such as
     `us-west-1`.
    * ``111122223333``
     - The AWS account ID of the resource owner.
    * ``11223344-1234-1122-2233-112233445566``
     - The resource ID of the certificate authority.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "`ExampleStatementID`",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`555555555555`"
 },
 "Action": [
 "acm-pca:DescribeCertificateAuthority",
 "acm-pca:GetCertificate",
 "acm-pca:GetCertificateAuthorityCertificate",
 "acm-pca:ListPermissions",
 "acm-pca:ListTags"
 ],
 "Resource": "arn:aws:acm-pca:`us-east-1`:`123456789012`:certificate-authority/`CA_ID`/certificate/`certificate_ID`"
 },
 {
 "Sid": "`ExampleStatementID2`",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`555555555555`"
 },
 "Action": [
 "acm-pca:IssueCertificate"
 ],
 "Resource": "arn:aws:acm-pca:`us-east-1`:`123456789012`:certificate-authority/`CA_ID`/certificate/`certificate_ID`",
 "Condition": {
 "StringEquals": {
 "acm-pca:TemplateArn": "arn:aws:acm-pca:::template/EndEntityCertificate/V1"
 }
 }
 }
 ]
}`

```

2. **File: policy2.json – Sharing access to a
   CA through AWS Organizations**

Replace `o-a1b2c3d4z5` with the AWS Organizations
ID.

For the resource ARN, replace the following with your own
values:

    * ``aws`` - The AWS
     partition. For example, `aws`,
     `aws-us-gov`, `aws-cn`, etc.
    * ``us-east-1`` - The AWS
     Region that the resource is available in, such as
     `us-west-1`.
    * ``111122223333``
     - The AWS account ID of the resource owner.
    * ``11223344-1234-1122-2233-112233445566``
     - The resource ID of the certificate authority.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "`ExampleStatementID3`",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "acm-pca:IssueCertificate",
 "Resource":"arn:aws:acm-pca:`us-east-1`:`123456789012`:certificate-authority/`CA_ID`/certificate/`certificate_ID`",
 "Condition": {
 "StringEquals": {
 "acm-pca:TemplateArn": "arn:aws:acm-pca:::template/EndEntityCertificate/V1",
 "aws:PrincipalOrgID": "`o-a1b2c3d4z5`"
 },
 "StringNotEquals": {
 "aws:PrincipalAccount": "`111122223333`"
 }
 }
 },
 {
 "Sid": "`ExampleStatementID4`",
 "Effect": "Allow",
 "Principal": "*",
 "Action": [
 "acm-pca:DescribeCertificateAuthority",
 "acm-pca:GetCertificate",
 "acm-pca:GetCertificateAuthorityCertificate",
 "acm-pca:ListPermissions",
 "acm-pca:ListTags"
 ],
 "Resource":"arn:aws:acm-pca:`us-east-1`:`123456789012`:certificate-authority/`CA_ID`/certificate/`certificate_ID`",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalOrgID": "`o-a1b2c3d4z5`"
 },
 "StringNotEquals": {
 "aws:PrincipalAccount": "`111122223333`"
 }
 }
 }
 ]
}`

```
