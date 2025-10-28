# Monitoring SSD storage utilization

You can monitor your file system's SSD storage capacity utilization using a variety of AWS and
NetApp tools. Using Amazon CloudWatch you can monitor storage capacity utilization and set alarms to alert you when
storage capacity utilization reaches a customizable threshold.

###### Note

We recommend that you don't exceed 80% storage capacity utilization of your SSD storage tier.
This ensures that tiering functions properly, and provides overhead for new
data. If your SSD storage tier is consistently above 80% storage capacity
utilization, you can increase your SSD storage tier's capacity. For more
information, see [Updating file system SSD storage and IOPS](storage-capacity-and-IOPS.md#increase-primary-storage "storage-capacity-and-IOPS.md#increase-primary-storage").

You can view a file system's available SSD storage and the overall storage distribution in the
Amazon FSx console. The **Available primary storage capacity** graph displays the amount of available SSD-based storage
capacity on a file system over time. The **Storage distribution** graph shows how a file system's
overall storage capacity is currently distributed over 3 categories:

- Capacity pool tier
- SSD tier - available
- SSD tier - used
  You can monitor your file system's SSD storage capacity utilization in the AWS Management Console, using the following procedure.

###### To monitor file system available SSD tier storage capacity (console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Choose **File systems** in the left-hand navigation column, then choose the
   ONTAP file system that you want to view storage capacity information for.
   The file system detail page appears.
3. In the second panel, choose the **Monitoring & performance** tab, then choose
   **Storage**. The **Available primary storage capacity**
   and **Storage capacity utilization per aggregate** graphs are displayed.
