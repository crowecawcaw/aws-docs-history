# Understanding Tape Status

Each tape has an associated status that tells you at a glance what the health of the tape
is. Most of the time, the status indicates that the tape is functioning normally and that no
action is needed on your part. In some cases, the status indicates a problem with the tape
that might require action on your part. You can find information following to help you
decide when you need to act.

###### Topics

- [Understanding Tape Status Information in a VTL](#tape-status "#tape-status")
- [Determining Tape Status in an
  Archive](#determine-tape-status-vts "#determine-tape-status-vts")

## Understanding Tape Status Information in a VTL

A tape's status must be AVAILABLE for you to read or write to the tape. The following
table lists and describes possible status values.

| Status            | Description                                                                                                                                                                                                                                                                                 | Tape Data Is Stored In                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| CREATING          | The virtual tape is being created. The tape can't be loaded into<br>a tape drive, because the tape is being created.                                                                                                                                                                        | —                                                                                                  |
| AVAILABLE         | The virtual tape is created and ready to be loaded into a tape<br>drive.                                                                                                                                                                                                                    | Amazon S3                                                                                          |
| IN TRANSIT TO VTS | The virtual tape has been ejected and is being uploaded for archive.<br>At this point, your Tape Gateway is uploading data to AWS. If the<br>amount of data being uploaded is small, this status might not appear.<br>When the upload is completed, the status changes to ARCHIVING.        | Amazon S3                                                                                          |
| ARCHIVING         | The virtual tape is being moved by your Tape Gateway to the archive,<br>which is backed by S3 Glacier Flexible Retrieval or<br>S3 Glacier Deep Archive. This process happens after the data<br>upload to AWS is completed.                                                                  | Data is being moved from Amazon S3 to S3 Glacier Flexible Retrieval or<br>S3 Glacier Deep Archive. |
| DELETING          | The virtual tape is being deleted.                                                                                                                                                                                                                                                          | Data is being deleted from Amazon S3                                                               |
| DELETED           | The virtual tape has been successfully deleted.                                                                                                                                                                                                                                             | —                                                                                                  |
| RETRIEVING        | The virtual tape is being retrieved from the archive to your<br>Tape Gateway. NoteThe virtual tape can be retrieved only to a<br>Tape Gateway.                                                                                                                                              | Data is being moved from S3 Glacier Flexible Retrieval or<br>S3 Glacier Deep Archive to Amazon S3  |
| RETRIEVED         | The virtual tape is retrieved from the archive. The retrieved tape is<br>write-protected.                                                                                                                                                                                                   | Amazon S3                                                                                          |
| RECOVERED         | The virtual tape is recovered and is read-only.<br>When your Tape Gateway is not accessible for any reason, you can<br>recover virtual tapes associated with that Tape Gateway to another<br>Tape Gateway. To recover the virtual tapes, first deactivate the<br>inaccessible Tape Gateway. | Amazon S3                                                                                          |
| IRRECOVERABLE     | The virtual tape can't be read from or written to. This status<br>indicates an error in your Tape Gateway.                                                                                                                                                                                  | Amazon S3                                                                                          |

## Determining Tape Status in an

Archive

You can use the following procedure to determine the status of a virtual tape in an
archive.

###### To determine the status of a virtual tape

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose **Tapes**.
3. In the **Status** column of the tape library grid, check the
   status of the tape.

The tape status also appears in the **Details** tab of each
virtual tape.

Following, you can find a description of the possible status values.

| Status     | Description                                                                                                         |
| ---------- | ------------------------------------------------------------------------------------------------------------------- |
| ARCHIVED   | The virtual tape has been ejected and is uploaded to the<br>archive.                                                |
| RETRIEVING | The virtual tape is being retrieved from the archive. NoteThe virtual tape can be retrieved only to a Tape Gateway. |
| RETRIEVED  | The virtual tape has been retrieved from the archive. The retrieved<br>tape is read-only.                           |

For additional information about how to work with tapes and VTL devices, see [Managing tapes in your virtual tape
library](managing-virtual-tapes-vtl.md "managing-virtual-tapes-vtl.md").
