# AWS CloudHSM audit log reference

AWS CloudHSM records HSM management commands in audit log events. Each event has an operation
code (`Opcode`) value that identifies the action that occurred and its response.
You can use the `Opcode` values to search, sort, and filter the logs.

The following table defines the `Opcode` values in an AWS CloudHSM audit log.

| Operation Code (Opcode)                                                     | Description                                                                                                  |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **User Login**: These events include the user name and user type            |
| `CN_LOGIN (0xd)`                                                            | [User login](cloudhsm_mgmt_util-loginLogout.md "cloudhsm_mgmt_util-loginLogout.md")                          |
| `CN_LOGOUT (0xe)`                                                           | [User logout](cloudhsm_mgmt_util-loginLogout.md "cloudhsm_mgmt_util-loginLogout.md")                         |
| `CN_APP_FINALIZE`                                                           | The connection with the HSM was closed. Any session keys or quorum tokens from this connection were deleted. |
| `CN_CLOSE_SESSION`                                                          | The session with the HSM was closed. Any session keys or quorum tokens from this session were deleted.       |
| **User<br>Management**: These events include the user name and user<br>type |
| `CN_CREATE_USER (0x3)`                                                      | [Create a crypto user (CU)](cloudhsm_mgmt_util-createUser.md "cloudhsm_mgmt_util-createUser.md")             |
| `CN_CREATE_CO`                                                              | [Create a crypto officer<br>(CO)](cloudhsm_mgmt_util-createUser.md "cloudhsm_mgmt_util-createUser.md")       |
| `CN_DELETE_USER`                                                            | [Delete a<br>user](cloudhsm_mgmt_util-deleteUser.md "cloudhsm_mgmt_util-deleteUser.md")                      |
| `CN_CHANGE_PSWD`                                                            | [Change a user<br>password](cloudhsm_mgmt_util-changePswd.md "cloudhsm_mgmt_util-changePswd.md")             |
| `CN_SET_M_VALUE`                                                            | Set [quorum authentication](quorum-auth-chsm-cli.md "quorum-auth-chsm-cli.md") (M of N) for a user action    |
| `CN_APPROVE_TOKEN`                                                          | Approve a [quorum authentication](quorum-auth-chsm-cli.md "quorum-auth-chsm-cli.md") token for a user action |
| `CN_DELETE_TOKEN`                                                           | Delete one or more [quorum tokens](quorum-auth-chsm-cli.md "quorum-auth-chsm-cli.md")                        |
| `CN_GET_TOKEN`                                                              | Request a signing token to initiate a [quorum operation](quorum-auth-chsm-cli.md "quorum-auth-chsm-cli.md")  |
| **Key<br>Management**: These events include the key handle                  |
| `CN_GENERATE_KEY`                                                           | [Generate a symmetric key](key_mgmt_util-genSymKey.md "key_mgmt_util-genSymKey.md")                          |
| `CN_GENERATE_KEY_PAIR (0x19)`                                               | Generate an asymmetric key pair                                                                              |
| `CN_CREATE_OBJECT`                                                          | Import a public key (without wrapping)                                                                       |
| `CN_MODIFY_OBJECT`                                                          | Set a key attribute                                                                                          |
| `CN_DESTROY_OBJECT (0x11)`                                                  | Deletion of a [session key](manage-key-sync.md#concepts-key-sync "manage-key-sync.md#concepts-key-sync")     |
| `CN_TOMBSTONE_OBJECT`                                                       | Deletion of a [token key](manage-key-sync.md#concepts-key-sync "manage-key-sync.md#concepts-key-sync")       |
| `CN_SHARE_OBJECT`                                                           | [Share or unshare a<br>key](cloudhsm_mgmt_util-shareKey.md "cloudhsm_mgmt_util-shareKey.md")                 |
| `CN_WRAP_KEY`                                                               | Export an encrypted copy of a key ([wrapKey](key_mgmt_util-wrapKey.md "key_mgmt_util-wrapKey.md"))           |
| `CN_UNWRAP_KEY`                                                             | Import an encrypted copy of a key ([unwrapKey](key_mgmt_util-unwrapKey.md "key_mgmt_util-unwrapKey.md"))     |
| `CN_DERIVE_KEY`                                                             | Derive a symmetric key from an existing key                                                                  |
| `CN_NIST_AES_WRAP`                                                          | Encrypt or decrypt a key with an AES key                                                                     |
| `CN_INSERT_MASKED_OBJECT_USER`                                              | Insert an encrypted key with attributes from another HSM in the cluster.                                     |
| `CN_EXTRACT_MASKED_OBJECT_USER`                                             | Wraps/encrypts a key with attributes from the HSM to be sent to another HSM in the cluster.                  |
| **Back up HSMs**                                                            |
| `CN_BACKUP_BEGIN`                                                           | Begin the backup process                                                                                     |
| `CN_BACKUP_END`                                                             | Completed the backup process                                                                                 |
| `CN_RESTORE_BEGIN`                                                          | Begin restoring from a backup                                                                                |
| `CN_RESTORE_END`                                                            | Completed the restoration process from a backup                                                              |
| **Certificate-Based Authentication**                                        |
| `CN_CERT_AUTH_STORE_CERT`                                                   | Stores the cluster certificate                                                                               |
| **HSM Instance<br>Commands**                                                |
| `CN_INIT_TOKEN (0x1)`                                                       | Start the HSM initialization process                                                                         |
| `CN_INIT_DONE`                                                              | The HSM initialization process has finished                                                                  |
| `CN_GEN_KEY_ENC_KEY`                                                        | Generate a key encryption key (KEK)                                                                          |
| `CN_GEN_PSWD_ENC_KEY (0x1d)`                                                | Generate a password encryption key (PEK)                                                                     |
| **HSM crypto commands**                                                     |
| `CN_FIPS_RAND`                                                              | Generate a FIPS-compliant random number[1](#hsm-audit-log-note-1 "#hsm-audit-log-note-1")                    |

[1] Only gets logged for hsm1.medium clusters.
