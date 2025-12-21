# Export stream session files

During a stream session, your application can generate output files that help you debug or verify your application, such as logs, diagnostic information, crash dumps, save files, user data, and screenshots. The export stream session files feature collects files that are created or modified during a session and exports them as a compressed ZIP file to a provided Amazon S3 location. The feature also collects performance stats for the session every second, which are included in the export ZIP file.

###### Warning

Before you export files, be aware of the following things:

- Files may contain sensitive information written by your application, including credentials information.
- File sizes may be large depending on your application size, which impacts your Amazon S3 storage cost.
- If you select an Amazon S3 bucket in an AWS Region that differs from the Region of the stream group, then the exported stream
  session files will move across regions.

## How it works

You must manually invoke this operation on an active stream session to export the files generated during that session. The stream
session must be active, specifically in one of the following statuses `ACTIVE`, `CONNECTED`,
`PENDING_CLIENT_RECONNECTION`, and `RECONNECTING`. At the end of the session, Amazon GameLift Streams exports the files to
your bucket in Amazon Simple Storage Service (Amazon S3). Thus, all exported data is within your ownership and is subject to the Amazon S3 bucket's permissions policy.

Here's a walkthrough of the stream session lifecycle with export files activated:

1. Amazon GameLift Streams begins a session by connecting the user to your application that's running on the compute resource.
2. While your application streams, it creates or modifies files in the filesystem of the runtime environment.
3. When the session ends, Amazon GameLift Streams gets a copy of all the new or modified files in the filesystem and exports the files to your
   Amazon S3 bucket.

Amazon GameLift Streams collects the following generated and modified files. Find them in the corresponding folders in the `.zip`
archive.

- `application/`: The folder where your application or game is stored.
- `profile/`: The user's profile folder contains the user's personal settings, configurations, and data.
- `temp/`: The system's temp folder contains temporary files and data that your application and the system creates.
  This can include cache files, log files, or intermediate processing data.
- `stats/`: Contains `perf_stats_v1.csv`, which holds performance stats for the session collected per-second. This includes application-level stats (CPU and memory utilization) and system-level stats (CPU, memory, GPU, and VRAM utilization). For a detailed description of each stat included in the CSV file, see [Performance stats reference](realtime-performance-stats.md#realtime-performance-stats-csv "realtime-performance-stats.md#realtime-performance-stats-csv")

To delete the files, delete the object in the Amazon S3 bucket.

## Cost impact

You incur a cost for having the files stored in Amazon S3. A stream session might generate a large amount of data depending on your
application. Be aware that with many stream sessions that have this feature enabled, the cost can add up.

For more information, refer to [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## Export files (Console)

###### To enable export stream session files in the Amazon GameLift Streams console

1. Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/").
2. In the navigation bar, choose **Sessions** to view a list of active and recent stream sessions within the last
   90 days.
3. In the **Active sessions** tab, select an active stream session.
4. Choose **Export files** to enable the export files feature for that stream session.
5. In the **Export stream sessions file** dialog box, choose either **Create a new S3 bucket**
   or **Select an existing S3 bucket**. Follow the steps in the console to create or select an S3 object to store
   the exported data into.

###### Warning

If the ZIP file name matches an existing one in the directory, the previous one will be overwritten. 6. Choose **Confirm**. You can now find the session listed in the **Exported files** tab. 7. Wait for the session to end and for the files to export.

Amazon GameLift Streams will export the files when the session is in **Terminated** state. When a session has terminated,
it will move from the **Active sessions** tab to the **Recent sessions** tab.

You can check the status of the export process in the **Session exports** tab. If the status is
**Pending**, the stream session is still active, so Amazon GameLift Streams hasn't exported the files yet. If the status is
**Succeeded**, you can download the files from Amazon S3 using the link provided. If the status is
**Failed**, hover over the status to see the reason for the failure.

## Export files (CLI)

**Prerequisite**

You must configure the AWS CLI with your user credentials and your chosen AWS Region. For setup instructions, refer to [Download the AWS CLI](setting-up.md#setting-up-prereqs "setting-up.md#setting-up-prereqs").

**To export stream session files in the AWS CLI**

In your AWS CLI use the [ExportStreamSessionFiles](../apireference/API_ExportStreamSessionFiles.md "../apireference/API_ExportStreamSessionFiles.md")
command, customized for your content.

```
aws gameliftstreams export-stream-session-files \
    --identifier `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4` \
    --stream-session-identifier `arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567`
    --ouput-uri s3://`amzn-s3-demo-bucket/prefix`
```

Where

`identifier`

An
[Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") or ID that uniquely identifies the stream group resource.

ARN example: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`

ID example: `sg-1AB2C3De4`

`stream-session-identifier`

An
[Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") or ID that uniquely identifies the stream session resource.

ARN example: `arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567`

ID example: `ABC123def4567`

`output-uri`

The
Amazon S3 bucket URI where Amazon GameLift Streams uploads the set of compressed exported files for this stream session.

There are two valid formats that you can provide. If the URI has a `.zip` or `.ZIP` file extension,
then Amazon GameLift Streams stores the exported files at the provided URI. Otherwise, Amazon GameLift Streams generates the name for a compressed folder and
stores it at the URI. The generated name follows the pattern:
`date-time-applicationId-streamGroupId-streamSessionId`. For example:

- If you provide a URI called `s3://amzn-s3-demo-bucket/MyGame_Session1.zip`, then Amazon GameLift Streams saves the files in that
  exact ZIP folder.
- If you provide a URI called `s3://amzn-s3-demo-bucket/MyGame_Session1/`, then Amazon GameLift Streams will save the files at
  `s3://amzn-s3-demo-bucket/MyGame_Session1/YYYYMMDD-HHMMSS-applicationId-streamGroupId-sessionId.zip`.

Be sure that your ZIP file name complies with the [Object key naming guidelines](../../../AmazonS3/latest/userguide/object-keys.md "../../../AmazonS3/latest/userguide/object-keys.md") in the _Amazon Simple Storage Service User
Guide_.

###### Warning

If the ZIP file name matches an existing one in the directory, the previous one will be overwritten.

You can check on the status of the active session by calling the [GetStreamSession](../apireference/API_GetStreamSession.md "../apireference/API_GetStreamSession.md") API. From the stream session summary, you can get details
about the status of exported files. If the status is **Pending**, then the stream session is still active, so Amazon GameLift Streams hasn't
exported the files yet. If the status is **Succeeded**, navigate to the output URI to see the files in Amazon S3. If the
status is **Failed**, check the `StatusReason` in the `ExportFilesMetaData`.
