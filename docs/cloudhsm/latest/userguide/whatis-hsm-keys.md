# Keys in AWS CloudHSM

AWS CloudHSM allows you to securely generate, store, and manage your encryption keys in
single-tenant HSMs that are in your AWS CloudHSM cluster. Keys can be symmetric or asymmetric,
can be session keys (ephemeral keys) for single sessions, token keys (persistent keys) for
long-term use, and can be exported from and imported into AWS CloudHSM Keys can also be used to
complete common cryptographic tasks and functions:

- Perform cryptographic data signing and signature verification with both symmetric and
  asymmetric encryption algorithms.
- Work with hash functions to compute message digests and hash-based message
  authentication codes (HMACs).
- Wrap and protect other keys.
- Access cryptographically secure random data.
  The maximum keys a cluster can have depends on the type of HSMs that are in the cluster. For
  example, hsm2m.medium stores more keys than hsm1,medium. For a comparison, see [AWS CloudHSM quotas](limits.md "limits.md").

Additionally, AWS CloudHSM follows a few foundational principles for key usage and
management:

**Many key types and algorithms to choose from**

To allow you to customize your own solutions, AWS CloudHSM provides many key types and
algorithms to choose from algorithms support a range of key sizes. For more information,
refer to the attributes and mechanism pages of each [Offload operations with AWS CloudHSM Client SDKs](use-hsm.md "use-hsm.md").

**How you manage keys**

AWS CloudHSM keys are managed through SDKs and command line tools. For information on how to
use these tools to manage keys, see [Keys in AWS CloudHSM](manage-keys.md "manage-keys.md") and [Best practices for AWS CloudHSM](best-practices.md "best-practices.md").

**Who owns keys**

In AWS CloudHSM, the crypto user (CU) who creates the key owns it. The owner can use the
**key share** and **key unshare** commands to share and
unshare the key with other CUs. For more information, see [Share and unshare keys using CloudHSM CLI](manage-keys-cloudhsm-cli-share.md "manage-keys-cloudhsm-cli-share.md").

**Access and usage can be controlled with attribute-based
encryption**

AWS CloudHSM allows you to use attribute-based encryption, a form of encryption that lets you
use key attributes to control who can decrypt data based on policies.
