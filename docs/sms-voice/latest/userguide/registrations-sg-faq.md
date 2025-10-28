# Singapore sender ID registration frequently

asked questions

Frequently asked questions about the Singapore sender ID number registration process
with AWS End User Messaging SMS.

###### To check if you own a Singapore sender ID

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**, choose
   **Sender ID**.
3. On the **Sender IDs** page, you can search by two letter country code `SG` to find if you have any Singapore sender IDs.
   While a typical review takes 1 – 3 weeks, it can take up to 5 weeks or longer in some cases to verify your information with government agencies.

A UEN is a Singapore business ID issued by Accounting and Corporate Regulatory Agency
(ACRA). Local companies and businesses in Singapore can get a UEN by applying through
ACRA. Once you pass through the registration and standard incorporation procedure, it will
be issued. You can apply for a UEN with ACRA via [Bizfile](https://www.bizfile.gov.sg/ngbbizfileinternet/faces/oracle/webcenter/portalapp/pages/BizfileHomepage.jspx "https://www.bizfile.gov.sg/ngbbizfileinternet/faces/oracle/webcenter/portalapp/pages/BizfileHomepage.jspx").

Yes. If you haven't registered your Singapore Sender ID any message sent using a Sender ID will likely have its ID
changed to **LIKELY-SCAM**

Follow the directions at [Create a new registration using the AWS End User Messaging SMS console](registrations-create.md "registrations-create.md") to register a Sender
ID.

Follow the directions at [Check a registration's status in AWS End User Messaging SMS](registrations-status.md "registrations-status.md") to check your registration
and status.

You will need to provide your companies address, a business contact, and a use case. You
can find the required information at [Create a new registration using the AWS End User Messaging SMS console](registrations-create.md "registrations-create.md").

If your registration is rejected, its status will be changed to **Requires
Updates** and you can make updates by following the directions in [Edit a registration in AWS End User Messaging SMS](registrations-edit.md "registrations-edit.md").

The IAM user/role that you use to visit the AWS End User Messaging SMS console must be enabled with the
`“sms-voice:*”` permission.

Yes. For more information on sender ID formatting rules, see [Considerations for a sender ID](sender-id.md#sender-id-considerations "sender-id.md#sender-id-considerations").
