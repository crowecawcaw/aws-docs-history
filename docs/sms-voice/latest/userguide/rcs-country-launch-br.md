

# Launching RCS in Brazil
<a name="rcs-country-launch-br"></a>

To launch your AWS RCS Agent in Brazil, submit a country launch registration using the `BR_RCS_LAUNCH_REGISTRATION` registration type. Brazil requires additional form fields, and ABR Telecom completes brand approval after you submit your registration.

## Registration form (console)
<a name="rcs-country-launch-br-console"></a>

The Brazil launch registration uses a custom form with additional fields beyond the standard baseline. The registration form collects the following information:
+ **Brand information** — Auto-populated from your testing agent configuration. You can review and adjust the brand name, description, website URL, and contact information.
+ **Use case selection** — Select the use case category for your RCS messaging.
+ **Tax code (CNPJ)** — Your Brazilian tax identification number (Cadastro Nacional da Pessoa Jurídica). This is required for all businesses operating in Brazil.
+ **Screenshot URL** — A URL to a screenshot demonstrating your RCS messaging experience.
+ **Brand approval** — Confirmation that you have authorization to use the brand for RCS messaging in Brazil. ABR Telecom completes brand approval after you submit your registration. For details, see [Brand approval and launch timeline](#rcs-country-launch-br-timeline).
+ **Privacy policy and terms of service** — URLs to your privacy policy and terms of service pages.

**Note**  
The Brazil registration form does not require a video URL. A screenshot URL is used instead.

## Brand approval and launch timeline
<a name="rcs-country-launch-br-timeline"></a>

In Brazil, ABR Telecom represents the three mobile operators (Claro, TIM, and Vivo) and manages the RCS agent launch workflow. You do not need to send a separate brand approval email to AWS. Complete brand approval as follows:

1. Submit the country launch registration in the AWS End User Messaging console.

1. ABR Telecom sends a brand approval email to the brand contact listed in your registration.

1. The brand contact opens the email and chooses the confirmation button labeled **CONFIRMO** (Portuguese for "I confirm") to complete brand approval.

1. ABR Telecom launches the agent on the carriers, typically within 48 business hours after confirmation.

**Note**  
The approval email is sent from `rcs@abrtelecom.com.br`. If the brand contact does not see it, try the following:  
Check the spam or junk folder.
If your organization restricts external email, add the `abrtelecom.com.br` sender domain to your email allowlist.
To resend the approval email, open the [status lookup page](https://rcs.abrportal.app/status-lookup) on the ABR Telecom website and choose **Reenviar E-mail de Aprovação da Marca** (Resend Brand Approval Email).

For general compliance guidance that applies to all countries, see [RCS country launch compliance guide](rcs-country-launch-compliance.md).