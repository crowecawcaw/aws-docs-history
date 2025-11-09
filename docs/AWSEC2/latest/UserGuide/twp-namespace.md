# Check Amazon EC2 instance support for torn write prevention

To confirm whether your instance and volume supports torn write prevention, and to view
the NVMe namespace vendor specific data that contains torn write prevention information, use
the following command.

```
`$` sudo nvme id-ns -v `device_name`
```

###### Note

The command returns the vendor-specific information in hex with ASCII interpretation.
You might need to build a tool, similar to `ebsnvme-id`, into your applications
that can read and parse the output.

For example, the following command returns the NVMe namespace vendor specific data that contains torn
write prevention information for `/dev/nvme1n1`.

```
`$` sudo nvme id-ns -v /dev/nvme1n1
```

If your instance and volume support torn write prevention, it returns the following AWS torn write prevention
information in the NVMe namespace vendor specific data.

###### Note

The bytes in the following table represent the offset in bytes from the beginning of the NVMe namespace
vendor specific data.

| Bytes     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0:31`    | The name of the device attachment mount point, for example `/dev/xvda`. You provide this<br>during volume attachment request and it can be used by the Amazon EC2 instance to create a symlink to the NVMe<br>block device(`nvmeXn1`).                                                                                                                                                                                                                                                                                           |
| `32:63`   | The volume ID. For example, `vol01234567890abcdef`. This field can be used to map the NVMe<br>device to the attached volume.                                                                                                                                                                                                                                                                                                                                                                                                     |
| `64:255`  | Reserved for future use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `256:257` | Namespace Torn Write Prevention Unit size (NTWPU). This field indicates the namespace specific size<br>of the write operation guaranteed to be written atomically to the NVM during a power failure or error<br>condition. This field is specified in logical blocks represented in zero based values.                                                                                                                                                                                                                           |
| `258:259` | Namespace Torn Write Prevention Granularity size (NTWPG). This field indicates the namespace specific<br>size increments below `NTWPU` of the write operation guaranteed to be written atomically to the<br>NVM during a power failure or error condition. That is, size should be `NTWPG<br>• n <= NTWPU`<br>where `n` is positive integer. The write operation LBA offset also must be aligned to this field.<br>This field is specified in logical blocks represented in zero based values.                                   |
| `260:263` | Namespace Torn Write Prevention Boundary size (NTWPB). This field indicates the atomic boundary size<br>for this namespace for the `NTWPU` value. Writes to this namespace that cross atomic boundaries<br>are not guaranteed to be written atomically to the NVM during a power failure or error condition. A<br>value of `0h` indicates that there are no atomic boundaries for power fail or error conditions.<br>All other values specify a size in terms of logical blocks using the same encoding as the `NTWPU`<br>field. |
