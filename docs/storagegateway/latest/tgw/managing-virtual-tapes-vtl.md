# Managing tapes in your virtual tape

library

Storage Gateway provides one virtual tape library (VTL) for each Tape Gateway you activate.
Initially, the library contains no tapes, but you can create tapes whenever you need to.
Your application can read and write to any tapes available on your Tape Gateway. A tape's
status must be AVAILABLE for you to write to the tape. These tapes are backed by Amazon Simple Storage Service
(Amazon S3)—that is, when you write to these tapes, the Tape Gateway stores data in Amazon S3.
For more information, see [Understanding Tape Status Information in a VTL](understand-tapes-status.md#tape-status "understand-tapes-status.md#tape-status").

###### Topics

- [Archiving Tapes](#main-archiving-tapes-managing-vtl "#main-archiving-tapes-managing-vtl")
- [Canceling Tape Archival](#main-canceling-archival-vtl "#main-canceling-archival-vtl")
  The tape library shows tapes in your Tape Gateway. The library shows the tape barcode,
  status, and size, amount of the tape used, and the gateway the tape is associated
  with.

When you have a large number of tapes in the library, the console supports searching for
tapes by barcode, by status, or by both. When you search by barcode, you can filter by
status and gateway.

###### To search by barcode, status, and gateway

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose **Tapes**, and then type a value
   in the search box. The value can be the barcode, status, or gateway. By default,
   Storage Gateway searches for all virtual tapes. However, you can also filter your search by
   status.

If you filter for status, tapes that match your criteria appear in the library in
the Storage Gateway console.

If you filter for gateway, tapes that are associated with that gateway appear in
the library in the Storage Gateway console.

###### Note

By default, Storage Gateway displays all tapes regardless of status.

## Archiving Tapes

You can archive the virtual tapes that are in your Tape Gateway. When you archive a tape,
Storage Gateway moves the tape to the archive.

To archive a tape, you use your backup software. Tape archival process consists of three
stages, seen as the tape statuses **IN TRANSIT TO VTS**,
**ARCHIVING**, and **ARCHIVED**:

- To archive a tape, use the command provided by your backup application. When the
  archival process begins the tape status changes to **IN TRANSIT TO
  VTS** and the tape is no longer accessible to your backup application.
  In this stage, your Tape Gateway is uploading data to AWS. If needed, you can
  cancel the archival in progress. For more information about canceling archival, see
  [Canceling Tape Archival](#main-canceling-archival-vtl "#main-canceling-archival-vtl").

###### Note

The steps for archiving a tape depend on your backup application. For detailed
instructions, see the documentation for your backup application.

- After the data upload to AWS completes, the tape status changes to
  **ARCHIVING** and Storage Gateway begins moving the tape to the
  archive. You cannot cancel the archival process at this point.
- After the tape is moved to the archive, its status changes to
  **ARCHIVED** and you can retrieve the tape to any of your
  gateways. For more information about tape retrieval, see [Retrieving Archived Tapes](retrieving-archived-tapes-vtl.md "retrieving-archived-tapes-vtl.md").

The steps involved in archiving a tape depend on your backup software. For instructions on
how to archive a tape by using Symantec NetBackup software, see [Archiving the Tape](backup_netbackup-vtl.md#GettingStarted-archiving-tapes-vtl "backup_netbackup-vtl.md#GettingStarted-archiving-tapes-vtl").

## Canceling Tape Archival

After you start archiving a tape, you might decide you need your tape back. For
example, you might want to cancel the archival process, get the tape back because the
archival process is taking too long, or read data from the tape. A tape that is being
archived goes through three statuses, as shown following:

- IN TRANSIT TO VTS: Your Tape Gateway is uploading data to AWS.
- ARCHIVING: Data upload is complete and the Tape Gateway is moving the tape to
  the archive.
- ARCHIVED: The tape is moved and the archive and is available for
  retrieval.

You can cancel archival only when the tape's status is IN TRANSIT TO VTS. Depending on
factors such as upload bandwidth and the amount of data being uploaded, this status
might or might not be visible in the Storage Gateway console. To cancel a tape archival, use the
[CancelRetrieval](../APIReference/API_CancelRetrieval.md "../APIReference/API_CancelRetrieval.md") action
in the API reference.
