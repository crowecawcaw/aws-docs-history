# Quorum authentication process for AWS CloudHSM Management Utility

The following steps summarize the quorum authentication processes. For the specific steps
 and tools, see [User management with quorum
 authentication enabled for AWS CloudHSM Management Utility](quorum-authentication-crypto-officers.md "quorum-authentication-crypto-officers.md").


1. Each HSM user creates an asymmetric key for signing. They do this outside of
 the HSM, taking care to protect the key appropriately.
2. Each HSM user logs in to the HSM and registers the public part of their signing
 key (the public key) with the HSM.
3. When an HSM user wants to do a quorum-controlled operation, each user logs in to the
 HSM and gets a *quorum token*.
4. The HSM user gives the quorum token to one or more other HSM users and asks for their
 approval.
5. The other HSM users approve by using their keys to cryptographically sign the quorum
 token. This occurs outside the HSM.
6. When the HSM user has the required number of approvals, the same user logs in to the HSM
 and gives the quorum token and approvals (signatures) to the HSM.
7. The HSM uses the registered public keys of each signer to verify the signatures. If
 the signatures are valid, the HSM approves the token.
8. The HSM user can now do a quorum-controlled operation.
