# Concepts

Learn the basic terms and concepts used in AWS Payment Cryptography and how you can use them to help you protect your data.

**Alias**

A user-friendly name that is associated with an AWS Payment Cryptography key. The alias can be used
interchangeably with [key ARN](#concepts.key-arn "#concepts.key-arn") in many of the AWS Payment Cryptography API operations.
Aliases allow keys to be rotated or otherwise changed without impacting your application code.
The alias name is a string of up to 256 characters. It uniquely identifies an
associated AWS Payment Cryptography key within an account and region. In AWS Payment Cryptography, alias names always
begin with `alias/`.

The format of an alias name is as follows:

```
alias/`<alias-name>`
```

For example:

```
alias/sampleAlias2
```

**Key ARN**

The key ARN is the Amazon Resource Name (ARN) of a key entry in AWS Payment Cryptography. It is a unique,
fully qualified identifier for the AWS Payment Cryptography key. A key ARN
includes an AWS account, region, and a randomly generated ID. The ARN is not related or derived from
the key material. As they are automatically assigned during create or import operations, these values are
not idempotent. Importing the same key multiple times will result in multiple key ARNs with their own lifecycle.

The format of a key ARN is as follows:

```
arn:`<partition>`:payment-cryptography:`<region>`:`<account-id>`:alias/`<alias-name>`
```

The following is a sample key ARN:

```
arn:aws:payment-cryptography:us-east-2:111122223333:key/kwapwa6qaifllw2h
```

**Key Identifier**

A Key Identifier is a reference to a key and one (or more) of them are typical inputs to AWS Payment Cryptography operations. Valid key identifiers could be either a
[Key Arn](#concepts.key-arn "#concepts.key-arn") a [Key Alias](#concepts.alias "#concepts.alias").

**AWS Payment Cryptography keys**

AWS Payment Cryptography keys (keys) are used for all cryptographic functions. Keys are either
generated directly by you using the create key command or added to the system by you calling key import. The origin of a key can be determined by reviewing the attribute KeyOrigin.
AWS Payment Cryptography also supports derived or intermediate keys used during cryptographic operations such as those used by DUKPT.

These keys have both immutable and mutable attributes defined at creation. Attributes,
such as algorithm, length, and usage are defined at creation and cannot be changed.
Others, such as effective date or expiration date, can be modified.
See the [AWS Payment Cryptography API Reference](../APIReference.md "../APIReference.md") for a complete list of AWS Payment Cryptography Key attributes.

AWS Payment Cryptography keys have key types, principally defined by [ANSI X9 TR 31](terminology.md#terms.tr31 "terminology.md#terms.tr31"),
that restrict their use to their intended purpose as specified in PCI PIN v3.1 Requirement 19.

Attributes are bound to keys using key blocks when stored, shared with other accounts,
or exported as specified in PCI PIN v3.1 Requirement 18-3.

Keys are identified in the AWS Payment Cryptography platform using a unique value known as a key Amazon Resource Name (`ARN`).

###### Note

Key `ARN` is generated when a key is initially created
or imported into the AWS Payment Cryptography service. Thus, if adding the same key material multiple times
using the import key
functionality, the same key material will be located
under multiple key `ARNS` but each with a different key lifecycle.
