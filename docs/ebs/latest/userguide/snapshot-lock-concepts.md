# Amazon EBS snapshot lock concepts

The following are important concepts to understand as you get started using snapshot lock.

###### Contents

- [Lock mode](snapshot-lock-concepts.md#lock-mode "snapshot-lock-concepts.md#lock-mode")
- [Lock duration](snapshot-lock-concepts.md#lock-duration "snapshot-lock-concepts.md#lock-duration")
- [Cooling-off period](snapshot-lock-concepts.md#cool-off "snapshot-lock-concepts.md#cool-off")
- [Lock state](snapshot-lock-concepts.md#lock-state "snapshot-lock-concepts.md#lock-state")

## Lock mode

You can lock a snapshot in one of two modes:

###### Governance mode

After a snapshot is locked, users with appropriate IAM permissions can unlock the snapshot
and modify the lock mode and lock duration or expiry date at any time. When you lock a snapshot
in governance mode, the snapshot is locked immediately; there is no cooling-off period. To delete
a snapshot after it has been locked in governance mode, you must first unlock the snapshot or
you must wait for the lock to expire.

You can use governance mode to meet your organization's data governance requirements by
ensuring that only certain users have permission to unlock snapshots and modify snapshot lock
configurations. You can also use governance mode to test your lock configuration before locking
a snapshot in compliance mode.

###### Compliance mode

When you lock a snapshot in compliance mode, you can optionally specify a cooling-off period
that starts immediately after you lock the snapshot. During the cooling-off period, users with
appropriate permissions can unlock the snapshot, change the lock mode, increase or decrease the
cooling-off period, and increase or decrease the lock duration or expiry date. After the cooling-off
period expires, you can't unlock the snapshot, change the lock mode, or decrease the lock duration
or expire date; you can only increase the lock duration or expiry date. To delete a snapshot after
it has been locked in compliance and the cooling-off period has expired, you must wait for the lock
to expire.

###### Note

You can lock a snapshot in compliance mode without a cooling-off period by omitting the
cooling-off period in the request. If you do this, the lock becomes effective immediately, and you
can't unlock the snapshot, change the lock mode, or decrease the lock duration or expire date; you
can only increase the lock duration or expiry date.

You can use compliance mode to protect snapshots that should not be deleted for a specific
period for compliance reasons. Compliance mode offers the following benefits:

- It enables WORM (write-once, read-many) configuration for your snapshots.
- It provides an additional layer of defense that protects snapshots from accidental or
  malicious deletions.
- It enforces retention periods, which prevent early deletions by privileged users, to meet
  your organization's data protection policies and procedures.

###### Note

The only way to delete a snapshot that is locked in compliance mode before its lock expires is
to close the associated AWS account.

## Lock duration

The lock duration is the period of time for which the snapshot is to remain locked. You can
specify the lock duration as one of the following, but not both:

###### Number of days

The lock duration is specified as a number of days for which the snapshot is to remain
locked. After the specified number of days has passed, the snapshot is automatically unlocked.
The duration can range from 1 day to 36500 days (100 years).

###### Lock expiration date

The lock duration is determined by an expiration date in the future. The snapshot remains
locked until the lock expiration date is reached. When the lock expiration date is reached,
the snapshot is automatically unlocked.

## Cooling-off period

The cooling-off period is an optional period of time that you can specify when you lock a
snapshot in compliance mode. During the cooling-off period, users with appropriate permissions
can unlock the snapshot, change the lock mode, increase or decrease the cooling-off period,
and increase or decrease the lock duration. After the cooling-off period expires, users can't
unlock the snapshot, change the lock mode, reinstate the cooling-off period, or decrease the
lock duration, regardless of their permissions.

A snapshot can't be deleted during the cooling-off period.

If specified, the cooling-off period starts immediately after you lock the snapshot. If
omitted, the snapshot is locked in compliance mode immediately without a cooling-off period.

The cooling-off period can range from 1 to 72 hours. To lock a snapshot in compliance mode
immediately without a cooling-off period, do not specify a cooling-off period in the request.

## Lock state

A snapshot lock can be in one of the following states:

- `compliance-cooloff` — The snapshot has been locked in
  compliance mode but it is still within the cooling-off period. The snapshot can't be
  deleted, but it can be unlocked and the lock settings can be modified by users with
  appropriate permissions.
- `governance` — The snapshot is locked in governance mode. The
  snapshot can't be deleted, but it can be unlocked and the lock settings can be
  modified by users with appropriate permissions.
- `compliance` — The snapshot is locked in compliance mode without
  a cooling-off period or the cooling-off period has expired. The snapshot can't be
  unlocked or deleted. The lock duration can only be increased by users with appropriate
  permissions.
- `expired` — The snapshot was locked in compliance or governance
  mode but the lock has expired. The snapshot is not locked and can be deleted.
