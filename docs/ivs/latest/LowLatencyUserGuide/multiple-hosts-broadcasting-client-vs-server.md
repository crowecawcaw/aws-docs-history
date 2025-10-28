# Broadcasting a Stage:

Client-Side versus Server-Side Composition

When developers want to broadcast a stage to an IVS channel, they have two
choices:

- With _client-side composition_, a host
  connects to a stage, downloads videos from other hosts, combines them into one
  stream, and broadcasts the mixed stream to an IVS channel. This approach allows
  for a high degree of layout flexibility: the app developer can control the look
  of the composition using the mixer API. However, client-side composition
  requires more client CPU resources to create the composition and more bandwidth
  to broadcast it. Also, if the host broadcasting the stage has network issues,
  they may impact the live stream for viewers.

Client-side composition is the preferred choice when users need a highly
personalized view of the broadcast content, such as incorporating overlays and
customizing elements that aren't compatible with server-side composition.

- With _server-side composition_, clients
  offload the composition and broadcasting of an IVS stage to a cloud service.
  Server-side composition and RTMP broadcast to a channel are invoked through IVS
  control-plane operations in the stage’s home region. Server-side composition
  offers numerous benefits, making it an attractive choice for users seeking
  efficient and reliable live streaming.

      + **Reduced client load** — With
       server-side composition, the burden of combining audio and video sources
       is shifted from individual client devices to the server itself.
       Server-side composition eliminates the need for client devices to use
       their CPU and network resources for compositing the view and
       transmitting it to IVS.
      + **Resilience** — By centralizing the
       composition process on the server, the broadcast becomes more robust.
       Even if a publisher device experiences technical limitations or network
       fluctuations, the server can adapt and provide a smoother stream to all
       the audience.
      + **Bandwidth efficiency** — Since the
       server handles the composition, stage publishers do not have to spend
       extra bandwidth broadcasting the video to an IVS channel.

  For more information, see [Server-Side
  Composition](../RealTimeUserGuide/server-side-composition.md "../RealTimeUserGuide/server-side-composition.md") in the _IVS Real-Time User
  Guide_.
