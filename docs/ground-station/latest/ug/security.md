# Data encryption at rest for AWS Ground Station

AWS Ground Station provides encryption by default to protect your sensitive data at rest using AWS owned encryption keys.

- _AWS owned keys_ - AWS Ground Station uses these keys by default to automatically encrypt personal,
  directly identifiable data and ephemerides. You cannot view, manage, or use AWS-owned keys, or audit their use;
  however, it is unnecessary to take any action or change programs to protect the keys that encrypt data.
  For more information, see [AWS-owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk")
  in the [AWS Key Management Service Developer Guide](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").

Encryption of data at rest by default helps by reducing the operational overhead and complexity involved in protecting sensitive data.
At the same time, it enables building secure applications that meet strict encryption compliance, as well as regulatory requirements.

AWS Ground Station enforces encryption on all sensitive, at-rest, data, however, for some AWS Ground Station resource,
such as ephemerides, you can choose to use a customer managed key in place of the default AWS managed keys.

- _Customer managed keys_ -- AWS Ground Station supports the use of a symmetric customer managed key
  that you create, own, and manage in place of the existing AWS owned encryption. Because you have
  full control of this layer of encryption, you can perform such tasks as:
  - Establishing and maintaining key policies
  - Establishing and maintaining IAM policies and grants
  - Enabling and disabling key policies
  - Rotating key cryptographic material
  - Adding tags
  - Creating key aliases
  - Scheduling keys for deletion

For more information, see [customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk")
in the [AWS Key Management Service Developer Guide](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").

The following table summarizes resources for which AWS Ground Station supports the use of Customer Managed Keys

| Data type                                                    | AWS owned key encryption | Customer managed key encryption (Optional) |
| ------------------------------------------------------------ | ------------------------ | ------------------------------------------ |
| Ephemeris data used to compute the trajectory of a Satellite | Enabled                  | Enabled                                    |
| Azimuth elevation ephemeris used to command antennas         | Enabled                  | Enabled                                    |

###### Note

AWS Ground Station automatically enables encryption at rest using AWS owned keys to protect personally
identifiable data at no charge. However, AWS KMS charges apply for using a customer managed key.
For more information about pricing, see the [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

For more information on AWS KMS, see the [AWS Key Management Service Developer Guide](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").

For information specific to each resource type, see:

- [Encryption at rest for TLE and OEM ephemeris data](security.md "security.md")
- [Encryption at rest for azimuth elevation ephemeris](security.md "security.md")

## Create a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console, or the AWS KMS APIs.

### To create a symmetric customer managed key

Follow the steps for creating symmetric customer managed key in the [AWS Key Management Service Developer Guide](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md").

### Key policy overview

Key policies control access to your customer managed key. Every customer managed key must have exactly one key
policy, which contains statements that determine who can use the key and how they can use it. When you create
your customer managed key, you can specify a key policy. For more information, see
[Managing access to customer managed keys](../../../kms/latest/developerguide/control-access.md "../../../kms/latest/developerguide/control-access.md") in the AWS Key Management Service Developer Guide.

To use your customer managed key with AWS Ground Station resources, you must configure the key policy to grant
appropriate permissions to the AWS Ground Station service. The specific permissions and policy configuration depend
on the type of resource you're encrypting:

- _For TLE and OEM ephemeris data_ - See [Encryption at rest for TLE and OEM ephemeris data](security.md "security.md") for specific key policy requirements and examples.
- _For azimuth elevation ephemeris data_ - See [Encryption at rest for azimuth elevation ephemeris](security.md "security.md") for specific key policy requirements and examples.

###### Note

The key policy configuration differs between ephemeris types. TLE and OEM ephemeris data uses grants
for key access, while azimuth elevation ephemeris uses direct key policy permissions. Ensure you configure your key
policy according to the specific resource type you're encrypting.

For more information about
[specifying permissions in a policy](../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements "../../../kms/latest/developerguide/control-access-overview.md#overview-policy-elements") and
[troubleshooting key access](../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam "../../../kms/latest/developerguide/policy-evaluation.md#example-no-iam") , see the AWS Key Management Service Developer Guide.

## Specifying a customer managed key for AWS Ground Station

You can specify a customer managed key to encrypt the following resources:

- Ephemeris (TLE, OEM, and azimuth elevation)

When you create a resource, you can specify the data key by providing a _kmsKeyArn_

- _kmsKeyArn_ - A
  [key identifier](../../../kms/latest/developerguide/concepts.md#key-id "../../../kms/latest/developerguide/concepts.md#key-id")
  for an AWS KMS customer managed key

## AWS Ground Station encryption context

An [encryption context](../../../kms/latest/developerguide/encrypt_context.md "../../../kms/latest/developerguide/encrypt_context.md")
is an optional set of key-value pairs that contain additional contextual information about the data.
AWS KMS uses the encryption context as additional authenticated data to support authenticated encryption.
When you include an encryption context in a request to encrypt data, AWS KMS binds the encryption context to the
encrypted data. To decrypt data, you include the same encryption context in the request.

AWS Ground Station uses different encryption context depending on the resource being encrypted and specifies
a specific encryption context for each key grant created.

For resource-specific encryption context details, see:

- [Encryption at rest for TLE and OEM ephemeris data](security.md "security.md")
- [Encryption at rest for azimuth elevation ephemeris](security.md "security.md")
