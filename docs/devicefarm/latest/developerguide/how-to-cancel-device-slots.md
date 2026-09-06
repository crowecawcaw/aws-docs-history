

# Cancelling a device slot in Device Farm
<a name="how-to-cancel-device-slots"></a>

You can cancel the number of device slots for both automated testing and remote access. The amount charged to your account for the next billing cycle will be listed underneath the billing period field..

For more information about device slots, see [Purchasing a device slot in Device Farm](how-to-purchase-device-slots.md).

------
#### [ Console ]

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Device slots**.

1. On the **Device slots** page, you can decrease the number of device slots to your desired amount by inputting the value into the **Desired slots** field corresponding to the device slot type you wish to modify. The amount charged to your account for the next billing cycle will be listed underneath **Next billing period cost**.

1. Choose **Save**. A **Confirm Change** window will appear. Review the information. When you are ready, type **confirm** and then choose **Confirm** to complete the transaction.

------
#### [ AWS CLI ]

You can run the **renew-offering** command to change the amount of devices for the next billing cycle.

------
#### [ API ]

Call the [RenewOffering](../../latest/APIReference/API_RenewOffering.html) operation to change the quantity of devices in your account.

------