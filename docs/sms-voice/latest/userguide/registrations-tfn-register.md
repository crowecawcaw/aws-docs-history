# US toll-free number registration form

###### Note

With our updated console experience you are now seeing a registration
**Name** field for your registration. This field is set to "–" as we
do not manually backfill any of your service values to prevent interruption to your service
and let you maintain your security posture. A registration **Name** is an
optional friendly name field that can be updated using the tags on the registration details
page. For more information on how to add a **Name** tag, see [Change a registration's name in AWS End User Messaging SMS](registrations-friendly-name.md "registrations-friendly-name.md").

After you've created your toll-free number registration you need to complete the form and
submit it for approval.

###### Complete a toll-free number registration

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Registrations**, choose the
   toll-free number registration to complete.

###### Note

If you already created a registration when requesting the toll-free number then you can use that
registration form. 3. In the **Company info** section, enter the following:

    * For **Company Name**, enter the name of your company.
    * For **Company website**, enter the URL for your company's
     website.
    * For **Address 1**, enter the street address of your corporate
     headquarters.
    * For **Address 2 - optional**, if needed enter suite number of
     your corporate headquarters.
    * For **City**, enter the city of your corporate headquarters.
    * For **State/Province**, enter the state of your corporate headquarters.
    * For **Zip Code/Postal code**, enter the zip code of your corporate
     headquarters.
    * For **Country**, enter the two digit ISO country code.
    * For **Business type**, choose the classification of your organization by ownership and purpose. Options include:




    	+ **Private profit** – Privately held for-profit company
    	+ **Public profit** – Publicly traded for-profit company
    	+ **Non-profit** – Non-profit organization
    	+ **Sole proprietor** – Sole proprietorship without employees
    	+ **Government** – Government entity
    ###### Note

    Unless you select **Sole proprietor**, the following three company identification fields are required: **Company identification number**, **Identification number type**, and **Identification number country**.
    * For **Company identification number**, enter your company's official tax identification or registration number (such as EIN or VAT) used to verify your business identity with telecommunications carriers. For example, `12-3456789`.
    * For **Identification number type**, choose the type of identification number you provided. This helps carriers verify your business credentials with the appropriate government authority. Options include EIN, CBN, CRN, PROVINCIAL\_NUMBER, VAT, ACN, ABN, BRN, SIREN, SIRET, NZBN, USt-IdNr, CIF, NIF, CNPJ, UID, NEQ, and OTHER.
    * For **Identification number country**, enter the two-letter ISO country code (for example, `US`, `CA`, `GB`) for the country where your identification number was issued. This must match the country of the authority that issued your identification number.
    * Choose **Next**.

4.  In the **Contact info** section, enter the following:

        * For **First Name**, enter the first name of the person who will be your business's point of contact.
        * For **Last Name**, enter the last name of the person who will be your business's point of contact.
        * For **Support Email**, enter the email address of the person who will
         be your business's point of contact.
        * For **Support Phone Number**, enter the phone number of
         the person who will be your business's point of contact. The
         phone number must start with a '+' and can't contain any spaces, hyphens, or parentheses.
         For example, `+1 (206) 555-0142` is not in the correct format, but
         `+12065550142` is.

    Choose **Next**.

5.  In **Messaging Use Case**, do the following:
    - For **Monthly SMS Volume**, choose the number of SMS messages that
      will be each month.
    - For **Use Case Category**, choose one of the following use case
      types:
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
      - **One time passcodes** – Use this for sending one-time passcodes for authentication.
      - **Non political polling and survey** – Use this to poll users on their preferences.
      - **Delivery notifications** – Use this for sending delivery status updates.
      - **Education** – Use this for educational content and notifications.
      - **Public announcements** – Use this for sending public service announcements.
      - **Customer care** – Use this for customer support communications.
      - **Non profit** – Use this for non-profit organization communications.
      - **Account notifications** – Use this for sending account-related notifications.
      - **Event notifications** – Use this for sending event-related updates.
      - **Financial transactions** – Use this for financial transaction notifications.
      - **Appointment reminders** – Use this for sending appointment reminders.
      - **Health care** – Use this for healthcare-related communications.
      - **Booking confirmations** – Use this for sending booking and reservation confirmations.
      - **Other** – Use this if your use case doesn't fall into any
        other category. Be sure that you fill out the **Use Case
        Details** for this option.

    - Complete **Use Case Details** to provide
      additional context to the selected **Use Case Category**.
    - For **Opt-in category**, choose one of the following options:
      - **Verbal**
      - **Digital form**
      - **Paper form**
      - **Text**
      - **QR code**

    - For **Opt-in Workflow Description** enter a description of how
      users consent to receive SMS messages. For example, by filling out an online form on
      your website.

    ###### Note

    If you don't have publicly accessible links to your Terms and Conditions and Privacy Policy
    documents then you can alternatively attach them to the registration
    form or another method like an [Amazon S3 presigned URL](../../../AmazonS3/latest/userguide/ShareObjectPreSignedURL.md "../../../AmazonS3/latest/userguide/ShareObjectPreSignedURL.md").
    - For **Opt-in workflow image**, upload an image showing how users
      consent to receiving messages. The supported file type is PNG and the maximum file
      size is 400KB. Additional information and examples of a compliant opt-in workflow can
      be found at [Obtain permission](best-practices.md#best-practices-sms-obtain-permission "best-practices.md#best-practices-sms-obtain-permission").

    ###### Important

    ###### Examples of opt-in mockups or screenshots:

        + **Website opt-in**: Mockup or screenshots of a
         web-form where the client adds their number and agrees to receive
         messages.
        + **Website Posting (Support)**: Where is the number advertised and where does the customer find the number to text in.
        + **Keyword or QR Code Opt-in**: Where does the
         customer find the keyword or QR code in order to opt-in to these messages.
        + **2FA/OTP**: Mockup or screenshot of opt-in if
         applicable, if verbal, provide a mockup or screenshot of the verbal opt-in
         script.
        + **Informational**: Provide a mockup or screenshot
         of a verbal consent workflow and provide the messaging content.

6.  Choose **Next**.
7.  In **Message samples**, do the following:
    - For **Message Sample 1**, enter an example message of an SMS message
      body that will be sent to your end users.
    - For **Message Sample 2 – optional** and **Message Sample
      3 – optional**, enter additional example messages, if needed, of the
      SMS message body that will be sent.

8.  Choose **Next**.
9.  On the **Review and submit** page verify the information you are about to submit is correct. To make updates choose **Edit** next to the section.
10. Choose **Submit registration**.
