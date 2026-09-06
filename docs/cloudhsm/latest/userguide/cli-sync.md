

# Synchronizing keys across cloned AWS CloudHSM clusters
<a name="cli-sync"></a>

Client-side and server-side synchronization are only for synchronizing keys within the *same* AWS CloudHSM cluster. If you copy a backup of a cluster to another region, use the [key replicate](cloudhsm_cli-key-replicate.md) command to replicate a key between two clusters. You might use cloned clusters for cross-region redundancy or to simplify your disaster recovery process. If you haven't installed CloudHSM CLI, see the instructions in [Getting started with AWS CloudHSM Command Line Interface (CLI)](cloudhsm_cli-getting-started.md).