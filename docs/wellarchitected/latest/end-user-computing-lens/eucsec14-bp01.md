# EUCSEC14-BP01 Encrypt disk volumes to protect data at rest

Protect security, integrity, and availability of data at rest to
make sure it is reliably accessible when needed.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Encrypt Amazon WorkSpaces Personal disk volumes. Each Amazon
WorkSpace Personal instance is provisioned with a root volume
(C: drive for Windows WorkSpaces Personal, root file system
for Amazon Linux WorkSpaces Personal) and a user volume (D:
drive for Windows WorkSpaces Personal, /home for Amazon Linux
WorkSpaces Personal). The encrypted WorkSpaces feature
encrypts one or both volumes. For WorkSpaces Personal
instances used by users (rather than for creating custom
images), it is a best practice for these to be encrypted. For
more details, see
[Encrypted
WorkSpaces in WorkSpaces Personal](../../../workspaces/latest/adminguide/encrypt-workspaces.md "../../../workspaces/latest/adminguide/encrypt-workspaces.md").
