# Stream selection fields

Limit what incoming bitrates are available for playback and sort the streams
in the output of an asset that uses this packaging configuration.

The minimum and maximum values take into account only the video bitrates. If
the video bitrate is _below the minimum_
specified rate, it's _not_ included in the
output, regardless of the sum of the bitrates for other tracks. Likewise, if the
video bitrate is _below the maximum_ specified
rate, it _is_ included in the output,
regardless of the sum of the bitrates for other tracks.

To set minimum and maximum bitrates and sort the output, select
**Enable stream selection** and complete the additional
fields as follows:

1. (Optional) For **Stream order**, choose from the
   following:
   - **Original** to sort the output streams in
     the same order that the incoming source uses.
   - **Ascending** to sort the output streams
     starting with the lowest bitrate and ending with the
     highest.
   - **Descending** to sort the output streams
     starting with the highest bitrate and ending with the
     lowest.

2. (Optional) For **Min video bitrate**, enter the
   minimum bitrate threshold (in bits per second) that video tracks must
   must be at or above to be available for playback from this endpoint. This ensures that
   tracks are _at least_ a certain bitrate.
3. (Optional) For **Max video bitrate**, enter
   the maximum bitrate threshold (in bits per second) that video tracks
   must be at or below to be available for playback from this endpoint. This ensures
   that tracks are _no more than_ a certain bitrate.
