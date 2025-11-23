# MediaTailor server-guided ad insertion overview and

implementation

AWS Elemental MediaTailor server-guided ad insertion (SGAI) provides an alternative to server-side ad
insertion by referencing ads as separate playlists rather than stitching them directly into
media playlists. This approach improves performance through cacheable manifests and enables
better scalability.

For information about how to use server-guided ad insertion with MediaTailor, choose the
applicable topic from the following list.

## Enable in the playback configuration

In order to allow players to use server-guided ad insertion, you must set
`Insertion Mode` to `PLAYER_SELECT` in the MediaTailor
playback configuration. This allows players to select either stitched or guided ad
insertion at session-initialization time.

## Create a server-guided session

When creating playback sessions, choose guided mode. The way to do this depends on
whether your players use implicit or explicit sessions.

### Implicitly created server-guided

sessions

Append `aws.insertionMode=GUIDED` to the HLS multivariant playlist
request. Example:

```
playback-endpoint/v1/master/hashed-account-id/origin-id/index.m3u8?aws.insertionMode=GUIDED
```

Where:

- `playback-endpoint` is the unique playback endpoint that
  AWS Elemental MediaTailor generated when the configuration was created.

Example

```
https://777788889999.mediatailor.us-east-1.amazonaws.com
```

- `hashed-account-id` is your AWS account ID.

Example

```
777788889999
```

- `origin-id` is the name that you gave when creating the
  configuration.

Example

```
myOrigin
```

- `index.m3u8` or is the name of the manifest from the test
  stream plus its file extension. Define this so that you get a fully
  identified manifest when you append this to the video content source that
  you configured in [Step 4: Create a configuration](getting-started-ad-insertion.md#getting-started-add-mapping "getting-started-ad-insertion.md#getting-started-add-mapping").

Using the values from the preceding examples, the full URLs are the
following.

- Example:

```
https://777788889999.mediatailor.us-east-1.amazonaws.com/v1/master/777788889999/myOrigin/index.m3u8?aws.insertionMode=GUIDED
```

### Explicitly created server-guided

sessions

Add `insertionMode=GUIDED` to JSON metadata the player sends in the
HTTP `POST` to the MediaTailor configuration's session-initialization prefix
endpoint.

The following example shows the structure of the JSON metadata:

```
{
  # other keys, e.g. "adsParams"
  "insertionMode": "GUIDED"       # this can be either GUIDED or STITCHED
}
```

With this initialization metadata, the playback session will use serer-guided ad
insertion.
