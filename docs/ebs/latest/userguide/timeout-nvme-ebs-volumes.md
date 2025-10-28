# NVMe I/O operation timeout for Amazon EBS volumes

Most operating systems specify a timeout for I/O operations submitted to NVMe devices.

###### Linux instances

On Linux, EBS volumes attached to Nitro-based instances use the default NVMe driver
provided by the operating system. Most operating systems specify a timeout for I/O
operations submitted to NVMe devices. The default timeout is 30 seconds and can be
changed using the `nvme_core.io_timeout` boot parameter. For most Linux
kernels earlier than version 4.6, this parameter is `nvme.io_timeout`.

If I/O latency exceeds the value of this timeout parameter, the Linux NVMe
driver fails the I/O and returns an error to the filesystem or application. Depending on
the I/O operation, your filesystem or application can retry the error. In some cases,
your filesystem might be remounted as read-only.

For an experience similar to EBS volumes attached to Xen instances, we
recommend setting `nvme_core.io_timeout` to the highest value possible. For
current kernels, the maximum is 4294967295, while for earlier kernels the maximum is 255. Depending on the version of Linux, the timeout might already be set to the
supported maximum value. For example, the timeout is set to 4294967295 by default for
Amazon Linux AMI 2017.09.01 and later.

You can verify the maximum value for your Linux distribution by writing a
value higher than the suggested maximum to
`/sys/module/nvme_core/parameters/io_timeout` and checking for the
**`Numerical result out of range`** error when attempting to save
the file.

###### Windows instances

On Windows, the default timeout is 60 seconds and the maximum is 255 seconds.
You can modify the `TimeoutValue` disk class registry setting
using the procedure described in [Registry Entries for SCSI Miniport Drivers](https://learn.microsoft.com/en-us/previous-versions/windows/drivers/storage/registry-entries-for-scsi-miniport-drivers "https://learn.microsoft.com/en-us/previous-versions/windows/drivers/storage/registry-entries-for-scsi-miniport-drivers").
