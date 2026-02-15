# Enabling overlay ads

MediaTailor support for overlay ads is enabled by default. A specific SCTE-35 ad-marker type
in the manifest triggers the insertion of an overlay ad. Because some players might not
support client-side rendering of overlay ads, you can disable the feature at the session
level.

###### To disable overlay-ad support using HLS or DASH playback prefixes:

- From the player, initialize a new MediaTailor playback session using a request in
  one of the following formats, according to your protocol:
  - Example: HLS format

  ```
  GET `mediatailorURL`/v1/master/`hashed-account-id`/`origin-id`/`asset-id`?aws.overlayAvails=off
  ```

  - Example: DASH format

  ```
  GET `mediatailorURL`/v1/master/`hashed-account-id`/`origin-id`/`asset-id`?aws.overlayAvails=off
  ```

###### To disable overlay-ad support using the session-initialization prefix:

- On the player, construct a JSON message body for the session initialization
  request to MediaTailor:
  - To disable ad-overlay support, add an `overlays` object as
    a top-level key with a value of `off`. The default `overlays`
    value is `on`.
  - (Optional) Provide any parameters that MediaTailor then passes to the ADS
    inside an `adsParams` object. These parameters correspond to
    `[player_params.param]` settings in the ADS template URL of the MediaTailor
    configuration.

###### Example: HLS

```
POST master.m3u8
    {
       "adsParams": {
           "deviceType": "ipad"
       },
       "overlayAvails": "off"
    }

```

###### Example: DASH

```
POST manifest.mpd
    {
        "adsParams": {
           "deviceType": "androidmobile"
       },
       "overlayAvails": "off"
    }
```
