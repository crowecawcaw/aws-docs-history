# 10DLC brand registration form

###### Note

With our updated console experience you are now seeing a registration
**Name** field for your registration. This field is set to "–" as we
do not manually backfill any of your service values to prevent interruption to your service
and let you maintain your security posture. A registration **Name** is an
optional friendly name field that can be updated using the tags on the registration details
page. For more information on how to add a **Name** tag, see [Change a registration's name in AWS End User Messaging SMS](registrations-friendly-name.md "registrations-friendly-name.md").

Before you can request a 10DLC phone number, you must register your company or brand.
Brand registrations are managed by an industry organization called the Campaign
Registry. You need to register your company per each AWS account and AWS Region that will use the company.

###### Note

Campaign Registry has implemented a two-factor authentication (2FA) for brand registrations.
If your **Legal form of organization** is PUBLIC_PROFIT you have to
provide the email address of a person who works at the brand who can complete the email
authentication. Email distribution lists are not allowed and the email domain must match
the domain of your business. The email authentication is sent from **noreply@auth.campaignregistry.com** and we recommend you add the email
address to your spam list allow rules.

After you've created your 10DLC brand registration you need to complete the form and
submit it for approval.

If your 10DLC brand registration is successful and you want to register for higher
throughput capabilities, then you must vet your 10DLC brand registration. For more
information on 10 DLC brand vetting, see [10DLC brand vetting form](registrations-10dlc-vetting.md "registrations-10dlc-vetting.md").

###### Note

For more information on expected registration times, see [United States 10DLC registration](registrations-10dlc.md "registrations-10dlc.md").

###### Complete a 10DLC brand registration

1.  Open the AWS End User Messaging SMS console at
    [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2.  In the navigation pane, under **Registrations**, choose the 10DLC
    brand registration to complete.
3.  In the **Brand Registration Information** section, enter the
    following:
    - For **Legal company name**, enter the name that the
      company is registered under. The name that you enter must be an exact match
      for the company name that's associated with the tax ID that you provide.

    ###### Important

    Make sure to use your company's exact legal name. Incorrect or
    incomplete information might result in your registration being delayed
    or denied.
    - For **Country of tax registration**, enter the two letter
      ISO country code for the country where your company is registered. For a
      list of ISO country codes, see [Supported countries and regions for SMS
      messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").
    - For **Tax ID or Business Registration Number**, enter
      your company's tax ID. The ID that you enter depends on the country that
      your company is registered in.
      - If you're registering a US or non-US entity that has an IRS
        Employer Identification Number (EIN), enter your nine-digit EIN. The
        legal company name, EIN, and physical address that you enter must
        all match the company information that is registered with the
        IRS.
      - If you're registering a Canadian entity, enter your federal or
        provincial Corporation number. Don't enter the Business Number (BN)
        provided by the CRA. The legal company name, Corporation number, and
        physical address that you enter must all match the company
        information that is registered with Corporations Canada.
      - If you're registering an entity that is based in another country,
        enter the primary tax ID for your country. In many countries, this
        is the numeric portion of your VAT ID number.

    - For **Legal form of organization**, choose the option
      that best describes your company.

    ###### Note

    The **US government** and
    **Not-for-profit** options can only be used to
    register United States-based organizations. If your organization is
    based in a country other than the US, you must register as
    **Private for-profit**, regardless of the actual
    legal form of your organization.
    - For **Stock symbol - optional** enter your companies
      stock symbol.

    For **Stock exchange - optional**, choose the stock
    exchange your company is listed on

    ###### Note

    If you chose **Public for profit** in the previous
    step, the company's stock symbol and the stock exchange fields are
    required.
    - For **Physical business address – Address/Street**,
      enter the physical street address associated with your company.
    - For **Physical business address – City**, enter the
      city where the physical address is located.
    - For **Physical business address – State or
      region**, enter the state or region where the address is
      located.
    - For **Physical business address – Zip Code/Postal
      Code**, enter the ZIP or postal code for the address.
    - For **Physical business address – Country**, enter
      the two digit ISO country code.
    - For **Brand verification email**, enter the email of a
      person who works at the brand who can complete the email authentication.
      Email distribution lists are not allowed and the email domain must match the
      domain of your business.

4.  Choose **Next**.
5.  In the **Additional company and contact info** section, enter the
    following:

        * For **Doing Business As (DBA) or brand name**, enter any
         other names that your company does business as.
        * For **Vertical**, choose the category that best describes
         the company you're registering.
        * For **Company website**, enter the full URL of your
         company's website. Include "http://" or "https://" at the beginning of the
         address.
        * For **Support Email**, enter the email address of the
         person who will be your business's point of contact.
        * For **Support Phone Number**, enter the phone number of
         the person who will be your business's point of contact. The phone number
         must start with a '+' and can't contain any spaces, hyphens, or parentheses.
         For example, `+1 (206) 555-0142` is not in the correct format,
         but `+12065550142` is.

    Choose **Next**.

6.  On the **Review and submit** page verify the information you are
    about to submit is correct. To make updates choose **Edit** next to
    the section.
7.  Choose **Submit registration**.

###### Important

If your **Legal form of organization** is PUBLIC_PROFIT then
once you submit your brand registration the authentication email is sent to the
email address specified in **Brand verification email**. Your
registration can not be approved until you complete brand authentication. The
authentication email is valid for 7 days and after that you have to [request a new authentication
email](registrations-10dlc-auth.md#registrations-10dlc-auth.title "registrations-10dlc-auth.md#registrations-10dlc-auth.title").

###### Note

After your registration has been approved you need to either register for the
optional **US 10DLC Brand vetting** or [10DLC campaign registration form](registrations-10dlc-register-campaign.md "registrations-10dlc-register-campaign.md").
For more information on registering for 10DLC, see [United States 10DLC registration](registrations-10dlc.md "registrations-10dlc.md").
