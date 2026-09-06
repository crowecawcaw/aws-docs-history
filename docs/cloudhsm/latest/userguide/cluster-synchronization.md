

# AWS CloudHSM cluster synchronization
<a name="cluster-synchronization"></a>

In an AWS CloudHSM cluster, AWS CloudHSM keeps the keys on the individual HSMs in sync. You don't need to do anything to synchronize the keys on your HSMs. Unlike keys, there is no server-side mechanism to synchronize HSM users across the cluster. The AWS CloudHSM CLI performs best-effort synchronization of user operations across HSMs, but inconsistencies can occur if an operation partially fails. If users become out of sync, the `user list` command will show inconsistencies. For more information, see [Client SDK 5 user or policy contains inconsistent values](troubleshoot-sdk5-inconsistent-value.md).

When you add a new HSM to a cluster, AWS CloudHSM makes a backup of all keys, users, and policies on an existing HSM. It then restores that backup onto the new HSM. This keeps the two HSMs in sync.

If the keys on HSMs in a cluster fall out of synchronization, AWS CloudHSM automatically resynchronizes them. To enable this, AWS CloudHSM uses the credentials of the [appliance user](understanding-users.md). This user exists on all HSMs provided by AWS CloudHSM and has limited permissions. It can get a hash of objects on the HSM and can extract and insert masked (encrypted) objects. AWS cannot view or modify your users or keys and cannot perform any cryptographic operations using those keys.

This automatic resynchronization applies only to keys. Users and policies (such as mTLS settings) are not automatically resynchronized. The CloudHSM CLI performs best-effort synchronization of user and policy operations across HSMs, but inconsistencies can still occur and you may need to resolve them manually. For more information, see [Client SDK 5 user or policy contains inconsistent values](troubleshoot-sdk5-inconsistent-value.md).