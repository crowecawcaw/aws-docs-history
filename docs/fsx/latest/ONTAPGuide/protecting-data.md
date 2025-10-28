# Protecting your data

Beyond automatically replicating your file system's data to ensure [high durability](high-availability-AZ.md "high-availability-AZ.md"), with Amazon FSx
you also have the following options that you can use to further protect your data:

- Native Amazon FSx volume backups that support your backup retention and compliance needs within Amazon FSx.
- Using AWS Backup to implement a centrally managed, automated backup and retention strategy across multiple AWS services.
- Snapshots that enable your users to easily undo unwanted file changes, by
  restoring files to previous versions.
- Use SnapLock to create write once, read many (WORM) storage volumes to prevent file modification or deletion
  once committed, for a specified retention period.
- FlexCache volumes offer storage efficient, cost effective, high-performance data replication
  for read-heavy workloads with data that remains largely unchanged.
- Use SnapMirror to create scheduled, automatic file system replication to a second file system for
  data protection and disaster recovery.

###### Topics

- [Protecting your data with volume backups](using-backups.md "using-backups.md")
- [Protecting your data with snapshots](snapshots-ontap.md "snapshots-ontap.md")
- [Protecting your data with Autonomous Ransomware Protection](ARP.md "ARP.md")
- [Protecting your data with SnapLock](snaplock.md "snaplock.md")
- [Replicating your data with FlexCache](using-flexcache.md "using-flexcache.md")
- [Replicating your data using NetApp SnapMirror](scheduled-replication.md "scheduled-replication.md")
