# Cancelling a device slot in Device Farm

You can cancel the number of device slots for both automated testing and remote access. For instructions, see
one of the following sections. The amount charged to your account for the next billing cycle will be listed
underneath the billing period field.

For more information about device slots, see [Purchasing a device slot in Device Farm](how-to-purchase-device-slots.md "how-to-purchase-device-slots.md").

## Cancel a device slot (console)

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm "https://console.aws.amazon.com/devicefarm").
2. In the navigation pane, choose **Mobile Device Testing**, and then choose
   **Device slots**.
3. On the **Purchase and manage device slots** page, you can decrease the number of device
   slots for both automated testing and remote access by decreasing the value under **Next
   billing period**. The amount charged to your account for the next billing cycle will be listed
   underneath the billing period field.
4. Choose **Save**. A **Confirm Change** window will appear. Review the
   information and then choose **Confirm** to complete the transaction.

## Cancel a device slot (AWS CLI)

You can run the **renew-offering** command to change the amount of devices for the next
billing cycle.

## Cancel a device slot (API)

Call the [RenewOffering](../../../cli/latest/reference/devicefarm/renew-offering.md "../../../cli/latest/reference/devicefarm/renew-offering.md") operation to change the quantity of devices in your account.
