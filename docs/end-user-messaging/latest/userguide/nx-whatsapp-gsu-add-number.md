

# Step 2: Add a WhatsApp business phone number
<a name="nx-whatsapp-gsu-add-number"></a>

Adding a phone number is part of the same embedded sign-up flow you started in Step 1. The number you register is displayed to your customers when you send them a message. To use a number that is already in use with the WhatsApp Messenger or WhatsApp Business app, delete it from that app first.

------
#### [ Console ]

**To add and verify a WhatsApp phone number**

1. For **Add a phone number for WhatsApp**, enter the phone number to register.

1. For **Choose how you would like to verify your number**, choose **Text message** or **Phone call**, choose **Next**, enter the verification code you receive, and choose **Next**.

1. For **Phone number verification**, enter an existing PIN or set a new PIN for the number. Optionally choose a Meta data localization region and add tags.

1. Turn on **Message and event publishing** and choose a destination so you can log events and receive inbound messages. For **Destination type**, choose either Amazon SNS or an Connect Customer Customer instance. For Amazon SNS, choose a new or existing standard topic; FIFO topics are not supported. The destination must already exist and grant AWS End User Messaging permission to publish to it. This is required to respond to customer messages. For more information, see [Monitoring](nx-whatsapp-scale-monitoring.md).

1. Choose **Add phone number** to complete setup.

------

After the number is verified, your WABA and AWS End User Messaging accounts are linked and you are ready to send. To send messages at scale, complete Business Verification with Meta. For the full create, verify, and manage operations, see [Phone numbers](nx-features-phone-numbers.md).