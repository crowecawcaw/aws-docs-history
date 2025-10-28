# Enabling Multiple Hosts on an Amazon IVS Stream

Amazon Interactive Video Service (IVS) enables developers to build applications that combine video and audio from multiple broadcasters (also referred to as _hosts_) into one live stream.

Use cases include:

- Guest spots – Broadcasters can invite viewers into the broadcast. This opens the
  door to collaborative content like karaoke and Q&A.
- Versus (VS) mode – Broadcasters are matched with each other to compete (e.g., in a
  singing competition).
- Group broadcasts – Multiple speakers can converse with each other in front of a
  large audience.
  To add multiple broadcasters to a live stream, you need to use both IVS Real-Time Streaming and IVS Low-Latency Streaming. IVS Real-Time Streaming is used to combine video and audio streams; Low-Latency Streaming, to broadcast the combined stream to viewers.

Real-Time Streaming provides a resource called a stage, a virtual space where broadcasters (hosts) can exchange audio and video in real time. You can then broadcast a stage to channels to reach a larger audience, and you can build applications where audience members can be brought "on stage" to contribute to the live conversation.

For more information about IVS Real-Time Streaming, see:

- [IVS
  Real-Time Streaming User Guide](../RealTimeUserGuide/what-is.md "../RealTimeUserGuide/what-is.md")
  - The IVS Broadcast SDKs incorporate real-time functionality. See the Guides
    for those SDKs: [Web](../RealTimeUserGuide/broadcast-web.md "../RealTimeUserGuide/broadcast-web.md"),
    [Android](../RealTimeUserGuide/broadcast-android.md "../RealTimeUserGuide/broadcast-android.md"), and [iOS](../RealTimeUserGuide/broadcast-ios.md "../RealTimeUserGuide/broadcast-ios.md"),
    especially the sections on "Publishing and Subscribing."

- [IVS
  Real-Time Streaming API Reference](../RealTimeAPIReference/Welcome.md "../RealTimeAPIReference/Welcome.md")
