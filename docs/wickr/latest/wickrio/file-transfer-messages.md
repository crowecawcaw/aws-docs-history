This guide provides documentation for Wickr IO Integrations. If you're
using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# File transfer messages

The msgtype for file transfer messages is 6000. This message type contains information
about a file transfer message. The "file" JSON object contains the details of the file being
transferred, described in this table:

| Field             | Description                                                    |
| ----------------- | -------------------------------------------------------------- |
| filename          | The display name of the file being transferred.                |
| guid              | A unique identifier for the transferred file.                  |
| uploadedbyuser    | The user who uploaded the file                                 |
| uploadedtimestamp | Upload time                                                    |
| localfilename     | The full path name of the file on the Wickr IO Gateway system. |

Files received by the Wickr IO client will be decrypted and remain on the Wickr IO
client until removed by your software.

The files sent for screen shots will be identified by a **isscreenshot**
key value pair, in the "file" object. This is a Boolean value, where true identifies the file as
a screenshot. If the **isscreenshot** key is not found then the file is not a
screen shot.

## One-to-one messages

The following shows the format of a file transfer message in 1:1 conversations:

```
 {
    "file": {
        "filename": "picture.jpeg",
        "guid": "AD20D048-9B60-4F32-A691-2D4BE4152E58",
        "localfilename": "/opt/WickrIO/clients/compliancebot01/attachments/attachment_20171116111610865_picture.jpeg",
        "uploadedbyuser": "cn0623_01@amazon.com",
        "uploadedtimestamp": "7/11/23 5:22 PM"
    },
    "message_id": "91a189c0cae911e79ec4eb19a763225b",
    "msg_ts": "1510849017.756174",
    "msgtype": 6000,
    "receiver":"user001",
    "sender": "user003",
    "sender_type": "normal",
    "time": "7/11/23 5:22 PM",
    "time_iso": "2023-07-11 17:22:02.348",
    "vgroupid": "53042f1bd04491c6f3732a871e27ab516a8d1534cc1e2d25c4e4869ce72e8541"
}
```

## Group and Room conversation messages

The following shows the format of a file transfer message in group or room conversation
conversations:

```
 {
    "file": {
        "filename": "picture.jpeg",
        "guid": "AD20D048-9B60-4F32-A691-2D4BE4152E58",
        "localfilename": "/opt/WickrIO/clients/compliancebot01/attachments/attachment_20171116111610865_picture.jpeg",
        "uploadedbyuser": "cn0623_01@amazon.com",
        "uploadedtimestamp": "7/11/23 5:22 PM"
    },
    "message_id": "91a189c0cae911e79ec4eb19a763225b",
    "msg_ts": "1510849017.756174",
    "msgtype": 6000,
    "sender": "user003",
    "sender_type": "normal",
    "time": "7/11/23 5:22 PM",
    "time_iso": "2023-07-11 17:22:02.348",
    "vgroupid": "S3042f1bd04491c6f3732a871e27ab516a8d1534cc1e2d25c4e4869ce72e8541"
}
```
