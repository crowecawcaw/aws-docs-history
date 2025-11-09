# What is Amazon IVS Real-Time Streaming?

Amazon Interactive Video Service (IVS) Real-Time Streaming gives you everything you need to add real-time audio and video to your applications.

Strengths:

- Real-time latency — Build applications for latency-sensitive use cases, helping your viewers stay connected and engaged with IVS real-time
  streaming. Deliver live streams with a latency that can be under 300 milliseconds from host to viewer.
- High concurrency — Unlock the potential of large-scale interactions with IVS real-time
  streaming. Accommodate audiences beyond 25,000 viewers and enable up to 12 hosts to take the
  virtual stage. (For default limits and instructions on requesting an increase, see _Service Quotas_ for [real-time streaming](service-quotas.md "service-quotas.md") and [low-latency
  streaming](../LowLatencyUserGuide/service-quotas.md "../LowLatencyUserGuide/service-quotas.md").)
- Mobile optimized — IVS real-time streaming is optimized for mobile use cases, catering to a diverse range of devices and network capabilities.
  By integrating the Amazon IVS broadcast SDKs for Android and iOS, your users can engage as hosts or viewers, enjoying high-quality live streams on their mobile devices.
  Use cases:

- Guest spots — Create applications that allow hosts to promote guests "on stage," turning viewers into hosts for real-time interactions.
- Versus (VS) mode — Produce experiences with side-by-side competitions and let viewers watch hosts compete in real-time.
- Audio rooms — Invite listeners to join the conversation as guests and foster deeper engagement in your audio rooms.
- Live video auctions — Turn auctions into interactive video events and maintain their excitement and integrity with real-time latency.
  In addition to the product documentation here, see [https://ivs.rocks/](https://ivs.rocks/ "https://ivs.rocks/"), a dedicated site to browse published content (demos, code samples,
  blog posts), estimate cost, and experience Amazon IVS through live demos.

## Global Solution, Regional Control

### Streaming and Viewing are Global

You can use Amazon IVS to stream to viewers worldwide:

- When you stream, Amazon IVS automatically ingests video at a location near you.
- Viewers can watch your live streams globally.

Another way of saying this is that the "data plane" is global. The data plane refers to
streaming/ingesting and viewing.

### Control is Regional

While the Amazon IVS data plane is global, the "control plane" is regional. The control
plane refers to the Amazon IVS console, API, and resources (stages).

Another way of saying this is that Amazon IVS is a "regional AWS service." That is, Amazon
IVS resources in each region are independent of similar resources in other regions. For example,
a stage that you create in one region is independent of stages you create in other regions.

When you use resources (e.g., create a stage), you must specify the region in which it
will be created. Subsequently, when you manage resources, you must do so from the same region
where they were created.

| If you use the ... | You specify the region by ...                                                                                                                                                                                                                                                                                                                                               |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon IVS console | Using the \*_Select a Region_<br>• drop-down in the top right<br>of the navigation bar.                                                                                                                                                                                                                                                                                     |
| Amazon IVS API     | Using the appropriate service endpoint. See the [Amazon IVS Real-Time Streaming API Reference](../RealTimeAPIReference/Welcome.md "../RealTimeAPIReference/Welcome.md").<br>(If you access the API through an SDK, set up the SDK’s `region` parameter.<br>See [Tools to Build on AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").) |
| AWS CLI            | Either:<br>• Appending `--region <aws-region>` to your CLI command.<br>• Putting the region in your local AWS configuration file.                                                                                                                                                                                                                                           |

_Remember, regardless of the region in which a stage was created,
you can stream to Amazon IVS from anywhere, and viewers can watch from anywhere._
