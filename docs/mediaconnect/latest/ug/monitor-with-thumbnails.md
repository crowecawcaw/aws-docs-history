# Viewing thumbnails of the source video

AWS Elemental MediaConnect can generate JPEG-format thumbnails of the video that is in the source in any
type of flow except for CDI flows. The thumbnail provides a visual verification that the
content contains video. You can view the thumbnails on the console or retrieve them
programmatically.

## How thumbnails are generated

When you have enabled thumbnails in a flow and when the flow is active, MediaConnect
generates a JPEG thumbnail with a 480 x 270 resolution.

The rate for generating the thumbnail is as follows:

- The fastest possible rate is one image every second.
- The rate might be slower, depending on the characteristics of the source
  video. For example, one image every 6 seconds.

## How thumbnails are displayed

As soon as the thumbnail is generated, MediaConnect displays it in the flow
**Details** page, in the **Preview**
section.

It also makes the thumbnail available as base 64 binary data. You can use an AWS API
to work with the binary data programmatically. MediaConnect encrypts thumbnails during
retrieval to the console Preview window or in transit for API responses.

The retrieval rate for thumbnails is as follows:

- The refresh rate for the MediaConnect console is every 2 seconds. If the rate is
  faster than the generation rate, the same thumbnail is displayed more than once
  on the console.
- The API retrieve rate is constrained by the [maximum
  TPS](quotas.md#limits-api "quotas.md#limits-api"). This constraint only matters if you are trying to retrieve
  thumbnails for multiple flows.

If you are retrieving thumbnails for only one flow, there is no point
retrieving the thumbnail more often than every second (the fastest possible
generation rate).

###### Topic

- [Requirements for thumbnails](thumbnails-specifications.md "thumbnails-specifications.md")
- [Limit on thumbnails in MediaConnect](#thumbnails-api-limits "#thumbnails-api-limits")
- [Enabling and viewing thumbnails in the
  console](thumbnails-enable-view-console.md "thumbnails-enable-view-console.md")
- [Enabling and retrieving
  thumbnails programmatically](thumbnails-enable-retrieve-programatically.md "thumbnails-enable-retrieve-programatically.md")

## Limit on thumbnails in MediaConnect

There is a limit to the number of thumbnails that you can view or retrieve. This limit
is the TPS (transactions per second). The thumbnails feature shares the global limits
for MediaConnect. For more details, see [Limits for API requests](quotas.md#limits-api "quotas.md#limits-api").
