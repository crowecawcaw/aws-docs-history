This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Calling messages

Calls can have four status values.

| Call status    | Status value |
| -------------- | ------------ |
| Call starting  | 0            |
| Call completed | 1            |
| Call missed    | 2            |
| Call cancelled | 3            |

**Call start**

The following is a call start example.

```
{
  "call": {
    "calluri": "35.94.128.212:16450",
    "calluriipv6": "[2600:1f14:e22:9c02::c8]:16450",
    "meetingid": 0,
    "participants": [
      "8995950dad747c24fd7c9e2da68edeb6c2c0ac6cb96d405c0c4c58e09ff46969",
      "ae182b20ce36a94c613af5a2964bbd616de662d3f8487dc39fa9400e739a3049"
    ],
    "status": 0,
    "version": 2,
    "versioncheck": true
  },
  "message_id": "4d421aa08be811eaaf7a493af2765a5b",
  "msg_ts": "1588364043.000000",
  "msgtype": 7000,
  "receiver": "user001",
  "sender": "user002",
  "sender_type": "normal",
  "time": "5/1/20 1:14 PM",
  "time_iso": "2020-05-01 13:14:03.000",
  "vgroupid": "4ebf561eb2214c4e6f924d09e37bf80b6f9b85cb96b72badb03753d9ed26f7f4"
}
```

###### Note

The **participants** array has the
**username\_hash** of the users that were on the call.

**Invite to call**

When a user is invited to an active call, it appears as a new call started. You can use
the **invitemsgid** field to match invites to the original call.

```
{
  "call": {
    "calluri": "18.234.76.29:16504",
    "calluriipv6": "[2600:1f18:2741:9e00::df8e]:16504",
    "invitemsgid": "87b5e4a095ef11ea99b03bd5dd4eaa9d",
    "meetingid": 0,
    "participants": [
      "ae182b20ce36a94c613af5a2964bbd616de662d3f8487dc39fa9400e739a3049"
    ],
    "startmsgid": "87b5e4a095ef11ea99b03bd5dd4eaa9d",
    "status": 0,
    "version": 2,
    "versioncheck": true
  },
  "message_id": "ce22f14095ef11eaa1cbdf2a74e88e51",
  "msg_ts": "1589466777.000000",
  "msgtype": 7000,
  "receiver": "user001",
  "sender": "user002",
  "sender_type": "normal",
  "time": "5/14/20 2:32 PM",
  "time_iso": "2020-05-14 14:32:57.000",
  "vgroupid": "7f1a06a35243584436f6df7170e0fc8a784022a66b5e5d168b419b14cecdcdad"
}
```

**Call end**

The following is a call end example. The **duration** field shows the
call length in seconds.

```
{
  "call": {
    "duration": 38,
    "meetingid": 1,
    "startmsgid": "72c9a3b08bea11eab9078f7ca8a1b909",
    "status": 1,
    "version": 2,
    "versioncheck": true
  },
  "message_id": "8b9d94408bea11ea89aea91887dfff41",
  "msg_ts": "1588365006.000000",
  "msgtype": 7000,
  "receiver": "user001",
  "sender": "user002",
  "sender_type": "normal",
  "time": "5/1/20 1:30 PM",
  "time_iso": "2020-05-01 13:30:06.000",
  "vgroupid": "4ebf561eb2214c4e6f924d09e37bf80b6f9b85cb96b72badb03753d9ed26f7f4"
}
```
