

# United Kingdom registration
<a name="nx-country-reg-gb"></a>

The following registrations are available for United Kingdom.

## Sender ID registration
<a name="nx-country-reg-gb-senderid"></a>

**Note**  
With our updated console experience you are now seeing a registration **Name** field for your registration. This field is set to "–" as we do not manually backfill any of your service values to prevent interruption to your service and let you maintain your security posture. A registration **Name** is an optional friendly name field that can be updated using the tags on the registration details page. For more information on how to add a **Name** tag, see registration name.

The United Kingdom's (UK) Mobile Ecosystem Forum (MEF) SMS Sender ID Protection Registry was established to help the identification and blocking of fraudulent SMS messages, protecting consumers as well as legitimate businesses and organizations. The registry enables organizations to register the Sender IDs used when sending SMS to customers in the UK, limiting the ability of fraudsters to impersonate a brand.

If you have protected your Sender ID with MEF you are required to register your Sender ID through AWS End User Messaging. 

**Important**  
If your Sender ID is protected by MEF then a completed Letter of Authorization (LOA) is required. The information provided must be of the end company. If you are registering on behalf of a company they are required to authorize AWS and the LOA should not include or reference your company information.  
Download the template for the [LOA](samples/AWS_Protected_Sender_ID_Letter-of-Authorisation_UK.zip).
Clearly specify the sender ID requested and have other details such as website and sample message templates filled in correctly with no missing details. The casing of the Sender ID must match what is registered with MEF.   
Complete all highlighted fields.
The LOA must be dated within the last 30 days.
Create a PDF of the LOA to upload as part of completing the **Sender ID info** section of your [UK registration](#nx-country-reg-gb). The maximum file size is 400 KB.
Complete the [UK sender ID registration form](#nx-country-reg-gb) and omit the **Letter of authorization image – optional** field.

**Topics**
+ [United Kingdom registration form](#nx-registration-uk-registrations-uk-form)

### United Kingdom sender ID registration form
<a name="nx-registration-uk-registrations-uk-form"></a>

Complete the following form to register your sender ID in the United Kingdom. If your sender ID is protected by then a completed [Letter of Authorization (LOA)](#nx-country-reg-gb) is required as well.

**Complete a United Kingdom sender ID registration**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Registrations**, choose the United Kingdom sender ID registration to complete.

1. In the **Company info** section, enter the following:
   + For **Company Name**, enter the name of your company. 
   + For **Tax ID or Business Registration Number**, enter you tax ID. 
   + For **Company website**, enter the URL for your company's website. 
   + For **Address 1**, enter the street address of your corporate headquarters. 
   + For **Address 2 - optional**, if needed enter suite number of your corporate headquarters. 
   + For **City**, enter the city of your corporate headquarters. 
   + For **State/Province (optional)**, enter the state of your corporate headquarters. 
   + For **Zip Code/Postal code**, enter the zip code of your corporate headquarters. 
   + For **Country**, enter the two digit ISO country code. 
   + Choose **Next**.

1. In the **Contact info** section, enter the following:
   + For **First Name**, enter the first name of the person who will be your business's point of contact.
   + For **Last Name**, enter the last name of the person who will be your business's point of contact. 
   + For **Contact Email**, enter the email address of the person who will be your business's point of contact.
   + For **Contact Phone Number**, enter the phone number of the person who will be your business's point of contact.

   Choose **Next**.

1. In the **Sender ID info** section, enter the following:
   + For **Sender ID**, enter the sender ID to request. For more information on sender ID formatting rules, see sender ID considerations
   + For **Letter of authorization image – optional**: Information provided must be that of the end company. If you are registering on behalf of a company they are required to authorize AWS and the LOA should not include or reference your company information.
     + Download the template for the [LOA](samples/AWS_Protected_Sender_ID_Letter-of-Authorisation_UK.zip).
     + Clearly specify the sender ID requested and have other details such as website and sample message templates filled in correctly with no missing details. The casing of the Sender ID must match what is registered with MEF. 

       Complete all highlighted fields.
     + The LOA must be dated within the last 30 days.
     + Create a PDF of the LOA to upload as part of completing the **Sender ID info** section for your UK registration. The maximum file size is 400 KB.
   + For **Sender ID connection – optional** you can add more details about the connection between the requested sender ID and company name.

   Choose **Next**.

1. In **Messaging Use Case**, do the following:
   + For **Monthly SMS Volume**, choose the number of SMS messages that will be each month.
   + For **Use case category**, choose one of the following use case types: 
     +  **Two-factor authentication** – Use this for sending two factor authentication codes.
     +  **One-time passwords** – Use this for sending a user a one time password.
     +  **Notifications** – Use this if you only intend to send your users important notifications.
     +  **Polling and surveys** – Use this to poll users on their preferences.
     +  **Info on demand** – This is for sending users messages after they have sent a request.
     +  **Promotions and Marketing** – Use this if you only intend to send marketing messages to your users.
     +  **Other** – Use this if your use case doesn't fall into any other category. Be sure that you fill out the **Use case details** for this option.
   + Complete **Use case details** to provide additional context to the selected **Use case category**.

1. Choose **Next**.

1. In **Message samples**, do the following:
   + For **Message Sample 1**, enter an example message of an SMS message body that will be sent to your end users. 
   + For **Message Sample 2 – optional** and **Message Sample 3 – optional**, enter additional example messages, if needed, of the SMS message body that will be sent.

1. Choose **Next**.

1. On the **Review and submit** page verify the information you are about to submit is correct. To make updates choose **Edit** next to the section.

1. Choose **Submit registration**.

## Dedicated number registration
<a name="nx-country-reg-gb-dednum"></a>

Registering a dedicated number is the first step in creating an origination identity.

To request a long code phone number, see the long code request process.

To register a short code number, see the short code request process.

Follow these directions to register your dedicated number in Italy.

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