

# Singapore registration
<a name="nx-country-reg-sg"></a>

The following registrations are available for Singapore.

## Sender ID registration
<a name="nx-country-reg-sg-senderid"></a>

AWS End User Messaging customers are able to send SMS traffic in Singapore using a Sender ID that has been registered through the Singapore SMS Sender ID Registry (SSIR). SSIR was launched in March of 2022 through the Singapore Network Information Centre (SGNIC) which is owned by Info-communications Media Development Authority (IMDA) of Singapore, and enables organizations to register their Sender ID when sending SMS to mobile phones in Singapore. To use a registered Singapore Sender ID you must obtain a Unique Entity Number (UEN), then submit a request to AWS End User Messaging to allow-list your account for usage of your Sender ID and finally complete the registration process through SSIR. 

If you do not register your sender ID any message sent using a sender ID will have its ID changed to **LIKELY-SCAM** per regulatory agency rules. Regulators will filter or block unregistered traffic at their discretion. 

**Important**  
Your Singapore registration must be completed in this order:  
[Registering for a Singapore Unique Entity Number (UEN)](#nx-registration-singapore-registrations-sg-uen)
Create a registration with **Registration type** set to Singapore sender ID registration and complete the registration form.
[Registering a Sender ID with Singapore Network Information Centre (SGNIC)](#nx-registration-singapore-registrations-sg-sgnic)

**Topics**
+ [Singapore Unique Entity Number (UEN)](#nx-registration-singapore-registrations-sg-uen)
+ [Register a Sender ID with Singapore Network Information Centre (SGNIC)](#nx-registration-singapore-registrations-sg-sgnic)
+ [Singapore sender ID registration frequently asked questions](#nx-registration-singapore-registrations-sg-faq)
+ [Singapore sender ID registration form](#nx-registration-singapore-form)

### Registering for a Singapore Unique Entity Number (UEN)
<a name="nx-registration-singapore-registrations-sg-uen"></a>

To start a registration with the SSIR you must first obtain a Singapore Unique Entity Number (UEN). A UEN is a unique entity number you receive when you register your business with the Account and Corporate Registry Authority (ACRA), for more information see [Who Must Register with ACRA?](https://www.acra.gov.sg/how-to-guides/before-you-start/who-must-register). The amount of time to process can vary depending on how easily the ACRA can validate your request. 

### Registering a Sender ID with Singapore Network Information Centre (SGNIC)
<a name="nx-registration-singapore-registrations-sg-sgnic"></a>

To register a sender ID with Singapore Network Information Centre (SGNIC) there are two steps that must be completed in the following order: 

**Register a sender ID with Singapore Network Information Centre (SGNIC)**

1. You must first work with AWS End User Messaging to register your Singapore (SG) Sender ID for your account. After this step is complete you can proceed to the next step.

1. Work with SGNIC to register your sender ID using the process at [SGNIC SMS Sender ID Registry](https://smsregistry.sg/web/login).

   1. When completing the process list AMCS SG Private Limited (Amazon Media Communications Services) as your participating aggregator.

**Warning**  
Doing these steps out of order might result in your sender ID being blocked by the service or will prevent your Sender ID from being preserved on the mobile device. 

**Note**  
Please note that you are required to submit a sender ID registration from each individual AWS account you require to use the sender ID.

### Singapore sender ID registration frequently asked questions
<a name="nx-registration-singapore-registrations-sg-faq"></a>

Frequently asked questions about the Singapore sender ID number registration process with AWS End User Messaging.

#### Do I currently have a Singapore sender ID
<a name="nx-registration-singapore-registrations-sg-faq1"></a>

**To check if you own a Singapore sender ID**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Sender ID**.

1. On the **Sender IDs** page, you can search by two letter country code **SG** to find if you have any Singapore sender IDs.

#### How long will registration take?
<a name="nx-registration-singapore-registrations-sg-faq9"></a>

While a typical review takes 1 – 3 weeks, it can take up to 5 weeks or longer in some cases to verify your information with government agencies.

#### What is a Unique Entity Number (UEN) and how do i get one?
<a name="nx-registration-singapore-registrations-sg-faq2"></a>

A UEN is a Singapore business ID issued by Accounting and Corporate Regulatory Agency (ACRA). Local companies and businesses in Singapore can get a UEN by applying through ACRA. Once you pass through the registration and standard incorporation procedure, it will be issued. You can apply for a UEN with ACRA via [Bizfile](https://www.bizfile.gov.sg/ngbbizfileinternet/faces/oracle/webcenter/portalapp/pages/BizfileHomepage.jspx).

#### Do I have to register for a Singapore Sender ID?
<a name="nx-registration-singapore-registrations-sg-faq7"></a>

Yes. If you haven't registered your Singapore Sender ID any message sent using a Sender ID will likely have its ID changed to **LIKELY-SCAM**

#### How do I register my Singapore Sender ID with AWS End User Messaging?
<a name="nx-registration-singapore-registrations-sg-faq3"></a>

Follow the directions at Create a registration to register a Sender ID.

#### What is the registration status of my Singapore Sender ID and what does it mean?
<a name="nx-registration-singapore-registrations-sg-faq4"></a>

Follow the directions at registration status to check your registration and status.

#### What information do I need to provide?
<a name="nx-registration-singapore-registrations-sg-faq5"></a>

You will need to provide your companies address, a business contact, and a use case. You can find the required information at Create a registration.

#### What if my Singapore Sender ID registration is rejected?
<a name="nx-registration-singapore-registrations-sg-faq6"></a>

If your registration is rejected, its status will be changed to **Requires Updates** and you can make updates by following the directions in Edit a registration.

#### What permissions do I need?
<a name="nx-registration-singapore-registrations-sg-faq8"></a>

The IAM user/role that you use to visit the AWS End User Messaging console must be enabled with the {{`“sms-voice:*”`}} permission.

#### Are there any restrictions to the formatting or allowed special characters for Singapore Sender IDs?
<a name="nx-registration-singapore-registrations-sg-faq10"></a>

Yes. For more information on sender ID formatting rules, see sender ID considerations.

#### What should I do if my Singapore Sender ID registration shows a status of Revoke?
<a name="nx-registration-singapore-registrations-sg-faq11"></a>

If your Singapore Sender ID registration shows a status of **Revoke**, this indicates that your Sender ID registration has been suspended by the Singapore SMS Sender ID Registry (SSIR). To resolve this issue, you must contact the Singapore Network Information Centre (SGNIC) directly to obtain further details regarding your registration suspension.

After you have resolved the issue with SGNIC, you can re-submit your existing registration through the AWS End User Messaging console. You do not need to create a new registration request.

### Singapore sender ID registration form
<a name="nx-registration-singapore-form"></a>

**Note**  
With our updated console experience you are now seeing a registration **Name** field for your registration. This field is set to "–" as we do not manually backfill any of your service values to prevent interruption to your service and let you maintain your security posture. A registration **Name** is an optional friendly name field that can be updated using the tags on the registration details page. For more information on how to add a **Name** tag, see registration name.

AWS End User Messaging customers are able to send SMS traffic in Singapore using a Sender ID that has been registered through the Singapore SMS Sender ID Registry (SSIR). SSIR was launched in March of 2022 through the Singapore Network Information Centre (SGNIC) which is owned by Info-communications Media Development Authority (IMDA) of Singapore, and enables organizations to register their Sender ID when sending SMS to mobile phones in Singapore. To use a registered Singapore Sender ID you must obtain a Unique Entity Number (UEN), then submit a request to AWS End User Messaging to allow-list your account for usage of your Sender ID and finally complete the registration process through SSIR. 

**Note**  
Before you request and register your sender ID you must obtain a Singapore Unique Entity Number (UEN). For more information, see [Registering for a Singapore Unique Entity Number (UEN)](#nx-registration-singapore-registrations-sg-uen).

**Complete a Singapore sender ID registration**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Registrations**, choose the Singapore sender ID registration to complete.

1. In the **Company info** section, enter the following:
   + For **Company Name**, enter the name of your company. 
   + For **Tax ID**, enter you Singapore Unique Entity Number. 
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
   + For **Support Email**, enter the email address of the person who will be your business's point of contact.
   + For **Support Phone Number**, enter the phone number of the person who will be your business's point of contact.

   Choose **Next**.

1. In the **Sender ID info** section, enter the following:
   + For **Sender ID**, enter the sender ID to request. For more information on sender ID formatting rules, see sender ID considerations
   + For **Are you registering on behalf of another brand/entity?** if yes then choose True. If you are not the end user sending the messages you are considered a "Representative" of the other brand/entity.
   + For **Letter of authorization image – optional**, if you checked the box as **Registering on behalf of another brand/entity?** , upload an image of the complete Letter of Authorization (LOA). The supported file type is PNG and the maximum file size is 400KB. A template for the LOA can be [downloaded](samples/Singapore_Sender_ID_Registration_LOA_Template.zip) for your convenience. 
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
**Note**  
After your registration has been submitted you need to register the send ID with Singapore Network Information Centre (SGNIC). For more information on how to register, see [Registering a Sender ID with Singapore Network Information Centre (SGNIC)](#nx-registration-singapore-registrations-sg-sgnic). Your registration will be considered complete once we have received signal from SGNIC.