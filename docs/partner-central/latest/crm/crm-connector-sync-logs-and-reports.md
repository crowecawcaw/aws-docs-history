# Sync logs and reports

The following topics explain how to use sync logs and reports in the AWS Partner CRM connector
app. The topics also list the log and report types, and the data they contain.

###### Topics

- [Sync logs](#sync-logs "#sync-logs")
- [Reports](#reports "#reports")

## Sync logs

In the connector app, the **Sync Log** tab displays the status of the
synchronization records for inbound and outbound APN synchronization. You use the tab to verify a successful sync and troubleshoot sync errors.

Use the included list views to toggle between
**Inbound** and **Outbound** synchronization
logs.

- **Inbound Orchestration** – Indicates the job that checks
  for available inbound records from APN.
- **Inbound Orchestration Record Retrieval** – Indicates the
  job that picks up and processes pending inbound records from APN.
- **Outbound Orchestration** – Indicates the job that sends
  pending outbound transactions from your organization to APN.

The **Sync Log** record page shows the status of the synchronization
job, the number of records in the payload, the number of records processed successfully, and
the number of records in error.

The related **Sync Log** details show the individual record details
processed as part of the synchronization job, plus their individual statuses. The following
tables explain each type of log file and their related contents.

### Log types

| **Purpose**                  | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Outbound File Retrieval**  | Created when the outbound job runs based on frequency and whether a new<br>set of pending records must be synced with AWS. Logs are created only when<br>records must match the following filter specification for the outbound sync:<br>`Updates for AWS` is `true` and `Last Sync<br>Date` is null, or `Last Sync Date` is before the `Last<br>Modified Date` and `Last Modified By` is the user who<br>scheduled the sync jobs. |
| **Inbound File Retrieval**   | Created based on your inbound sync schedule. The log lists the callouts<br>that check for pending inbound transactions from AWS.                                                                                                                                                                                                                                                                                                   |
| **Inbound Record Retrieval** | Created only when the parent Inbound File Retrieval job identifies<br>pending inbound transactions from AWS. The log contains the details of the<br>file from AWS that contains the opportunity or lead records.                                                                                                                                                                                                                   |

### Outbound file retrieval results

| **Direction** | **Purpose**            | **Status**    | **Definition**                                                                                               |
| ------------- | ---------------------- | ------------- | ------------------------------------------------------------------------------------------------------------ |
| **From AWS**  | Inbound file retrieval | `API Success` | A list call to the bucket succeeded, The call checked for pending inbound<br>records that must be processed. |
| **From AWS**  | Inbound file retrieval | `Error`       | The list call failed, typically due to invalid credentials or a permission<br>issue.                         |

### Inbound file retrieval results

| **Direction** | **Purpose**              | **Status**    | **Definition**                                                                                                                                                                                                                                                                                     |
| ------------- | ------------------------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **From AWS**  | Inbound record retrieval | `API success` | A `get` call was made to retrieve the file listed from the `Inbound File<br>Retrieval` operation, if one or more files exist and await processing.                                                                                                                                                 |
| **From AWS**  | Inbound record retrieval | `Partial`     | The file was retrieved but processing failed for some records. Review the sync log to troubleshoot the<br>failure.                                                                                                                                                                                 |
| **From AWS**  | Inbound record retrieval | `Error`       | Processing failed for all records due to one of the following<br>reasons:<br>• A a connection error prevented file retrieval.<br>• The file was retrieved but none of the records in the file could be<br>written to your Salesforce object, typically due to a validation or<br>permission issue. |
| **From AWS**  | Inbound record retrieval | `API success` | If one or more files are present and awaiting processing, a `get` call is made<br>to retrieve the file listed from the `Inbound File Retrieval`<br>operation.                                                                                                                                      |
| **From AWS**  | Inbound record retrieval | `Partial`     | The file was retrieved but processing failed for some of the records. Review the sync log to troubleshoot the<br>failure.                                                                                                                                                                          |
| **From AWS**  | Inbound record retrieval | `Error`       | Processing failed for all records due to one of the<br>following reasons:<br>• A connection error prevented file retrieval.<br>• The file was retrieved but none of the records in the file could be<br>written to your Salesforce object, most likely due to a validation or<br>permission issue. |
| **From AWS**  | Inbound record retrieval | `Processed`   | Processing succeeded and the records inserted into<br>your mapped object.                                                                                                                                                                                                                          |

## Reports

The AWS Partner CRM connector package includes reports that allow you to track the
status of the synchronization between your organization and APN.

###### To view reports for synchronization

1. In the AWS Partner CRM connector app, choose the **Reports** tab.
2. Choose **All Folders**, then **AWS Partner CRM
   connector**.

Available reports include the following:

- **Inbound Sync Logs** – `Error: Inbound`
  synchronization record failures by day.
- **Inbound Sync Logs** – `Success: Inbound`
  synchronization record successes by day.
- **Outbound Sync Logs** – `Error: Outbound`
  synchronization record failures by day.
- **Outbound Sync Logs** – `Success: Outbound`
  synchronization record successes by day.
- **Synchronization Summary** – Summary of inbound and
  outbound synchronization jobs by day.
