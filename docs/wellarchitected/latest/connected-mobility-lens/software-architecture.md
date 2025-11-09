# Software and architecture

| CMSUS_4: Are you using efficient software designs and architectures to minimize<br>the average resources required per unit of work? |
| ----------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                     |

**CMSUS_BP4.1: Optimize areas of code that consume the most
resources**

Optimize the code that runs within different components of your architecture to
minimize resource usage while maximizing performance. For more details, see  [SUS03-BP03](../sustainability-pillar/sus_sus_software_a4.md "../sustainability-pillar/sus_sus_software_a4.md"), [SUS03-BP04](../sustainability-pillar/sus_sus_software_a5.md "../sustainability-pillar/sus_sus_software_a5.md") in the _Sustainability Pillar
whitepaper_.

**Prescriptive guidance:**

- Make software running at edge devices as efficient as possible. Run performance
  tests with managed device farms for testing to identify bottlenecks in advance. It might
  not be easy to upgrade hardware resources at the edge.

| CMSUS_5: Are you selecting technologies to minimize data transfer, processing,<br>and storage requirements? |
| ----------------------------------------------------------------------------------------------------------- |
|                                                                                                             |

**CMSUS_BP5.1: Use software patterns and architectures that best
support data access and storage patterns**

Understand how data is used within your workload, consumed by your users, transferred,
and stored. Use software patterns and architectures that best support data access and
storage to minimize the compute, networking, and storage resources required to support the
workload. For more details, see  [SUS03-BP05](../sustainability-pillar/sus_sus_software_a6.md "../sustainability-pillar/sus_sus_software_a6.md") in the _Sustainability Pillar
whitepaper_.

**Prescriptive guidance:**

- Connected mobility applications might be generating different types of data. Use
  software and architecture patterns that align best to your data characteristics and
  access patterns. For example, use [modern data
  architecture on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/modern-data-architecture/ "https://aws.amazon.com/big-data/datalakes-and-analytics/modern-data-architecture/") that allows you to use purpose-built services optimized
  for your unique use cases. These architecture patterns allow for efficient data
  processing and reduce the resource usage.

| CMSUS_6: What is the downstream impact on the devices with the design and<br>architecture? |
| ------------------------------------------------------------------------------------------ |
|                                                                                            |

**CMSUS_BP6.1: Optimize impact on devices and equipment**

Understand the devices and equipment used in your architecture and use strategies to
reduce their usage. This can minimize the overall environmental impact of your cloud
workload. For more details, see [SUS03-BP04](../sustainability-pillar/sus_sus_software_a5.md "../sustainability-pillar/sus_sus_software_a5.md") in the _Sustainability Pillar
whitepaper_.

**Prescriptive guidance:**

- Most of the automotive grade devices have a specific boot and runtime. Having the
  devices on for a long time (unnecessarily) or booting them from sleep state to run state
  has adverse effect on the device lifetime. Need for such reboots and wake-up signals are
  increasing due to use cases like Shared mobility and companion app driven controls. Best
  practice is to minimize these wake-up calls to get the status of the ECU instead define
  events that can only send Wake-up within the vehicle bus and send the logs (push instead
  of pull).
- Perform power studies to enable keeping long lived connections, while using the
  least amount of power.
- To wake up the device from deep-sleep (like the TCUs), use TCP/IP-based wake up
  instead of SMS message wake up through the mobile network.
- Encourage teams to implement Software Defined Vehicle Architectures with
  Virtualized Hardware development. With this, customers can benefit from unwanted
  hardware sample manufacturing and decrease carbon footprint.
