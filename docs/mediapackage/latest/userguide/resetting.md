# Reset for AWS Elemental MediaPackage channels and endpoints

There might come a time in your content streaming workflow that you need to reset the
content that MediaPackage has ingested or is outputting.

###### Channel reset uses

For channels (ingest), a reset removes previously ingested content. When you reset the
channel, you must also stop the stream from the encoder. Thirty seconds after the
channel reset, start the stream from the encoder. With the old content removed from the
channel and the ingest stream restarted, you can clear out content that has issues.

Resetting a channel is especially useful when you receive `409` errors from
your encoder, which are often caused by encoder reconfigurations that change the numbering
logic of CMAF ingest segments. In cross-Region workflows, this logic change can cause
incompatibility between new segments and old because segment numbering starts to go
backward.

Channel reset is also useful when you switch between input sources with embedded time
codes, and input sources without.

###### Origin endpoint reset uses

For origin endpoints (output), a reset clears out previous content to refresh the
output stream. This can help remove content that causes unexpected behaviors, content
from a special event, and other situations when you don't want the previous content to
be available for viewing.

Resetting an endpoint is especially useful with event-based endpoints. If the specified
manifest length reaches beyond the current running time of the content, customers could view
content from previous events.

Endpoint reset is also useful when the previous content caused unexpected behaviors, like
what could happen if the stream has multiple stream set changes or interruptions in the
upstream content.

For steps to reset a channel or endpoint, see the following sections:

- [Resetting channel history](channel-reset.md "channel-reset.md")
- [Resetting an endpoint](endpoint-reset.md "endpoint-reset.md")
