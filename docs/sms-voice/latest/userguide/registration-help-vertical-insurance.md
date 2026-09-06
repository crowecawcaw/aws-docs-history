

# Insurance Brokers
<a name="registration-help-vertical-insurance"></a>

This guide covers A2P SMS registration requirements specific to insurance brokers, agencies, and Managing General Agents (MGAs). Insurance messaging is permitted but requires careful attention to how your use case is described and how consent is collected.

## What's allowed
<a name="registration-help-vertical-insurance-what-s-allowed"></a>
+ Policy renewal reminders and payment due notifications
+ Claims status updates and adjuster appointment confirmations
+ Quote follow-ups where the consumer initiated the request
+ Open enrollment reminders for existing policyholders
+ Appointment confirmations and rescheduling
+ Policy document delivery notifications

## What's prohibited
<a name="registration-help-vertical-insurance-what-s-prohibited"></a>
+ Cold outreach to purchased lead lists (no prior relationship)
+ Messages promoting specific policy products without prior consent
+ Sharing consumer data across multiple agency brands under one registration

## Common denial reasons
<a name="registration-help-vertical-insurance-common-denial-reasons"></a>

### Brand identity issues
<a name="registration-help-vertical-insurance-brand-identity-issues"></a>


**Denial title reference**  

| Denial title | What it means for insurance brokers | 
| --- | --- | 
| Invalid brand URL | Your agency website is inaccessible, parked, or under construction. Reviewers must verify your business exists and offers insurance services. | 
| Insufficient website content | A single landing page with only a quote form is insufficient. Your site must show who you are, what lines you write, and how consumers can contact you. | 
| Invalid brand business connection | The brand name on your registration doesn't match the entity shown on your website or state insurance license. If you operate under a DBA, ensure it's reflected consistently. | 
| DBA name mismatch | Your "Doing Business As" name doesn't match what appears on your website or consumer-facing materials. Common when agencies rebrand but don't update all assets. | 
| Non-compliant brand affiliation: high-risk financial | Your website or brand materials reference payday loans, debt consolidation, or other high-risk financial services alongside insurance. Separate these lines of business into distinct registrations. | 

### Campaign description issues
<a name="registration-help-vertical-insurance-campaign-description-issues"></a>


**Denial title reference**  

| Denial title | What it means for insurance brokers | 
| --- | --- | 
| Campaign unclear | Your description doesn't clearly explain what messages consumers will receive. "Insurance communications" is too vague. Instead, specify: "Policy renewal reminders and claims status updates for existing auto and home policyholders." | 
| Campaign not qualified for use case | The selected use case category doesn't match your actual messaging. Insurance brokers typically register under "Customer Care" or "Account Notifications" – not "Marketing." | 
| Campaign non-compliant content: high-risk financial | Your campaign description or samples reference financial products beyond standard insurance (e.g., premium financing with high APR, investment products). Keep insurance messaging separate from financial services. | 
| Campaign undeclared direct lending | If you offer premium financing, you must declare the Direct Lending content attribute. Failure to disclose triggers this denial even if lending is a minor part of your business. | 
| Campaign to brand mismatch | The campaign describes services for a different brand or agency than what's registered. Each brand/agency needs its own registration. | 

### Opt-in workflow issues
<a name="registration-help-vertical-insurance-opt-in-workflow-issues"></a>


**Denial title reference**  

| Denial title | What it means for insurance brokers | 
| --- | --- | 
| Opt-in workflow insufficient consent | Your quote request form collects a phone number but doesn't explicitly state the consumer will receive SMS messages. A phone number field alone is not consent. | 
| Opt-in workflow missing | No screenshot or URL showing where consumers agree to receive texts. Provide your quote form, application, or client portal showing the SMS consent checkbox. | 
| Opt-in workflow mismatch | The brand name on your opt-in form doesn't match your registered brand. For example, your form might say "ABC Insurance Group" but you registered as "ABC Agency LLC." This difference triggers a mismatch. | 
| Marketing consent not separated | Your form bundles marketing SMS consent with the quote request or policy application. Marketing opt-in must be a separate, unchecked checkbox – not buried in terms acceptance. | 
| Opt-in workflow non compliant message frequency disclosure | Your consent language doesn't tell consumers how often they'll hear from you. Add: "You may receive up to 4 messages per month regarding your policy." | 
| Opt-in workflow non-compliant HELP or STOP | Your opt-in disclosure is missing instructions for how to get help or opt out. Include: "Reply STOP to unsubscribe. Reply HELP for support." | 
| Opt-in workflow non compliant message and data rates disclosure | Missing the "Message and data rates may apply" disclosure near your consent language. | 
| Opt-in data shared with third parties | Your opt-in indicates consumer data may be shared with other agencies, carriers, or lead buyers. Each entity that will send messages needs its own consent. | 

### Sample message issues
<a name="registration-help-vertical-insurance-sample-message-issues"></a>


**Denial title reference**  

| Denial title | What it means for insurance brokers | 
| --- | --- | 
| Sample message(s) mismatch | Your sample messages don't match the use case you described. If you registered for "claims updates" but samples show marketing offers, this triggers a mismatch. | 
| Sample message(s) URL shortener | Messages contain bit.ly, tinyurl, or other shortened links. Use your full branded domain (e.g., abcinsurance.com/renew). | 
| Sample messages(s) embedded phone number | If you selected the 'embedded phone number' option during registration, your sample messages must contain a phone number. Otherwise, deselect that option during resubmission. | 
| Non-compliant message samples: high-risk financial services | Samples reference premium financing rates, APR disclosures, or debt-related language that crosses into high-risk financial territory. | 

## Insurance-specific registration tips
<a name="registration-help-vertical-insurance-insurance-specific-registration-tips"></a>

### Describe your use case precisely
<a name="registration-help-vertical-insurance-describe-your-use-case-precisely"></a>

**Bad:** "We send insurance messages to our clients."

**Good:** "We send policy renewal reminders, payment due notifications, and claims status updates to existing policyholders of ABC Insurance Agency who opted in during their policy application."

### Separate marketing from servicing
<a name="registration-help-vertical-insurance-separate-marketing-from-servicing"></a>

If you send both marketing (new product offers, cross-sell) and servicing (renewal reminders, claims updates) messages, register them as separate campaigns:
+ **Campaign 1 (Customer Care):** "Policy renewal reminders, payment confirmations, and claims status updates for existing policyholders."
+ **Campaign 2 (Marketing):** "Promotional offers for additional coverage options sent to existing policyholders who separately opted in to marketing communications."

### Multi-carrier agencies
<a name="registration-help-vertical-insurance-multi-carrier-agencies"></a>

If your agency represents multiple insurance carriers, register under your agency brand – not the carrier's brand. Your consumers have a relationship with your agency, not directly with the carrier for messaging purposes.

### Premium financing disclosure
<a name="registration-help-vertical-insurance-premium-financing-disclosure"></a>

Premium financing means paying insurance premiums in installments with interest. If any part of your business involves premium financing, you must select the **Direct Lending** content attribute during registration. Omitting this when your website mentions financing options triggers the "Campaign undeclared direct lending" denial.

## Opt-in form example
<a name="registration-help-vertical-insurance-optin-example"></a>

For a insurance-specific opt-in form example, see the form screenshots in this section. This vertical follows the [Transactional opt-in](registration-help-optin-transactional.md) with industry-specific disclosures.

![Insurance quote form showing an unchecked SMS consent checkbox with agency name, message frequency, data rates, and opt-out disclosures](http://docs.aws.amazon.com/sms-voice/latest/userguide/images/vertical-insurance-optin.png)
