# Service quotas for Amazon FSx for Lustre

Following, you can find out about quotas when working with Amazon FSx for Lustre.

###### Topics

- [Quotas that you can increase](#soft-limits "#soft-limits")
- [Resource quotas for each file
  system](#limits-MFS-resources-file-system "#limits-MFS-resources-file-system")
- [Additional considerations](#limits-additional-considerations "#limits-additional-considerations")

## Quotas that you can increase

Following are the quotas for Amazon FSx for Lustre per AWS account, per AWS Region, which you
can increase.

| Resource                                                              | Default | Description                                                                                                                                                                          |
| --------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Lustre Persistent 1 file systems                                      | 100     | The maximum number of Amazon FSx for Lustre Persistent 1 file systems that you can create in this account.                                                                           |
| Lustre Persistent 2 file systems                                      | 100     | The maximum number of Amazon FSx for Lustre Persistent 2 file systems that you can create in this account.                                                                           |
| Lustre Persistent HDD storage capacity (per file system)              | 102000  | The maximum amount of HDD storage capacity (in GiB) that you can configure for an Amazon FSx for Lustre persistent file system.                                                      |
| Lustre Persistent 1 file storage capacity                             | 100800  | The maximum amount of storage capacity (in GiB) that you can configure for all Amazon FSx for Lustre Persistent 1 file systems in this account.                                      |
| Lustre Persistent 2 file storage capacity                             | 100800  | The maximum amount of storage capacity (in GiB) that you can configure for all Amazon FSx for Lustre Persistent 2 file systems in this account.                                      |
| Lustre Scratch file systems                                           | 100     | The maximum number of Amazon FSx for Lustre scratch file systems that you can create in this account.                                                                                |
| Lustre Scratch storage capacity                                       | 100800  | The maximum amount of storage capacity (in GiB) that you can configure for all Amazon FSx for Lustre scratch file systems in this account.                                           |
| Lustre Persistent Intelligent-Tiering throughput capacity             | 100000  | The total amount of throughput capacity (in MBps) allowed for all Amazon FSx for Lustre Intelligent-Tiering file systems in this account.                                            |
| Lustre Persistent Intelligent-Tiering SSD read cache storage capacity | 100800  | The maximum amount of provisioned SSD read cache storage capacity (in GiB) that you can configure for<br>all Amazon FSx for Lustre Intelligent-Tiering file systems in this account. |
| Lustre backups                                                        | 500     | The maximum number of user-initiated backups that you can have for all Amazon FSx for Lustre file systems in this account.                                                           |

###### To request a quota increase

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard").
2. In the navigation pane, choose **AWS services**.
3. Choose **Lustre**.
4. Choose a quota.
5. Choose **Request quota increase**, and follow
   the directions to request a quota increase.
6. To view the status of the quota request, choose **Quota request history**
   in the console navigation pane.

For more information, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

## Resource quotas for each file

system

Following are the limits on Amazon FSx for Lustre resources for each file system in an AWS
Region.

| Resource                                                                                          | Limit per file system |
| ------------------------------------------------------------------------------------------------- | --------------------- |
| Maximum number of tags                                                                            | 50                    |
| Maximum retention period for automated backups                                                    | 90 days               |
| Maximum number of backup copy requests in progress<br>to a single destination Region per account. | 5                     |
| Number of file updates from linked S3 bucket per file systems                                     | 10 million / month    |
| Minimum storage capacity, SSD file systems                                                        | 1.2 TiB               |
| Minimum storage capacity, HDD file systems                                                        | 6 TiB                 |
| Minimum throughput per unit of storage, SSD                                                       | 50 MBps               |
| Maximum throughput per unit of storage, SSD                                                       | 1000 MBps             |
| Minimum throughput per unit of storage, HDD                                                       | 12 MBps               |
| Maximum throughput per unit of storage, HDD                                                       | 40 MBps               |

## Additional considerations

In addition, note the following:

- You can use each AWS Key Management Service (AWS KMS) key on up to 125 Amazon FSx for Lustre file systems.
- For a list of AWS Regions where you can create file systems, see [Amazon FSx Endpoints and Quotas](../../../general/latest/gr/fsxn.md "../../../general/latest/gr/fsxn.md") in the _AWS General Reference_.
