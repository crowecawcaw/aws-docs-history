# IVS Costs | Real-Time Streaming

See the [IVS Pricing page](https://aws.amazon.com/ivs/pricing/ "https://aws.amazon.com/ivs/pricing/") for details about costs for IVS.

- **Subscribing and publishing to stages** — Subscribing and publishing consume resources,
  and you will incur an hourly rate for the time you are connected to the stage.
- **Recording** — Individual participant recording incurs no additional Amazon IVS charges,
  while composite recording incurs charges for the hourly rate for the video encoded. Both recording options incur standard
  S3 storage and request costs. Thumbnails incur no additional IVS charges.
- **Participant replication**
  — Replica participants are billed the same as regular participants.

For example, suppose you have two stages, Stage A with Participant A and Stage B with Participant B.
You are charged for two participants.

If Participant A is replicated to Stage B, you now have three connected participants (Participant A,
Participant B, and the replica of Participant A). For the duration of the replication, you are charged for
three participants.

More information is on the IVS Pricing page.
