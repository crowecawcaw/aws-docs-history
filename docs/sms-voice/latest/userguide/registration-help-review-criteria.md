

# Review criteria
<a name="registration-help-review-criteria"></a>

When you submit a campaign registration, reviewers evaluate your application against eight criteria. Understanding these criteria helps you prepare a complete submission that passes review on the first attempt.

## 1. Brand identity
<a name="registration-help-review-1-brand-identity"></a>

**What to do:** Register your brand with accurate, verifiable business information. Your legal business name, EIN, physical address, support email, and phone number must match public records and be consistent across all registration fields.

**Why:** Reviewers confirm that the registering entity is a real, legitimate business. They cross-reference your registration details against public business records, your website, and your messaging content.
+ Legal business name matches state or federal records
+ EIN is valid and belongs to the registering entity
+ Physical address is complete and verifiable (not a PO Box)
+ Support email uses a branded domain (not Gmail, Yahoo, Outlook, or other public providers)
+ Support phone number is active and reachable
+ DBA name (if used) is consistent with brand registration
+ Only one brand is registered per EIN
+ Brand vetting is complete before submitting campaigns


**Common mistakes**  

| Mistake | Related denial title | 
| --- | --- | 
| Using a public email domain for support | Public email domain | 
| Physical address cannot be verified | Brand address invalid | 
| Same EIN registered for multiple brands | Brand multi-use | 
| Website missing or inaccessible | Invalid brand URL | 
| DBA name doesn't match legal entity | DBA name mismatch | 
| Brand vetting score too low | Brand invalid vetting | 
| Brand not verified before campaign submission | Brand unverified | 
| Support phone number missing or invalid | Invalid brand phone number | 

**Tip**  
**Good:** "Acme Health Services LLC" with EIN matching IRS records, physical address at 123 Main St Suite 400 Austin TX 78701, support email support@acmehealth.com, phone (512) 555-0100.  
**Bad:** "Acme Health" with a Gmail address, unverifiable PO Box, and disconnected phone number.

## 2. Website verification
<a name="registration-help-review-2-website-verification"></a>

**What to do:** Provide a live, publicly accessible website URL that clearly identifies your business, describes your services, and demonstrates a connection to your declared messaging use case.

**Why:** Reviewers visit your website to confirm the business exists, operates legitimately, and that the messaging program aligns with the business described on the site. The website must be accessible without authentication.
+ URL resolves and loads without errors
+ No login or authentication required to view
+ Business name is clearly displayed
+ Contact information is visible
+ Services or products are described
+ Content relates to the declared messaging use case
+ No prohibited content visible (SHAFT, gambling, illegal substances)
+ Site has substantive content beyond a single form
+ Domain has clean reputation (not flagged for malware or phishing)


**Common mistakes**  

| Mistake | Related denial title | 
| --- | --- | 
| URL is broken or doesn't resolve | Invalid brand URL | 
| Site requires login to access | Website requires authentication | 
| Only a lead capture form with no business context | Website contains only a form | 
| Not enough information about the business | Insufficient website content | 
| Domain flagged in threat intelligence databases | High-risk domain reputation | 
| Website references affiliate marketing | Non-compliant brand affiliation | 
| Website references prohibited content categories | Non-compliant brand affiliation | 

**Tip**  
**Good:** https://www.acmehealth.com with About, Services, Contact, Privacy Policy, and Terms pages. The site describes appointment reminder and health notification services.  
**Bad:** A single-page site with only a phone number collection form, or a URL that returns a 404 error.

## 3. Campaign description
<a name="registration-help-review-3-campaign-description"></a>

**What to do:** Write a clear, specific description of what messages you send, who receives them, and why. The description must match your selected use case, sample messages, and website content.

**Why:** Reviewers read your campaign description to understand the purpose of your messaging program. Vague, inconsistent, or mismatched descriptions are among the most common reasons for rejection.
+ Clearly states what type of messages are sent
+ Identifies who receives messages (customers, patients, subscribers)
+ Explains the business purpose
+ Matches the selected use case category
+ Consistent with sample messages
+ Consistent with website content
+ Brand name in description matches registered brand
+ Written in English
+ Unique content (not copied from other fields)
+ Single brand per campaign (not multiple companies)
+ If ISV: identifies the end brand, not the platform


**Common mistakes**  

| Mistake | Related denial title | 
| --- | --- | 
| Description doesn't match samples or use case | Campaign mismatch | 
| Too vague to understand the program purpose | Campaign unclear | 
| Brand name doesn't match registration | Campaign to brand mismatch | 
| Same text pasted across multiple fields | Duplicate content across fields | 
| Non-English content without translation | Non-English campaign content | 
| Multiple brands referenced in one campaign | Multiple brands in one campaign | 
| Describes personal or P2P messaging | Personal or P2P use case detected | 
| Direct lending not declared as content attribute | Campaign undeclared direct lending | 
| ISV registered instead of end brand | Invalid brand business connection | 

**Tip**  
**Good:** "Acme Health Services sends appointment reminders, lab result notifications, and prescription refill alerts to patients who opted in through our patient portal. Messages are sent when appointments are scheduled, results are available, or refills are ready."  
**Bad:** "We send messages to users." or "Testing SMS for our app."

## 4. Use case classification
<a name="registration-help-review-4-use-case-classification"></a>

**What to do:** Select the use case category that most accurately describes your messaging program. Ensure your campaign description, sample messages, and opt-in materials all align with the selected category.

**Why:** Reviewers verify that your selected use case matches the actual content of your campaign. Mismatches between the declared use case and your messaging content trigger rejections.
+ Selected use case matches campaign description
+ Selected use case matches sample messages
+ Content attributes correctly selected (e.g., direct lending)
+ Not using a test use case for production traffic
+ Charity use case selected if soliciting donations
+ Political use case selected if sending political messages
+ Use case is a permitted category (not prohibited content)
+ Only one campaign per use case (no duplicates)


**Common mistakes**  

| Mistake | Related denial title | 
| --- | --- | 
| Samples indicate charity but use case is not Charity | Campaign mismatch: charity | 
| Samples indicate political but use case is not Political | Campaign mismatch: political | 
| Same use case duplicated across multiple campaigns | Campaign multi use | 
| Test or non-production use case for live traffic | Campaign non-compliant content: non-subscriber facing | 
| Direct lending content without content attribute selected | Campaign undeclared direct lending | 
| Emergency alert use case (not permitted for 10DLC) | Emergency alert use case not permitted | 
| Campaign not qualified for selected use case | Campaign not qualified for use case | 

**Tip**  
**Good:** Use case "Customer Care" selected for a campaign sending order confirmations, shipping updates, and support responses. Sample messages show order status and delivery notifications.  
**Bad:** Use case "Marketing" selected but sample messages contain two-factor authentication codes.

## 5. Message samples
<a name="registration-help-review-5-message-samples"></a>

**What to do:** Provide at least two distinct sample messages that represent the actual messages your campaign sends. Include your brand name, use brackets for variable content, and include opt-out instructions in at least one sample.

**Why:** Reviewers read your samples to verify they match your declared use case, contain your brand name, and don't include prohibited content or restricted URL patterns.
+ At least two different sample messages provided
+ Samples reflect actual messages the campaign sends
+ Brand name appears in samples
+ Opt-out instructions included (e.g., "Reply STOP to unsubscribe")
+ Variable fields use brackets: [name], [order number], [date]
+ No public URL shorteners (bit.ly, tinyurl, etc.)
+ No prohibited content (SHAFT, gambling, illegal substances)
+ Samples match the declared use case
+ If embedded phone number is selected, it appears in samples
+ Each sample contains unique content


**Common mistakes**  

| Mistake | Related denial title | 
| --- | --- | 
| Brand name missing from samples | Sample message(s) mismatch | 
| Samples don't match declared use case | Sample messages use case mismatch | 
| Contains public URL shorteners | Sample message(s) URL shortener | 
| Embedded phone selected but not in samples | Sample messages(s) embedded phone number | 
| Prohibited SHAFT content in samples | Non-compliant message samples: SHAFT | 
| High-risk financial content in samples | Non-compliant message samples: high-risk financial services | 
| Gambling content in samples | Non-compliant message samples: gambling | 
| Samples indicate charity but use case differs | Sample messages use case mismatch: charity | 
| Samples indicate political but use case differs | Sample messages use case mismatch: political | 

**Tip**  
**Good:** - "Acme Health: Your appointment with Dr. [name] is confirmed for [date] at [time]. Reply HELP for help or STOP to cancel messages." - "Acme Health: Your lab results are ready. Log in to your patient portal to view them. Msg & data rates apply."  
**Bad:** - "Your code is 123456" (no brand name, single sample) - "Click here: bit.ly/abc123" (public URL shortener)

## 6. Opt-in mechanism
<a name="registration-help-review-6-opt-in-mechanism"></a>

**What to do:** Describe and demonstrate how end users provide consent to receive your messages. Provide accessible URLs or screenshots showing the complete opt-in flow with all required disclosures visible at the point of consent.

**Why:** Reviewers verify that you collect proper, affirmative consent before sending messages. The opt-in mechanism must show clear consent with all required disclosures visible where the user opts in.
+ Opt-in method clearly described (web form, keyword, paper form, QR code)
+ URL or screenshot provided and accessible without login
+ Brand name visible in opt-in flow
+ Message frequency disclosure present (e.g., "Up to 4 msgs/month")
+ "Message and data rates may apply" disclosure present
+ HELP and STOP instructions visible
+ Link to Terms and Conditions included
+ Link to Privacy Policy included
+ Privacy policy states mobile opt-in data is not shared with third parties
+ Consent checkbox is unchecked by default (not pre-selected)
+ Marketing consent is separate from transactional consent
+ Each declared opt-in method has complete workflow details
+ Consent is freely given (not bundled as condition of service)


**Common mistakes**  

| Mistake | Related denial title | 
| --- | --- | 
| No opt-in URL or screenshot provided | Opt-in workflow missing | 
| Missing "message and data rates" disclosure | Opt-in workflow non compliant message and data rates disclosure | 
| Missing message frequency disclosure | Opt-in workflow non compliant message frequency disclosure | 
| Missing HELP/STOP instructions | Opt-in workflow non-compliant HELP or STOP | 
| Missing privacy policy link | Opt-in workflow non compliant privacy policy | 
| Missing terms and conditions link | Opt-in workflow non compliant terms and conditions | 
| Consent not sufficiently explicit | Opt-in workflow insufficient consent | 
| Brand name missing from opt-in flow | Opt-in workflow mismatch | 
| Checkbox pre-selected by default | Opt-in checkbox missing or pre-selected | 
| Marketing consent bundled with transactional | Marketing consent not separated | 
| Opt-in data shared with third parties | Opt-in data shared with third parties | 
| Missing required consent language | Non-compliant consent language | 
| Multiple opt-in methods but incomplete details | Incomplete opt-in workflow details | 

**Tip**  
**Good:** Web form at https://www.acmehealth.com/sms-signup showing: - Unchecked checkbox: "I agree to receive appointment reminders via SMS from Acme Health (up to 8 msgs/month). Msg & data rates may apply. Reply STOP to cancel, HELP for help." - Links to Terms of Service and Privacy Policy below the checkbox.  
**Bad:** A form that says "Enter your phone number" with no disclosures, or a pre-checked checkbox buried in Terms of Service acceptance.

## 7. Opt-out compliance
<a name="registration-help-review-7-opt-out-compliance"></a>

**What to do:** Configure compliant STOP, HELP, and opt-in confirmation messages. The STOP response must acknowledge the request, confirm no further messages will be sent, and include your brand name. The HELP response must provide at least one support contact method.

**Why:** Reviewers verify that recipients can easily stop messages and get support. Non-compliant opt-out, HELP, or opt-in confirmation messages are a common rejection reason.
+ STOP keyword triggers opt-out confirmation
+ Opt-out message acknowledges the request
+ Opt-out message confirms no further messages will be sent
+ Opt-out message includes brand name
+ HELP keyword triggers support response
+ HELP message includes brand name
+ HELP message includes at least one contact method (email, phone, or URL)
+ Email domain in HELP message matches brand
+ Opt-in confirmation message includes HELP and STOP instructions
+ Opt-in confirmation message includes message frequency
+ Opt-in confirmation message includes "Message and data rates may apply"
+ Opt-in confirmation message includes brand name


**Common mistakes**  

| Mistake | Related denial title | 
| --- | --- | 
| Opt-out message missing brand name | Opt-out message mismatch | 
| Opt-out doesn't confirm messages will stop | Non-compliant opt-out message | 
| HELP message missing support contact info | Non-compliant help message | 
| HELP message brand name doesn't match registration | Help message mismatch | 
| Opt-in message missing HELP/STOP instructions | Non-compliant opt-in message HELP and STOP | 
| Opt-in message missing frequency or data rate disclosure | Non-compliant opt-in message | 
| Opt-in message brand name doesn't match | Opt-in message mismatch | 
| No opt-in confirmation message provided | Missing opt-in message | 

**Tip**  
**Good:** "Acme Health: You've been unsubscribed and will no longer receive messages from us. Reply HELP for assistance." **Good HELP response:** "Acme Health: For support, email support@acmehealth.com or call (512) 555-0100. Reply STOP to unsubscribe."  
**Bad:** "You have been removed." (no brand name, doesn't confirm messages stop) **Bad HELP response:** "Text STOP to stop." (no brand name, no contact method)

### Opt-out handling for OTP and 2FA programs
<a name="registration-help-review-7-otp-opt-out"></a>

OTP and 2FA programs must adhere to the same opt-out response requirements as other use cases. If a recipient replies STOP to an OTP message, you must send a compliant opt-out acknowledgment response.

However, if your SMS program is compliant with all applicable regulations, you are not required to permanently opt out the recipient's phone number when they text STOP. A subsequent request for an OTP code by the end user (for example, initiating a new login attempt) is considered a new opt-in.

Your STOP response for OTP programs must meet the following requirements:
+ Include your brand or program name
+ Confirm the user is unsubscribed from the OTP program
+ Provide instructions for opting back in (for example, "request a new code to login")
+ Include HELP contact information
+ Be under 160 GSM characters with no special characters

**Example STOP response for OTP:** "You are unsubscribed from {{BRAND NAME}} OTP. Opt back in by replying {{OPT-IN KEYWORD}} or requesting a new code to login. Reply HELP for help or call {{xxx-xxx-xxxx}}."

### STOP behavior on US Toll-Free Numbers
<a name="registration-help-review-7-tfn-stop"></a>

US Toll-Free Numbers handle opt-outs differently from Short Codes and 10DLC numbers. On a Toll-Free Number, the opt-out flow is managed at the network level by US carriers and cannot be customized by the sender.

When a recipient replies STOP to a Toll-Free Number, the carrier automatically blocks all future messages from that number and sends a network-level response. The sender cannot override this block. The recipient must text UNSTOP or START to the same number to resume receiving messages.

This means the OTP guidance above (a subsequent user-initiated request constitutes a new opt-in) does not apply to Toll-Free Numbers. On a Toll-Free Number, if a user texts STOP, they will not receive messages from that number again until they explicitly text UNSTOP or START — regardless of any subsequent actions they take in your application.

For OTP and password reset use cases on Toll-Free Numbers, account for this behavior when designing your messaging flow. Provide users with instructions to text UNSTOP if they need to re-enable messages.

## 8. Content compliance
<a name="registration-help-review-8-content-compliance"></a>

**What to do:** Ensure your messaging content, website, and business do not involve prohibited or restricted content categories. If your content involves age-restricted products, implement a compliant age gate requiring date-of-birth entry.

**Why:** Mobile operators prohibit certain content categories entirely and restrict others to businesses with proper safeguards. Campaigns associated with prohibited content are rejected and may not be eligible for resubmission.
+ No SHAFT content (sex, hate, alcohol, firearms, tobacco/vape) without compliant age gate
+ No gambling content
+ No illegal substances (cannabis, CBD, controlled substances)
+ No high-risk financial services (payday loans, crypto, debt collection, credit repair)
+ No affiliate marketing or third-party lead generation
+ No sweepstakes messaging
+ No third-party job board content
+ If age-restricted products: age gate requires full DOB entry (not yes/no confirmation)
+ Privacy policy states mobile opt-in data is not shared with third parties
+ Terms and conditions include carrier liability statement
+ Terms and conditions include opt-out instructions
+ Terms and conditions include message frequency disclosure
+ Terms and conditions include customer care contact information
+ Terms and conditions include link to privacy policy
+ Terms and conditions include use case description


**Common mistakes**  

| Mistake | Related denial title | 
| --- | --- | 
| High-risk financial content (payday loans, crypto) | Campaign non-compliant content: high-risk financial | 
| Cannabis or CBD content | Prohibited content: cannabis or CBD | 
| Gambling content | Campaign non-compliant content: gambling. | 
| SHAFT content without compliant age gate | Campaign non-compliant content: missing age gate | 
| Affiliate marketing or lead generation | Campaign non-compliant content: affiliate marketing. | 
| Sweepstakes content | Campaign non-compliant content: sweepstakes | 
| Third-party job board content | Campaign non-compliant content: third party job boards. | 
| Privacy policy allows third-party data sharing | Non-compliant privacy policy | 
| Terms missing carrier liability statement | Non-compliant Terms and Conditions: carrier liability | 
| Terms missing opt-out instructions | Non-compliant Terms and Conditions: opt-out instructions | 
| Terms missing message frequency | Non-compliant Terms and Conditions: message frequency | 
| Terms missing customer care contact | Non-compliant Terms and Conditions: customer care info | 
| Terms missing privacy policy link | Non-compliant Terms and Conditions: privacy policy | 
| Terms missing use case description | Non-compliant Terms and Conditions: use case description | 
| Spam or phishing association detected | Spam or phishing association | 

## Next steps
<a name="registration-help-review-criteria-next-steps"></a>
+ If your registration was denied, see [Rejection troubleshooting](registration-help-rejection-troubleshooting.md) to find your specific denial reason and resolution steps.
+ For opt-in form examples, see [Compliant opt-in examples](registration-help-optin-examples.md).
+ For industry-specific guidance, see the vertical guides for your business type.