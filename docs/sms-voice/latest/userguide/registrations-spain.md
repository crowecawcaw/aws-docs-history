# Spain sender ID registration in AWS End User Messaging SMS

All alphanumeric sender IDs used to send SMS messages to Spanish mobile numbers (+34) must be registered in the CNMC (Comisión Nacional de los Mercados y la Competencia) National Alias Registry. Starting September 15, 2026, unregistered sender IDs will be blocked and will not deliver messages to Spanish recipients.

Unregistered alphanumeric sender IDs will be blocked by Spanish mobile operators starting September 15, 2026. Generic sender IDs that do not clearly identify your business are not permitted by CNMC and cannot be registered.

Dedicated phone numbers (local long codes or short codes, international toll-free numbers) are not affected by this regulation and do not require registration.

###### Important

- Starting September 15, 2026, Spanish mobile operators will block all SMS messages sent using unregistered alphanumeric sender IDs. Complete your CNMC registration before this date to avoid delivery disruptions.
- New Spain short code provisioning is temporarily on hold. If you need a dedicated number for Spain, request a long code instead. For more information, see [Dedicated phone numbers for Spain](dedicated-number-spain.md "dedicated-number-spain.md").
- We are currently processing new information about how customers can register their Sender IDs in the CNMC Portal as part of the Spain Sender ID registration process. We will update our public documentation as soon as we have concrete details.

###### CNMC portal access and digital certificate requirements

The CNMC registration portal requires authentication with a valid digital certificate. The following certificate types are accepted:

- A qualifying digital certificate issued by the Spanish government
- An eIDAS-compliant qualified digital certificate issued by one of the EU countries listed below
  Qualifying EU countries for eIDAS certificates: Austria, Belgium, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Poland, Portugal, Romania, Slovakia, Slovenia, and Sweden.

If you do not have a qualifying digital certificate issued by the Spanish government or by one of the qualifying EU countries listed above, you have two options:

**Option A: Appoint a representative and register your sender IDs**

You must appoint a representative in Spain or a qualifying EU country who holds a valid digital certificate. The representative must also have an apostilled notarized power of attorney authorizing them to act on your behalf. We recommend engaging legal counsel to advise on the process for appointing an authorized representative.

**Option B: Switch to dedicated phone numbers for Spain**

Dedicated phone numbers (local long codes, international toll-free numbers) are not affected by this regulation and do not require CNMC registration. Note that new short code provisioning for Spain is temporarily on hold; request a long code instead. You can request a dedicated phone number for Spain through the [AWS End User Messaging console](https://console.aws.amazon.com/sms-voice/home "https://console.aws.amazon.com/sms-voice/home"). For more information, see [Dedicated phone numbers for Spain](dedicated-number-spain.md "dedicated-number-spain.md"). For registration processing timelines, see [Registration processing times](registration-eta.md "registration-eta.md").

###### CNMC verification process

After you submit your registration at the CNMC portal, CNMC sends a verification email to the representative email address you provided. You (or your representative) must then log into the portal with the qualifying digital certificate and approve the registration within 10 business days.

If you registered your sender ID with multiple downstream providers, you may receive a separate verification request for each provider.

###### How to register your sender ID for Spain

To complete your Spain sender ID registration, you must:

1.  **Register your sender ID in the CNMC National Alias Registry** (directly or through an appointed representative) – Go to [https://tramites.cnmc.gob.es/formulario/213/](https://tramites.cnmc.gob.es/formulario/213/ "https://tramites.cnmc.gob.es/formulario/213/") and authenticate with your valid digital certificate. During registration:

        * Select each of our downstream SMS providers as **PRO** (Registered Provider of Origin):




        | CNMC Portal Name | Provider |
        | --- | --- |
        | SINCH COMMUNICATIONS SPAIN, S.L. | Sinch |
        | VONAGE, B.V. | Vonage |
        | Twilio Ireland Limited | Twilio |
        * Select **Amazon Web Services** as **TERCERO** (Third Party).
        * Select the alias relationship type that applies to your sender ID.

    After submission, approve the CNMC verification notification within 10 business days.

2.  **Complete the AWS sender ID registration form** – Submit the registration form in the [AWS End User Messaging SMS console](https://console.aws.amazon.com/sms-voice/home "https://console.aws.amazon.com/sms-voice/home") so we can inform our downstream SMS providers. See the procedure below for step-by-step instructions.

###### Complete the AWS registration form

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Registrations**, choose **Create registration**.

###### Note

If you already created a registration when requesting the origination identity, use that existing registration form.

For **Registration form name**, enter a friendly name.

Choose **Next**. 3. In the **Sender ID info** section, enter the following:

    * For **Sender ID**, enter the sender ID to register. The sender ID must be between 3 and 11 alphanumeric characters.

Choose **Next**. 4. In the **Alias relationship type** section, select the type that matches how you established the right to use this sender ID:

    * **OEPM/EUIPO trademark** – The alias is a registered trademark with the Spanish Patent and Trademark Office (OEPM) or the EU Intellectual Property Office (EUIPO).
    * **OEPM trade name** – The alias is a registered trade name with OEPM.
    * **Commercial Register company name** – The alias matches the company name in the Spanish Commercial Register.
    * **Red.es/ICANN domain** – The alias corresponds to a domain registered with Red.es or an ICANN-accredited registrar.
    * **Other public registry** – The alias is registered in another official public registry.
    * **Legitimate habitual use** – The alias has been in legitimate habitual use by the holder.

Choose **Next**. 5. In the **Alias holder information** section, enter the following:

    * For **Holder type**, select **PF** (natural person) or **PJ** (legal entity).
    * For **Tax ID**, enter the holder's NIF or CIF.
    * For **Legal name**, enter the holder's full legal name or company name.
    * For **Surnames**, enter the holder's surnames. This field is required for natural persons (PF) only.

Choose **Next**. 6. In the **Representative information** section, enter the following:

    * For **Representative type**, select the type of representative.
    * For **Tax ID**, enter the representative's NIF or CIF.
    * For **Name**, enter the representative's name.
    * For **Surnames**, enter the representative's surnames.
    * For **Email**, enter the email address for CNMC verification notifications.
    * For **Phone – optional**, enter a contact phone number.

###### Note

If you do not have a qualifying digital certificate issued by the Spanish government or by one of the qualifying EU countries listed above, the representative must be your appointed representative with a valid digital certificate and apostilled notarized power of attorney.

Choose **Next**. 7. If the representative is a company, complete the **Person acting for company representative** section with the individual's details.

Choose **Next**. 8. In the **Company info** section, enter the following:

    * For **Company Name**, enter the name of your company as officially registered.
    * For **Tax ID**, enter your company's tax identification number.
    * For **DBA (Doing Business As) – optional**, enter any trade name your company uses.
    * For **Company website**, enter the URL for your company's website.
    * For **Area of business**, describe your company's industry or sector.

Choose **Next**. 9. In the **Company address** section, enter your company's registered address.

Choose **Next**. 10. In the **Contact info** section, enter the contact details for the person managing this registration.

Choose **Next**. 11. In **Messaging Use Case**, do the following:

    * For **Use case category**, choose the category that best describes your messaging use case.
    * For **Use case description**, provide additional context about how you will use this sender ID.
    * For **Monthly volume**, enter the estimated number of messages you plan to send per month.
    * For **Opt-in workflow**, describe how recipients consent to receive your messages.

Choose **Next**. 12. In **Message samples**, do the following:

    * For **Message Sample 1**, enter an example SMS message body that will be sent to your end users.
    * For **Message Sample 2 – optional** and **Message Sample 3 – optional**, enter additional example messages if needed.

Choose **Next**. 13. On the **Review and submit** page, verify the information you are about to submit is correct. To make updates, choose **Edit** next to the section. 14. Choose **Submit registration**.

###### Useful links

- [CNMC Registration Portal](https://tramites.cnmc.gob.es/formulario/213/ "https://tramites.cnmc.gob.es/formulario/213/")
- [CNMC FAQ – Gestión del Registro de Alias](https://sede.cnmc.gob.es/tramites/telecomunicaciones/gestion-del-registro-de-alias "https://sede.cnmc.gob.es/tramites/telecomunicaciones/gestion-del-registro-de-alias")
- [AWS End User Messaging console](https://console.aws.amazon.com/sms-voice/home "https://console.aws.amazon.com/sms-voice/home")
- [Dedicated phone numbers for Spain](dedicated-number-spain.md "dedicated-number-spain.md")
- [Registration processing times](registration-eta.md "registration-eta.md")
- [AWS Support](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home")
