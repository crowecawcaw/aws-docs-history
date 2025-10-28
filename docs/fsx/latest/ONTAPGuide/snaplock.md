# Protecting your data with SnapLock

SnapLock is a feature that allows you to protect your files by transitioning them to a
write once, read many (WORM) state, which prevents modification or deletion for a specified
retention period. You can use SnapLock to meet regulatory compliance, to
protect business-critical data from ransomware attacks, and to provide an additional layer
of protection for your data against alteration or deletion.

Amazon FSx for NetApp ONTAP supports the Compliance and Enterprise modes of retention with SnapLock.
For more information, see [Understanding SnapLock Compliance](snaplock-compliance.md "snaplock-compliance.md") and [Understanding SnapLock Enterprise](snaplock-enterprise.md "snaplock-enterprise.md").

You can create SnapLock volumes on FSx for ONTAP file systems created on or after July 13, 2023.
Existing file systems will get SnapLock support during an upcoming weekly maintenance window.

###### Topics

- [How SnapLock works](how-snaplock-works.md "how-snaplock-works.md")
- [Understanding SnapLock Compliance](snaplock-compliance.md "snaplock-compliance.md")
- [Understanding SnapLock Enterprise](snaplock-enterprise.md "snaplock-enterprise.md")
- [Understanding the
  SnapLock retention period](snaplock-retention.md "snaplock-retention.md")
- [Committing files to WORM state](worm-state.md "worm-state.md")
