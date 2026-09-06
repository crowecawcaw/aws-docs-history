

# Usage type format
<a name="billing-usage-type-format"></a>

MediaLive usage types follow a general naming convention that encodes the channel configuration, region, and processing details into a single string.

The general format is:

```
{Tier}-{Region}-{Direction/Category}-{Codec}-{Resolution}-{Level/Framerate}-{Quality}-{Reservation}
```

Not all components appear in every usage type. The format varies by category. For example, input usage types include a bitrate level but not a framerate, while output usage types include a framerate but not a bitrate level.