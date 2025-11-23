# Edit a monitor

You can edit information for a Network Synthetic Monitor, including change the name, setting a new
aggregation period, or adding or removing tags. Changing a monitor's information does not change
any of its associated probes.

You can work with monitors and probes by using either the Amazon CloudWatch
console or the AWS Command Line Interface. To work with Network Synthetic Monitor programmatically, see the
[Network Synthetic Monitor API Reference](../../../networkmonitor/latest/APIReference/Welcome.md "../../../networkmonitor/latest/APIReference/Welcome.md") and
[networkmonitor](../../../cli/latest/reference/networkmonitor.md "../../../cli/latest/reference/networkmonitor.md") in the AWS Command Line Interface Command Reference.

###### To edit a monitor using the console

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"), and then, under **Network
   Monitoring**, choose **Synthetic monitors**.
2. In the **Monitors** section, choose the monitor that you want to
   edit.
3. On the monitor dashboard page, choose **Edit**.
4. For the **Monitor name**, enter the new name for the monitor.
5. For the **Aggregation period**, choose how often you want to send
   metrics to CloudWatch. Valid periods are:
   - **30 seconds**
   - **60 seconds**

###### Note

A shorter aggregation period provides faster detection of network issues. However, the
aggregation period that you choose can affect your billing costs. For more information about pricing, see the [Amazon CloudWatch pricing](https://aws.amazon.com//cloudwatch/pricing/ "https://aws.amazon.com//cloudwatch/pricing/") page. 6. (Optional) In the **Tags** section, add **Key** and
**Value** pairs to further help identify this resource, allowing you to
search or filter on specific information. You can also just change the
**Value** of any current **Key**.

    1. Choose **Add new tag**.
    2. Enter a **Key** name and associated **Value**.
    3. Choose **Add new tag** to add the new tag.


    You can add multiple tags by choosing **Add new tag**, or you can
     remove a tag by choosing **Remove**.
    4. If you want to associate your tags with the monitor, keep **Add tags to probes
     created by monitor** checked. This adds the tags to the monitor probes, which can
     be helpful if you're using tag-based authentication or metering.

7. Choose **Save changes**.
