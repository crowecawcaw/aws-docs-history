# Share and unshare keys with KMU and CMU

In AWS CloudHSM, the CU who creates the key owns it. The owner manages the key, can export and
delete it, and can use the key in cryptographic operations. The owner can also share the key
with other CU users. Users with whom the key is shared can use the key in cryptographic
operations, but they cannot export or delete the key, or share it with other users.

You can share keys with other CU users when you create the key, such as by using the
`-u` parameter of the [genSymKey](key_mgmt_util-genSymKey.md "key_mgmt_util-genSymKey.md") or
[genRSAKeyPair](key_mgmt_util-genRSAKeyPair.md "key_mgmt_util-genRSAKeyPair.md") commands. To share existing
keys with a different HSM user, use the [cloudhsm_mgmt_util](cloudhsm_mgmt_util.md "cloudhsm_mgmt_util.md") command line tool. This is different from most of the tasks
documented in this section, which use the [key_mgmt_util](key_mgmt_util.md "key_mgmt_util.md")
command line tool.

Before you can share a key, you must start cloudhsm_mgmt_util, enable end-to-end
encryption, and log in to the HSMs. To share a key, log in to the HSM as the crypto user (CU)
that owns the key. Only key owners can share a key.

Use the **shareKey** command to share or unshare a key, specifying the
handle of the key and the IDs of the user or users. To share or unshare with more than one
user, specify a comma-separated list of user IDs. To share a key, use `1` as the
command's last parameter, as in the following example. To unshare, use `0`.

```
`aws-cloudhsm >` `shareKey 524295 4 1``*************************CAUTION********************************
This is a CRITICAL operation, should be done on all nodes in the
cluster. AWS does NOT synchronize these changes automatically with the
nodes on which this operation is not executed or failed, please
ensure this operation is executed on all nodes in the cluster.
****************************************************************

Do you want to continue(y/n)? `y`
shareKey success on server 0(10.0.2.9)
shareKey success on server 1(10.0.3.11)
shareKey success on server 2(10.0.1.12)`
```

The following shows the syntax for the **shareKey** command.

```
`aws-cloudhsm >` `shareKey `<key handle>` `<user ID>` `<Boolean: 1 for share, 0 for unshare>``
```
