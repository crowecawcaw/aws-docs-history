

# Toll-free registration
<a name="nx-reg-type-tollfree"></a>

Toll-free numbers in the following countries and regions require registration before you can send messages. Select a country or region to review its requirements and the step-by-step registration process.

## United States Toll-free number registration process
<a name="nx-dednum-us-tfn"></a>

**Important**  
It can take up to 15 business days for your registration to be processed after it is submitted.

**Important**  
Starting September 15, 2026, all new toll-free number registrations require a **Privacy Policy URL** and a **Terms and Conditions URL**. Each URL must be publicly accessible and relevant to your business. Existing verified toll-free numbers are not affected by this requirement.

If you use AWS End User Messaging to send messages to recipients in the United States or the US territories of Puerto Rico, US Virgin Islands, Guam and American Samoa, you can use toll-free phone numbers (TFN) to deliver those messages. After you request a TFN you then complete and submit the registration for the TFN. Each TFN requires a specific use case. For example, if you register a TFN to use for one-time passwords, it can only be used for sending one-time passwords. If a TFN is used for anything other than the specified use case, it can be revoked. 

**Register a toll-free number**

1. You first need to request the toll-free number. When you request the toll-free number in the **Registration Required** window enter a friendly name for the registration. 

1. You can begin the registration process by choosing **Begin registration** or choose **Register later** to come back and complete the form.

**Topics**
+ [Toll-free number forbidden use cases](#registrations-tfn-forbidden-use-cases)
+ [Toll-free number registration rejection reasons](#registrations-tfn-rejection-reason)
+ [Toll-free number frequently asked questions](#registrations-tfn-register-faq)
+ [US toll-free number registration form](nx-dednum-us-tfn-register.md)
+ [TFN business verification](nx-dednum-us-tfn-verification.md)

### Toll-free number forbidden use cases
<a name="registrations-tfn-forbidden-use-cases"></a>

Please be aware that AWS is limited in our ability to send any messages or register TFNs for some use cases. Certain use cases are blocked entirely (for example, use cases related to controlled substance, or phishing) and other might be subject to high levels of filtering (for example, high risk financial messages). You might be unable to register TFNs associated with restricted content use cases defined in SMS message content best practices.

### Toll-free number registration rejection reasons
<a name="registrations-tfn-rejection-reason"></a>

If your Toll-free number registration was rejected, use the following table to determine why it was rejected and what you can do to fix your Toll-free number registration. After you determine why the registration was rejected, you can modify the existing registration to address that issue and resubmit. For more information, see editing a registration.


**Reason for rejection**  

| AWS End User Messaging rejection short description | AWS End User Messaging rejection long description | 
| --- | --- | 
| Compliant Opt In Missing | The opt-in process or screenshot is missing. A compliant opt-in process or screenshot will clearly specify how your recipient is able to provide their explicit consent to receive SMS messages. Some common rejection reasons: missing explicit language around SMS opt-in consent, mismatch between provided company name and opt-in screenshots, receiving a text message cannot be required to sign up for service, or SMS opt-in consent cannot be included in the Terms of Service. For more information, see obtaining permission best practices.  | 
| Invalid Business Connection | The contact information and company/application information does not have a clear connection. SMS Messages can't be sent on behalf of a 3rd party. To be verified please resubmit explaining the connection between your contact and company/application information. | 
| Invalid Company Info | The company information you provided is unable to be verified. In order to be verified please confirm your company website is valid and aligns with your company name and address. | 
| Invalid Multi Numbers | A single Toll Free number can only be associated with a single business. Please either resubmit a new registration request for each company with its own phone number or explain the connections between the multiple businesses called out. | 
| Invalid Overall | The information provided has been considered invalid. Please confirm your company website, use case, opt-in, and message samples are all valid inputs and align with other inputs in your registration. | 
| Invalid URL | The company URL you provided is unable to be accessed. To be verified please confirm your provided company website is valid and active. | 
| Non Compliant Opt In | The opt-in process or screenshot you have provided is either insufficient or non compliant. A compliant opt-in process or screenshot will clearly specify how your recipient is able to provide their explicit consent to receive SMS messages. Some common rejection reasons: missing explicit language around SMS opt-in consent, mismatch between provided company name and opt-in screenshots, receiving a text message cannot be required to sign up for service, or SMS opt-in consent cannot be included in the Terms of Service. For more information, see obtaining permission best practices. | 
| Non Compliant Opt In Consent | The opt-in process or screenshot you have provided does not show explicit consent. Explicit consent is the deliberate action of a user having the option to request a specific message. A compliant opt-in process or screenshot will clearly specify how your recipient is able to provide their explicit consent to receive SMS messages. Some common rejection reasons: missing explicit language around SMS opt-in consent, mismatch between provided company name and opt-in screenshots, receiving a text message cannot be required to sign up for service, or SMS opt-in consent cannot be included in the Terms of Service. For more information, see obtaining permission best practices. | 
| Non Compliant Opt In Third Party | The opt-in process or screenshot you have provided is either insufficient or non compliant due to opt-in information being shared with 3rd parties. A compliant opt-in process or screenshot will clearly specify how your recipient is able to provide their explicit consent to receive SMS messages and is not shared with 3rd parties. Please resubmit after you remove any language around opt-in information sharing or include language specifically stating opt-in information is not shared with 3rd parties. For more information, see obtaining permission best practices. | 
| Non Compliant Use Case | The use case and/or message samples provided are considered restricted content under US Telecom regulations. Please refer to the documentation below for a full list of items considered restricted content. If you believe your content is falsely considered restricted you can attempt to update your sample messages and use case and re-submit the registration. For more information, see obtaining permission best practices. | 
| Invalid Privacy Policy URL | The Privacy Policy URL provided is missing, inaccessible, or does not contain a valid privacy policy relevant to your business. Verify that the URL is publicly accessible, points to an active page, and contains privacy policy content consistent with the opt-in disclosures presented to your message recipients. | 
| Invalid Terms and Conditions URL | The Terms and Conditions URL provided is missing, inaccessible, or does not contain valid terms and conditions relevant to your business. Verify that the URL is publicly accessible, points to an active page, and contains terms and conditions content consistent with the opt-in disclosures presented to your message recipients. | 

### Toll-free number frequently asked questions
<a name="registrations-tfn-register-faq"></a>

Frequently asked questions about the toll-free number registration process.

#### Do I currently own a toll-free number?
<a name="registrations-tfn-register-faq1"></a>

**To check if you own a toll-free number**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **SMS and voice**, choose **Phone numbers**.

1. Toll-free numbers have their **type** listed as **toll free**.

#### Do I have to register my toll-free number?
<a name="registrations-tfn-register-faq7"></a>

Yes. If you currently own a toll-free number, you must register to use it. 

#### How do I purchase a toll-free number?
<a name="registrations-tfn-register-faq2"></a>

Follow the directions at the phone number request process to purchase a toll-free number.

#### How do I register my toll-free number?
<a name="registrations-tfn-register-faq3"></a>

If you already procured your TFN and created a registration form then follow the directions at the toll-free number registration to complete the form. If you need to create a registration then follow the directions at creating a registration to register a toll-free number. 

#### What is the registration status of my toll-free number and what does it mean?
<a name="registrations-tfn-register-faq4"></a>

Follow the directions at the registration status to check your registration and status.

#### What information do I need to provide?
<a name="registrations-tfn-register-faq5"></a>

You will need to provide your companies address, a business contact, and a use case. You can find the required information at the toll-free number registration.

#### What if my registration is rejected?
<a name="registrations-tfn-register-faq6"></a>

If your registration is rejected, its status will be changed to **Requires Updates** and you can make updates by following the directions in editing a registration.

#### What are the Privacy Policy URL and Terms and Conditions URL fields?
<a name="registrations-tfn-register-faq9"></a>

Starting September 15, 2026, all new toll-free number registrations require a **Privacy Policy URL** and a **Terms and Conditions URL**. Each field accepts a single publicly accessible URL with a maximum length of 500 characters. The URLs must point to documents that are relevant to your business and consistent with the opt-in disclosures presented to your message recipients. Existing verified toll-free numbers are not affected by this requirement.

#### What permissions do I need?
<a name="registrations-tfn-register-faq8"></a>

The IAM permissions that you use to visit the AWS End User Messaging console must be enabled with the {{`"sms-voice:*"`}} permission.