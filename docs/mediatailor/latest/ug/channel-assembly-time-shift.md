# Time-shifting a channel's playback

With MediaTailor channel assembly, you can time-shift a channel's playback. Time-shifting allows
viewers to watch a channel's content at a time other than the original broadcast time. For
example, a viewer can start watching a program from the beginning, even if they join the
broadcast after it has started. Or, a viewer can pause a program and resume watching it
later.

To time-shift a channel's playback, you add a `start` parameter to the channel's
playback URL. The `start` parameter specifies the time when playback should begin,
relative to the current time. For example, if the current time is 2:00 PM, and you want to start
playback from 1:00 PM, you would set the `start` parameter to `-3600`,
which is -1 hour in seconds.

The `start` parameter accepts both positive and negative values, in seconds:

- Negative values indicate a time in the past, relative to the current time. For example,
  `start=-3600` means "start playback from 1 hour ago."
- Positive values indicate a time in the future, relative to the current time. For
  example, `start=3600` means "start playback from 1 hour in the future."
  The following example shows how to add the `start` parameter to a channel's
  playback URL:

```
https://a1b2c3d4e5f6.mediapackage.us-west-2.amazonaws.com/out/v1/examplechannel/index.m3u8?start=-3600
```

In this example, playback starts from 1 hour ago.

The `start` parameter is subject to the following limitations:

- The maximum time-shift window is 24 hours in the past or future.
- Time-shifting is only available for channels that use the linear playback mode.
- Time-shifting is not available for channels that use the loop playback mode.
  If you specify a `start` parameter that is outside the available time-shift
  window, MediaTailor returns an error.
