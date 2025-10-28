# Buy Reserved Instances for Amazon EC2

To buy a Reserved Instance for Amazon EC2, you can use the Amazon EC2 console, a command line tool, or an SDK
to search for Reserved Instance offerings from AWS and third-party sellers, adjusting your search
parameters until you find the exact match that you're looking for.

When you search for Reserved Instances to buy, you receive a quote on the cost of the returned
offerings. When you proceed with the purchase, AWS automatically places a limit price
on the purchase price. The total cost of your Reserved Instances won't exceed the amount that you
were quoted.

If the price rises or changes for any reason, the purchase is not completed. When you
are purchasing a third-party seller’s Reserved Instance from the Amazon EC2 Reserved Instance Marketplace, if there are
offerings similar to your choice but at a lower upfront price, AWS sells you the
offerings at the lower upfront price.

Before you confirm your purchase, review the details of the Reserved Instance that you plan to buy,
and make sure that all the parameters are accurate. After you purchase a Reserved Instance (either
from a third-party seller in the Reserved Instance Marketplace or from AWS), you cannot cancel your
purchase. You can queue a purchase for a future date, and cancel the queued purchase
before its scheduled time.

To purchase and modify Reserved Instances, ensure that your user has the appropriate
permissions, such as the ability to describe Availability Zones. For information, see
[Example: Work with Reserved Instances](ExamplePolicies_EC2.md#iam-example-reservedinstances "ExamplePolicies_EC2.md#iam-example-reservedinstances") (API) or [Example: Work with Reserved Instances](iam-policies-ec2-console.md#ex-reservedinstances "iam-policies-ec2-console.md#ex-reservedinstances") (console).

###### Tasks

- [Choosing a platform](#ri-choosing-platform "#ri-choosing-platform")
- [Queue your purchase](#ri-queued-purchase "#ri-queued-purchase")
- [Buy Standard Reserved Instances](#ri-buying-standard "#ri-buying-standard")
- [Buy Convertible Reserved Instances](#ri-buying-convertible "#ri-buying-convertible")
- [Buy from the Reserved Instance Marketplace](#ri-market-buying-guide "#ri-market-buying-guide")
- [Cancel a queued purchase](#cancel-queued-purchase "#cancel-queued-purchase")
- [Renew a Reserved Instance](#renew-ri "#renew-ri")

## Choosing a platform

Amazon EC2 supports the following platforms for Reserved Instances:

- Linux/UNIX
- Linux with SQL Server Standard
- Linux with SQL Server Web
- Linux with SQL Server Enterprise
- SUSE Linux
- Red Hat Enterprise Linux
- Red Hat Enterprise Linux with HA
- Windows
- Windows with SQL Server Standard
- Windows with SQL Server Web
- Windows with SQL Server Enterprise

###### Considerations

- If you bring your existing subscription (BYOS) for **Red Hat
  Enterprise Linux**, **SUSE Linux**, or
  **Ubuntu Pro**, you must choose an offering for the
  **Linux/Unix** platform.
- Reserved Instances are not supported on instances running **macOS** or
  Ubuntu Pro (EC2 subscription-included, i.e., not BYOS). For saving with
  On-Demand instance pricing, we recommend that you use macOS and Ubuntu Pro
  (EC2 subscription-included) instances with Savings Plans. For more
  information, see [Savings Plans
  User Guide](../../../savingsplans/latest/userguide/what-is-savings-plans.md "../../../savingsplans/latest/userguide/what-is-savings-plans.md").

To ensure that an instance runs in a specific Reserved Instance, the platform of the Reserved Instance must
match the platform of the AMI used to launch the instance. For Linux AMIs, it is
important to check whether the AMI platform uses the general value
**Linux/UNIX** or a more specific value like **SUSE
Linux**.

Console

###### To check the AMI platform

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **AMIs**.
3. Select the AMI.
4. On the **Details** tab, note the value of
   **Platform details**.

AWS CLI

###### To check the AMI platform

Use the [describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md") command and check the value of
`PlatformDetails`.

```
aws ec2 describe-images \
    --image-id `ami-0abcdef1234567890` \
    --query Images[*].PlatformDetails
```

The following is example output.

```
[
    "Linux/UNIX"
]
```

PowerShell

###### To check the AMI platform

Use the [Get-EC2Image](../../../powershell/latest/reference/items/Get-EC2Image.md "../../../powershell/latest/reference/items/Get-EC2Image.md") cmdlet and check the value of
`PlatformDetails`.

```
Get-EC2Image `
    -ImageId `ami-0abcdef1234567890` | `
    Select PlatformDetails
```

The following is example output.

```
PlatformDetails
---------------
Linux/UNIX
```

## Queue your purchase

By default, when you purchase a Reserved Instance, the purchase is made immediately.
Alternatively, you can queue your purchases for a future date and time. For example,
you can queue a purchase for around the time that an existing Reserved Instance expires. This can
help you ensure that you have uninterrupted coverage.

You can queue purchases for regional Reserved Instances, but not zonal Reserved Instances or Reserved Instances from
other sellers. You can queue a purchase up to three years in advance. On the
scheduled date and time, the purchase is made using the default payment method.
After the payment is successful, the billing benefit is applied.

You can set a date for your queued purchases in the Amazon EC2 console, and the
purchase is queued until 00:00 UTC on this date. To specify a different time for the
queued purchase, use an AWS SDK or command line tool.

You can view your queued purchases in the Amazon EC2 console. The status of a queued
purchase is **queued**. You can cancel a queued purchase any time
before its scheduled time. For details, see [Cancel a queued purchase](#cancel-queued-purchase "#cancel-queued-purchase").

## Buy Standard Reserved Instances

You can buy Standard Reserved Instances in a specific Availability Zone and get a capacity
reservation. Alternatively, you can forego the capacity reservation and purchase a
regional Standard Reserved Instance.

After the purchase is complete, if you already have a running instance that
matches the specifications of the Reserved Instance, the billing benefit is immediately applied.
You do not need to restart your instances. If you do not have a suitable running
instance, launch an instance and ensure that you match the exact criteria that you
specified for your Reserved Instance. For more information, see [Use your Reserved Instances](using-reserved-instances.md "using-reserved-instances.md").

For examples of how Reserved Instances are applied to your running instances, see [How Reserved Instance discounts are applied](apply_ri.md "apply_ri.md").

Console

###### To buy Standard Reserved Instances

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Reserved
   Instances**, and then choose **Purchase
   Reserved Instances**.
3. For **Offering class**, choose
   **Standard** to display Standard
   Reserved Instances.
4. To purchase a capacity reservation, toggle on **Only
   show offerings that reserve capacity** in the
   top-right corner of the purchase screen. When you toggle on this
   setting, the **Availability Zone** field
   appears.

To purchase a regional Reserved Instance, toggle off this setting. When you
toggle off this setting, the **Availability
Zone** field disappears. 5. Select other configurations as needed, and then choose
**Search**. 6. For each Reserved Instance that you want to purchase, enter the desired
quantity, and choose **Add to cart**.

To purchase a Standard Reserved Instance from the Reserved Instance Marketplace, look for
**3rd party** in the
**Seller** column in the search results.
The **Term** column displays non-standard
terms. For more information, see [Buy from the Reserved Instance Marketplace](#ri-market-buying-guide "#ri-market-buying-guide"). 7. To see a summary of the Reserved Instances that you selected, choose
**View cart**. 8. If **Order on** is **Now**,
the purchase is completed immediately after you choose
**Order all**. To queue a purchase, choose
**Now** and select a date. You can select a
different date for each eligible offering in the cart. The
purchase is queued until 00:00 UTC on the selected date. 9. To complete the order, choose **Order
all**.

If, at the time of placing the order, there are offerings
similar to your choice but with a lower price, AWS sells you
the offerings at the lower price. 10. Choose **Close**.

The status of your order is listed in the
**State** column. When your order is
complete, the **State** value changes from
`Payment-pending` to `Active`. When
the Reserved Instance is `Active`, it is ready to use.

If the status goes to `Retired`, AWS might not
have received your payment.

AWS CLI

###### To buy a Standard Reserved Instance

1. Find available Reserved Instances using the [describe-reserved-instances-offerings](../../../cli/latest/reference/ec2/describe-reserved-instances-offerings.md "../../../cli/latest/reference/ec2/describe-reserved-instances-offerings.md") command.
   Specify `standard` for the
   `--offering-class` option to return only Standard
   Reserved Instances. You can apply additional criteria to narrow your results.
   For example, use the following command to purchase a regional
   `t2.large` Reserved Instance with a default tenancy for
   `Linux/UNIX` for a 1-year term only.

```
aws ec2 describe-reserved-instances-offerings \
    --instance-type `t2.large` \
    --offering-class standard \
    --product-description "`Linux/UNIX`" \
    --instance-tenancy `default` \
    --filters Name=duration,Values=`31536000` \
              Name=scope,Values=`Region`
```

To find Reserved Instances on the Reserved Instance Marketplace only, use the
`marketplace` filter and do not specify a
duration in the request, as the term might be shorter than a
1– or 3-year term.

```
aws ec2 describe-reserved-instances-offerings \
    --instance-type `t2.large` \
    --offering-class standard \
    --product-description "`Linux/UNIX`" \
    --instance-tenancy `default` \
    --filters Name=`marketplace`,Values=true
```

When you find a Reserved Instance that meets your needs, take note of the
offering ID. For example:

```
"ReservedInstancesOfferingId": "bec624df-a8cc-4aad-a72f-4f8abc34caf2"
```

2. Use the [purchase-reserved-instances-offering](../../../cli/latest/reference/ec2/purchase-reserved-instances-offering.md "../../../cli/latest/reference/ec2/purchase-reserved-instances-offering.md") command to buy
   your Reserved Instance. You must specify the Reserved Instance offering ID you obtained
   the previous step and you must specify the number of instances
   for the reservation.

```
aws ec2 purchase-reserved-instances-offering \
    --reserved-instances-offering-id `bec624df-a8cc-4aad-a72f-4f8abc34caf2` \
    --instance-count `1`
```

By default, the purchase is completed immediately.
Alternatively, to queue the purchase, add the following option
to the previous call.

```
--purchase-time "`2020`-`12`-`01`T`00`:`00`:`00`Z"
```

3. Use the [describe-reserved-instances](../../../cli/latest/reference/ec2/describe-reserved-instances.md "../../../cli/latest/reference/ec2/describe-reserved-instances.md") command to get the
   status of your Reserved Instance.

```
aws ec2 describe-reserved-instances \
    --reserved-instances-ids `b847fa93-e282-4f55-b59a-1342fec06327` \
    --query ReservedInstances[].State
```

PowerShell

###### To buy a Standard Reserved Instance

1. Find available Reserved Instances using the [Get-EC2ReservedInstancesOffering](../../../powershell/latest/reference/items/Get-EC2ReservedInstancesOffering.md "../../../powershell/latest/reference/items/Get-EC2ReservedInstancesOffering.md") cmdlet. Specify
   `standard` for the `-OfferingClass`
   parameter to return only Standard Reserved Instances. You can apply
   additional criteria to narrow your results. For example, use the
   following command to purchase a regional `t2.large`
   Reserved Instance with a default tenancy for `Linux/UNIX` for a
   1-year term only.

```
Get-EC2ReservedInstancesOffering `
    -InstanceType "`t2.large`" `
    -OfferingClass "standard" `
    -ProductDescription "`Linux/UNIX`" `
    -InstanceTenancy "`default`" `
    -Filters @{Name="duration"; Values="`31536000`"} `
             @{Name="scope"; Values="`Region`"
```

To find Reserved Instances on the Reserved Instance Marketplace only, use the
`marketplace` filter and do not specify a
duration in the request, as the term might be shorter than a
1– or 3-year term.

```
Get-EC2ReservedInstancesOffering `
    -InstanceType `t2.large` `
    -OfferingClass "standard" `
    -ProductDescription "`Linux/UNIX`" `
    -InstanceTenancy `default` `
    -Filters @{Name="`marketplace`"; Values="true"}
```

When you find a Reserved Instance that meets your needs, take note of the
offering ID. For example:

```
bec624df-a8cc-4aad-a72f-4f8abc34caf2
```

2. Use the [New-EC2ReservedInstance](../../../powershell/latest/reference/items/New-EC2ReservedInstance.md "../../../powershell/latest/reference/items/New-EC2ReservedInstance.md") cmdlet to buy your Reserved Instance.
   You must specify the Reserved Instance offering ID you obtained the previous
   step and you must specify the number of instances for the
   reservation.

```
New-EC2ReservedInstance `
    -ReservedInstancesOfferingId "`bec624df-a8cc-4aad-a72f-4f8abc34caf2`" `
    -InstanceCount `1`
```

By default, the purchase is completed immediately.
Alternatively, to queue the purchase, add the following
parameter to the previous call.

```
-PurchaseTime "`2020`-`12`-`01`T`00`:`00`:`00`Z"
```

3. Use the [Get-EC2ReservedInstance](../../../powershell/latest/reference/items/Get-EC2ReservedInstance.md "../../../powershell/latest/reference/items/Get-EC2ReservedInstance.md") cmdlet to get the status of
   your Reserved Instance.

```
Get-EC2ReservedInstance `
    -ReservedInstancesId `b847fa93-e282-4f55-b59a-1342fec06327` | `
    Select State
```

## Buy Convertible Reserved Instances

You can buy Convertible Reserved Instances in a specific Availability Zone and get a capacity reservation.
Alternatively, you can forego the capacity reservation and purchase a regional
Convertible Reserved Instance.

If you already have a running instance that matches the specifications of the
Reserved Instance, the billing benefit is immediately applied. You do not have to restart your
instances. If you do not have a suitable running instance, launch an instance and
ensure that you match the same criteria that you specified for your Reserved Instance. For more
information, see [Use your Reserved Instances](using-reserved-instances.md "using-reserved-instances.md").

For examples of how Reserved Instances are applied to your running instances, see [How Reserved Instance discounts are applied](apply_ri.md "apply_ri.md").

Console

###### To buy Convertible Reserved Instances

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Reserved
   Instances**, and then choose **Purchase
   Reserved Instances**.
3. For **Offering class**, choose
   **Convertible** to display Convertible Reserved Instances.
4. To purchase a capacity reservation, toggle on **Only
   show offerings that reserve capacity** in the
   top-right corner of the purchase screen. When you toggle on this
   setting, the **Availability Zone** field
   appears.

To purchase a regional Reserved Instance, toggle off this setting. When you
toggle off this setting, the **Availability
Zone** field disappears. 5. Select other configurations as needed and choose
**Search**. 6. For each Convertible Reserved Instance that you want to purchase, enter the quantity,
and choose **Add to cart**. 7. To see a summary of your selection, choose **View
cart**. 8. If **Order on** is **Now**,
the purchase is completed immediately after you choose
**Order all**. To queue a purchase, choose
**Now** and select a date. You can select a
different date for each eligible offering in the cart. The
purchase is queued until 00:00 UTC on the selected date. 9. To complete the order, choose **Order
all**.

If, at the time of placing the order, there are offerings
similar to your choice but with a lower price, AWS sells you
the offerings at the lower price. 10. Choose **Close**.

The status of your order is listed in the
**State** column. When your order is
complete, the **State** value changes from
`Payment-pending` to `Active`. When
the Reserved Instance is `Active`, it is ready to use.

If the status goes to `Retired`, AWS might not
have received your payment.

AWS CLI

###### To buy a Convertible Reserved Instance

1. Find available Reserved Instances using the [describe-reserved-instances-offerings](../../../cli/latest/reference/ec2/describe-reserved-instances-offerings.md "../../../cli/latest/reference/ec2/describe-reserved-instances-offerings.md") command.
   Specify `convertible` for the
   `--offering-class` option to return only Convertible Reserved Instances.
   You can apply additional criteria to narrow your results. For
   example, use the following command to purchase a regional
   `t2.large` Reserved Instance with a default tenancy for
   `Linux/UNIX`.

```
aws ec2 describe-reserved-instances-offerings \
    --instance-type `t2.large` \
    --offering-class convertible \
    --product-description "`Linux/UNIX`" \
    --instance-tenancy `default` \
    --filters Name=scope,Values=`Region`
```

When you find a Reserved Instance that meets your needs, take note of the
offering ID. For example:

```
"ReservedInstancesOfferingId": "bec624df-a8cc-4aad-a72f-4f8abc34caf2"
```

2. Use the [purchase-reserved-instances-offering](../../../cli/latest/reference/ec2/purchase-reserved-instances-offering.md "../../../cli/latest/reference/ec2/purchase-reserved-instances-offering.md") command to buy
   your Reserved Instance. You must specify the Reserved Instance offering ID you obtained
   the previous step and you must specify the number of instances
   for the reservation.

```
aws ec2 purchase-reserved-instances-offering \
    --reserved-instances-offering-id `bec624df-a8cc-4aad-a72f-4f8abc34caf2` \
    --instance-count `1`
```

By default, the purchase is completed immediately.
Alternatively, to queue the purchase, add the following option
to the previous call.

```
--purchase-time "`2020`-`12`-`01`T`00`:`00`:`00`Z"
```

3. Use the [describe-reserved-instances](../../../cli/latest/reference/ec2/describe-reserved-instances.md "../../../cli/latest/reference/ec2/describe-reserved-instances.md") command to get the
   status of your Reserved Instance.

```
aws ec2 describe-reserved-instances \
    --reserved-instances-ids `b847fa93-e282-4f55-b59a-1342fec06327` \
    --query ReservedInstances[].State
```

PowerShell

###### To buy a Convertible Reserved Instance

1. Find available Reserved Instances using the [Get-EC2ReservedInstancesOffering](../../../powershell/latest/reference/items/Get-EC2ReservedInstancesOffering.md "../../../powershell/latest/reference/items/Get-EC2ReservedInstancesOffering.md") cmdlet. Specify
   `convertible` for the `-OfferingClass`
   parameter to return only Convertible Reserved Instances. You can apply additional
   criteria to narrow your results. For example, use the following
   command to purchase a regional `t2.large` Reserved Instance with a
   default tenancy for `Linux/UNIX`.

```
Get-EC2ReservedInstancesOffering `
    -InstanceType "`t2.large`" `
    -OfferingClass "convertible" `
    -ProductDescription "`Linux/UNIX`" `
    -InstanceTenancy "`default`" `
    -Filters @{Name="scope"; Values="`Region`"
```

When you find a Reserved Instance that meets your needs, take note of the
offering ID. For example:

```
bec624df-a8cc-4aad-a72f-4f8abc34caf2
```

2. Use the [New-EC2ReservedInstance](../../../powershell/latest/reference/items/New-EC2ReservedInstance.md "../../../powershell/latest/reference/items/New-EC2ReservedInstance.md") cmdlet to buy your Reserved Instance.
   You must specify the Reserved Instance offering ID that you obtained the
   previous step and you must specify the number of instances for
   the reservation.

```
New-EC2ReservedInstance `
    -ReservedInstancesOfferingId "`bec624df-a8cc-4aad-a72f-4f8abc34caf2`" `
    -InstanceCount `1`
```

By default, the purchase is completed immediately.
Alternatively, to queue the purchase, add the following
parameter to the previous call.

```
-PurchaseTime "`2020`-`12`-`01`T`00`:`00`:`00`Z"
```

3. Use the [Get-EC2ReservedInstance](../../../powershell/latest/reference/items/Get-EC2ReservedInstance.md "../../../powershell/latest/reference/items/Get-EC2ReservedInstance.md") cmdlet to get the status of
   your Reserved Instance.

```
Get-EC2ReservedInstance `
    -ReservedInstancesId `b847fa93-e282-4f55-b59a-1342fec06327` | `
    Select State
```

## Buy from the Reserved Instance Marketplace

You can purchase Reserved Instances from third-party sellers who own Reserved Instances that they no longer
need from the Reserved Instance Marketplace. You can do this using the Amazon EC2 console or a command line
tool. The process is similar to purchasing Reserved Instances from AWS. For more information,
see [Buy Standard Reserved Instances](#ri-buying-standard "#ri-buying-standard").

There are a few differences between Reserved Instances purchased in the Reserved Instance Marketplace and Reserved Instances
purchased directly from AWS:

- **Term** – Reserved Instances that you purchase from
  third-party sellers have less than a full standard term remaining. Full
  standard terms from AWS run for one year or three years.
- **Upfront price** – Third-party Reserved Instances
  can be sold at different upfront prices. The usage or recurring fees remain
  the same as the fees set when the Reserved Instances were originally purchased from
  AWS.
- **Types of Reserved Instances** – Only Amazon EC2
  Standard Reserved Instances can be purchased from the Reserved Instance Marketplace. Convertible Reserved Instances, Amazon RDS, and
  Amazon ElastiCache Reserved Instances are not available for purchase on the Reserved Instance Marketplace.

Basic information about you is shared with the seller, for example, your ZIP code
and country information.

This information enables sellers to calculate any necessary transaction taxes that
they have to remit to the government (such as sales tax or value-added tax) and is
provided as a disbursement report. In rare circumstances, AWS might have to
provide the seller with your email address, so that they can contact you regarding
questions related to the sale (for example, tax questions).

For similar reasons, AWS shares the legal entity name of the seller on the
buyer's purchase invoice. If you need additional information about the seller for
tax or related reasons, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Cancel a queued purchase

You can queue a purchase up to three years in advance. You can cancel a queued
purchase any time before its scheduled time.

Console

###### To cancel a queued purchase

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Reserved
   Instances**.
3. Select one or more Reserved Instances.
4. Choose **Actions**, **Delete queued
   Reserved Instances**.
5. When prompted for confirmation, choose
   **Delete**, and then
   **Close**.

AWS CLI

###### To cancel a queued purchase

Use the [delete-queued-reserved-instances](../../../cli/latest/reference/ec2/delete-queued-reserved-instances.md "../../../cli/latest/reference/ec2/delete-queued-reserved-instances.md") command.

```
aws ec2 delete-queued-reserved-instances \
    --reserved-instances-ids `b847fa93-e282-4f55-b59a-1342fec06327`
```

PowerShell

###### To cancel a queued purchase

Use the [Remove-EC2QueuedReservedInstance](../../../powershell/latest/reference/items/Remove-EC2QueuedReservedInstance.md "../../../powershell/latest/reference/items/Remove-EC2QueuedReservedInstance.md") cmdlet.

```
Remove-EC2QueuedReservedInstance `
    -ReservedInstancesId `b847fa93-e282-4f55-b59a-1342fec06327`
```

## Renew a Reserved Instance

You can renew a Reserved Instance before it is scheduled to expire. Renewing a Reserved Instance queues the
purchase of a Reserved Instance with the same configuration until the current Reserved Instance
expires.

You must renew a Reserved Instance using the Amazon EC2 console.

###### To renew a Reserved Instance using a queued purchase

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Reserved
   Instances**.
3. Select the Reserved Instance to renew.
4. Choose **Actions**, **Renew Reserved
   Instances**.
5. To complete the order, choose **Order all**, and then
   **Close**.
