# Extend Capacity Blocks

With Capacity Blocks, you reserve compute capacity for your workloads, ensuring availability and consistency. To accommodate your changing needs, you can extend the duration of your existing Capacity Blocks as required.

To extend a Capacity Block, it must have a status of `active` or
`scheduled`, and have no extensions that are
`payment-pending`. You can request to extend the duration of your
Capacity Block up to a minimum of 1 hour or a maximum of 56 days before it expires.
You can extend your Capacity Block by 1-day increments up to 14 days, and 7-day increments
up to 182 days (26 weeks) total. When you extend your Capacity Block, its end date will be
updated so that your instances can continue to run without disruption.

- There is no limit to the number of extensions you can apply to a Capacity Block
- Your Capacity Reservation ID will remain the same after extending the block
- Capacity Blocks can only be extended if there is sufficient capacity available to support them, which is not guaranteed.

## Billing

The price of a Capacity Block offering is charged up front. The extension will remain in `payment-pending` until the bill is paid. If your payment can't be processed within 12 hours, or up to 35 minutes before the Capacity Block is scheduled to end (whichever comes first), your extension is not successful and the status changes to `payment-failed`. Your Capacity Block reservation will remain `active` and will be terminated on the original end date.

After your payment is processed successfully, the Capacity Block extension status changes to `payment-succeeded` and the end date of the Capacity Block reservation will be updated to the new end date.
The details of your extension can be viewed in the **Capacity Block Extension details** section of the console, or by using the
[describe-capacity-block-extension-history](../../../cli/latest/reference/ec2/describe-capacity-block-extension-history.md "../../../cli/latest/reference/ec2/describe-capacity-block-extension-history.md") command.

## Extend your Capacity Block

Console

###### To extend a Capacity Block

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Capacity Reservations**.
3. On the **Capacity Reservations overview** page, you see a resource table with details about all of your Capacity Reservations resources. Select the reservation ID for the Capacity Block that you want to extend.
4. From the **Actions** drop down menu, choose **Extend Capacity Block**.
5. Under **Duration**, enter the number of days or weeks you need to extend the reservation for.
6. Choose **Find Capacity Block**.
7. If a Capacity Block is available that meets your specifications, an offering appears under **Recommended Capacity Blocks**. To view other Capacity Block offerings, adjust your search inputs and choose **Find Capacity Blocks** again.
8. When you find a Capacity Block offering that you want to purchase, choose **Extend**.
9. In the pop-up window **Extend Capacity Block**, enter _confirm_, then choose **Extend**.

AWS CLI

###### To find a Capacity Block extension

Use the [describe-capacity-block-extension-offerings](../../../cli/latest/reference/ec2/describe-capacity-block-extension-offerings.md "../../../cli/latest/reference/ec2/describe-capacity-block-extension-offerings.md") command. The following example
searches for a 48 hour Capacity Block extension for the specified Reservation.

```
aws ec2 describe-capacity-block-extension-offerings \
    --capacity-reservation-id `cr-1234567890abcdefg` \
    --capacity-block-extension-duration-hours `48`
```

###### To extend a Capacity Block

Use the [purchase-capacity-block-extension](../../../cli/latest/reference/ec2/purchase-capacity-block-extension.md "../../../cli/latest/reference/ec2/purchase-capacity-block-extension.md") command. Specify the extension
offering ID from the output of the previous example.

```
aws ec2 purchase-capacity-block-extension \
    --capacity-block-extension-offering-id `cbe-0123456789abcdefg` \
    --capacity-reservation-id `cr-1234567890abcdefg`
```

PowerShell

###### To find a Capacity Block extension

Use the [Get-EC2CapacityBlockExtensionOffering](../../../powershell/latest/reference/items/Get-EC2CapacityBlockExtensionOffering.md "../../../powershell/latest/reference/items/Get-EC2CapacityBlockExtensionOffering.md") cmdlet. The following example
searches for a 48 hour Capacity Block extension for the specified Reservation.

```
Get-EC2CapacityBlockExtensionOffering `
    -CapacityReservationId `cr-1234567890abcdefg` `
    -CapacityBlockExtensionDurationHour `48`
```

###### To extend a Capacity Block

Use the [Invoke-EC2CapacityBlockExtension](../../../powershell/latest/reference/items/Invoke-EC2CapacityBlockExtension.md "../../../powershell/latest/reference/items/Invoke-EC2CapacityBlockExtension.md") cmdlet. Specify the extension
offering ID from the output of the previous example.

```
Invoke-EC2CapacityBlockExtension `
    -CapacityBlockExtensionOfferingId `cbe-0123456789abcdefg` `
    -CapacityReservationId `cr-1234567890abcdefg`
```
