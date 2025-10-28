# Design principles

The Well-Architected Framework identifies the following set of
design principles in order to facilitate good design in the cloud
with IoT:

- **Decouple ingestion from
  processing**: In IoT applications, the ingestion layer
  must be a highly scalable system that can handle a high rate of
  streaming device data. By decoupling the fast rate of ingestion
  from the processing portion of your application through the use
  of queues, buffers, and messaging services, your IoT application
  can scale elastically as needed and make several decisions
  without impacting devices, such as the frequency it processes
  data or the type of data it is interested in.
- **Design for offline behavior**:
  Due to things like connectivity issues or misconfigured
  settings, devices may go offline for longer periods of time than
  anticipated. Design your edge software to handle extended
  periods of offline connectivity and create metrics in the cloud
  to track devices that are not connected or communicating on a
  regular timeframe.
- **Design for lean data at the edge and
  enrich in the cloud**: Given the constrained nature of
  IoT devices, the initial device schema will be optimized for
  storage on the physical device and efficient transmissions from
  the device to your IoT application. For this reason, unformatted
  device data will often not be enriched with static application
  information that can be inferred from the cloud. As data is
  ingested into your application, you should first enrich the data
  with human readable attributes, deserialize, or expand any
  fields that the device serialized, and then format the data in a
  data store that is tuned to support your applications read
  requirements.
- **Handle personalization**:
  Devices that connect to the edge or cloud through Wi-Fi must
  receive the SSID name and credentials as one of the first steps
  performed when setting up the device. This data is usually
  infeasible to write to the device during manufacturing since it
  is sensitive and site-specific or from the cloud since the
  device is not connected yet. These factors frequently make
  personalization data distinct from the device client certificate
  and private key, which are conceptually upstream, and from
  cloud-provided firmware and configuration updates, which are
  conceptually downstream. Supporting personalization can impact
  design and manufacturing, since it may mean that the device
  itself requires a user interface for direct data input, or the
  need to provide a smartphone application to connect the device
  to the local network.
- **Make sure that devices regularly send
  status checks**: Even if devices are regularly offline
  for extended periods of time, make sure that the device firmware
  contains application logic that sets a regular interval to send
  device status information to your IoT application. Devices must
  be active participants in making sure that your application has
  the right level of visibility. Sending this regularly occurring
  IoT message make sures that your IoT application gets an updated
  view of the overall status of a device, and can create processes
  when a device does not communicate within its expected period of
  time.
- **Use Gateways for edge computing, network
  segmentation, security compliance and bridging administrative
  domains:** By splitting the workload between local and
  remote processing helps to balance the timeliness and high
  bandwidth of local resources with the scale and elasticity of
  remote resources. Edge gateways can be used to mediate data
  flows between a low latency local-area network (LAN) and
  resources on the high-latency wide-area network (WAN), protocols
  used in each environment and can also mediate between security
  and administrative domains such as in a Perdue Enterprise
  Network Architecture (PERA), ANSI/ISA-95 network segmentation.
  Edge gateways are also used in consumer IoT systems. For
  example, a smart home gateway which collects data from multiple
  smart home devices.
- **Build security into your IoT solution
  and apply security at all layers:** IoT implementations
  can have some unique considerations not present in traditional
  IT deployments. For example, deploying a consumer IoT device can
  introduce a new classification of threats that needs to be
  addressed and industrial IoT requires more thought around
  reliability, safety and compliance. Many legacy OT systems have
  limited security features and use industrial protocols which
  does not support authentication, authorization and encryption.
  In industrial IoT, the convergence of IT and OT systems is
  creating a mix of technologies that were designed to withstand
  risky network environments and ones that were not, which creates
  risk management difficulties that need to be controlled. So,
  building security into every part of your IoT solution is
  essential for minimizing risks to your data, business assets,
  and reputation. Apply a defense in-depth approach with multiple
  security controls.
