# Cleaning up a DLAMI instance

When you no longer need your DLAMI instance, you can stop it or terminate it on Amazon EC2 to
avoid incurring unexpected charges.

If you stop an instance, you can keep it around and start it later when you want to use it
again. Your configurations, files, and other non-volatile information are stored in a
volume on Amazon Simple Storage Service (Amazon S3). While your instance is stopped, you incur S3 charges for
retaining the volume, but you don't incur charges for compute resources. When your start
the instance again, it will mount that storage volume with your data.

If you terminate an instance, it's gone, and you cannot start it again. Of course, you
won't incur any more charges for the compute resources with a terminated instance.
However, your data still resides on Amazon S3, and you can continue to incur S3 charges. To
prevent all further charges related to your terminated instance, you must also delete
the storage volume on Amazon S3. For instructions, see [Terminate Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md") in the
_Amazon EC2 User Guide_.

For more information about Amazon EC2 instance states, such as `stopped` and
`terminated`, see [Amazon EC2 instance state
changes](../../../AWSEC2/latest/UserGuide/ec2-instance-lifecycle.md "../../../AWSEC2/latest/UserGuide/ec2-instance-lifecycle.md") in the _Amazon EC2 User Guide_.
