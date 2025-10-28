# Managing file system throughput

_Elastic throughput_ is the default throughput mode in the
Amazon EFS console and is recommended for most use cases. With Elastic throughput,
performance automatically scales up or down to meet the needs of your workload activity. If,
however, you know the specific access patterns for your workloads (including throughput,
latency, and storage needs), then you can choose to change the throughput mode.

###### Note

While Elastic throughput is designed to scale elastically with your throughput, we recommend implementing proper governance through
monitoring metrics with CloudWatch (MeteredIOBytes) and usage alerts as part of your operational best practices. This helps you maintain optimal
resource utilization and stay within your planned operational parameters. For more information, see [Monitoring metrics with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

Other throughput modes you can choose include:

- **Provisioned throughput** – You
  specify a level of throughput that the file system can drive independent of the file
  system's size or burst credit balance.
- **Bursting throughput** – Throughput
  scales with the amount of storage in your file system and supports bursting to higher
  levels for up to 12 hours per day.
  For more information about Amazon EFS throughput modes, see [Throughput modes](performance.md#throughput-modes "performance.md#throughput-modes").

###### Note

You can change the throughput mode and the provisioned throughput amount after the file
system is available. Changing throughput mode does not cause application downtime. However,
any time that you change the file system to Provisioned throughput or increase
the provisioned throughput amount, you must wait at least 24 hours before you can change the
throughput mode again or decrease the provisioned amount.

You can manage the file system throughput mode by using the Amazon EFS console, the AWS Command Line Interface
(AWS CLI), and Amazon EFS API.

###### To manage file system throughput

1.  Open the Amazon Elastic File System console at
    [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2.  In the left navigation pane, choose **File systems** to display the
    list of EFS file systems in your account.
3.  Choose the file system that you want to change the throughput mode for.
4.  On the file system details page, in the **General** section, choose
    **Edit**. The **Edit** page displays.
5.  Modify the **Throughput mode** setting.

        * To use Elastic throughput or Provisioned throughput,
         choose **Enhanced**, and then choose **Elastic** or
         **Provisioned**.


        If you choose **Provisioned**, then, in
         **Provisioned Throughput (MiB/s)**, enter the amount of
         throughput to provision for file system requests. The amount of **Maximum Read
         Throughput** is displayed at three times the amount of the throughput that
         you enter. EFS file systems meter read requests at one-third the rate of
         other requests. After you enter the throughput, an estimate of the monthly cost for
         the file system is shown.


        ###### Note

        You can change the throughput mode and the provisioned throughput amount after the
         file system is available. However, any time that you change the file system
         throughput to Provisioned or increase the provisioned throughput amount,
         you must wait at least 24 hours before you can change the throughput mode again or
         decrease the provisioned amount.
        * To use Bursting throughput, choose
         **Bursting**.

    For more information about choosing the correct throughput mode for your performance
    needs, see [Throughput modes](performance.md#throughput-modes "performance.md#throughput-modes").

6.  Choose **Save changes** to implement your changes.
    Use the [update-file-system](../../../cli/latest/reference/efs/update-file-system.md "../../../cli/latest/reference/efs/update-file-system.md") CLI command, or the [UpdateFileSystem](API_UpdateFileSystem.md "API_UpdateFileSystem.md") API action to
    change a file system's throughput mode.
