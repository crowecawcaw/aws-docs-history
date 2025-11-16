AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# How to identify a Snowball Edge

Use the `describe-device` command to find the device type, then look up the returned value of `DeviceType` in the table below to determine the configuration.

```

  snowballEdge describe-device

```

###### Example of `describe-device` output

```

  {
  "DeviceId" : "JID-206843500001-35-92-20-211-23-06-02-18-24",
  "UnlockStatus" : {
    "State" : "UNLOCKED"
  ...
  "DeviceType" : "V3_5C"
}

```

| `DeviceType` and Snowball Edge device configurations | `DeviceType` value                                          | Device configuration |
| ---------------------------------------------------- | ----------------------------------------------------------- | -------------------- |
| `V3_5C`                                              | Snowball Edge compute-optimized with AMD EPYC Gen2 and NVME |
| `V3_5S`                                              | Snowball Edge storage-optimized 210 TB                      |

For more information about Snowball Edge device configurations, see [AWS Snowball Edge device hardware information](device-differences.md "device-differences.md").
