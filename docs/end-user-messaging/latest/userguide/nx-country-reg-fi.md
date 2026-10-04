

# Finland registration
<a name="nx-country-reg-fi"></a>

The following registrations are available for Finland.

## Sender ID registration
<a name="nx-country-reg-fi-senderid"></a>

Follow these directions to register your sender ID in Finland. As required by Finnish regulation (Traficom Order 28 L/2025 M), all sender IDs used to send SMS messages to Finnish mobile numbers must be pre-registered with local operators.

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Registrations**, choose **Create registration**.
**Note**  
If you already created a registration when requesting the origination identity then you should use that registration form. 

   For **Registration form name** enter a friendly name.

   Choose **Next**.

1. In the **Sender ID info** section, enter the following:
   + For **Sender ID**, enter the sender ID to request. The sender ID must be between 3 and 11 alphanumeric characters. For more information on sender ID formatting rules, see sender ID considerations

   Choose **Next**.

1. In the **Company info** section, enter the following:
   + For **Company Name**, enter the name of your company as officially registered.
   + For **Company identification number – optional**, enter your tax ID or business registration number (such as a Finnish Business ID or VAT number), if available.
   + For **Company website**, enter the URL for your company's website.

   Choose **Next**.

1. In **Messaging Use Case**, do the following:
   + For **Use case category**, choose one of the following use case types:
     + **One-time passwords** – Use this for sending a user a one-time password or verification code.
     + **Account or security alerts** – Use this for sending account notifications or security alerts.
     + **Purchase or delivery notifications** – Use this if you only intend to send your users important notifications.
     + **Public service announcements** – An informational message that is meant to raise the audience's awareness about an important issue.
     + **Polling and surveys** – Use this to poll users on their preferences.
     + **Info on demand** – This is for sending users messages after they have sent a request.
     + **Promotions and marketing** – Use this for sending promotional or marketing messages.
     + **Other** – Use this if your use case doesn't fall into any other category. Be sure that you fill out the **Use case details** for this option.
   + Complete **Use case description** to provide additional context to the selected **Use case category**.

   Choose **Next**.

1. In **Message samples**, do the following:
   + For **Message Sample 1**, enter an example message of an SMS message body that will be sent to your end users.
   + For **Message Sample 2 – optional** and **Message Sample 3 – optional**, enter additional example messages, if needed, of the SMS message body that will be sent.

   Choose **Next**.

1. On the **Review and submit** page verify the information you are about to submit is correct. To make updates choose **Edit** next to the section.

1. Choose **Submit registration**.

## Dedicated number registration
<a name="nx-country-reg-fi-dednum"></a>

Registering a dedicated number is the first step in creating an origination identity.

To request a long code phone number, see the long code request process.

To register a short code number, see the short code request process.

Follow these directions to register your dedicated number in Finland.

**Complete Common Dedicated Number registration form**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Registrations**, choose the registration number to complete.
**Note**  
If you already created a registration when requesting the toll-free number then you can use that registration form. 

1. In the **Company info** section, enter the following:
   + For **Company Name**, enter the legal name of your company. 
   + For **Company identification number**, enter the legal identification number of your company (such as EIN or VAT).
   + For **Doing Business As (DBA) name**, enter the DBA or brand name if different from the legal name of your company.
   + For **Company website**, enter the full URL of your company website.

   Choose **Next**.

1. In the **Company Address** section, enter the following:
   + For **Address 1**, enter the physical street address associated with your company.
   + For **Address 2**, enter the unit number of the physical address, if applicable.
   + For **City** enter city where the physical address is located.
   + For **State / Province (optional)**, enter the state, province, or region where the physical address is located.
   + For **Postal code (optional)**, enter the postal code / ZIP code where the physical address is located.
   + For **Country code**, enter the two-digit ISO country code where the physical address is located.

   Choose **Next**.

1. In the ** Service Information and Use Case** section, enter the following:

   In order to give approval, mobile carriers need to know how you plan to use your dedicated number, and how you will interact with end users.
   + For **Service name**, Name of your SMS service or feature.
   + For **Use case category**, select the category which most closely aligns with your use case.
   + For **Use case description**, enter a description of your use case for sending SMS messages with this long code..
   + For **Monthly SMS volume**, enter a estimated number of SMS messages which will be sent from this long code each month.
   + For **Is this a one-way or two-way program?**, select whether you require only sending outbound messages with this number or if you require 2-way messaging (both outbound and inbound).
   + For **Opt-in Method**, enter a how the user will opt-in..
   + For **Opt-in method other**, ff you chose Other, please explain.
   + For **Opt-in method user experience flow 1**, provide a step-by-step description of the end user experience when signing up for the SMS service..
   + For **Opt-in mock-up 1**, attach a mock up showing the call-to-action or opt-in location.
   + For **Opt-in method user experience flow 2**, provide a step-by-step description of the end user experience when signing up for the SMS service.
   + For **Opt-in mock-up 2**, attach a mock up showing the call-to-action or opt-in location.
   + For **Opt-in method user experience flow 3**, provide a step-by-step description of the end user experience when signing up for the SMS service.
   + For **Opt-in mock-up 3**, attach a mock up showing the call-to-action or opt-in location.

   Choose **Next**.

1. On the **Review and submit** page verify the information you are about to submit is correct. To make updates choose **Edit** next to the section.

1. Choose **Submit registration**.