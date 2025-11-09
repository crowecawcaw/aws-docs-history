# EBS volume metrics

Compute Optimizer analyzes the following CloudWatch metrics of your EBS volumes.

| Metric             | Description                                        |
| ------------------ | -------------------------------------------------- |
| `VolumeReadBytes`  | The read bytes per second of the EBS volume.       |
| `VolumeWriteBytes` | The write bytes per second of the EBS volume.      |
| `VolumeReadOps`    | The read operations per second of the EBS volume.  |
| `VolumeWriteOps`   | The write operations per second of the EBS volume. |

For more information about these metrics, see [Amazon CloudWatch metrics for Amazon EBS](../../../AWSEC2/latest/UserGuide/using_cloudwatch_ebs.md "../../../AWSEC2/latest/UserGuide/using_cloudwatch_ebs.md") in the
_Amazon Elastic Compute Cloud User Guide_.
