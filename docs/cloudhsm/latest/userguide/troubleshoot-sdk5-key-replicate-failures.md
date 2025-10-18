# AWS CloudHSM Client SDK 5 key replicate
 failures

The `key replicate` command in the CloudHSM CLI replicates a key from a source AWS CloudHSM cluster to a destination AWS CloudHSM cluster. This guide addresses failures caused by inconsistencies within the source cluster or between the source and destination clusters.
 


## Problem: The selected key is not synchronized throughout the cluster


The key replication process checks for key synchronization throughout the source cluster. 
 If any key information or attributes have the value "inconsistent", this means the key isn't synchronized across the cluster. 
 Key replication fails with the following error message:
 



```
{
  "error_code": 1,
  "data": "The selected key is not synchronized throughout the cluster"
}
```

To check for key desynchronization in the source cluster:


1. Run the `key list` command in the CloudHSM CLI.
2. Use the `--filter` flag to specify the key.
3. Add the `--verbose` flag to see the full output with key coverage information.


```
`aws-cloudhsm >` `key list --filter attr.label=`example-desynchronized-key-label` --verbose``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x000000000048000f",
 "key-info": {
 "key-owners": [
 {
 "username": "cu1",
 "key-coverage": "full"
 }
 ],
 "shared-users": [],
 "key-quorum-values": {
 "manage-key-quorum-value": 0,
 "use-key-quorum-value": 0
 },
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "aes",
 "label": "example-desynchronized-key-label",
 "id": "0x",
 "check-value": "0xbe79db",
 "class": "secret-key",
 "encrypt": false,
 "decrypt": false,
 "token": true,
 "always-sensitive": true,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": true,
 "sign": "inconsistent",
 "trusted": false,
 "unwrap": false,
 "verify": true,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 16
 }
 }
 ],
 "total_key_count": 1,
 "returned_key_count": 1
 }
}`
      
```

###### Resolution: Synchronize key information and attributes throughout the source cluster

To synchronize key information and attributes throughout the source cluster:

1. For inconsistent key attributes: Use the `key set-attribute` command to set the desired attribute for the specific key.
2. For inconsistent shared user coverage: Use the `key share` or `key
 unshare` commands to adjust key sharing with the desired users.

## Problem: Key with same reference exists in destination cluster with different
 information or attributes


 If a key with the same reference exists in the destination cluster but has different
 information or attributes, the following error may occur: 



```
{
  "error_code": 1,
  "data": "Key replicate failed on 1 of 3 connections"
}
```

###### Resolution

1. Determine which version of the key should be kept.
2. Delete the unwanted key version using the `key delete` command in the appropriate cluster.
3. Replicate the key from the cluster that has the correct version.
