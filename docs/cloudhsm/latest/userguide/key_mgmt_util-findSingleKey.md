# Verify an AWS CloudHSM key using KMU

Use the **findSingleKey** command in the AWS CloudHSM key_mgmt_util tool to verify that a
key exists on all hardware security modules (HSM) in the AWS CloudHSM cluster.

Before you run any key_mgmt_util command, you must [start
key_mgmt_util](key_mgmt_util-setup.md#key_mgmt_util-start "key_mgmt_util-setup.md#key_mgmt_util-start") and [log in](key_mgmt_util-log-in.md "key_mgmt_util-log-in.md") to the HSM as a crypto user
(CU).

## Syntax

```
findSingleKey -h

findSingleKey -k `<key-handle>`
```

## Example

This command verifies that key `252136` exists on all three HSMs in the
cluster.

```
Command: findSingleKey -k 252136
Cfm3FindKey returned: 0x00 : HSM Return: SUCCESS

        Cluster Error Status
        Node id 2 and err state 0x00000000 : HSM Return: SUCCESS
        Node id 1 and err state 0x00000000 : HSM Return: SUCCESS
        Node id 0 and err state 0x00000000 : HSM Return: SUCCESS
```

## Parameters

**-h**

Displays help for the command.

Required: Yes

**-k**

Specifies the key handle of one key in the HSM. This parameter is required.

To find key handles, use the [findKey](key_mgmt_util-listUsers.md "key_mgmt_util-listUsers.md")
command.

Required: Yes

## Related topics

- [findKey](key_mgmt_util-listUsers.md "key_mgmt_util-listUsers.md")
- [getKeyInfo](key_mgmt_util-listUsers.md "key_mgmt_util-listUsers.md")
- [getAttribute](key_mgmt_util-findKey.md "key_mgmt_util-findKey.md")
