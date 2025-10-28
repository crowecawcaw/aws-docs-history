# Understanding the

SnapLock retention period

When you create a SnapLock volume, you can set a default retention period for the
volume, or you can set the retention period for write once, read many (WORM) files
explicitly. During the retention period, you can't delete or modify WORM-protected
files. The retention period is used to calculate the retention time. For example, if you
transition a file to WORM on July 14, 2023 at midnight and set the retention period to
five years, then the retention time would be until July 14, 2028 at midnight.

For more information about WORM, see [Committing files to WORM state](worm-state.md "worm-state.md").

## Retention period policies

The retention period is determined by values that you assign to the following
parameters:

- Default retention – The default retention period that's assigned to
  a WORM file if you don't provide an explicit retention period for it.
- Minimum retention – The shortest retention period that can be
  assigned to a WORM file.
- Maximum retention – The longest retention period that can be
  assigned to a WORM file.

###### Note

Even after the retention period expires, you can't modify a WORM file. You can
only delete it or set a new retention period to turn on WORM
protection again.

You can specify the retention period using several different units of time. The
following table lists the specific ranges that are supported.

| Type         | Value      | Notes                                                                                                             |
| ------------ | ---------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Seconds      | 0 - 65,535 |                                                                                                                   |
| Minutes      | 0 - 65,535 |                                                                                                                   |
| Hours        | 0 - 24     |                                                                                                                   |
| Days         | 0 - 365    |                                                                                                                   |
| Months       | 0 -12      |                                                                                                                   |
| Years        | 0 - 100    |                                                                                                                   |
| Infinite     | -          | Retains the files forever. Available for **Default retention**, **Maximum retention**, and **Minimum retention**. |
| Unspecified1 | -          | Retains the files until you set a retention period. Available for **Default retention** only.                     | ###### Note 1When you transition files to WORM with an unspecified retention period, they are given the minimum retention period that is configured for the SnapLock volume. When you transition the WORM-protected files to an absolute retention time, the new retention period must be greater than the minimum period that you set on the files previously. ## Expired retention period After a WORM file's retention period expires, you can delete the file or set a new retention period to turn WORM protection back on. WORM files aren't automatically deleted after their retention period expires. You still can't modify the content of a WORM file, even after its retention period has expired. ## Setting the retention period of a SnapLock volume You can set the retention period of a SnapLock volume with the Amazon FSx console, the AWS CLI, the Amazon FSx API, and the ONTAP CLI and REST API. To set the retention period with the Amazon FSx API, use the [`SnaplockRetentionPeriod`](../APIReference/API_SnaplockRetentionPeriod.md "../APIReference/API_SnaplockRetentionPeriod.md") configuration. In the Amazon FSx console, for **Retention period**, enter values for **Default retention**, **Minimum retention**, and **Maximum retention**. Then choose a corresponding **Unit** for each. |
