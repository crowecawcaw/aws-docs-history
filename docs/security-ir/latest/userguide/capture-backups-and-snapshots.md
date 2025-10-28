# Capture backups and snapshots

Setting up backups of key systems and databases are critical for recovering from a
security incident and for forensics purposes. With backups in place, you can restore your
systems to their previous safe state. On AWS, you can take snapshots of various resources.
Snapshots provide you with point-in-time backups of those resources. There are many AWS
services that can support you in backup and recovery. Refer to the [Backup and Recovery Prescriptive Guidance](../../../prescriptive-guidance/latest/backup-recovery/services.md "../../../prescriptive-guidance/latest/backup-recovery/services.md") for details on these services and
approaches for backup and recovery. For more details, see the [Use backups to
recover from security incidents](https://aws.amazon.com/blogs/security/use-backups-to-recover-from-security-incidents/ "https://aws.amazon.com/blogs/security/use-backups-to-recover-from-security-incidents/") blog post.

Especially when it comes to situations such as ransomware, it’s critical for your backups
to be well protected. Refer to the
[Top 10
security best practices for securing backups in AWS](https://aws.amazon.com/blogs/security/top-10-security-best-practices-for-securing-backups-in-aws/ "https://aws.amazon.com/blogs/security/top-10-security-best-practices-for-securing-backups-in-aws/") blog post for guidance on securing your
backups. In addition to securing your backups, you should regularly test your backup and restore
processes to verify that the technology and processes you have in place work as expected.
