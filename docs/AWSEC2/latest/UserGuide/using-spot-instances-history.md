# View Spot Instance pricing history

Spot Instance prices are set by Amazon EC2 and adjust gradually based on long-term trends in supply
and demand for Spot Instance capacity.

When your Spot request is fulfilled, your Spot Instances launch at the current Spot price, not
exceeding the On-Demand price. You can view the Spot price history for the last 90 days,
filtering by instance type, operating system, and Availability Zone.

For the _current_ Spot Instance prices, see [Amazon EC2 Spot Instances Pricing](https://aws.amazon.com/ec2/spot/pricing/ "https://aws.amazon.com/ec2/spot/pricing/").

Console

###### To view the Spot price history

1.  Open the Amazon EC2 console at
    [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2.  In the navigation pane, choose **Spot Requests**.
3.  Choose **Pricing history**.
4.  For **Graph**, choose to compare the price history by
    **Availability Zones** or by **Instance
    Types**.

        * If you choose **Availability Zones**, then choose the **Instance
         type**, operating system (**Platform**),
         and **Date range** for which to view the price
         history.
        * If you choose **Instance Types**, then choose up to five
         **Instance type(s)**, the **Availability
         Zone**, operating system (**Platform**),
         and **Date range** for which to view the price
         history.

    The following screenshot shows a price comparison for different instance types.

![The Spot Instance pricing history tool in the Amazon EC2 console.](images/spot-instance-pricing-history.png) 5. Hover (move your pointer) over the graph to display the prices at specific times in the
selected date range. The prices are displayed in the information blocks above
the graph. The price displayed in the top row shows the price on a specific
date. The price displayed in the second row shows the average price over the
selected date range. 6. To display the price per vCPU, toggle on **Display normalized
prices**. To display the price for the instance type, toggle off
**Display normalized prices**.

AWS CLI

###### To view the Spot price history

Use the following [describe-spot-price-history](../../../cli/latest/reference/ec2/describe-spot-price-history.md "../../../cli/latest/reference/ec2/describe-spot-price-history.md") command.

```
aws ec2 describe-spot-price-history \
    --instance-types `c6i.xlarge` \
    --product-descriptions "`Linux/UNIX`" \
    --start-time `2025-04-01T00:00:00` \
    --end-time `2025-04-02T00:00:0`
```

PowerShell

###### To view the Spot price history

Use the [Get-EC2SpotPriceHistory](../../../powershell/latest/reference/items/Get-EC2SpotPriceHistory.md "../../../powershell/latest/reference/items/Get-EC2SpotPriceHistory.md") cmdlet.

```
Get-EC2SpotPriceHistory `
    -InstanceType `c6i.xlarge` `
    -ProductDescription "`Linux/UNIX`" `
    -UtcStartTime `2025-04-01T00:00:00` `
    -UtcEndTime `2025-04-02T00:00:0`
```
