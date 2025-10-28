# Best Practice 2.6 – Make frequent,

small, and reversible changes

Frequent, small, and reversible changes reduce the scope and impact of a change.
Although many SAP NetWeaver solutions only support a “patch forward” approach, consider
using feature toggles in custom development to allow rollback. This eases troubleshooting,
enables faster remediation, and provides the option to roll back a change.

**Suggestion 2.6.1 - Divide development and releases into frequent and
smaller changes where possible**

**Suggestion 2.6.2 - Because many SAP solutions only support a “patch
forward” approach (and do not allow reversible transports), consider using feature toggles
in custom development to allow disablement of features rather than
rollback/withdraw**

**Suggestion 2.6.3 - For non-reversible SAP changes, consider
additional rollback options, such as whole system snapshots, database backup, and
restore options**

- AWS Blog: [Amazon EBS crash-consistent snapshots](https://aws.amazon.com/blogs/storage/taking-crash-consistent-snapshots-across-multiple-amazon-ebs-volumes-on-an-amazon-ec2-instance/ "https://aws.amazon.com/blogs/storage/taking-crash-consistent-snapshots-across-multiple-amazon-ebs-volumes-on-an-amazon-ec2-instance/")
- AWS Documentation: [Restoring to a specified time using Point-In-Time Recovery (PITR)](../../../aws-backup/latest/devguide/point-in-time-recovery.md "../../../aws-backup/latest/devguide/point-in-time-recovery.md")
- AWS Documentation: [AWS
  Backint for SAP HANA](https://aws.amazon.com/backint-agent/ "https://aws.amazon.com/backint-agent/")
