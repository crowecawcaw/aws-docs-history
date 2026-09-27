

# MediaTailor server-guided ad insertion overview and implementation
<a name="server-guided"></a>

AWS Elemental MediaTailor server-guided ad insertion (SGAI) provides an alternative to server-side ad insertion by referencing ads as separate playlists rather than stitching them directly into media playlists. This approach improves performance through cacheable manifests and enables better scalability.

For information about how to use server-guided ad insertion with MediaTailor, choose the applicable topic from the following list.

## Enable in the playback configuration
<a name="enable-in-config"></a>

To let players use server-guided ad insertion, set the insertion mode on the playback configuration to allow player selection:
+ In the MediaTailor console, on the playback configuration, set **Insertion mode** to **Player select**.
+ In the `PutPlaybackConfiguration` API, AWS CLI, or AWS CloudFormation, set `InsertionMode` to `PLAYER_SELECT`.

With this setting, players can select either stitched or guided ad insertion when the session initializes. The other option, **Stitched only** (`STITCHED_ONLY`), is the default. It requires every session to use server-side (stitched) ad insertion. While the configuration is set to **Stitched only**, players can't use server-guided ad insertion, and a player that requests it fails to initialize the session. A player that connects to a **Player select** configuration but doesn't request a mode uses stitched insertion by default. For more information about insertion mode, see [Ad insertion mode](ad-behavior.md#ad-insertion-mode).

## Create a server-guided session
<a name="create-guided-session"></a>

When creating playback sessions, choose guided mode. The way to do this depends on whether your players use implicit or explicit sessions.

### Implicitly created server-guided sessions
<a name="create-implicit-guided-session"></a>

Append `aws.insertionMode=GUIDED` to the HLS multivariant playlist request. Example:

```
playback-endpoint/v1/master/hashed-account-id/origin-id/index.m3u8?aws.insertionMode=GUIDED
```

Where:
+ `playback-endpoint` is the unique playback endpoint that AWS Elemental MediaTailor generated when the configuration was created. 

  Example

  ```
  https://777788889999.mediatailor.us-east-1.amazonaws.com
  ```
+ `hashed-account-id` is your AWS account ID. 

  Example

  ```
  777788889999
  ```
+ `origin-id` is the name that you gave when creating the configuration. 

  Example

  ```
  myOrigin
  ```
+ `index.m3u8` or is the name of the manifest from the test stream plus its file extension. Define this so that you get a fully identified manifest when you append this to the video content source that you configured in [Step 4: Create a configuration](getting-started-ad-insertion.md#getting-started-add-mapping). 

Using the values from the preceding examples, the full URLs are the following.
+ Example:

  ```
  https://777788889999.mediatailor.us-east-1.amazonaws.com/v1/master/777788889999/myOrigin/index.m3u8?aws.insertionMode=GUIDED
  ```

### Explicitly created server-guided sessions
<a name="create-explicit-guided-session"></a>

Add `insertionMode=GUIDED` to JSON metadata the player sends in the HTTP `POST` to the MediaTailor configuration's session-initialization prefix endpoint.

The following example shows the structure of the JSON metadata:

```
{
  # other keys, e.g. "adsParams"
  "insertionMode": "GUIDED"       # this can be either GUIDED or STITCHED
}
```

With this initialization metadata, the playback session will use serer-guided ad insertion.