# Delay content availability from AWS Elemental MediaPackage

You can specify a duration (in seconds) for MediaPackage to delay when content is available to
players. The minimum time is 0 seconds. The following rules determine the maximum time:

- If `startoverwindow` is equal to `0`, the maximum time is 86,400 seconds (24 hours).
- If `startoverwindow` is not equal to `0`, the maximum time is the value of `startoverwindow`.
  Use `time_delay` to redefine the live point and make content available at a time
  that equals "now" minus the delay specified. With a 60-second `time_delay`,
  content that MediaPackage receives at 12:20 isn't available until 12:21. Requests for playback at 12:20
  will be served with content from 12:19. Likewise, if you're serving content across time zones,
  you can set a `time_delay` equal to the time zone difference to make content available
  at, for example, 8:00 local time.

The time delay duration must be less than the startover window duration.

###### Tip

Use a `time_delay` to help reduce buffering during input switching when
you're using input redundancy with short output segments. Note that the delay can increase
latency in content playback.

## Using clip start with time delay

When you use the time delay function in MediaPackage, content availability is delayed by the
specified amount. As content progresses, the manifest grows to your specified manifest
window (seconds). Until the manifest has reached that window size with new content, content
from before the start time can be available.

For example, one event ends at 925, and the other starts at 930. You set the time delay for the 930 event so that content is available at 932, and you defined your manifest window as 900 seconds (15 minutes). A viewer starts watching the event at 935, which is 3 minutes into the event. The manifest is 15 minutes long, so there is still another 12 minutes of content available from before the event started, so the viewer can see content from the event that ended at 925.

Depending on your contractual obligations, you might not want viewers to have access to the
earlier content. To mitigate these concerns, you can use the clip start functionality in
MediaPackage. With clip start, you can specify the earliest available content in the manifest. In
the previous example, you could set the clip start time to 930 to ensure that viewers can’t
see content from before the current event.

You can enable the clip start setting on this endpoint so that all manifests that originate from this endpoint will include the clipped time. For information about adding clip start to an endpoint, see [Creating an origin endpoint in AWS Elemental MediaPackage](endpoints-create.md "endpoints-create.md").

Alternatively, manifest requests that include the
`aws.manifestsettings=clip_start_time:` query parameter will be clipped so
that content from before the specified time is not available. Requests to this endpoint that
don’t include the query parameter will receive a standard manifest, as defined by the
endpoint’s settings. MediaPackage returns an error to the requesting device if the clip start is
set on the endpoint and included in request query parameters.

###### A note about start parameters

Clip start can’t be used with _start_ and _end_ parameters.

Clip start and start parameters offer similar functionality, but have different practical
purposes.

- Clip start is used to ensure that content before the set time is blocked. The
  manifest continues to grow, up to the defined window duration.
- Start is used to ensure that content before the set time is blocked. If used
  with an _end_ parameter, the returned manifest ends
  at the specified time. If not used with an _end_ parameter, the returned manifest continues to grow up to the value of the
  startover window.
