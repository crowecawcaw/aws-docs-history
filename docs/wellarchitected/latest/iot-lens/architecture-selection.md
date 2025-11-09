# Architecture selection

The optimal embedded software for a particular system varies based
on the hardware footprint of the device. For example, network
security protocols, while necessary for preserving data privacy
and integrity, can have a relatively large RAM footprint. For
intranet and internet connections, use TLS with a combination of a
strong cipher suite and minimal footprint.

| IOTPERF01: How do your architectural<br>decisions adapt to device hardware resources? |
| ------------------------------------------------------------------------------------- |
|                                                                                       |

AWS IoT supports elliptic curve cryptography (ECC) for devices connecting to AWS IoT using TLS. A secure software and hardware system on device should take precedence during the selection criteria for your devices. AWS also has a number of IoT partners that provide hardware solutions that can securely integrate to AWS IoT.

In addition to selecting the right hardware partner, you might choose to use a number of software components to run your application logic on the device, including FreeRTOS and AWS IoT Greengrass. You can orchestrate native OS processes on specific hardware to improve performance and you also can run containerized workloads for isolation.

Defining and analyzing key performance metrics for your IoT applications helps you understand the performance characteristics for your application. Logging and end-to-end application monitoring are key for measuring, evaluating, and optimizing the performance of your IoT applications.

## IOTPERF01-BP01 Optimize for device hardware resources utilization

When designing IoT solutions, it's crucial to consider the
limited hardware resources available on edge devices, such as
processing power, memory, and battery life. Optimizing resource
utilization can significantly improve performance, efficiency,
and overall device longevity. AWS offers several services and
tools to help architects and developers optimize their solutions
for device hardware constraints.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTPERF01-BP01-01**
_Apply efficient runtimes
and code language for embedded devices._

When making architectural decisions, thoroughly evaluate the
hardware capabilities of the target devices, and select
appropriate AWS services and configurations to optimize resource
utilization. This approach can lead to improved performance,
extended battery life, and cost savings by reducing cloud
processing and data transfer requirements. Some key tools to
consider in your device components are:

- **AWS IoT Device Client
  SDK**: Provides lightweight, optimized libraries
  for various programming languages. These libraries enable
  efficient communication with AWS IoT Core and other AWS
  services, minimizing resource consumption on edge devices.
  For optimal performance, select based on your device
  constraints, prioritizing lower-level languages for
  battery-powered or resource-limited deployments:
  - **Embedded C SDK**: Best
    for highly constrained devices with minimal RAM
    (256KB+). Offers lowest memory footprint and power
    consumption.
  - **C++ SDK**: Balances
    performance with developer productivity for embedded
    Linux applications and gateways.
  - **Python, JavaScript, or Java
    SDKs**: Choose only when device resources
    permit, as they trade performance for ease of
    development, in general.

- **FreeRTOS:** A real-time
  operating system for microcontrollers that is designed to be
  resource-efficient and highly configurable. It allows
  developers to tailor the OS to specific hardware
  requirements, reducing the overall footprint.
- For more complex scenarios, AWS IoT Greengrass is an open
  source edge runtime and cloud service that helps you build,
  deploy, and manage device software. It manages devices to
  act locally on the data they generate, run predictions based
  on machine learning models, filter and aggregate device
  data, and only transmit necessary information to the cloud.
  By processing data locally, AWS IoT Greengrass minimizes
  network latency and optimizes resource utilization,
  particularly for time-sensitive or bandwidth-constrained
  applications.

**Prescriptive guidance
IOTPERF01-BP01-02** _Leverage edge gateways as hubs to bridge
communications with the cloud._

Edge gateways act as intermediaries, aggregating data from
multiple devices, performing local processing and filtering, and
intelligently managing communication with the cloud. This
approach offloads workloads from the cloud and reduces network
traffic and latency. By implementing edge gateways with AWS IoT Greengrass, you can deploy AWS Lambda functions, machine
learning models, and other application components directly on
these gateways, enabling real-time processing and
decision-making at the edge. This architecture not only enhances
performance but also improves resilience by allowing continued
operation during intermittent cloud connectivity, maintaining
data integrity, and minimizing potential disruptions.

### Resources

- [AWS IoT Device SDKs, Mobile SDKs, and AWS IoT Device
  Client](../../../iot/latest/developerguide/iot-sdks.md "../../../iot/latest/developerguide/iot-sdks.md")
- [AWS IoT Greengrass GitHub](https://github.com/aws-greengrass "https://github.com/aws-greengrass")
- [FreeRTOS
  GitHub](https://github.com/FreeRTOS "https://github.com/FreeRTOS")
