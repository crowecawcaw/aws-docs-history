# Amazon EBS snapshot lock

You can lock your Amazon EBS snapshots to protect them against accidental or malicious deletions,
or to store them in WORM (write-once-read-many) format for a specific duration. While a
snapshot is locked, it can't be deleted by any user, regardless of their IAM permissions. You
can continue to use a locked snapshot in the same way that you would use any other snapshot.

###### Note

Snapshot lock has been assessed by Cohasset Associates for use in environments that are
subject to SEC 17a-4, CFTC, and FINRA regulations. For more information about how snapshot lock
relates to these regulations, see the [Cohasset Associates Compliance Assessment](https://d1.awsstatic.com/Amazon-EBS-Cohasset-Assessment-2023-11-14-final.pdf "https://d1.awsstatic.com/Amazon-EBS-Cohasset-Assessment-2023-11-14-final.pdf").

You can lock snapshots in one of two modes: _compliance mode_ or
_governance mode_, and they can be locked for a specific duration or until a
specific date. For more information, see [Lock mode](snapshot-lock-concepts.md#lock-mode "snapshot-lock-concepts.md#lock-mode")
and [Lock duration](snapshot-lock-concepts.md#lock-duration "snapshot-lock-concepts.md#lock-duration").

###### Pricing

You can lock and unlock snapshots at no additional cost. You pay the standard Amazon EBS snapshot
storage costs for locked snapshots.

###### Topics

- [Concepts](snapshot-lock-concepts.md "snapshot-lock-concepts.md")
- [Considerations](snapshot-lock-considerations.md "snapshot-lock-considerations.md")
- [Control access](snapshot-lock-iam.md "snapshot-lock-iam.md")
- [Lock a snapshot](lock-snapshot.md "lock-snapshot.md")
- [Unlock a snapshot](unlock-snapshot.md "unlock-snapshot.md")
- [Update snapshot lock settings](update-snapshot-lock.md "update-snapshot-lock.md")
- [Monitor snapshot lock](monitor-snapshot-lock.md "monitor-snapshot-lock.md")
