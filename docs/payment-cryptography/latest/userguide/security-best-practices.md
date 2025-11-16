# Security best practices for AWS Payment Cryptography

AWS Payment Cryptography supports many security features that are either built-in or that you can optionally implement to enhance the
protection of your encryption keys and ensure that they are used for their intended purpose, including [IAM policies](security_iam_service-with-iam.md "security_iam_service-with-iam.md"),
an extensive set of policy condition keys to refine your key policies and IAM policies and built-in enforcement of PCI PIN rules regarding key blocks.

###### Important

The general
guidelines provided do not represent a complete security solution. Because not
all best practices are appropriate for all situations, these are not intended to be
prescriptive.

- **Key Usage and Modes of Use**: AWS Payment Cryptography follows and enforces key usage and mode of use restrictions as described in
  ANSI X9 TR 31-2018 Interoperable Secure Key Exchange Key Block Specification and consistent with PCI PIN Security Requirement 18-3.
  This limits the ability to use a single key for multiple purposes and cryptographically binds the key metadata (such as permitted operations) to the key material itself.
  AWS Payment Cryptography automatically enforces these restrictions such as that a key encryption key (TR31_K0_KEY_ENCRYPTION_KEY) cannot also be used for data decryption. See
  [Understanding key attributes for AWS Payment Cryptography key](keys-validattributes.md "keys-validattributes.md") for more details.
- **Limit sharing of symmetric key material**: Only share symmetric key material (such as Pin Encryption Keys or Key Encryption Keys) with
  at most one other entity. If there is a need to transit sensitive material to more entities or partners, create additional keys. AWS Payment Cryptography never exposes
  symmetric key material or asymmetric private key material in the clear.
- **Use aliases or tags to associate keys with certain use cases or partners**: Aliases can be used to easily denote the use case associated with
  a key such as alias/BIN_12345_CVK to denote a card verification key associated with BIN 12345. To provide more flexibility, consider
  creating tags such as bin=12345, use_case=acquiring,country=us,partner=foo. Aliases and tags can also be used to
  limit access such as enforcing access controls between issuing and acquiring use cases.
- **Practice least privileged access**: IAM can be used to limit production access to systems rather than individuals, such as
  prohibiting individual users from creating keys or running cryptographic operations. IAM can also be used to limit access to both commands and keys that may not be applicable
  for your use case, such as limiting the ability to generate or validate pins for an acquirer. Another way to use least privileged access is to restrict sensitive
  operations (such as key import) to specific service accounts. See [AWS Payment Cryptography identity-based policy
  examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md") for examples.
  **See also**

- [Identity and access management for AWS Payment Cryptography](security-iam.md "security-iam.md")
- [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in
  the _IAM User Guide_
