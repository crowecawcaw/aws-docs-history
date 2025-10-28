# Assessing performance with logging messages

Elemental Live continually writes to log files to capture status
information about the health of each event.

When there are encoding problems, the first recourse of Elemental Live is to automatically
lower the output quality. The next recourse is to drop or repeat frames. Elemental Live never
chooses to slow down output, because then it would not be running in real time.

## Viewing relevant logging

messages

You can parse the log files for information that is useful for
identifying density, speed, or quality issues.

For example, the following command pulls specific log messages:

```
grep -irE "SyncRepeat|low quality|dropped| C " /opt/elemental_se/web/log/10000/
```

This command performs a case insensitive (-i), recursive (-r) search
for extended regular expressions (-E). The messages it finds are those in
the following table. The command searches in the specified path on the
appliance. Note that `10000` is the name of the folder where logs are
stored.

## Messages and their

meaning

The following table lists the Elemental Live messages that relate to
performance, and identifies possible causes of the message.

| Message         | Meaning                                                                                                                                               | Possible performance issue                                                                                                                                                                                                                                                                                                                                         |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Low quality** | The encoder is automatically lowering quality of encoding in an attempt to keep up with the speed at which frames are being delivered to the encoder. | CPU: Not enough available CPU power                                                                                                                                                                                                                                                                                                                                |
| **Dropped**     | The encoder is dropping frames, which typically indicates that Elemental Live can't keep up with the rate at which it is receiving frames to encode.  | CPU: Not enough available CPU power                                                                                                                                                                                                                                                                                                                                |
| **SyncRepeat**  | The encoder is repeating frames.                                                                                                                      | CPU: Not enough CPU power to encode the current frame. The current video might be very complex. Or the CPU usage might generally be at its maximum. I/O: Not enough available I/O bandwidth Network: Elemental Live can't ingest the input. Perhaps there are network issues. One way that Elemental Live recovers from an input failure is through repeat frames. |
| **C**           | A **C** beside a message identifies a critical error.                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                    | ## Dealing with issues The solution to dropped or repeated frames is typically to decrease density on the appliance. You might also fine tune the video quality. See [Encoding parameters that affect performance](performance-encoding-params.md "performance-encoding-params.md"). |
