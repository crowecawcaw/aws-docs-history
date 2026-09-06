

# AWS CloudHSM audit log reference
<a name="cloudhsm-audit-log-reference"></a>

AWS CloudHSM records HSM management commands in audit log events. Each event has an operation code (`Opcode`) value that identifies the action that occurred and its response. You can use the `Opcode` values to search, sort, and filter the logs.

The following table defines the `Opcode` values in an AWS CloudHSM audit log.


| Operation Code (Opcode) | Description | 
| --- |--- |
| **User Login**: These events include the user name and user type | 
| --- |
| CN\_LOGIN (0xd) | [User login](cloudhsm_mgmt_util-loginLogout.md) | 
| CN\_LOGOUT (0xe) | [User logout](cloudhsm_mgmt_util-loginLogout.md) | 
| CN\_APP\_FINALIZE | The connection with the HSM was closed. Any session keys or quorum tokens from this connection were deleted. | 
| CN\_CLOSE\_SESSION | The session with the HSM was closed. Any session keys or quorum tokens from this session were deleted. | 
| **User Management**: These events include the user name and user type | 
| --- |
| CN\_CREATE\_USER (0x3) | [Create a crypto user (CU)](cloudhsm_mgmt_util-createUser.md) | 
| CN\_CREATE\_CO | [Create a crypto officer (CO)](cloudhsm_mgmt_util-createUser.md) | 
| CN\_DELETE\_USER | [Delete a user](cloudhsm_mgmt_util-deleteUser.md) | 
| CN\_CHANGE\_PSWD | [Change a user password](cloudhsm_mgmt_util-changePswd.md) | 
| CN\_SET\_M\_VALUE | Set [quorum authentication](quorum-auth-chsm-cli.md) (M of N) for a user action | 
| CN\_APPROVE\_TOKEN | Approve a [quorum authentication](quorum-auth-chsm-cli.md) token for a user action | 
| CN\_DELETE\_TOKEN | Delete one or more [quorum tokens](quorum-auth-chsm-cli.md) | 
| CN\_GET\_TOKEN | Request a signing token to initiate a [quorum operation](quorum-auth-chsm-cli.md) | 
| **Key Management**: These events include the key handle | 
| --- |
| CN\_GENERATE\_KEY | [Generate a symmetric key](key_mgmt_util-genSymKey.md) | 
| CN\_GENERATE\_KEY\_PAIR (0x19) | Generate an asymmetric key pair | 
| CN\_CREATE\_OBJECT | Import a public key (without wrapping) | 
| CN\_MODIFY\_OBJECT | Set a key attribute | 
| CN\_DESTROY\_OBJECT (0x11) | Deletion of a [session key](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-key-sync.html#concepts-key-sync) | 
| CN\_TOMBSTONE\_OBJECT | Deletion of a [token key](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-key-sync.html#concepts-key-sync) | 
| CN\_SHARE\_OBJECT | [Share or unshare a key](cloudhsm_mgmt_util-shareKey.md) | 
| CN\_WRAP\_KEY | Export an encrypted copy of a key ([wrapKey](key_mgmt_util-wrapKey.md)) | 
| CN\_UNWRAP\_KEY | Import an encrypted copy of a key ([unwrapKey](key_mgmt_util-unwrapKey.md)) | 
| CN\_DERIVE\_KEY | Derive a symmetric key from an existing key | 
| CN\_NIST\_AES\_WRAP | Encrypt or decrypt a key with an AES key | 
| CN\_INSERT\_MASKED\_OBJECT\_USER | Insert an encrypted key with attributes from another HSM in the cluster. | 
| CN\_EXTRACT\_MASKED\_OBJECT\_USER | Wraps/encrypts a key with attributes from the HSM to be sent to another HSM in the cluster. | 
| **Session Management** | 
| --- |
| CN\_ENCRYPT\_SESSION\_V2 (0x107) | Establishes an authenticated end-to-end encrypted session. | 
| END\_MARKER\_OPCODE (0xffff) | Inserts an end-marker in the audit logs buffer indicating no more loggable commands are allowed on the HSM | 
| **Back up HSMs** | 
| --- |
| CN\_BACKUP\_BEGIN | Begin the backup process | 
| CN\_BACKUP\_END | Completed the backup process | 
| CN\_RESTORE\_BEGIN | Begin restoring from a backup | 
| CN\_RESTORE\_END | Completed the restoration process from a backup | 
| **Certificate-Based Authentication** | 
| --- |
| CN\_CERT\_AUTH\_STORE\_CERT | Stores the cluster certificate | 
| **HSM Instance Commands** | 
| --- |
| CN\_INIT\_TOKEN (0x1) | Start the HSM initialization process | 
| CN\_INIT\_DONE | The HSM initialization process has finished | 
| CN\_GEN\_KEY\_ENC\_KEY | Generate a key encryption key (KEK) | 
| CN\_GEN\_PSWD\_ENC\_KEY (0x1d) | Generate a password encryption key (PEK) | 
| **HSM crypto commands** | 
| --- |
| CN\_FIPS\_RAND | Generate a FIPS-compliant random number[1](#hsm-audit-log-note-1) | 

[1] Only gets logged for hsm1.medium clusters.