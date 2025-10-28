# Synchronizing keys across cloned AWS CloudHSM clusters

Client-side and server-side synchronization are only for synchronizing keys within the
_same_ AWS CloudHSM cluster. If you copy a backup of a
cluster to another region, you can use the syncKey command of the cloudhsm_mgmt_util
(CMU) for synchronizing keys between clusters. You might use cloned clusters for
cross-region redundancy or to simplify your disaster recovery process. For more
information, see [syncKey](cloudhsm_mgmt_util-syncKey.md "cloudhsm_mgmt_util-syncKey.md").
