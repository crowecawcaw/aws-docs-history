

# Switching modes in MediaConnect

When a router output takes a new router input, its switching mode determines when the output switches to the new content. You choose a switching mode for each router output.


| Switching mode | Description | 
| --- | --- | 
| Immediate | The router output switches to the new router input immediately. Your downstream decoder might briefly show artifacts while it recovers. | 
| Key frame | The router output waits for a key frame on the new router input before it switches. Your downstream decoder can start decoding the new content at the switch point. | 

## How key frame switching works
<a name="switching-modes-how-it-works"></a>

When a router output that uses key frame switching takes a new router input, MediaConnect does the following at the switch point:
+ Waits for a key frame on the new router input, up to the key frame wait time.
+ Sends an updated program association table (PAT) and program map table (PMT), so that your downstream decoder detects the change.
+ Sets the discontinuity indicator on the first packet of each elementary stream. Decoders that read this indicator report fewer continuity count errors.

MediaConnect applies the same steps when the router output starts receiving content from a router input.

## Key frame wait
<a name="switching-modes-key-frame-wait"></a>

The key frame wait is the maximum time, in milliseconds, that the router output waits for a key frame on the new router input before it switches. You can set a value from 0 to 10,000. The default is 3,000.

Set the key frame wait to at least the Group of Pictures (GOP) duration of your content, which your upstream encoder determines. If the wait time is shorter than the GOP duration, MediaConnect makes a best effort to switch without a key frame.

If you set the key frame wait to 0, the router output switches without waiting for a key frame. MediaConnect still sends the updated PAT and PMT and sets the discontinuity indicators.

## Supported content
<a name="switching-modes-supported-content"></a>

Key frame switching waits for a key frame in single-program transport streams that carry MPEG-2, H.264, or H.265 video. For other content, MediaConnect switches without waiting for a key frame.

Router outputs that use RTMP Push always wait for a key frame when they switch to a new router input.

## Alerts
<a name="switching-modes-alerts"></a>

When MediaConnect can't switch on a key frame, it switches anyway and shows an alert on the router output.


| Alert | Case | What MediaConnect does | 
| --- | --- | --- | 
| Key Frame Switching Unsupported Video | The content has more than one program, has no video, or uses a video codec other than MPEG-2, H.264, or H.265 | Switches without waiting for a key frame. Sends the updated PAT and PMT and sets the discontinuity indicators. | 
| Key Frame Switching Seek Timeout | The content has no PAT or PMT within 1 second of the switch point | Switches immediately. | 
| Key Frame Switching Seek Timeout | No key frame arrives within the key frame wait | Switches, sends the updated PAT and PMT, and sets the discontinuity indicators. Your downstream decoder waits for the next key frame. | 

To resolve the *Key Frame Switching Seek Timeout* alert, check that your upstream encoder sends key frames, or increase the key frame wait.