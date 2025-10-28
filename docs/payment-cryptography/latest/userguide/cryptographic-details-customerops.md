# Customer operations

AWS Payment Cryptography has full responsibility for the HSM physical compliance under PCI standards. The service also provides a secure key store and
ensures that keys can only be used for the purposes permitted by PCI standards and specified by you during creation or import.
You are responsible for configuring key attributes and access to leverage the security and compliance capabilities of the service.

###### Topics

- [Generating keys](#w4aac34c25b7 "#w4aac34c25b7")
- [Importing keys](#w4aac34c25b9 "#w4aac34c25b9")
- [Exporting keys](#w4aac34c25c11 "#w4aac34c25c11")
- [Deleting keys](#w4aac34c25c13 "#w4aac34c25c13")
- [Rotating keys](#w4aac34c25c15 "#w4aac34c25c15")

## Generating keys

When creating keys, you set the attributes that the service uses to enforce compliant use of the key:

- Algorithm and key length
- Usage
- Availability and expiration

Tags that are used for attribute-based access control (ABAC) are used to limit keys for use with specific partners or applications should also be set during creation. Be sure to include policies to limit roles permitted to delete or change tags.

You should ensure that the policies that determine the roles that may use and manage the key are set prior to the creation of the key.

###### Note

IAM policies on the CreateKey commands may be used
to enforce and demonstrate dual control for key generation.

## Importing keys

When importing keys, the attributes to enforce compliant
use of the key are set by the service using the cryptographically bound information in the key block. The mechanism for setting fundamental
key context is to use key blocks created with the source HSM and
protected by a shared or asymmetric [KEK](terminology.md#terms.kek "terminology.md#terms.kek"). This aligns with
PCI PIN requirements and preserves usage, algorithm, and key strength from the source application.

Important key attributes, tags, and access control policies must be
established on import in addition to the information in the key block.

Importing keys using cryptograms does not transfer key attributes from the source
application. You must set the attributes appropriately by using this mechanism.

Often keys are exchanged using clear text components,
transmitted by key custodians, then loaded with
ceremony implementing dual control in a secure room.
This is not directly supported by AWS Payment Cryptography. The API will export a public key with a
certificate that can be imported by your own HSM to export a
key block that is importable by the service.
The enables use of your own HSM for loading clear text components.

You should use Key check values (KCV) to verify that imported keys match source keys.

IAM policies on the ImportKey API may be used to enforce and
demonstrate dual control for key import.

## Exporting keys

Sharing keys with partners or on-premises applications
may require exporting keys. Using key blocks for
exports maintains fundamental key context with the encrypted key material.

Key tags can be used to limit the export of keys to KEK that
share the same tag and value.

AWS Payment Cryptography does not provide or display clear text key components.
This requires direct access by key custodians to
PCI PTS HSM or ISO 13491 tested secure cryptographic devices (SCD)
for display or printing.
You can establish an asymmetric KEK or a symmetric KEK
with your SCD to conduct the clear text key component
creation ceremony under dual control.

Key check values (KCV) should be used to verify that imported by the destination HSM match source keys.

## Deleting keys

You can use the delete key API to schedule keys for deletion after a
period of time that you configure. Before that time keys are recoverable.
Once keys are deleted they are permanently removed from the service.

IAM policies on the DeleteKey API may be used to enforce
and demonstrate dual control for key deletion.

## Rotating keys

The effect of key rotation can be implemented using key alias by creating or importing a new key, then modifying the key alias to refer to the new key.
The old key would be deleted or disabled, depending on your management practices.
