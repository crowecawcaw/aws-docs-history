# Managing discovery tool storage

The discovery tool stores collected data in a local database on the appliance or host. The tool collects data continuously, so the database grows with the size of your server inventory and the length of the collection period.

The discovery tool tracks its own disk usage and warns you as space runs low. It also pauses collection before the disk fills, so that you do not lose data. You manage storage on the **Settings** page in the discovery tool console.

## Understanding disk usage states

The discovery tool responds to disk usage as follows.

| Disk usage       | State                                        | Discovery tool behavior                                                                                                                                                |
| ---------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Below 85%        | **Ok**, or *_Advisory_<br>• at 70% and above | Collection runs normally. Below 70%, the console reports **Collection running normally**. At 70% and above, it reports **Disk usage elevated**. No action is required. |
| 85% to below 90% | **Warning**                                  | Collection runs normally. The console reports **Disk space getting low**.                                                                                              |
| 90% or above     | **Critical**                                 | The discovery tool pauses all collection. The console shows an error that you cannot dismiss.                                                                          |

The discovery tool checks disk usage every 5 minutes. These thresholds are fixed. You cannot change them.

A database write can fail because the disk is full. If that happens, the discovery tool pauses collection immediately. It does not wait for the next check.

While collection is paused, the discovery tool skips scheduled rounds. **Start** and **Collect data now** are not available. You can still export data you already collected. You can also change retention settings. For more information about restarting collection, see [Resuming collection](#discovery-tool-storage-resume "#discovery-tool-storage-resume").

## Resuming collection

Collection does not resume on its own. After you free space, choose **Resume collection** on the **Settings** page.

You can resume collection only after usage falls below 85%. That is the warning level, not the 90% critical level. The lower threshold prevents collection from pausing again immediately. If usage is still 85% or higher, free more space first.

**Prune data** counts toward freeing space, even though the database file does not shrink. For more information, see [Reviewing usage and pruning data](#discovery-tool-storage-prune "#discovery-tool-storage-prune"). The discovery tool tracks the free space inside the database, and new data reuses that space without growing the file. In most cases, pruning is enough to resume collection without a larger disk.

## Configuring data retention

By default, the discovery tool keeps collected data for 30 days. It deletes older data once a day. You can set one period for all modules, or set it per module.

###### To configure data retention

1. Open the discovery tool console at `https://<discovery-tool-vm-ip>:5000`.
2. Choose **Settings**.
3. For **Global retention (days)**, enter the number of days to keep data.
4. (Optional) Set a different period for one or more modules.
5. Choose **Save**.

Shorter retention saves space, but it also reduces the range of data you can export. An export can only include data that the discovery tool still holds. We recommend that you keep retention as long as the range you plan to export.

You can change retention settings even while collection is paused.

## Reviewing usage and pruning data

The **Settings** page shows current disk usage. It also shows free space inside the database, and a **Database usage by module** breakdown. This information shows which module holds the most data.

**Prune data** deletes data older than a period that you set. It applies only to the modules that you select. You can use your saved period, or set a different one for that run.

###### Important

Pruning deletes collected data permanently. If you set 0 days, the discovery tool deletes all data for the modules that you select. Export any data you still need first.
