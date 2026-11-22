

# Retrieving the results of a remote access session in AWS Device Farm

For information about sessions, see [Sessions](sessions.md).
+ [Prerequisites](#how-to-access-session-results-prerequisites)
+ [Viewing session details](#how-to-view-session-details)
+ [Downloading session video or logs](#how-to-access-session-files)

## Prerequisites
<a name="how-to-access-session-results-prerequisites"></a>
+ Complete a session. Follow the instructions in [Using a remote access session in AWS Device Farm](how-to-use-session.md), and then return to this page.

## Viewing session details
<a name="how-to-view-session-details"></a>

When a remote access session ends, the Device Farm console displays a table that contains details about activity during the session. For more information, see [Analyzing Log Information](how-to-use-reports.md#how-to-use-reports-console-log).

To return to the details of a session at a later time:

1. On the Device Farm navigation panel, choose **Mobile Device Testing**, then choose **Projects**.

1. Choose the project containing the session.

1. Choose **Remote access**, and then choose the session you want to review from the list.

## Downloading session video or logs
<a name="how-to-access-session-files"></a>

When a remote access session ends, the Device Farm console provides access to a video capture of the session and activity logs. In the session results, choose the **Files** tab for a list of links to the session video and logs. You can view these files in the browser or save them locally.

The **Files** tab lists the following files.

****Video****  
A video capture of the device screen during the session.

****Logcat****  
The log of the Android device during the session.

****Device Connect Command Log****  
A log of the Android Debug Bridge (adb) commands that you ran through Device Connect for AWS Device Farm during the session. The log is a tab-separated values (TSV) file with one header row and one row for each connection to the device. Most adb commands open one connection. The bridge also opens connections of its own, for example to keep the session active. Commands that the bridge handles on your computer, such as `adb devices` and `adb forward`, have no row. For more information about Device Connect, see [Using local adb tools with Device Connect](device-connect.md).  
The columns are `start_time`, `outcome`, `duration_seconds`, `bytes_in`, `bytes_out`, `requests`, `detail`, and `output`. The `outcome` is `ok`, `fail`, `denied`, `timeout`, or `adb-connect-failed`. A `denied` row is an adb command that Device Farm refused. For more information, see [Refused commands](device-connect-support.md#device-connect-supported-commands-refused). The `detail` column gives the reason for an outcome other than `ok`. The `output` column holds the first 256 bytes of the response. A longer response ends with `...[truncated]`.  
The following example shows the log of a short session. The first row is `adb get-state`. The next three rows are `adb reverse` commands that add, list, and remove a reverse rule. The last row is `adb reverse tcp:0 tcp:21889`, which Device Farm refused.  

```
start_time	outcome	duration_seconds	bytes_in	bytes_out	requests	detail	output
2026-11-14T23:46:28.523Z	ok	0.007	18	14	host:get-state		
2026-11-14T23:46:28.826Z	ok	3.044	61	12	host:transport-any | reverse:forward:tcp:21099;tcp:21889		OKAY
2026-11-14T23:46:38.831Z	ok	0.019	46	44	host:transport-any | reverse:list-forward		0020R3CN30ABCDE tcp:21099 tcp:21889\n
2026-11-14T23:47:01.468Z	ok	0.047	55	12	host:transport-any | reverse:killforward:tcp:21099		OKAY
2026-11-14T23:47:16.397Z	fail	0.018	57	61	host:transport-any | reverse:forward:tcp:0;tcp:21889	reverse tcp:0 is not supported on AWS Device Farm
```

You can also list the files with the [`ListArtifacts`](https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListArtifacts.html) API. Each entry has a `url` that you can download with a GET request. For example, the following command lists the files of a session.

```bash
aws devicefarm list-artifacts \
  --type FILE \
  --arn arn:aws:devicefarm:us-west-2:111122223333:session:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef/00000
```

This will show output such as the following. The Device Connect Command Log has the type `DEVICE_CONNECT_COMMAND_LOG`.

```
{
    "artifacts": [
        {
            "arn": "arn:aws:devicefarm:us-west-2:111122223333:artifact:12345678-1111-2222-333-456789abcdef/12345678-1111-2222-333-456789abcdef/00000",
            "name": "Device Connect Command Log",
            "type": "DEVICE_CONNECT_COMMAND_LOG",
            "extension": "tsv",
            "url": "https://prod-us-west-2-results.s3.dualstack.us-west-2.amazonaws.com/111122223333/12345678..."
        }
    ]
}
```