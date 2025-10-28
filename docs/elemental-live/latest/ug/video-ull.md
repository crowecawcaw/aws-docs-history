# Setting up for ultra-low latency

If you are sending output to an HTTP server or to AWS Elemental MediaStore, you can
produce ultra-low latency outputs if you create a DASH output and enable
chunked encoding and chunked transfer.

With chunked encoding and transfer Elemental Live delivers more quickly,
without any decrease in quality. When you enable chunked encoding and
transfer, Elemental Live divides the video into fragments, with several
fragments in each segment. Elemental Live delivers the fragments before the
entire segment is complete. Delivery of smaller chunks more frequently can
speed up handling by the downstream system, assuming that the downstream
system can handle the frequency.

From the Elemental Live side, this feature works with any downstream
system that can accept DASH. But you should always discuss your requirements
with the downstream system administrator, to make sure that they are prepared
to accept the output.

###### Setup

###### Note

The information in this section assumes that you are familiar with the
general steps for creating an event.

To produce an ultra-low latency DASH output, create a DASH output group
in the usual way, with these additions:

1. Enable **Chunked Encoding**.
2. Change **Fragment Length** and **Segment
   Length** if necessary. For information about these fields, choose the
   ? icon that appears when you hover over the field name.
3. In **HTTP Push Dialect**, choose the appropriate
   option. The **Chunked Transfer** field appears.
4. Enable **Chunked Transfer**.
