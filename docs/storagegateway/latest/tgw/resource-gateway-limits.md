# AWS Storage Gateway quotas

In this topic, you can find information about volume and tape quotas, configuration, and
performance limits for Storage Gateway.

###### Topics

- [Quotas for tapes](#resource-tape-limits "#resource-tape-limits")
- [Recommended local disk sizes for your gateway](#disk-sizes "#disk-sizes")

## Quotas for tapes

The following table lists quotas for tapes.

| Description                                           | Tape Gateway |
| ----------------------------------------------------- | ------------ |
| Minimum size of a virtual tape                        | 100 GiB      |
| Maximum size of a virtual tape                        | 15 TiB       |
| Maximum number of virtual tapes assigned to a gateway | 1,500        |
| Total size of all tapes assigned to a gateway         | 1 PiB        |
| Maximum number of virtual tapes in archive            | No limit     |
| Total size of all tapes in archive                    | No limit     |

## Recommended local disk sizes for your gateway

| Gateway Type | Cache (Minimum) | Cache (Maximum) | Upload Buffer (Minimum) | Upload Buffer (Maximum) |
| ------------ | --------------- | --------------- | ----------------------- | ----------------------- |
| Tape gateway | 150 GiB         | 64 TiB          | 150 GiB                 | 2 TiB                   |

###### Note

You can configure one or more local drives for your cache and upload buffer, up to the maximum capacity.

When adding cache or upload buffer to an existing gateway, it's important to create new disks
in your host (hypervisor or Amazon EC2 instance). Don't change the size of existing disks if the disks have been previously allocated
as either a cache or upload buffer.
