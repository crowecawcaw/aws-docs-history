# EUCSEC14-BP02 Encrypt data in transit in your EUC environment

Use encryption to protect data confidentiality while in transit
inside your EUC environment.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Use AWS EUC streaming protocols to encrypt streaming data in
transit. Amazon WorkSpaces and Amazon WorkSpaces Applications provide
data encryption of pixel streaming traffic between instances
and end user devices by default. Evaluate the default levels
of encryption to verify that they provide sufficient
protection in terms of key length and cipher suites and
satisfy the requirements of the organization. For further
details regarding the encryption used for Amazon AppStream,
see
[Data
Protection in Amazon WorkSpaces Applications](../../../appstream2/latest/developerguide/data-protection.md "../../../appstream2/latest/developerguide/data-protection.md") , and for Amazon WorkSpaces, see

[Data
Protection in Amazon WorkSpaces.](../../../workspaces/latest/adminguide/data-protection.md "../../../workspaces/latest/adminguide/data-protection.md")
