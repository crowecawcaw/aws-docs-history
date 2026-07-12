This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Verification messages

AWS Wickr displays verification messages when a client verifies another client whose
account might have become unverified.

```
{
  "keyverify": {
    "msgtype": 3,
    "verifiedkey": "00040115f7ba8af2b6f2e2e7f8e61cf61d750f25aff2df..."
  },
  "message_id": "6054031032fc11ee9a74053bb1017859",
  "msg_ts": "1691177002.000000",
  "msgtype": 3000,
  "receiver": "user001@example.com",
  "sender": "user002@example.com",
  "sender_type": "normal",
  "time": "8/4/23 7:23 PM",
  "time_iso": "2023-08-04 19:23:22.000",
  "vgroupid": "31767dd6dc31cd5d87579e2694b041116d31ae1750cbcec8e957d237c7fe0591"
}
```

Verification messages have an additional nested **msgtype**.

| Verification message type         | msgtype value |
| --------------------------------- | ------------- |
| Verification request              | 1             |
| Verification response and request | 2             |
| Verification acceptance           | 3             |
| Verification rejection            | 4             |
| "Not Now" response                | 5             |
