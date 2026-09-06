

# Singapore sender ID registration frequently asked questions
<a name="registrations-sg-faq"></a>

Frequently asked questions about the Singapore sender ID number registration process with AWS End User Messaging SMS.

## Do I currently have a Singapore sender ID
<a name="registrations-sg-faq1"></a>

**To check if you own a Singapore sender ID**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Sender ID**.

1. On the **Sender IDs** page, you can search by two letter country code **SG** to find if you have any Singapore sender IDs.

## How long will registration take?
<a name="registrations-sg-faq9"></a>

While a typical review takes 1 – 3 weeks, it can take up to 5 weeks or longer in some cases to verify your information with government agencies.

## What is a Unique Entity Number (UEN) and how do i get one?
<a name="registrations-sg-faq2"></a>

A UEN is a Singapore business ID issued by Accounting and Corporate Regulatory Agency (ACRA). Local companies and businesses in Singapore can get a UEN by applying through ACRA. Once you pass through the registration and standard incorporation procedure, it will be issued. You can apply for a UEN with ACRA via [Bizfile](https://www.bizfile.gov.sg/ngbbizfileinternet/faces/oracle/webcenter/portalapp/pages/BizfileHomepage.jspx).

## Do I have to register for a Singapore Sender ID?
<a name="registrations-sg-faq7"></a>

Yes. If you haven't registered your Singapore Sender ID any message sent using a Sender ID will likely have its ID changed to **LIKELY-SCAM**

## How do I register my Singapore Sender ID with AWS End User Messaging SMS?
<a name="registrations-sg-faq3"></a>

Follow the directions at [Create a new registration using the AWS End User Messaging SMS console](registrations-create.md) to register a Sender ID.

## What is the registration status of my Singapore Sender ID and what does it mean?
<a name="registrations-sg-faq4"></a>

Follow the directions at [Check a registration's status in AWS End User Messaging SMS](registrations-status.md) to check your registration and status.

## What information do I need to provide?
<a name="registrations-sg-faq5"></a>

You will need to provide your companies address, a business contact, and a use case. You can find the required information at [Create a new registration using the AWS End User Messaging SMS console](registrations-create.md).

## What if my Singapore Sender ID registration is rejected?
<a name="registrations-sg-faq6"></a>

If your registration is rejected, its status will be changed to **Requires Updates** and you can make updates by following the directions in [Edit a registration in AWS End User Messaging SMS](registrations-edit.md).

## What permissions do I need?
<a name="registrations-sg-faq8"></a>

The IAM user/role that you use to visit the AWS End User Messaging SMS console must be enabled with the {{`“sms-voice:*”`}} permission.

## Are there any restrictions to the formatting or allowed special characters for Singapore Sender IDs?
<a name="registrations-sg-faq10"></a>

Yes. For more information on sender ID formatting rules, see [Considerations for a sender ID](sender-id.md#sender-id-considerations).

## What should I do if my Singapore Sender ID registration shows a status of Revoke?
<a name="registrations-sg-faq11"></a>

If your Singapore Sender ID registration shows a status of **Revoke**, this indicates that your Sender ID registration has been suspended by the Singapore SMS Sender ID Registry (SSIR). To resolve this issue, you must contact the Singapore Network Information Centre (SGNIC) directly to obtain further details regarding your registration suspension.

After you have resolved the issue with SGNIC, you can re-submit your existing registration through the AWS End User Messaging SMS console. You do not need to create a new registration request.