# Insufficient DB instances available

The `InsufficientDBInstanceCapacity` error can be returned when you try to create, start, or modify a
DB instance. It can also be returned when you try to restore a DB instance from a DB snapshot. When this error is
returned, a common cause is that the specific DB instance class isn't available in the requested Availability Zone.
You can try one of the following to solve the problem:

- Retry the request with a different DB instance class.
- Retry the request with a different Availability Zone.
- Retry the request without specifying an explicit Availability Zone.

For information about troubleshooting instance capacity issues for Amazon EC2, see
[Insufficient instance capacity](../../../AWSEC2/latest/UserGuide/troubleshooting-launch.md#troubleshooting-launch-capacity "../../../AWSEC2/latest/UserGuide/troubleshooting-launch.md#troubleshooting-launch-capacity") in the Amazon EC2 User Guide.
