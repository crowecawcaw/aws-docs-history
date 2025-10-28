# Pause I/O fault injection

Use AWS Fault Injection Service and the Pause I/O action to temporarily stop I/O between an Amazon EBS volume
and the instances to which it is attached to test how your workloads handle I/O interruptions.

For more information about AWS FIS, see the [_AWS Fault Injection Service User Guide_](../../../fis/latest/userguide/what-is.md "../../../fis/latest/userguide/what-is.md").

###### Considerations

Keep in mind the following considerations for pausing volume I/O:

- Pause I/O is supported on all [Nitro-based instance types](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md").
- To test your OS timeout configuration, set the experiment duration equal to or greater
  than the value specified for `nvme_core.io_timeout`. For more information, see
  [NVMe I/O operation timeout for Amazon EBS volumes](timeout-nvme-ebs-volumes.md "timeout-nvme-ebs-volumes.md").
- If you drive I/O to a volume that has I/O paused, the following happens:

      + The volume's status transitions to `impaired` within 120 seconds. For more
       information, see [Amazon EBS volume status checks](monitoring-volume-checks.md "monitoring-volume-checks.md").
      + The CloudWatch metrics for queue length (`VolumeQueueLength`) will be non-zero.
       Any alarms or monitoring should monitor for a non-zero queue depth. For more information see
       [Metrics for Amazon EBS volumes](using_cloudwatch_ebs.md#ebs-volume-metrics "using_cloudwatch_ebs.md#ebs-volume-metrics").
      + The CloudWatch metrics for `VolumeReadOps` or `VolumeWriteOps` will be
       `0`, which indicates that the volume is no longer processing I/O.

  You can perform a basic experiment from the Amazon EC2 console, or you can perform more advanced
  experiments using the AWS FIS console. For more information about performing advanced experiments using
  the AWS FIS console, see [Tutorials for AWS FIS](../../../fis/latest/userguide/fis-tutorials.md "../../../fis/latest/userguide/fis-tutorials.md") in the _AWS Fault Injection Service User Guide_.

###### To perform a basic experiment using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Volumes.**
3. Select the volume for which to pause I/O and choose **Actions**, **Fault
   injection**, **Pause volume I/O**.
4. For **Duration**, enter the duration for which to pause I/O between the volume
   and the instances. The field next to the Duration dropdown list shows the duration in ISO 8601 format.
5. In the **Service access** section, select the IAM service role
   for AWS FIS to assume to perform the experiment. You can use either the default role, or an existing role
   that you created. For more information, see [Create an IAM role for AWS FIS
   experiments](../../../fis/latest/userguide/getting-started-iam-service-role.md "../../../fis/latest/userguide/getting-started-iam-service-role.md").
6. Choose **Pause volume I/O**. When prompted, enter `start` in the
   confirmation field and choose **Start experiment**.
7. Monitor the progress and impact of your experiment. For more information, see
   [Monitoring AWS FIS](../../../fis/latest/userguide/monitoring-experiments.md "../../../fis/latest/userguide/monitoring-experiments.md")
   in the _AWS FIS User Guide_.
