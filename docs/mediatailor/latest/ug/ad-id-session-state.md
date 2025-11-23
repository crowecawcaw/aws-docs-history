# Enabling ad ID signaling for sessions

The ad ID signaling feature must be enabled during session initialization. The process
to enable the feature differs from creating sessions using the HLS/DASH playback prefix
(implicit session initialization), versus the session initialization prefix (explicit
session initialization).

###### To enable ad ID for the session using HLS/DASH playback prefixes

- From the player, initialize a new MediaTailor playback session using a request in
  one of the following formats, according to your protocol:
  - Example: HLS format

  ```
  GET `<mediatailorURL>`/v1/master/`<hashed-account-id>`/`<origin-id>`/`<asset-id>`?aws.adSignalingEnabled=true
  ```

  - Example: DASH format

  ```
  GET `<mediatailorURL>`/v1/dash/`<hashed-account-id>`/`<origin-id>`/`<asset-id>`?aws.adSignalingEnabled=true
  ```

###### To enable ad ID for the session using the session initialization prefix

- On the player, construct a JSON message body for the session initialization
  request to MediaTailor:
  - Inside an `adsParams` object, provide any parameters that
    MediaTailor should pass to the ADS. These parameters correspond to
    `[player_params.param]` settings in the ADS template URL
    of the MediaTailor configuration.
  - To enable ad ID signaling, add an `adSignaling` object as a
    top level object, and inside, add a parameter called
    `enabled` and value of `true`. The default
    `adSignaling` value is `disabled`.

  - Example: HLS format

  ```
  POST master.m3u8
      {
         "adsParams": {
             "deviceType": "ipad"
         },
         "adSignaling": {
             "enabled": "true"
         },
         "reportingMode": "client"
      }
  ```

  - Example: DASH format

  ```
  POST manifest.mpd
      {
          "adsParams": {
             "deviceType": "ipad"
         },
         "adSignaling": {
              "enabled": "true"
          },
          "reportingMode": "client"
      }
  ```
