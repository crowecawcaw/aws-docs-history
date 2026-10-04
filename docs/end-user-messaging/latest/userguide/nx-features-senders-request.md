

# Request a sender ID
<a name="nx-features-senders-request"></a>

Before you request a sender ID, verify that they are available in the destination country. See the SMS supported countries and regions documentation.

**Note**  
Some countries require you to register your sender ID before it can be used for sending. All countries with sender ID registration requirements have self-service registration forms available in the console. For the full list of countries and their registration walkthroughs, see the country registration documentation.

To request a sender ID using the AWS End User Messaging console, follow these steps:

**Request a sender ID**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Sender ID** and then **Request originator**.

1. On the **Select country** page, choose the country from the dropdown that messages will be sent to. Choose **Next** to continue defining the use case and for a suggested phone number or sender ID type.

1. In the **Messaging use case** section, under **Number capabilities**, choose **Text messages (SMS)**, **Text to audio messages (Voice)**, or both depending on your requirements.

1. Under **Estimated monthly SMS message volume per month – optional**, choose the estimated number of SMS messages you will send each month.

1. For **Company headquarters – optional**, choose **Local** if your company headquarters is in the same country as your recipients, or **International** if it is not.

1. For **Two-way messaging**, choose **Yes** if you require two-way messaging.

1. Choose **Next**.

1. Under **Originator type**, choose **Sender ID**. If sender ID isn't available, choose **Previous** to go back and modify your use case.

   In the **Sender ID** field, enter a sender ID. The sender ID must be 1-11 alphanumeric characters including letters (A-Z), numbers (0-9), or hyphens (-). It must contain at least one letter and cannot start or end with a hyphen. A minimum of 3 characters is recommended.

1. Use **Resource policy** to share the sender ID with other AWS accounts or AWS services. You must use **Resource policy** to share the sender ID with Amazon Pinpoint or Amazon SNS even if you are using the same AWS account.

1. Choose **Next**.

1. On **Review and request**, verify and edit your request before submitting it. Choose **Request**.

1. A **Registration Required** window might appear depending on the type of number you requested.

   1. For **Registration form name**, enter a name.

   1. Choose **Complete registration** to finish registering the sender ID, or **Register later**.
**Important**  
You are still billed the recurring monthly lease fee regardless of registration status.