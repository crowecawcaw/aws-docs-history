# Enabling and Disabling Webcam Support

AppStream 2.0 supports real-time audio-video (AV) by redirecting local webcam video input to
AppStream 2.0 streaming sessions. This capability enables your users to use their local webcam
for video and audio conferencing within an AppStream 2.0 streaming session. With real-time AV
and support for real-time audio, your users can collaborate by using familiar video and
audio conferencing applications without having to leave their AppStream 2.0 streaming
session.

To use this feature, you must use a Linux AppStream 2.0 image that uses a Linux AppStream 2.0 agent
released on or after September 21, 2022.

###### Note

Real-time AV is not supported for stream.standard.small instances powered by Rocky
Linux or Red Hat Enterprise Linux. Users don't see the Camera and Mic icons on the
client toolbar.

The real-time AV feature is enabled by default for Linux streaming sessions. To
configure webcam permissions for your users on a Linux image builder, create
`/etc/appstream/appstream.conf` and add the following
contents:

###### Note

Specify `1` to enable webcam, or `0` to
disable webcam.

```
[webcam]
permission = 1
```
