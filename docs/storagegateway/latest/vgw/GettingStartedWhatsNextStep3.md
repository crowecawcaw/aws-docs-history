# Where do I go from here?

In the preceding sections, you created and provisioned a gateway and then connected your
host to the gateway's storage volume. You added data to the gateway's iSCSI volume, took a
snapshot of the volume, and restored it to a new volume, connected to the new volume, and
verified that the data shows up on it.

After you finish the exercise, consider the following:

- If you plan on continuing to use your gateway, read about sizing the upload buffer
  more appropriately for real-world workloads. For more information, see [Sizing Your Volume Gateway's
  Storage for Real-World Workloads](#GettingStartedSizingForRealWorld "#GettingStartedSizingForRealWorld").
  Other sections of this guide include information about how to do the following:

- To learn more about storage volumes and how to manage them, see [Managing Your
  Volume Gateway](managing-gateway-common.md "managing-gateway-common.md").
- If you don't plan on continuing to use your gateway, consider deleting the gateway
  to avoid incurring any charges. For more information, see [Cleaning up unnecessary resources](best-practices.md#cleanup "best-practices.md#cleanup").
- To troubleshoot gateway problems, see [Troubleshooting your gateway](troubleshooting-gateway-issues.md "troubleshooting-gateway-issues.md").
- To optimize your gateway, see [Optimizing gateway performance](Performance.md#Optimizing-common "Performance.md#Optimizing-common").
- To learn about Storage Gateway metrics and how you can monitor how your gateway
  performs, see [Monitoring Storage Gateway](Main_monitoring-gateways-common.md "Main_monitoring-gateways-common.md").
- To learn more about configuring your gateway's iSCSI targets to store data, see
  [Connecting to your volumes from a Windows
  client](ConfiguringiSCSIClient.md "ConfiguringiSCSIClient.md").
  To learn about sizing your Volume Gateway's storage for real-world workloads and
  cleaning up resources you don't need, see the following sections.

## Sizing Your Volume Gateway's

Storage for Real-World Workloads

By this point, you have a simple, working gateway. However, the assumptions used to
create this gateway are not appropriate for real-world workloads. If you want to use
this gateway for real-world workloads, you need to do two things:

1. Size your upload buffer appropriately.
2. Set up monitoring for your upload buffer, if you haven't done so
   already.

Following, you can find how to do both of these tasks. If you activated a gateway for
cached volumes, you also need to size your cache storage for real-world
workloads.

###### To size your upload buffer and cache storage for a gateway-cached setup

- Use the formula shown in [Determining the size of
  upload buffer to allocate](decide-local-disks-and-sizes.md#CachedLocalDiskUploadBufferSizing-common "decide-local-disks-and-sizes.md#CachedLocalDiskUploadBufferSizing-common") for sizing the
  upload buffer. We strongly recommend that you allocate at least 150 GiB for the
  upload buffer. If the upload buffer formula yields a value less than 150 GiB,
  use 150 GiB as your allocated upload buffer.

The upload buffer formula takes into account the difference between throughput
from your application to your gateway and throughput from your gateway to AWS,
multiplied by how long you expect to write data. For example, assume that your
applications write text data to your gateway at a rate of 40 MB per second for
12 hours a day and your network throughput is 12 MB per second. Assuming a
compression factor of 2:1 for the text data, the formula specifies that you need
to allocate approximately 675 GiB of upload buffer space.

###### To size your upload buffer for a stored setup

- Use the formula discussed in [Determining the size of
  upload buffer to allocate](decide-local-disks-and-sizes.md#CachedLocalDiskUploadBufferSizing-common "decide-local-disks-and-sizes.md#CachedLocalDiskUploadBufferSizing-common"). We strongly
  recommend that you allocate at least 150 GiB for your upload buffer. If the
  upload buffer formula yields a value less than 150 GiB, use 150 GiB as your
  allocated upload buffer.

The upload buffer formula takes into account the difference between throughput
from your application to your gateway and throughput from your gateway to AWS,
multiplied by how long you expect to write data. For example, assume that your
applications write text data to your gateway at a rate of 40 MB per second for
12 hours a day and your network throughput is 12 MB per second. Assuming a
compression factor of 2:1 for the text data, the formula specifies that you need
to allocate approximately 675 GiB of upload buffer space.

###### To monitor your upload buffer

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose the **Gateway** tab, choose the
   **Details** tab, and then find the **Upload Buffer
   Used** field to view your gateway's current upload buffer.
3. Set one or more alarms to notify you about upload buffer use.

We highly recommend that you create one or more upload buffer alarms in the
Amazon CloudWatch console. For example, you can set an alarm for a level of use you want
to be warned about and an alarm for a level of use that, if exceeded, is cause
for action. The action might be adding more upload buffer space. For more
information, see [To set an upper threshold alarm for a
gateway's upload buffer](PerfUploadBuffer-common.md#GatewayAlarm1-common "PerfUploadBuffer-common.md#GatewayAlarm1-common").
