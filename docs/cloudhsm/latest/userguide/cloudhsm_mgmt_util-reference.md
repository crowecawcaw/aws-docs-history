# Reference for AWS CloudHSM Management Utility

commands

The AWS CloudHSM cloudhsm_mgmt_util command line tool helps crypto officers manage users in the hardware
security modules (HSMs) in the AWS CloudHSM cluster. It also includes commands that allow crypto users
(CUs) to share keys, and get and set key attributes. These commands complement the primary key
management commands in the [key_mgmt_util](key_mgmt_util.md "key_mgmt_util.md") command line tool.

For a quick start, see [Cloned clusters in AWS CloudHSM](cloudhsm_mgmt_util-getting-started.md "cloudhsm_mgmt_util-getting-started.md").

Before you run any cloudhsm_mgmt_util command, you must start cloudhsm_mgmt_util and log in to the HSM. Be sure that
you log in with the user account type that can run the commands you plan to use.

To list all cloudhsm_mgmt_util commands, run the following command:

```
`aws-cloudhsm>` `help`
```

To get the syntax for a cloudhsm_mgmt_util command, run the following command:

```
`aws-cloudhsm>` `help `<command-name>``
```

###### Note

Use the syntax as per the documentation. While the built-in software help may provide additional options, these should not be considered supported and should not be utilized in production code.

To run a command, enter the command name, or enough of the name to distinguish it from the
names of other cloudhsm_mgmt_util commands.

For example, to get a list of users on the HSMs, enter **listUsers** or
**listU**.

```
`aws-cloudhsm>` `listUsers`
```

To end your cloudhsm_mgmt_util session, run the following command:

```
`aws-cloudhsm>` `quit`
```

For help interpreting the key attributes, see the [AWS CloudHSM key attribute reference for KMU](key-attribute-table.md "key-attribute-table.md").

The following topics describe commands in cloudhsm_mgmt_util.

###### Note

Some commands in key_mgmt_util and cloudhsm_mgmt_util have the same names. However, the commands typically have
different syntax, different output, and slightly different functionality.

| Command                                                                                                         | Description                                                                                                                | User Type                   |
| --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| [changePswd](cloudhsm_mgmt_util-changePswd.md "cloudhsm_mgmt_util-changePswd.md")                               | Changes the passwords of users on the HSMs. Any user can change their own password. COs can change anyone's password.      | CO                          |
| [createUser](cloudhsm_mgmt_util-createUser.md "cloudhsm_mgmt_util-createUser.md")                               | Creates users of all types on the HSMs.                                                                                    | CO                          |
| [deleteUser](cloudhsm_mgmt_util-deleteUser.md "cloudhsm_mgmt_util-deleteUser.md")                               | Deletes users of all types from the HSMs.                                                                                  | CO                          |
| [findAllKeys](cloudhsm_mgmt_util-findAllKeys.md "cloudhsm_mgmt_util-findAllKeys.md")                            | Gets the keys that a user owns or shares. Also gets a hash of the key ownership and sharing data for all keys on each HSM. | CO, AU                      |
| [getAttribute](cloudhsm_mgmt_util-getAttribute.md "cloudhsm_mgmt_util-getAttribute.md")                         | Gets an attribute value for an AWS CloudHSM key and writes it to a file or stdout (standard output).                       | CU                          |
| [getHSMInfo](cloudhsm_mgmt_util-getHSMInfo.md "cloudhsm_mgmt_util-getHSMInfo.md")                               | Gets information about the hardware on which an HSM is running.                                                            | All. Login is not required. |
| [getKeyInfo](cloudhsm_mgmt_util-getKeyInfo.md "cloudhsm_mgmt_util-getKeyInfo.md")                               | Gets owners, shared users, and the quorum authentication status of a key.                                                  | All. Login is not required. |
| [info](cloudhsm_mgmt_util-info.md "cloudhsm_mgmt_util-info.md")                                                 | Gets information about an HSM, including the IP address, hostname, port, and current user.                                 | All. Login is not required. |
| [listUsers](cloudhsm_mgmt_util-listUsers.md "cloudhsm_mgmt_util-listUsers.md")                                  | Gets the users in each of the HSMs, their user type and ID, and other attributes.                                          | All. Login is not required. |
| [loginHSM and logoutHSM](cloudhsm_mgmt_util-loginLogout.md "cloudhsm_mgmt_util-loginLogout.md")                 | Log in and log out of an HSM.                                                                                              | All.                        |
| [quit](cloudhsm_mgmt_util-quit.md "cloudhsm_mgmt_util-quit.md")                                                 | Quits cloudhsm_mgmt_util.                                                                                                  | All. Login is not required. |
| [server](cloudhsm_mgmt_util-server.md "cloudhsm_mgmt_util-server.md")                                           | Enters and exits server mode on an HSM.                                                                                    | All.                        |
| [registerQuorumPubKey](cloudhsm_mgmt_util-registerQuorumPubKey.md "cloudhsm_mgmt_util-registerQuorumPubKey.md") | Associates an HSM user with an asymmetric RSA-2048 key pair.                                                               | CO                          |
| [setAttribute](cloudhsm_mgmt_util-setAttribute.md "cloudhsm_mgmt_util-setAttribute.md")                         | Changes the values of the label, encrypt, decrypt, wrap, and unwrap attributes of an existing key.                         | CU                          |
| [shareKey](cloudhsm_mgmt_util-shareKey.md "cloudhsm_mgmt_util-shareKey.md")                                     | Shares an existing key with other users.                                                                                   | CU                          |
| [syncKey](cloudhsm_mgmt_util-syncKey.md "cloudhsm_mgmt_util-syncKey.md")                                        | Syncs a key across cloned AWS CloudHSM clusters.                                                                           | CU, CO                      |
| [syncUser](cloudhsm_mgmt_util-syncUser.md "cloudhsm_mgmt_util-syncUser.md")                                     | Syncs a user across cloned AWS CloudHSM clusters.                                                                          | CO                          |
