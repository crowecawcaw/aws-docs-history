AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Calibrating a large transfer with Snowball Edge

You can calibrate the transfer performance by transferring a representative set of your data partitions. Choose multiple partitions that you have defined and transfer them to a Snowball Edge device. Make a record of the transfer speed and total
transfer time for each operation. If the calibration's results are less than the target
transfer rate, you may be able to copy multiple parts of your data transfer at the same
time. In this case, repeat the calibration with the additional partitions of your data set.

Continue adding parallel copy operations during calibration until you see diminishing
returns in the sum of the transfer speed of all instances currently transferring data.
End the last active instance and make a note of your new target transfer rate.

You can transfer data faster to Snowball Edge by transferring data in parallel
using one of the following scenarios:

- Using multiple sessions of the S3 adapter on a workstation against a single
  Snowball Edge device.
- Using multiple sessions of the S3 adapter on multiple workstations against a
  single Snowball Edge device.
- Using multiple sessions of the S3 interface (using a single or multiple
  workstations) targeting multiple Snowball Edge.
  When you complete these steps, you should know how quickly you can transfer data to a Snowball Edge device.
