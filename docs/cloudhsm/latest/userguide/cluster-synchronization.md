# AWS CloudHSM cluster synchronization

In an AWS CloudHSM cluster, AWS CloudHSM keeps the keys on the individual HSMs in sync. You don't need
to do anything to synchronize the keys on your HSMs. To keep the users and policies on each
HSM in sync, update the AWS CloudHSM client configuration file before you [manage HSM users](manage-hsm-users.md "manage-hsm-users.md"). For more information, see [Keep HSM users in
sync](troubleshooting-keep-hsm-users-in-sync.md "troubleshooting-keep-hsm-users-in-sync.md").

When you add a new HSM to a cluster, AWS CloudHSM makes a backup of all keys, users, and policies
on an existing HSM. It then restores that backup onto the new HSM. This keeps the two HSMs in
sync.

If the HSMs in a cluster fall out of synchronization, AWS CloudHSM automatically resynchronizes
them. To enable this, AWS CloudHSM uses the credentials of the [appliance
user](understanding-users.md "understanding-users.md"). This user exists on all HSMs provided by AWS CloudHSM and has limited permissions. It
can get a hash of objects on the HSM and can extract and insert masked (encrypted) objects.
AWS cannot view or modify your users or keys and cannot perform any cryptographic operations
using those keys.
