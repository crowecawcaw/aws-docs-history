# Interleave 4K inputs

AWS Elemental Live supports 4K uncompressed sources that are formatted
as 2SI (2 Sample Interleave).

To configure an event for this input, do the following:

1. Make sure that the source is formatted as 2SI.
2. In the **Input** section of the event, set the
   **Select Type** field to **Interleave 4K
   (HD-2SI)**.
   The **Interleave 4K (HD-2SI)** setting is applied to
   fours ports on the appliance: ports 1-4, or ports 5-8, or ports 9-12, or
   ports 13-16.

When you start the event, the **Media Info** in the
output will report the input as either 2SI or SDI.

###### Note

If you choose the **Interleave 4K** input type, you
must make sure that the source is formatted as 2SI, not as Quadrant. If
you mismatch the source format and the input type, Elemental Live will
ingest the source, but there will be readily observable video issues.
