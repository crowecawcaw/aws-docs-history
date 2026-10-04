

# Austria registration
<a name="nx-country-reg-at"></a>

The following registrations are available for Austria.

## Sender ID registration
<a name="nx-country-reg-at-senderid"></a>

All alphanumeric sender IDs used to send SMS messages to Austrian mobile numbers (\+43) must be registered with the RTR (Rundfunk und Telekom Regulierungs-GmbH), the Austrian telecommunications regulator. Starting October 1, 2026, unregistered alphanumeric sender IDs will be blocked by Austrian mobile operators and will not deliver messages to Austrian recipients.

Dedicated phone numbers (local long codes or short codes) are not affected by this regulation and do not require registration.

Austria sender IDs must comply with the following rules:
+ Minimum 3 characters, maximum 11 characters
+ Permitted characters: A-Z, a-z, 0-9, space, \+, -, \_, &
+ German umlauts (ä, ö, ü, ß) are not permitted
+ Cannot begin with a plus sign (\+)
+ Cannot have leading or trailing spaces
+ Cannot resemble a phone number
+ Generic terms are not permitted (for example: doctor, pharmacy, OTP, SMS info)
+ Case-sensitive — registering "MyBrand" does not cover "MYBRAND"

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Registrations**, choose **Create registration**.
**Note**  
If you already created a registration when requesting the origination identity, use that existing registration form.

   For **Registration form name**, enter a friendly name.

   Choose **Next**.

1. In the **Sender ID info** section, enter the following:
   + For **Sender ID**, enter the sender ID to register. The sender ID must be between 3 and 11 characters, using only permitted characters (A-Z, a-z, 0-9, space, \+, -, \_, &). No German umlauts are allowed. The value is case-sensitive — register the exact casing you intend to use when sending messages.
   + For **Sender ID description**, provide a description of how this sender ID relates to your company. If the connection between your sender ID and your company name is not obvious, upload proof such as a trademark certificate in the **Proof of sender ID connection** field.

   Choose **Next**.

1. In the **Company info** section, enter the following:
   + For **Company name**, enter your company name as officially registered.
   + For **Company address**, enter your company's registered address including postal code.
   + For **Contact email**, enter the email address for communications about this registration.

   Choose **Next**.

1. In the **Proof of sender ID connection** section:
   + If your sender ID does not obviously match your company name, upload supporting documentation such as a trademark certificate that demonstrates your right to use the sender ID.

   Choose **Next**.

1. In the **Letter of authorization** section:
   + Download, complete, and attach the [letter of authorization](samples/Austria_SenderId_LetterOfAuthorization.zip). Valid upload file types are PDF, PNG, and JPEG with a maximum file size of 500KB.

   Choose **Next**.

1. In **Messaging Use Case**, do the following:
   + For **Use case category**, choose the category that best describes your messaging use case.
   + For **Use case description**, provide additional context about how you will use this sender ID.

   Choose **Next**.

1. In **Message samples**, do the following:
   + For **Message Sample 1**, enter an example SMS message body that will be sent to your end users.
   + For **Message Sample 2 – optional** and **Message Sample 3 – optional**, enter additional example messages if needed.

   Choose **Next**.

1. On the **Review and submit** page, verify the information you are about to submit is correct. To make updates, choose **Edit** next to the section.

1. Choose **Submit registration**.

What happens if I send messages with an unregistered sender ID after October 1, 2026?  
Messages sent using an unregistered alphanumeric sender ID will be blocked by Austrian mobile operators and will not be delivered.

Can I update my registration details after submitting?  
No. Once a registration is submitted, the associated information cannot be amended. You must create a new registration and wait for the 14-day activation period to complete.

Can I re-register a deleted sender ID?  
Yes, but you must wait 30 days after deletion before you can re-register the same sender ID.

Are dedicated phone numbers affected by this regulation?  
No. Dedicated phone numbers (local long codes, short codes) are not affected and do not require registration.

Is my sender ID case-sensitive?  
Yes. Austria sender ID registrations are case-sensitive. If you register "MyBrand", messages sent as "MYBRAND" or "mybrand" are treated as different sender IDs and will be blocked if not separately registered.

## Dedicated number registration
<a name="nx-country-reg-at-dednum"></a>

Registering a dedicated number is the first step in creating an origination identity.

To request a long code phone number, see the long code request process.

Follow these directions to register your dedicated number in Australia.

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