# Singapore sender ID registration form

###### Note

With our updated console experience you are now seeing a registration
**Name** field for your registration. This field is set to "–" as we
do not manually backfill any of your service values to prevent interruption to your service
and let you maintain your security posture. A registration **Name** is an
optional friendly name field that can be updated using the tags on the registration details
page. For more information on how to add a **Name** tag, see [Change a registration's name in AWS End User Messaging SMS](registrations-friendly-name.md "registrations-friendly-name.md").

AWS End User Messaging SMS customers are able to send SMS traffic in Singapore using a Sender ID that has been
registered through the Singapore SMS Sender ID Registry (SSIR). SSIR was launched in March of
2022 through the Singapore Network Information Centre (SGNIC) which is owned by
Info-communications Media Development Authority (IMDA) of Singapore, and enables organizations
to register their Sender ID when sending SMS to mobile phones in Singapore. In order to use a
registered Singapore Sender ID you must obtain a Unique Entity Number (UEN), then submit a
request to AWS End User Messaging SMS to allow-list your account for usage of your Sender ID and finally complete the
registration process through SSIR.

###### Note

Before you request and register your sender ID you must obtain a Singapore Unique Entity Number (UEN).
For more information, see [Registering for a Singapore Unique Entity
Number (UEN)](registrations-sg-uen.md "registrations-sg-uen.md").

###### Complete a Singapore sender ID registration

1.  Open the AWS End User Messaging SMS console at
    [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2.  In the navigation pane, under **Registrations**, choose the
    Singapore sender ID registration to complete.
3.  In the **Company info** section, enter the following:
    - For **Company Name**, enter the name of your company.
    - For **Tax ID**, enter you Singapore Unique Entity Number.
    - For **Company website**, enter the URL for your company's
      website.
    - For **Address 1**, enter the street address of your corporate
      headquarters.
    - For **Address 2 - optional**, if needed enter suite number of
      your corporate headquarters.
    - For **City**, enter the city of your corporate headquarters.
    - For **State/Province**, enter the state of your corporate headquarters.
    - For **Zip Code/Postal code**, enter the zip code of your corporate
      headquarters.
    - For **Country**, enter the two digit ISO country code.
    - Choose **Next**.

4.  In the **Contact info** section, enter the following:

        * For **First Name**, enter the first name of the person who will be your business's point of contact.
        * For **Last Name**, enter the last name of the person who will be your business's point of contact.
        * For **Support Email**, enter the email address of the person who will
         be your business's point of contact.
        * For **Support Phone Number**, enter the phone number of the person who
         will be your business's point of contact.

    Choose **Next**.

5.  In the **Sender ID info** section, enter the following:

        * For **Sender ID**, enter the sender ID to request. For more information on sender ID formatting rules, see [Considerations for a sender ID](sender-id.md#sender-id-considerations "sender-id.md#sender-id-considerations")
        * For **Are you registering on behalf of another brand/entity?** if yes then choose True. If you are not the end user sending the messages you are considered a "Representative" of the other brand/entity.
        * For **Letter of authorization image – optional**, if you checked the
         box as **Registering on behalf of another brand/entity?** , upload an image of the complete Letter of Authorization (LOA). The
         supported file type is PNG and the maximum file size is 400KB. A template for the LOA
         can be [downloaded](samples/Singapore_Sender_ID_Registration_LOA_Template.md "samples/Singapore_Sender_ID_Registration_LOA_Template.md") for your convenience.
        * For **Sender ID connection – optional** you can add more details about the connection between the requested sender ID and company name.

    Choose **Next**.

6.  In **Messaging Use Case**, do the following:
    - For **Monthly SMS Volume**, choose the number of SMS messages that
      will be each month.
    - For **Use case category**, choose one of the following use
      case types:
      - **Two-factor authentication** – Use this for sending two
        factor authentication codes.
      - **One-time passwords** – Use this for sending a user a one
        time password.
      - **Notifications** – Use this if you only intend to send
        your users important notifications.
      - **Polling and surveys** – Use this to poll users on their
        preferences.
      - **Info on demand** – This is for sending users messages
        after they have sent a request.
      - **Promotions and Marketing** – Use this if you only intend
        to send marketing messages to your users.
      - **Other** – Use this if your use case doesn't
        fall into any other category. Be sure that you fill out the
        **Use case details** for this option.

    - Complete **Use case details** to provide additional
      context to the selected **Use case category**.

7.  Choose **Next**.
8.  In **Message samples**, do the following:
    - For **Message Sample 1**, enter an example message of an SMS message
      body that will be sent to your end users.
    - For **Message Sample 2 – optional** and **Message Sample
      3 – optional**, enter additional example messages, if needed, of the
      SMS message body that will be sent.

9.  Choose **Next**.
10. On the **Review and submit** page verify the information you are about to submit is correct. To make updates choose **Edit** next to the section.
11. Choose **Submit registration**.

###### Note

After your registration has been submitted you need to register the send ID with
Singapore Network Information Centre (SGNIC). For more information on how to
register, see [Registering a Sender ID with Singapore Network Information Centre (SGNIC)](registrations-sg-sgnic.md "registrations-sg-sgnic.md"). Your
registration will be considered complete once we have received signal from
SGNIC.
