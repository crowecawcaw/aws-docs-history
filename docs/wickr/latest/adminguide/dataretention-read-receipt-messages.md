

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Read receipt messages
<a name="dataretention-read-receipt-messages"></a>

Read receipts confirm that a user has read messages in a conversation. The **message\_timestamp\_secs** field indicates which message was read, and the **read\_receipt\_timestamp** field shows when it was read.

```
{
  "readreceipt": {
    "status": "READ",
    "message_timestamp_secs": "1780503683",
    "message_timestamp_usecs": "0",
    "read_receipt_timestamp": "1780503700"
  },
  "message_id": "9a0b1c2d3e4f5a6b7c8d9e0f",
  "msg_ts": "1780503700.000000",
  "msgtype": 9200,
  "sender": "user001@example.com",
  "sender_type": "normal",
  "time": "6/3/26 4:21 PM",
  "time_iso": "2026-06-03 16:21:40.000",
  "vgroupid": "S3f8a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9"
}
```