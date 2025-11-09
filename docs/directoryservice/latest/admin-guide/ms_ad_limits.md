# AWS Managed Microsoft AD quotas

The following are the default quotas for AWS Managed Microsoft AD. Each quota is per Region unless
otherwise noted.

| AWS Managed Microsoft AD quotas                                                                                     | Resource                       | Default quota |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------- |
| AWS Managed Microsoft AD directories (Standard and Enterprise Editions)                                             | 20                             |
| AWS Managed Microsoft AD directories (Hybrid Edition)                                                               | 5                              |
| Manual snapshots (Standard and Enterprise Editions) \*                                                              | 5 per AWS Managed Microsoft AD |
| Manual snapshots age \*\*                                                                                           | 180 days                       |
| Maximum number of domain controllers per directory                                                                  | 20                             |
| Shared domains per Standard Microsoft AD \*\*\*                                                                     | 25                             |
| Shared domains per Enterprise Microsoft AD \*\*\*                                                                   | 500                            |
| Shared domains per Hybrid Microsoft AD \*\*\*                                                                       | 125                            |
| Maximum number of registered certificate authority (CA) certificates per<br>directory                               | 5                              |
| Maximum number of total AWS Regions in a single AWS Managed Microsoft AD<br>(Enterprise Edition) directory \*\*\*\* | 5                              |

\* The manual snapshot quota cannot be changed.

\*\* The maximum supported age of a manual snapshot is 180 days and cannot be changed. This is
due to the Tombstone-Lifetime attribute of deleted objects which defines the useful shelf life
of a system-state backup of Active Directory. It is not possible to restore from a snapshot
older than 180 days. For more information, see [Useful shelf life of a system-state backup of Active Directory](https://learn.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/shelf-life-system-state-backup-ad "https://learn.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/shelf-life-system-state-backup-ad") on the Microsoft
website.

\*\*\* The shared domain default quota refers to the number of accounts that an individual directory can be shared to.

\*\*\*\* This includes 1 primary Region and up to 4 additional Regions. For more information, see
[Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").

###### Note

You cannot attach a public IP address to your AWS elastic network interface
(ENI).

For information regarding application design and load distribution, see [Best practices when programming your applications for an AWS Managed Microsoft AD](ms_ad_best_practices.md#program_apps "ms_ad_best_practices.md#program_apps").

For storage and object quotas, see the **Comparison Table** on
the [AWS Directory Service
Pricing](https://aws.amazon.com/directoryservice/pricing/ "https://aws.amazon.com/directoryservice/pricing/") page.
