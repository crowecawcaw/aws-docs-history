# Choose storage that supports device longevity

There are several low-power memory storage options that are
suitable for IoT devices due to their energy-efficient
characteristics. When choosing storage, the use case and
workload dictates much of the decision. For example, for a
device that is deployed to a harsh environment that is not easy
to access, choose storage that is durable and resilient.  Also
consider the wear and tear on flash memory due to the workload,
and its impact on device longevity.  Provision the amount of
storage beyond current requirements for the application to allow
for additional use cases in the future, thereby extending the
device's useful life. In summary, the appropriate type and
amount of storage for the device application should be carefully
chosen as it can have an impact on the operational phase of the
device as well as the overall cost.

File system choices can impact processor and memory requirements
for the device, in turn impacting the power draw and ultimately
sustainability. Choosing a lightweight file system such as
[littleFS](https://github.com/littlefs-project/littlefs/blob/master/DESIGN.md "https://github.com/littlefs-project/littlefs/blob/master/DESIGN.md")
or
[Reliance
Edge](https://www.tuxera.com/products/reliance-edge/ "https://www.tuxera.com/products/reliance-edge/") for embedded systems can help reduce power
consumption and increase the life-time of the storage through
features such as wear leveling, power-efficient file updates,
power-safe operations, small footprint, and customizable
configuration options.

For IoT use cases that demand higher power edge gateways,
various disk drives or solid-state drives may also be used.
Using techniques like RAID, though more power intensive, can
improve the performance and resiliency of gateways or servers
and in turn improve the overall sustainability of the system by
reducing the need for truck rolls.

A key consideration for storage selection is to support dual
partitioning of persistent storage for Over the Air Update (OTA)
capability.  In addition, the flash subsystem must be capable of
independent erase and write operations for each partition (or
image block).

When deciding on storage options for a use case, satisfying just
the requirements of the application will not always be the most
sustainable practice. Think about the performance of the storage
over the life of the device, whether the device has enough
storage to support buffering/analysis of data to alleviate the
need to transmit, and if the storage supports extensibility and
longevity of devices to reduce the operational impact and carbon
footprint of upgrades and replacements.
