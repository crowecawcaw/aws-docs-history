# Quotas

Following, you can find out about quotas when working with Amazon FSx for Windows File Server.

###### Topics

- [Quotas that you can increase](#soft-limits "#soft-limits")
- [Resource quotas for each file
  system](#limits-MFS-resources-file-system "#limits-MFS-resources-file-system")
- [Additional considerations](#limits-additional-considerations "#limits-additional-considerations")
- [Quotas specific to Microsoft Windows](#ntfs-limits "#ntfs-limits")

## Quotas that you can increase

Following are the quotas for Amazon FSx for Windows File Server for each AWS account, per AWS Region,
that you can increase.

| Resource                     | Default | Description                                                                                                                             |
| ---------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Windows file systems         | 100     | The maximum number of Amazon FSx for Windows Server file systems that you can create in this account.                                   |
| Windows throughput capacity  | 10240   | The total amount of throughput capacity (in MBps) allowed for all Amazon FSx for Windows file systems in this account.                  |
| Windows HDD storage capacity | 524288  | The maximum amount of HDD storage capacity (in GiB) allowed for all Amazon FSx for Windows File Server file systems in this account.    |
| Windows SSD storage capacity | 524288  | The maximum amount of SSD storage capacity (in GiB) allowed for all Amazon FSx for Windows File Server file systems in this account.    |
| Windows total SSD IOPS       | 500,000 | The total amount of SSD IOPS allowed for all Amazon FSx for Windows File Server file systems in this account.                           |
| Windows backups              | 500     | The maximum number of user-initiated backups for all Amazon FSx for Windows File Server file systems that you can have in this account. |

###### To request a quota increase

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/dashboard").
2. In the navigation pane, choose **AWS services**.
3. Choose **Amazon FSx**.
4. Choose a quota.
5. Choose **Request quota increase**, and follow
   the directions to request a quota increase.
6. To view the status of the quota request, choose **Quota request history**
   in the console navigation pane.

For more information, see [Requesting a quota
increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

## Resource quotas for each file

system

Following are the quotas on Amazon FSx for Windows File Server resources for each file system in an AWS Region.

| Resource                                                                                          | Limit per file system |
| ------------------------------------------------------------------------------------------------- | --------------------- |
| Maximum number of tags                                                                            | 50                    |
| Maximum retention period for automated backups                                                    | 90 days               |
| Maximum number of backup copy requests in progress<br>to a single destination Region per account. | 5                     |
| Minimum storage capacity, SSD file systems                                                        | 32 GiB                |
| Minimum storage capacity, HDD file systems                                                        | 2,000 GiB             |
| Maximum storage capacity, SSD and HDD                                                             | 64 TiB                |
| Minimum SSD IOPS                                                                                  | 96                    |
| Maximum SSD IOPS                                                                                  | 400,000               |
| Minimum throughput capacity                                                                       | 8 MBps                |
| Maximum throughput capacity                                                                       | 12,288 MBps           |
| Maximum number of file shares                                                                     | 100,000               |

## Additional considerations

In addition, note the following:

- You can use each AWS Key Management Service (AWS KMS) key on up to 125 Amazon FSx file systems.
- For a list of AWS Regions where you can create file systems, see [Amazon FSx Endpoints and Quotas](../../../general/latest/gr/fsxn.md "../../../general/latest/gr/fsxn.md") in the _AWS General Reference_.
- You map your file shares from Amazon EC2 instances in your virtual private cloud (VPC) with
  their Domain Name Service (DNS) names.

## Quotas specific to Microsoft Windows

For more information, see [NTFS](https://docs.microsoft.com/en-us/windows/desktop/FileIO/filesystem-functionality-comparison#limits "https://docs.microsoft.com/en-us/windows/desktop/FileIO/filesystem-functionality-comparison#limits") limits on the Microsoft Windows Dev Center.
