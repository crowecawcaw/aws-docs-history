# Basic concepts

Learning some basic terms and concepts will help you get the most out of AWS Key Management Service.

**AWS KMS key**

###### Note

AWS KMS is replacing the term _customer master key (CMK)_ with _AWS KMS key_ and _KMS key_. The concept has not changed. To prevent breaking changes, AWS KMS is keeping some variations of this term.

A logical key that represents the top of your key hierarchy. A KMS key is given an Amazon Resource
Name (ARN) that includes a unique key identifier, or key ID.
AWS KMS keys have three types:

- **Customer managed key** – Customers create and control the
  lifecycle and key policies of customer managed keys. All
  requests made against these keys are logged as
  CloudTrail events.
- **AWS managed keys** – AWS creates and controls the
  lifecycle and key policies of
  AWS managed keys, which are resources in a
  customer’s AWS account. Customers can view
  access policies and CloudTrail events for
  AWS managed keys, but cannot manage any
  aspect of these keys. All requests made against
  these keys are logged as CloudTrail events.
- **AWS owned keys** – These keys are created
  and exclusively used by AWS for internal
  encryption operations across different AWS
  services. Customers do not have visibility into
  key policies or AWS owned key usage in
  CloudTrail.

**Alias**

A user-friendly name that is associated with a KMS key. The alias can be used interchangeably with key ID in many of the AWS KMS API operations.

**Permissions**

A policy attached to a KMS key that defines permissions on the key. The default policy
allows any principals that you define, as well as allowing
the AWS account to add IAM policies that reference the
key.

**Grants**

The delegated permission to use a KMS key when the intended IAM principals or duration of usage
is not known at the outset and therefore cannot be added to
a key or IAM policy. One use of grants is to deﬁne
scoped-down permissions for how an AWS service can use a
KMS key. The service may need to use your key to do asynchronous
work on your behalf on encrypted data in the absence of a
direct-signed API call from you.

**Data keys**

Cryptographic keys generated on HSMs, protected by a KMS key. AWS KMS allows
authorized entities to obtain data keys protected by a KMS key.
They can be returned both as plaintext (unencrypted) data
keys and as encrypted data keys. Data keys can be symmetric
or asymmetric (with both the public and private portions
returned).

**Ciphertexts**

The encrypted output of AWS KMS, sometimes referred to as customer ciphertext to eliminate
confusion. Ciphertext contains encrypted data with
additional information that identifies the KMS key to use in the
decryption process. Encrypted data keys are one common
example of ciphertext produced when using a KMS key, but any
data under 4 KB in size can be encrypted under a KMS key to
produce a ciphertext.

**Encryption context**

A key–value pair map of additional information that is associated with AWS KMS–protected
information. AWS KMS uses authenticated encryption to protect
data keys. The encryption context is incorporated into the
AAD of the authenticated encryption in AWS KMS–encrypted
ciphertexts. This context information is optional and not
returned when requesting a key (or an encryption operation).
But if used, this context value is required to successfully
complete a decryption operation. An intended use of the
encryption context is to provide additional authenticated
information. This information can help you enforce policies
and be included in the AWS CloudTrail logs. For example, you
could use a key–value pair of {"key name":"satellite uplink
key"} to name the data key. Subsequent use of the key
creates an AWS CloudTrail entry that includes “key name”:
“satellite uplink key.” This additional information can
provide useful context to understand why a given KMS key
was used.

**Public key**

When using asymmetric ciphers (RSA or elliptic curve), the
public key is the “public component” of a public-private key
pair. The public key can be shared and distributed to
entities that need to encrypt data for the owner of the
public-private key pair. For digital signature operations,
the public key is used to verify the signature.

**Private key**

When using asymmetric ciphers (RSA or elliptic curve), the private key is the “private
component” of a public-private key pair. The private key is
used to decrypt data or create digital signatures. Similar
to symmetric KMS keys, private keys are encrypted in HSMs.
They are decrypted only into the short term memory of the
HSM and only for the time needed to process your
cryptographic request.
