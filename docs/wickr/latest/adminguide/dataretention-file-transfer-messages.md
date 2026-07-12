This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# File transfer messages

The **file** JSON object contains the details of the file being
transferred, described in the following table.

| Field             | Description                                                |
| ----------------- | ---------------------------------------------------------- |
| filename          | The display name of the file being transferred.            |
| guid              | A unique identifier for the transferred file.              |
| isscreenshot      | Boolean field that identifies if the file is a screenshot. |
| localfilename     | The path name of the file in the compliance output.        |
| uploadedbyuser    | The display name of the user, if known.                    |
| uploadedtimestamp | The time when the file was uploaded by the user.           |

The following shows the format of a file transfer message. The
**msgtype** for file transfer messages is 6000. The compliance
system decrypts files that it receives and stores them in the compliance output
location.

```
{
  "file": {
    "filename": "quarterly-report.pdf",
    "guid": "068ed9ed-d6e4-4f41-984f-b82f74b16fde",
    "localfilename": "compliance-output-file-quarterly-report.pdf",
    "uploadedbyuser": "user002@example.com",
    "uploadedtimestamp": "8/4/23 7:15 PM"
  },
  "message_id": "4f8d3b6032fb11ee9a74053bb1017859",
  "msg_ts": "1691176544.000000",
  "msgtype": 6000,
  "receiver": "user001@example.com",
  "sender": "user002@example.com",
  "sender_type": "normal",
  "time": "8/4/23 7:15 PM",
  "time_iso": "2023-08-04 19:15:44.000",
  "vgroupid": "7ad65d17b945d7672190ecab6902fdd06eff162b91adfcda23df3b2ff95875e8"
}
```
