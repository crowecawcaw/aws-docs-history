# Viewing the common snapshot

The common snapshot is used to maintain incrementality between your backups. This procedure explains how to identity the common snapshot on your volume.

###### To view a volume's common snapshot

- To determine which snapshot is a volume's common snapshot, use the
  [**volume snapshot show**](https://docs.netapp.com/us-en/ontap-cli-9131/volume-snapshot-show.html "https://docs.netapp.com/us-en/ontap-cli-9131/volume-snapshot-show.html")
  ONTAP CLI command.

```
volume snapshot show -volume `volume-name`
```

In the output, the name of the common snapshot has the format of `backup-`id``,
 where `id` is a 17 digit alphanumeric string, as shown in the following example:

```
`FsxIdabc12345::>` `volume snapshot show -volume test_vol`
 `---Blocks---
Vserver Volume Snapshot Size Total% Used%
-------- -------- --------------------------- -------- ------ -----
dest-svm test_vol
 snap1 144KB 0% 3%
 snap2 832KB 0% 16%
 ---> backup-abcdef0123456789a 4.87MB 0% 53% <---
 weekly.2024-05-26_0015 5.02MB 0% 54%
 weekly.2024-06-02_0015 2.22MB 0% 34%
 daily.2024-06-04_0010 284KB 0% 6%
 daily.2024-06-05_0010 4.29MB 0% 50%
 hourly.2024-06-05_0705 168KB 0% 4%
8 entries were displayed.`
```

###### Important

Do not delete the common snapshot on the volume because it is used to maintain
incrementality between your backups. Deleting a volume's common snapshot will
cause the next backup to be a full backup of the volume instead of an incremental backup.
