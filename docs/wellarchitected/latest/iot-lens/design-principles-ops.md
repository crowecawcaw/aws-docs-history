# Design principles

In addition to the overall Well-Architected Framework operational
excellence design principles, there are five design principles for
operational excellence for IoT:

- **Plan for device
  provisioning**: Design your device provisioning
  process to create your initial device identity in a secure
  location. Implement a public key infrastructure (PKI) that is
  responsible for distributing unique certificates to IoT
  devices. As described above, selection of crypto hardware with
  a pre-generated private key and certificate alleviates the
  operational cost of running a PKI. Otherwise, PKI can be done
  offline with a Hardware Security Module (HSM) during the
  manufacturing process, or during device bootstrapping. Use
  technologies that can manage the Certificate Authority (CA)
  and HSM in the cloud.
- **Implement device
  bootstrapping**: The design must have ability to
  devices to programmatically update their configuration
  information using a globally distributed bootstrap API. A
  bootstrapping design makes sure that you can programmatically
  send the device new configuration settings through the cloud.
  These changes should include settings such as which IoT
  endpoint to communicate with, how frequently to send an
  overall status for the device, and updated security settings
  such as server certificates. The process of bootstrapping goes
  beyond initial provisioning and plays a critical role in
  device operations by providing a programmatic way to update
  device configuration through the cloud. A bootstrapping API
  and endpoint must be available for the entire defined life of
  all devices, and must be able to respond to requests for all
  versions of firmware that have ever been deployed on a device.
  Devices that support personalization by a technician in the
  industrial domain or user in the consumer domain can also
  undergo provisioning. For example, a smartphone application
  that interacts with the device over Bluetooth LE and with the
  cloud over Wi-Fi.
- **Document device communication
  patterns**: An operations team must formulate how the
  behavior of a device will scale once deployed to a fleet of
  devices. A cloud engineer should review the device
  communication patterns and extrapolate the total expected
  inbound and outbound traffic of device data and determine the
  expected infrastructure necessary in the cloud to support the
  entire fleet of devices. During operational planning, these
  patterns should be measured using device and cloud-side
  metrics to make sure that expected usage patterns are met in
  the system.
- **Implement over the air (OTA)
  updates**: In order to benefit from long-term
  investments in hardware, you must be able to continuously
  update the firmware on the devices with new capabilities. In
  the cloud, you can apply a firmware update process that allows
  you to target specific devices for firmware updates, roll out
  changes over time, track success and failures of updates, and
  have the ability to roll back or put a stop to firmware
  changes based on key performance indicators (KPIs).
- **Implement functional testing on
  physical assets**: IoT device hardware and firmware
  must undergo rigorous testing before being deployed in the
  field. The tests make sure that your IoT device will perform
  as expected when deployed. Acceptance and functional testing
  are critical on the path to production. The goal of functional
  testing is to run your hardware components, embedded firmware,
  and device application software through rigorous testing
  scenarios, such as intermittent or reduced connectivity or
  failure of peripheral sensors, while profiling the performance
  of the hardware.
- **Design and build for operations at
  scale**: Design and build a solution for logging,
  monitoring, troubleshooting, fleet management, life cycle
  device and application management at scale. The amount of data
  ingested from connected devices with low latency and high
  throughput rate should scale and not impact the application.
  For example, the data plane operations should seamlessly
  operate when the fleet grows.
