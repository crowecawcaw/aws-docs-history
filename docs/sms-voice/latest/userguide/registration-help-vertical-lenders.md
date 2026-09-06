

# Direct Lenders
<a name="registration-help-vertical-lenders"></a>

This guide covers registration requirements for direct lending organizations including mortgage lenders, auto lenders, personal loan providers, and other licensed financial institutions that originate loans directly to consumers.

## What's allowed
<a name="registration-help-vertical-lenders-what-s-allowed"></a>

Direct lenders who originate loans directly to consumers may register campaigns for:
+ **Loan status notifications** – Application received, under review, approved, funded, payment due
+ **Payment reminders** – Upcoming due dates, payment confirmations, late payment notices
+ **Account servicing** – Balance updates, rate change notifications, escrow updates
+ **Two-factor authentication** – Login verification, transaction confirmation
+ **Customer care** – Support responses, document request follow-ups
+ **Marketing (with proper consent)** – Refinance offers, new product announcements, rate alerts

**Note**  
**Important:** You must select the **Direct lending or loan arrangement** content attribute during registration, even if the specific campaign is not directly about loan origination (for example, 2FA for a lending portal).

## What's prohibited
<a name="registration-help-vertical-lenders-what-s-prohibited"></a>

The following lending-related activities are **not permitted** on A2P 10DLC:


**Prohibited activity reference**  

| Prohibited activity | Why | 
| --- | --- | 
| Payday loans / short-term high-interest loans | Classified as high-risk financial services | 
| Third-party loan solicitation | Lead generation / affiliate marketing | 
| Debt collection on behalf of others | Third-party debt collection is restricted | 
| Debt consolidation or credit repair marketing | High-risk financial category | 
| Student loan refinancing solicitation | High-risk financial category | 
| Cryptocurrency or investment-related lending | High-risk financial category | 

Campaigns involving these activities are **not eligible for resubmission**.

## Content attribute requirement
<a name="registration-help-vertical-lenders-content-attribute-requirement"></a>

All campaigns associated with a financial services organization must select the **Direct lending or loan arrangement** content attribute – regardless of the specific campaign use case.

**Example:** A mortgage lender registering a campaign solely for appointment reminders must still select this attribute because the brand is a lending organization.

Failure to select this attribute triggers the following denial:

**Campaign undeclared direct lending** – From the campaign description it appears that the purpose of your campaign is direct lending but the Direct lending or loan arrangement content attribute has not been selected. If your campaign is associated with a financial services organization, select the Direct lending or loan arrangement content attribute even if the specific campaign use case does not directly relate to loan offering (for example, two-factor authentication). Either update your campaign description or select the Direct lending or loan arrangement content attribute and resubmit.

## Compliance checklist
<a name="registration-help-vertical-lenders-compliance-checklist"></a>

Before submitting your registration, verify:
+ **Content attribute selected** – Direct lending or loan arrangement is checked
+ **Brand website is live** – Shows company name, NMLS number (if applicable), contact info, and services
+ **Business email domain** – Uses your company domain, not Gmail/Yahoo/Outlook
+ **Campaign description** – Clearly states the lending use case and identifies your company
+ **Sample messages** – Include your brand name, reflect actual messages you'll send
+ **Opt-in workflow documented** – Shows how borrowers consent to receive SMS
+ **TCPA consent language** – Separate checkbox for marketing messages (unchecked by default)
+ **Privacy policy** – States mobile opt-in data will not be shared with third parties
+ **Terms and conditions** – Include message frequency, opt-out instructions, carrier liability disclaimer
+ **HELP message** – Contains brand name and support contact (email, phone, or URL)
+ **STOP message** – Acknowledges opt-out and confirms no further messages

## Common rejection reasons
<a name="registration-help-vertical-lenders-common-rejection-reasons"></a>


**Common rejection reasons for lenders**  

| Denial title | What it means | How to fix | 
| --- | --- | --- | 
| Campaign undeclared direct lending | Your brand is a lending organization but you did not select the Direct lending or loan arrangement content attribute. | Select the content attribute and resubmit. This applies even for non-lending campaigns (2FA, appointment reminders) if your brand is a lender. | 
| Campaign non-compliant content: high-risk financial | Your campaign content references prohibited financial services: payday loans, short-term high-interest loans, third-party loan solicitation, student loans, cryptocurrency, stocks and investing platforms, debt collection, debt consolidation, debt reduction, or credit repair. | This campaign is not eligible for resubmission under A2P 10DLC. If you believe this rejection is in error, open a support case for assistance. | 
| Non-compliant brand affiliation: high-risk financial | Your brand's website references high-risk financial services such as payday loans, short-term high-interest loans, third-party loan solicitation, cryptocurrency, or stocks and investing platforms. | This campaign is not eligible for resubmission under A2P 10DLC. If you believe this rejection is in error, open a support case for assistance. | 
| Non-compliant message samples: high-risk financial services | Your sample messages reference high-risk financial services such as loans or cryptocurrency. | If your lending activity is legitimate direct lending (mortgage, auto, personal loans from a licensed lender), update your sample messages to clearly reflect direct lending language rather than language that could be interpreted as high-risk solicitation. Resubmit with corrected samples. | 
| Opt-in workflow insufficient consent | Your opt-in process does not demonstrate that express written consent was obtained. For lending campaigns with marketing content, consent must be freely given and cannot be bundled as a condition of the loan application. | Implement a separate, unchecked checkbox for SMS marketing consent that is not required to complete the loan application. Ensure your opt-in clearly states what messages the borrower will receive. Update your opt-in workflow and resubmit. | 
| Marketing consent not separated | Your opt-in combines marketing consent with transactional/informational consent. Under TCPA guidelines, consumers must have a separate choice to opt in to promotional messages. | Create distinct opt-in mechanisms: one for transactional messages (loan status, payment reminders) and a separate optional checkbox for marketing messages (refinance offers, new products). Resubmit with the updated workflow. | 
| Campaign to brand mismatch | The company name in your campaign description doesn't match your registered brand name or DBA name. | Ensure the company name in your campaign description matches your brand registration exactly. If you operate under a DBA, update your brand registration to include it. Resubmit. | 
| Opt-in workflow non compliant privacy policy | Your opt-in flow is missing a link to your privacy policy, or your privacy policy does not state that mobile opt-in data will not be shared with third parties. | Add a direct link to your privacy policy within your opt-in flow. Ensure the privacy policy explicitly states that no mobile information will be shared with third parties or affiliates for marketing or promotional purposes. Resubmit. | 

## Opt-in form example
<a name="registration-help-vertical-lenders-optin-example"></a>

For a lender-specific opt-in form example, see the form screenshots in this section. This vertical follows the [Transactional opt-in](registration-help-optin-transactional.md) with industry-specific disclosures.

![Lender opt-in form example](http://docs.aws.amazon.com/sms-voice/latest/userguide/images/vertical-lender-optin.png)
