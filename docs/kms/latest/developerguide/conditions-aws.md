# AWS global condition keys

AWS defines [global condition
keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys"), a set of policy conditions keys for all AWS services that use IAM for
access control. AWS KMS supports all global condition keys. You can use them in AWS KMS key
policies and IAM policies.

For example, you can use the [aws:PrincipalArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalarn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalarn") global condition key to allow access to an AWS KMS key
(KMS key) only when the principal in the request is represented by the Amazon Resource Name
(ARN) in the condition key value. To support [attribute-based access
control](abac.md "abac.md") (ABAC) in AWS KMS, you can use the [aws:ResourceTag/_tag-key_](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") global condition key
in an IAM policy to allow access to KMS keys with a particular tag.

To help prevent an AWS service from being used as a confused deputy in a policy where
the principal is an [AWS
service principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services"), you can use the [aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") or [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition keys. For details, see [Using aws:SourceArn or
aws:SourceAccount condition keys](least-privilege.md#least-privilege-source-arn "least-privilege.md#least-privilege-source-arn").

For information about AWS global condition keys, including the types of requests in
which they are available, see [AWS Global Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_. For examples of using global condition keys in IAM policies,
see [Controlling
Access to Requests](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-requests "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-requests") and [Controlling Tag
Keys](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-tag-keys "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-tag-keys") in the _IAM User Guide_.

The following topics provide special guidance for using condition keys based on IP
addresses and VPC endpoints.

###### Topics

- [Using the IP address condition in policies with
  AWS KMS permissions](#conditions-aws-ip-address "#conditions-aws-ip-address")
- [Using VPC endpoint conditions in policies with AWS KMS
  permissions](#conditions-aws-vpce "#conditions-aws-vpce")
- [Using IPv6 addresses in IAM and AWS KMS key
  policies](#KMS-IPv6-policies "#KMS-IPv6-policies")

## Using the IP address condition in policies with

AWS KMS permissions

You can use AWS KMS to protect your data in an [integrated AWS service](service-integration.md "service-integration.md"). But use caution when specifying the [IP address condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IPAddress "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IPAddress") or the `aws:SourceIp` condition key in
the same policy statement that allows or denies access to AWS KMS. For example, the policy in
[AWS: Denies
Access to AWS Based on the Source IP](../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md") restricts AWS actions to requests from
the specified IP range.

Consider this scenario:

1. You attach a policy like the one shown at [AWS: Denies Access
   to AWS Based on the Source IP](../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-ip.md") to an IAM identity. You set the value of the
   `aws:SourceIp` condition key to the range of IP addresses for the user's
   company. This IAM identity has other policies attached that allow it to use Amazon EBS,
   Amazon EC2, and AWS KMS.
2. The identity attempts to attach an encrypted EBS volume to an EC2 instance. This
   action fails with an authorization error even though the user has permission to use all
   the relevant services.

Step 2 fails because the request to AWS KMS to decrypt the volume's encrypted data key
comes from an IP address that is associated with the Amazon EC2 infrastructure. To succeed, the
request must come from the IP address of the originating user. Because the policy in step 1
explicitly denies all requests from IP addresses other than those specified, Amazon EC2 is denied
permission to decrypt the EBS volume's encrypted data key.

Also, the `aws:SourceIP` condition key is not effective when the request
comes from an [Amazon VPC endpoint](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md"). To
restrict requests to a VPC endpoint, including an [AWS KMS VPC
endpoint](kms-vpc-endpoint.md "kms-vpc-endpoint.md"), use the `aws:SourceVpce` or `aws:SourceVpc`
condition keys. For more information, see [VPC Endpoints -
Controlling the Use of Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md#vpc-endpoints-iam-access "../../../vpc/latest/userguide/vpc-endpoints.md#vpc-endpoints-iam-access") in the _Amazon VPC User
Guide_.

## Using VPC endpoint conditions in policies with AWS KMS

permissions

[AWS KMS supports Amazon Virtual Private Cloud (Amazon VPC) endpoints](kms-vpc-endpoint.md "kms-vpc-endpoint.md") that
are powered by [AWS
PrivateLink](../../../vpc/latest/userguide/VPC_Introduction.md#what-is-privatelink "../../../vpc/latest/userguide/VPC_Introduction.md#what-is-privatelink"). You can use the following [global condition
keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys") in key policies and IAM policies to control access to AWS KMS resources when
the request comes from a VPC or uses a VPC endpoint. For details, see [Use VPC endpoints to control access to AWS KMS resources](vpce-policy-condition.md "vpce-policy-condition.md").

- `aws:SourceVpc` limits access to requests from the specified VPC.
- `aws:SourceVpce` limits access to requests from the specified VPC
  endpoint.

If you use these condition keys to control access to KMS keys, you might inadvertently
deny access to AWS services that use AWS KMS on your behalf.

Take care to avoid a situation like the [IP
address condition keys](#conditions-aws-ip-address "#conditions-aws-ip-address") example. If you restrict requests for a KMS key to a VPC
or VPC endpoint, calls to AWS KMS from an integrated service, such as Amazon S3 or Amazon EBS, might
fail. This can happen even if the source request ultimately originates in the VPC or from
the VPC endpoint.

## Using IPv6 addresses in IAM and AWS KMS key

policies

Before trying to access AWS KMS over IPv6, ensure any key and IAM policies containing IP
address restrictions are updated to include IPv6 address ranges. IP based policies that are
not updated to handle IPv6 addresses may result in clients incorrectly losing or gaining
access when they start using IPv6. For general guidance on KMS access controls, see [KMS key access and permissions](control-access.md "control-access.md"). To learn about KMS and dual
stack support, see [Dual-stack endpoint support](ipv6-kms.md "ipv6-kms.md").

###### Important

These statements do not allow any actions. Use these statements in combination with
other statements that allow specific actions.

The following statement explicitly denies access to all KMS permissions for requests
originating from the `192.0.2.*` range of IPv4 addresses. Any IP addresses
outside of this range are not explicitly denied KMS permissions. Since all IPv6 addresses
are outside of the denied range, this statement does not explicitly deny KMS permissions for
any IPv6 addresses.

```
{
     "Sid": "DenyKMSPermissions",
     "Effect": "Deny",
    "Action": [
        "kms:*"
    ],
    "Resource": "*",
    "Condition": {
        "NotIpAddress": {
            "aws:SourceIp": [
                "`192.0.2.0/24`"
            ]
        }
    }
}
```

You can modify the `Condition` element to deny both IPv4
(`192.0.2.0/24`) and IPv6 (`2001:db8:1234::/32`) address ranges as
shown in the following example.

```
{
    "Sid": "DenyKMSPermissions",
    "Effect": "Deny",
    "Action": [
        "kms:*"
    ],
    "Resource": "*",
    "Condition": {
        "NotIpAddress": {
            "aws:SourceIp": [
                "`192.0.2.0/24`",
                "`2001:db8:1234::/32`"
            ]
        }
    }
}
```
