# Connecting to AWS Payment Cryptography through a VPC endpoint

You can connect directly to AWS Payment Cryptography through a private interface endpoint in your virtual
private cloud (VPC). When you use an interface VPC endpoint, communication between your VPC and
AWS Payment Cryptography is conducted entirely within the AWS network.

AWS Payment Cryptography supports Amazon Virtual Private Cloud (Amazon VPC) endpoints powered by [AWS PrivateLink](../../../vpc/latest/privatelink.md "../../../vpc/latest/privatelink.md"). Each VPC endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") (ENIs) with private IP
addresses in your VPC subnets.

The interface VPC endpoint connects your VPC directly to AWS Payment Cryptography without an internet gateway,
NAT device, VPN connection, or AWS Direct Connect connection. The instances in your VPC do not need
public IP addresses to communicate with AWS Payment Cryptography.

###### Regions

AWS Payment Cryptography supports VPC endpoints and VPC endpoint policies in all AWS Regions in which
[AWS Payment Cryptography](../../../general/latest/gr/payment-cryptography.md "../../../general/latest/gr/payment-cryptography.md") is supported.

###### Topics

- [Considerations for AWS Payment Cryptography VPC endpoints](#vpce-considerations "#vpce-considerations")
- [Creating a VPC endpoint for AWS Payment Cryptography](#vpce-create-endpoint "#vpce-create-endpoint")
- [Connecting to an AWS Payment Cryptography VPC endpoint](#vpce-connect "#vpce-connect")
- [Controlling access to a VPC endpoint](#vpce-policy "#vpce-policy")
- [Using a VPC endpoint in a policy statement](#vpce-policy-condition "#vpce-policy-condition")
- [Logging your VPC endpoint](#vpce-logging "#vpce-logging")

## Considerations for AWS Payment Cryptography VPC endpoints

###### Note

Although VPC endpoints allows you to connect to the service in as few as one availability zone(AZ), we recommend
connecting to three availability zones for high availability and redundancy purposes.

Before you set up an interface VPC endpoint for AWS Payment Cryptography, review the [Interface endpoint
properties and limitations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") topic in the _AWS PrivateLink Guide_.

AWS Payment Cryptography support for a VPC endpoint includes the following.

- You can use your VPC endpoint to call all [AWS Payment Cryptography Control plane operations](../APIReference/API_Operations.md "../APIReference/API_Operations.md") and [AWS Payment Cryptography Data plane operations](../DataAPIReference/API_Operations.md "../DataAPIReference/API_Operations.md") from a
  VPC.
- You can create an interface VPC endpoint that connects to an AWS Payment Cryptography region endpoint.
- AWS Payment Cryptography consists of a control plane and a data plane. You can chose to setup one or both sub-services AWS PrivateLink but each is configured separately.
- You can use AWS CloudTrail logs to audit your use of AWS Payment Cryptography keys through the VPC endpoint.
  For details, see [Logging your VPC endpoint](#vpce-logging "#vpce-logging").

## Creating a VPC endpoint for AWS Payment Cryptography

You can create a VPC endpoint for AWS Payment Cryptography by using the Amazon VPC console or the Amazon VPC API. For
more information, see [Create an interface
endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") in the _AWS PrivateLink Guide_.

- To create a VPC endpoint for AWS Payment Cryptography, use the following service names:

```
com.amazonaws.`region`.payment-cryptography.controlplane
```

```
com.amazonaws.`region`.payment-cryptography.dataplane
```

For example, in the US West (Oregon) Region (`us-west-2`), the service
names would be:

```
com.amazonaws.us-west-2.payment-cryptography.controlplane
```

```
com.amazonaws.us-west-2.payment-cryptography.dataplane
```

To make it easier to use the VPC endpoint, you can enable a [private DNS name](../../../vpc/latest/privatelink/verify-domains.md "../../../vpc/latest/privatelink/verify-domains.md") for your VPC
endpoint. If you select the **Enable DNS Name** option, the standard AWS Payment Cryptography
DNS hostname resolves to your VPC endpoint. For example,
`https://controlplane.payment-cryptography.us-west-2.amazonaws.com` would resolve to a VPC endpoint connected
to service name `com.amazonaws.us-west-2.payment-cryptography.controlplane`.

This option makes it easier to use the VPC endpoint. The AWS SDKs and AWS CLI use the
standard AWS Payment Cryptography DNS hostname by default, so you do not need to specify the VPC endpoint URL in
applications and commands.

For more information, see [Accessing a
service through an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint") in the
_AWS PrivateLink Guide_.

## Connecting to an AWS Payment Cryptography VPC endpoint

You can connect to AWS Payment Cryptography through the VPC endpoint by using an AWS SDK, the AWS CLI or
AWS Tools for PowerShell. To specify the VPC endpoint, use its DNS name.

For example, this [list-keys](../APIReference/list-keys.md "../APIReference/list-keys.md") command
uses the `endpoint-url` parameter to specify the VPC endpoint. To use a command
like this, replace the example VPC endpoint ID with one in your account.

```
`$` `aws payment-cryptography list-keys --endpoint-url `https://vpce-1234abcdf5678c90a-09p7654s-us-east-1a.ec2.us-east-1.vpce.amazonaws.com``
```

If you enabled private hostnames when you created your VPC endpoint, you do not need to
specify the VPC endpoint URL in your CLI commands or application configuration. The standard
AWS Payment Cryptography DNS hostname resolves to your VPC endpoint. The AWS CLI and SDKs use this hostname by
default, so you can begin using the VPC endpoint to connect to an AWS Payment Cryptography regional endpoint
without changing anything in your scripts and applications.

To use private hostnames, the `enableDnsHostnames` and
`enableDnsSupport` attributes of your VPC must be set to `true`. To
set these attributes, use the [ModifyVpcAttribute](../../../AWSEC2/latest/APIReference/API_ModifyVpcAttribute.md "../../../AWSEC2/latest/APIReference/API_ModifyVpcAttribute.md") operation. For details, see [View and update DNS attributes for your
VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating") in the _Amazon VPC User Guide_.

## Controlling access to a VPC endpoint

To control access to your VPC endpoint for AWS Payment Cryptography, attach a _VPC
endpoint policy_ to your VPC endpoint. The endpoint policy determines whether
principals can use the VPC endpoint to call AWS Payment Cryptography operations with specific AWS Payment Cryptography resources.

You can create a VPC endpoint policy when you create your endpoint, and you can change the
VPC endpoint policy at any time. Use the VPC management console, or the [CreateVpcEndpoint](../../../AWSEC2/latest/APIReference/API_CreateVpcEndpoint.md "../../../AWSEC2/latest/APIReference/API_CreateVpcEndpoint.md") or [ModifyVpcEndpoint](../../../AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.md "../../../AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.md") operations. You can
also create and change a VPC endpoint policy by [using an AWS CloudFormation template](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md").
For help using the VPC management console, see [Create an interface
endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") and [Modifying an
interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#modify-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#modify-interface-endpoint") in the _AWS PrivateLink Guide_.

For help writing and formatting a JSON policy document, see the [IAM JSON Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the
_IAM User Guide_.

###### Topics

- [About VPC endpoint policies](#vpce-policy-about "#vpce-policy-about")
- [Default VPC endpoint policy](#vpce-default-policy "#vpce-default-policy")
- [Creating a VPC endpoint policy](#vpce-policy-create "#vpce-policy-create")
- [Viewing a VPC endpoint policy](#vpce-policy-get "#vpce-policy-get")

### About VPC endpoint policies

For an AWS Payment Cryptography request that uses a VPC endpoint to be successful, the principal requires
permissions from two sources:

- An [identity-based policy](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md") must give the principal permission
  to call the operation on the resource (AWS Payment Cryptography keys or alias).
- A VPC endpoint policy must give the principal permission to use the endpoint to make
  the request.

For example, a key policy might give a principal permission to call [Decrypt](../DataAPIReference/API_DecryptData.md "../DataAPIReference/API_DecryptData.md") on a particular AWS Payment Cryptography keys. However,
the VPC endpoint policy might not allow that principal to call `Decrypt` on that
AWS Payment Cryptography keys by using the endpoint.

Or a VPC endpoint policy might allow a principal to use the endpoint to call [StopKeyUsage](../APIReference/API_StopKeyUsage.md "../APIReference/API_StopKeyUsage.md") on certain AWS Payment Cryptography keys. But if
the principal doesn't have those permissions from a IAM policy, the
request fails.

### Default VPC endpoint policy

Every VPC endpoint has a VPC endpoint policy, but you are not required to specify the
policy. If you don't specify a policy, the default endpoint policy allows all operations by
all principals on all resources over the endpoint.

However, for AWS Payment Cryptography resources, the principal must also have permission to call the
operation from an [IAM policy](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
Therefore, in practice, the default policy says that if a principal has permission to call
an operation on a resource, they can also call it by using the endpoint.

```
{
  "Statement": [
    {
      "Action": "*",
      "Effect": "Allow",
      "Principal": "*",
      "Resource": "*"
    }
  ]
}
```

To allow principals to use the VPC endpoint for only a subset of their permitted
operations, [create or update the VPC endpoint
policy](#vpce-policy-create "#vpce-policy-create").

### Creating a VPC endpoint policy

A VPC endpoint policy determines whether a principal has permission to use the VPC
endpoint to perform operations on a resource. For AWS Payment Cryptography resources, the principal must also
have permission to perform the operations from an [IAM policy](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

Each VPC endpoint policy statement requires the following elements:

- The principal that can perform actions
- The actions that can be performed
- The resources on which actions can be performed

The policy statement doesn't specify the VPC endpoint. Instead, it applies to any VPC
endpoint to which the policy is attached. For more information, see [Controlling access to services with VPC
endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

The following is an example of a VPC endpoint policy for AWS Payment Cryptography. When attached to a VPC
endpoint, this policy allows `ExampleUser` to use the VPC endpoint to call the
specified operations on the specified AWS Payment Cryptography keys. Before using a policy like this one,
replace the example principal and [key identifier](concepts.md#concepts.key-identifer "concepts.md#concepts.key-identifer") with valid
values from your account.

```
{
   "Statement":[
      {
         "Sid": "AllowDecryptAndView",
         "Principal": {"AWS": "`arn:aws:iam::111122223333:user/ExampleUser`"},
         "Effect":"Allow",
         "Action": [
             "payment-cryptography:Decrypt",
             "payment-cryptography:GetKey",
             "payment-cryptography:ListAliases",
             "payment-cryptography:ListKeys",
             "payment-cryptography:GetAlias"
          ],
         "Resource": "`arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h`"
      }
   ]
}
```

AWS CloudTrail logs all operations that use the VPC endpoint. However, your CloudTrail logs
don’t include operations requested by principals in other accounts or operations for
AWS Payment Cryptography keys in other accounts.

As such, you might want to create a VPC endpoint policy that prevents principals in
external accounts from using the VPC endpoint to call any AWS Payment Cryptography operations on any keys in
the local account.

The following example uses the [aws:PrincipalAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalaccount") global condition key to deny access to all principals for
all operations on all AWS Payment Cryptography keys unless the principal is in the local account. Before using
a policy like this one, replace the example account ID with a valid one.

```
{
  "Statement": [
    {
      "Sid": "AccessForASpecificAccount",
      "Principal": {"AWS": "*"},
      "Action": "payment-cryptography:*",
      "Effect": "Deny",
      "Resource": "arn:aws:payment-cryptography:*:`111122223333`:key/*",
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalAccount": "`111122223333`"
        }
      }
    }
  ]
}
```

### Viewing a VPC endpoint policy

To view the VPC endpoint policy for an endpoint, use the [VPC management console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/") or the [DescribeVpcEndpoints](../../../AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.md")
operation.

The following AWS CLI command gets the policy for the endpoint with the specified VPC
endpoint ID.

Before using this command, replace the example endpoint ID with a valid one from your
account.

```
`$` `aws ec2 describe-vpc-endpoints \
--query 'VpcEndpoints[?VpcEndpointId==``vpce-1234abcdf5678c90a``].[PolicyDocument]'
--output text`
```

## Using a VPC endpoint in a policy statement

You can control access to AWS Payment Cryptography resources and operations when the request comes from VPC
or uses a VPC endpoint. To do so, use one an [IAM policy](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")

- Use the `aws:sourceVpce` condition key to grant or restrict access based on
  the VPC endpoint.
- Use the `aws:sourceVpc` condition key to grant or restrict access based on
  the VPC that hosts the private endpoint.

###### Note

The `aws:sourceIP` condition key is not effective when the request
comes from an [Amazon VPC endpoint](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md"). To
restrict requests to a VPC endpoint, use the `aws:sourceVpce` or
`aws:sourceVpc` condition keys. For more information, see [Identity and access management for VPC
endpoints and VPC endpoint services](../../../vpc/latest/privatelink/vpc-endpoints-iam.md "../../../vpc/latest/privatelink/vpc-endpoints-iam.md") in the _AWS PrivateLink Guide_.

You can use these global condition keys to control access to AWS Payment Cryptography keys,
aliases, and to operations like [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")
that don't depend on any particular resource.

For example, the following sample key policy allows a user to perform particular cryptographic
operations with a AWS Payment Cryptography keys only when the request uses the specified VPC endpoint, blocking access both from the Internet and AWS PrivateLink connections (if setup). When a user
makes a request to AWS Payment Cryptography, the VPC endpoint ID in the request is compared to the
`aws:sourceVpce` condition key value in the policy. If they do not match, the
request is denied.

To use a policy like this one, replace the placeholder AWS account ID and VPC endpoint
IDs with valid values for your account.

JSON

```
`{
 "Id": "example-key-1",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnableIAMPolicies",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:root"
 ]
 },
 "Action": [
 "payment-cryptography:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "RestrictUsageToMyVPCEndpoint",
 "Effect": "Deny",
 "Principal": "*",
 "Action": [
 "payment-cryptography:EncryptData",
 "payment-cryptography:DecryptData"
 ],
 "Resource": "arn:aws:payment-cryptography:us-east-1:111122223333:key/*",
 "Condition": {
 "StringNotEquals": {
 "aws:sourceVpce": "`vpce-1234abcdf5678c90a`"
 }
 }
 }

 ]
}`

```

You can also use the `aws:sourceVpc` condition key to restrict access to your
AWS Payment Cryptography keys based on the VPC in which VPC endpoint resides.

The following sample key policy allows commands that manage the AWS Payment Cryptography keys only when they
come from `vpc-12345678`. In addition, it allows commands that use the AWS Payment Cryptography keys
for cryptographic operations only when they come from `vpc-2b2b2b2b`. You might use
a policy like this one if an application is running in one VPC, but you use a second, isolated
VPC for management functions.

To use a policy like this one, replace the placeholder AWS account ID and VPC endpoint
IDs with valid values for your account.

JSON

```
`{
 "Id": "example-key-2",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAdminActionsFrom`VPC12345678`",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`111122223333`"
 },
 "Action": [
 "payment-cryptography:Create*",
 "payment-cryptography:Encrypt*",
 "payment-cryptography:ImportKey*",
 "payment-cryptography:GetParametersForImport*",
 "payment-cryptography:TagResource",
 "payment-cryptography:UntagResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:sourceVpc": "`vpc-12345678`"
 }
 }
 },
 {
 "Sid": "AllowKeyUsageFrom`VPC2b2b2b2b`",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`111122223333`"
 },
 "Action": [
 "payment-cryptography:Encrypt*",
 "payment-cryptography:Decrypt*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:sourceVpc": "`vpc-2b2b2b2b`"
 }
 }
 },
 {
 "Sid": "AllowListReadActionsFromEverywhere",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`111122223333`"
 },
 "Action": [
 "payment-cryptography:List*",
 "payment-cryptography:Get*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Logging your VPC endpoint

AWS CloudTrail logs all operations that use the VPC endpoint. When a request to AWS Payment Cryptography uses a VPC
endpoint, the VPC endpoint ID appears in the [AWS CloudTrail
log](monitoring-cloudtrail.md "monitoring-cloudtrail.md") entry that records the request. You can use the endpoint ID to audit the use of
your AWS Payment Cryptography VPC endpoint.

To protect your VPC, requests that are denied by a [VPC endpoint
policy](#vpce-policy "#vpce-policy"), but otherwise would have been allowed, are not recorded in [AWS CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md").

For example, this sample log entry records a [GenerateMac](../DataAPIReference/API_GenerateMac.md "../DataAPIReference/API_GenerateMac.md") request that used the
VPC endpoint. The `vpcEndpointId` field appears at the end of the log entry.

```
{
      "eventVersion": "1.08",
      "userIdentity": {
          "principalId": "TESTXECZ5U9M4LGF2N6Y5:i-98761b8890c09a34a",
          "arn": "arn:aws:sts::111122223333:assumed-role/samplerole/i-98761b8890c09a34a",
          "accountId": "111122223333",
          "accessKeyId": "TESTXECZ5U2ZULLHHMJG",
          "sessionContext": {
              "sessionIssuer": {
                  "type": "Role",
                  "principalId": "TESTXECZ5U9M4LGF2N6Y5",
                  "arn": "arn:aws:iam::111122223333:role/samplerole",
                  "accountId": "111122223333",
                  "userName": "samplerole"
              },
              "webIdFederationData": {},
              "attributes": {
                  "creationDate": "2024-05-27T19:34:10Z",
                  "mfaAuthenticated": "false"
              },
              "ec2RoleDelivery": "2.0"
          }
      },
      "eventTime": "2024-05-27T19:49:54Z",
      "eventSource": "payment-cryptography.amazonaws.com",
      "eventName": "CreateKey",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "172.31.85.253",
      "userAgent": "aws-cli/2.14.5 Python/3.9.16 Linux/6.1.79-99.167.amzn2023.x86_64 source/x86_64.amzn.2023 prompt/off command/payment-cryptography.create-key",
      "requestParameters": {
          "keyAttributes": {
              "keyUsage": "TR31_M1_ISO_9797_1_MAC_KEY",
              "keyClass": "SYMMETRIC_KEY",
              "keyAlgorithm": "TDES_2KEY",
              "keyModesOfUse": {
                  "encrypt": false,
                  "decrypt": false,
                  "wrap": false,
                  "unwrap": false,
                  "generate": true,
                  "sign": false,
                  "verify": true,
                  "deriveKey": false,
                  "noRestrictions": false
              }
          },
          "exportable": true
      },
      "responseElements": {
          "key": {
              "keyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h",
              "keyAttributes": {
                  "keyUsage": "TR31_M1_ISO_9797_1_MAC_KEY",
                  "keyClass": "SYMMETRIC_KEY",
                  "keyAlgorithm": "TDES_2KEY",
                  "keyModesOfUse": {
                      "encrypt": false,
                      "decrypt": false,
                      "wrap": false,
                      "unwrap": false,
                      "generate": true,
                      "sign": false,
                      "verify": true,
                      "deriveKey": false,
                      "noRestrictions": false
                  }
              },
              "keyCheckValue": "A486ED",
              "keyCheckValueAlgorithm": "ANSI_X9_24",
              "enabled": true,
              "exportable": true,
              "keyState": "CREATE_COMPLETE",
              "keyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY",
              "createTimestamp": "May 27, 2024, 7:49:54 PM",
              "usageStartTimestamp": "May 27, 2024, 7:49:54 PM"
          }
      },
      "requestID": "f3020b3c-4e86-47f5-808f-14c7a4a99161",
      "eventID": "b87c3d30-f3ab-4131-87e8-bc54cfef9d29",
      "readOnly": false,
      "eventType": "AwsApiCall",
      "managementEvent": true,
      "recipientAccountId": "111122223333",
      "vpcEndpointId": "vpce-1234abcdf5678c90a",
      "eventCategory": "Management",
      "tlsDetails": {
          "tlsVersion": "TLSv1.3",
          "cipherSuite": "TLS_AES_128_GCM_SHA256",
          "clientProvidedHostHeader": "vpce-1234abcdf5678c90a-oo28vrvr.controlplane.payment-cryptography.us-east-1.vpce.amazonaws.com"
      }
  }
```
