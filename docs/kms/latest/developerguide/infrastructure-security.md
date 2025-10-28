# Infrastructure security in AWS Key Management Service

As a managed service, AWS Key Management Service (AWS KMS) is protected by the AWS global network
security procedures that are described in the [Amazon Web
Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf").

To access AWS KMS over the network, you can call the AWS KMS API operations that are
described in the [AWS Key Management Service API Reference](../APIReference.md "../APIReference.md"). AWS KMS requires TLS 1.2 and
recommends TLS 1.3 in all regions. AWS KMS
also supports hybrid post-quantum TLS for AWS KMS service endpoints in all regions, except
China Regions. AWS KMS does not support hybrid post-quantum TLS for FIPS endpoints in AWS GovCloud (US).
To use [standard AWS KMS
endpoints](../../../general/latest/gr/kms.md "../../../general/latest/gr/kms.md") or [AWS KMS FIPS endpoints](../../../general/latest/gr/kms.md "../../../general/latest/gr/kms.md"), clients
must support TLS 1.2 or later. Clients must also support cipher suites with perfect forward
secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman
(ECDHE). Most modern systems, such as Java 7 and later, support these modes.

Additionally, requests must be signed by using an access key ID and a secret access key that
is associated with an IAM principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate temporary security credentials to sign requests.

You can call these API operations from any network location, but AWS KMS supports
global policy conditions that let you control access to a KMS key based on the source IP
address, VPC, and VPC endpoint. You can use these condition keys in key policies and IAM
policies. However, these conditions can prevent AWS from using the KMS key on your behalf.
For details, see [AWS global condition keys](conditions-aws.md "conditions-aws.md").

For example, the following key policy statement allows users who can assume the
`KMSTestRole` role to use this AWS KMS key for the specified [cryptographic operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations") unless the source IP
address is one of the IP addresses specified in the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": {"AWS":
 "arn:aws:iam::`111122223333`:role/`KMSTestRole`"},
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "NotIpAddress": {
 "aws:SourceIp": [
 "192.0.2.0/24",
 "203.0.113.0/24"
 ]
 }
 }
 }
}`

```

## Isolation of Physical Hosts

The security of the physical infrastructure that AWS KMS uses is subject to the controls
described in the **Physical and Environmental Security** section
of the [Amazon Web Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf"). You can find more detail in
compliance reports and third-party audit findings listed in the previous section.

AWS KMS is supported by dedicated hardened hardware security modules (HSMs) designed with
specific controls to resist physical attacks. The HSMs are physical devices that _do not_ have a virtualization layer, such as a hypervisor, that
shares the physical device among several logical tenants. The key material for AWS KMS keys
is stored only in volatile memory on the HSMs, and only while the KMS key is in use. This
memory is erased when the HSM moves out of the operational state, including intended and
unintended shutdowns and resets. For detailed information about the operation of AWS KMS HSMs,
see [AWS Key Management Service Cryptographic Details](../cryptographic-details.md "../cryptographic-details.md").
