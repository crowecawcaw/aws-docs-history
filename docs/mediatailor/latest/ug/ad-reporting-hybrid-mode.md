# Hybrid mode with server-side ad beacons

MediaTailor supports a hybrid mode for session tracking. In this mode, the service emits
playback-related ad-tracking events, but makes the complete client-side tracking payload
available for the session

To enable hybrid tracking using playback prefixes, from the player
initialize a new MediaTailor playback session using a request in one of the
following formats, according to your protocol:

###### Example : HLS format

```
POST master.m3u8
    {
        "adsParams": {
           "deviceType": "ipad"
       },
       "reportingMode":"server"
    }
```

###### Example : DASH format

```
POST manifest.mpd
    {
        "adsParams": {
           "deviceType": "ipad"
       },
       "reportingMode":"server"
    }
```

MediaTailor maintains the following tracking events in hybrid mode:

- Impression
- Start
- First quartile
- Midpoint
- Third quartile
- Complete
- `breakStart` (vmap)
- `breakEnd` (vmap)
