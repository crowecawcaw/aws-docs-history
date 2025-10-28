# Quorum authentication process for CloudHSM CLI

The following steps summarize the quorum authentication processes for CloudHSM CLI. For the
specific steps and tools, see [User management with quorum authentication enabled
for AWS CloudHSM using CloudHSM CLI](quorum-auth-chsm-cli-admin.md "quorum-auth-chsm-cli-admin.md").

1. Each hardware security module (HSM) user creates an asymmetric key for signing. Users do
   this outside of the HSM, taking care to protect the key appropriately.
2. Each HSM user logs in to the HSM and registers the public part of their signing
   key (the public key) with the HSM.
3. When an HSM user wants to do a quorum-controlled operation, the same user logs in to the
   HSM and gets a _quorum token_.
4. The HSM user gives the quorum token to one or more other HSM users and asks for their
   approval.
5. The other HSM users approve by using their keys to cryptographically sign the quorum
   token. This occurs outside the HSM.
6. When the HSM user has the required number of approvals, the same user logs in to the HSM
   and runs the quorum-controlled operation with the **--approval** argument, supplying
   the signed quorum token file, which contains all necessary approvals (signatures).
7. The HSM uses the registered public keys of each signer to verify the signatures. If
   the signatures are valid, the HSM approves the token and the quorum-controlled operation is performed.
