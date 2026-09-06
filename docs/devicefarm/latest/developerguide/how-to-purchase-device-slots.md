

# Purchasing a device slot in Device Farm
<a name="how-to-purchase-device-slots"></a>

Device farm has two billing methods for testing on public mobile devices: metered and unmetered. With metered billing, you pay-as-you-go based on device minutes. To learn more about metered, pay-as-you-go pricing, visit here: [https://aws.amazon.com/device-farm/pricing/](https://aws.amazon.com/device-farm/pricing/). With unmetered billing, you reserve device concurrency through Device slots, which are billed at a flat monthly rate. This page covers unmetered, device slot billing.

Device slots correspond to your concurrency in Device Farm, determining how many test jobs (devices) or remote access sessions you can run simultaneously with unmetered billing. Device slots are specific to testing type (automated testing or remote access) and device platform (android or ios). Slots are not tied to any specific device make or model. You can use the Device Farm console, AWS Command Line Interface (AWS CLI), or Device Farm API to purchase device slots.

## Purchase device slots
<a name="how-to-purchase-device-slots-methods"></a>

------
#### [ Console ]

1. Sign in to the Device Farm console at [https://console.aws.amazon.com/devicefarm](https://console.aws.amazon.com/devicefarm).

1. In the navigation pane, choose **Mobile Device Testing**, and then choose **Device slots**.

1. On the **Device slots** page, you can choose the number of **Automated testing** and **Remote access** device slots per platform that you want to purchase. Specify slot amounts in the **Desired slots** column.

   As you change the slot amount, the text dynamically updates with the billing amount. For more information, see [AWS Device Farm pricing](https://aws.amazon.com/device-farm/pricing/).
**Important**  
If you change the number of device slots but see a **contact us** or **contact us to purchase** message, your AWS account is not yet approved to purchase the number of device slots that you requested.  
These options prompt you to send an email to the Device Farm support team. In the email, specify the number of each device type that you want to purchase and for which billing cycle.
**Note**  
Changes to the device slots apply to your entire account and affect all projects.  
![Device slots page on the Device Farm console](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-console-device-slots-default-view.png)

1. Choose **Purchase**. A **Confirm purchase** window will appear. Review the information. When you are ready, type **confirm** and then choose **Confirm** to complete the transaction.

![Purchase confirmation page on the Device Farm console](http://docs.aws.amazon.com/devicefarm/latest/developerguide/images/aws-device-farm-console-device-slots-purchase-confirm.png)


On the **Device slots** page, you can see the number of device slots that you currently have, as well as the number of device slots you will have for your next billing period.

------
#### [ AWS CLI ]

You can run the **purchase-offering** command to purchase the offering.

To list your Device Farm account settings, including the maximum number of device slots that you can purchase and the number of remaining free trial minutes, run the **get-account-settings** command. You'll see output similar to the following:

```
{
    "accountSettings": {
        "maxSlots": {
            "{{GUID}}": 1,
            "{{GUID}}": 1,
            "{{GUID}}": 1,
            "{{GUID}}": 1
        },
        "unmeteredRemoteAccessDevices": {
            "ANDROID": 0,
            "IOS": 0
        },
        "maxJobTimeoutMinutes": 150,
        "trialMinutes": {
            "total": 1000.0,
            "remaining": 954.1
        },
        "defaultJobTimeoutMinutes": 150,
        "awsAccountNumber": "{{AWS-ACCOUNT-NUMBER}}",
        "unmeteredDevices": {
            "ANDROID": 0,
            "IOS": 0
        }
    }
}
```

To list the device slot offerings that are available to you, run the **list-offerings** command. You should see output similar to the following:

```
{
    "offerings": [
        {
            "recurringCharges": [
                {
                    "cost": {
                        "amount": 250.0,
                        "currencyCode": "USD"
                    },
                    "frequency": "MONTHLY"
                }
            ],
            "platform": "IOS",
            "type": "RECURRING",
            "id": "{{GUID}}",
            "description": "iOS Unmetered Device Slot"
        },
        {
            "recurringCharges": [
                {
                    "cost": {
                        "amount": 250.0,
                        "currencyCode": "USD"
                    },
                    "frequency": "MONTHLY"
                }
            ],
            "platform": "ANDROID",
            "type": "RECURRING",
            "id": "{{GUID}}",
            "description": "Android Unmetered Device Slot"
        },
        {
            "recurringCharges": [
                {
                    "cost": {
                        "amount": 250.0,
                        "currencyCode": "USD"
                    },
                    "frequency": "MONTHLY"
                }
            ],
            "platform": "ANDROID",
            "type": "RECURRING",
            "id": "{{GUID}}",
            "description": "Android Remote Access Unmetered Device Slot"
        },
        {
            "recurringCharges": [
                {
                    "cost": {
                        "amount": 250.0,
                        "currencyCode": "USD"
                    },
                    "frequency": "MONTHLY"
                }
            ],
            "platform": "IOS",
            "type": "RECURRING",
            "id": "{{GUID}}",
            "description": "iOS Remote Access Unmetered Device Slot"
        }
    ]
}
```

To list the available offering promotions, run the **list-offering-promotions** command.

**Note**  
This command returns only promotions that you haven't yet purchased. As soon as you purchase one or more slots across any offering using a promotion, that promotion no longer appears in the results.

You should see output similar to the following:

```
{
    "offeringPromotions": [
        {
            "id": "2FREEMONTHS",
            "description": "New device slot customers get 3 months for the price of 1."
        }
    ]
}
```

To get the offering status, run the **get-offering-status** command. You should see output similar to the following: 

```
{
    "current": {
        "{{GUID}}": {
            "offering": {
                "platform": "IOS",
                "type": "RECURRING",
                "id": "{{GUID}}",
                "description": "iOS Unmetered Device Slot"
            },
            "quantity": 1
        },
        "{{GUID}}": {
            "offering": {
                "platform": "ANDROID",
                "type": "RECURRING",
                "id": "{{GUID}}",
                "description": "Android Unmetered Device Slot"
            },
            "quantity": 1
        }
    },
    "nextPeriod": {
        "{{GUID}}": {
            "effectiveOn": 1459468800.0,
            "offering": {
                "platform": "IOS",
                "type": "RECURRING",
                "id": "{{GUID}}",
                "description": "iOS Unmetered Device Slot"
            },
            "quantity": 1
        },
        "{{GUID}}": {
            "effectiveOn": 1459468800.0,
            "offering": {
                "platform": "ANDROID",
                "type": "RECURRING",
                "id": "{{GUID}}",
                "description": "Android Unmetered Device Slot"
            },
            "quantity": 1
        }
    }
}
```

The **renew-offering** and **list-offering-transactions** commands are also available for this feature. For more information, see the [AWS CLI reference](cli-ref.md).

------
#### [ API ]

1. Call the [GetAccountSettings](../../latest/APIReference/API_GetAccountSettings.html) operation to list your account settings.

1. Call the [ListOfferings](../../latest/APIReference/API_ListOfferings.html) operation to list the device slot offerings available to you.

1. Call the [ListOfferingPromotions](../../latest/APIReference/API_ListOfferingPromotions.html) operation to list the offering promotions that are available.
**Note**  
This operation returns only promotions that you haven't yet purchased. As soon as you purchase one or more slots using an offering promotion, that promotion no longer appears in the results.

1. Call the [PurchaseOffering](../../latest/APIReference/API_PurchaseOffering.html) operation to purchase an offering.

1. Call the [GetOfferingStatus](../../latest/APIReference/API_GetOfferingStatus.html) operation to get the offering status.

The [RenewOffering](../../latest/APIReference/API_RenewOffering.html) and [ListOfferingTransactions](../../latest/APIReference/API_ListOfferingTransactions.html) operations are also available for this feature.

For information about using the Device Farm API, see [Automating Device Farm](api-ref.md).

------