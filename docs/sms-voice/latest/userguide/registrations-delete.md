

# Delete a registration in AWS End User Messaging SMS
<a name="registrations-delete"></a>

You can delete your registration if it is no longer needed. This will permanently delete the registration.

**To delete a registration**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Registrations**.

1. On the **Registrations** table, select the **Registration ID** that you want.

1. Choose **Delete registration** and in the window enter **delete**. 

1. Choose **Delete registration**.

## Delete a 10DLC campaign registration
<a name="registrations-delete-10DLC-campaign"></a>

You have to delete all phone numbers associated with a 10DLC campaign registration before you can delete the 10DLC campaign registration.

**Important**  
When you remove a phone number from a 10DLC campaign, you no longer have access to that phone number. Additionally, deleted 10DLC campaigns can't be restored.

**To delete a 10DLC campaign registration**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Registrations**.

1. On the **Registrations** table, select the **Registration ID** of the 10DLC campaign.

1. Choose **Associated resources** tab. 

1. For more information on releasing phone numbers, see [Release a phone number](phone-numbers-delete.md). 

   To release a phone number:

   1. Choose the phone number and then on the phone number detail's page choose **Release phone number**.

   1. On the **Release phone number** window enter **release** and choose **Release phone number**.

1. Once all phone numbers have been released, choose **Delete registration** and in the window enter **delete**.

## Delete a 10DLC brand registration
<a name="registrations-delete-10DLC-brand"></a>

To delete a 10DLC brand registration you must delete any 10DLC campaigns associated with the 10DLC brand registration. To delete a 10DLC campaign registration you must release all phone numbers associated to the 10DLC campaign registration.

**To delete a 10DLC brand registration**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Registrations**.

1. On the **Registrations** table, select the **Registration ID** of the 10DLC brand.

1. Choose **Associated resources** tab.

1. For each 10DLC campaign registration follow these directions to [release all phone numbers and delete a 10DLC campaign registration](#registrations-delete-10DLC-campaign). 

1. Once all 10DLC campaign registrations are deleted, choose **Delete registration** and in the window enter **delete**. 