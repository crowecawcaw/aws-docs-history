

# Launching RCS in France
<a name="rcs-country-launch-fr"></a>

To launch your AWS RCS Agent in France, submit a country launch registration using the `FR_RCS_LAUNCH_REGISTRATION` registration type. France has strict requirements for brand name matching and language that you must follow to avoid registration denial.

## Registration form (console)
<a name="rcs-country-launch-fr-console"></a>

The France launch registration uses the standard baseline form. The registration form collects the following information:
+ **Brand information** — Auto-populated from your testing agent configuration. You can review and adjust the brand name, description, website URL, and contact information.
+ **Use case selection** — Select the use case category for your RCS messaging.
+ **Screen recording** — A screen recording that demonstrates your RCS messaging experience. For detailed video requirements, see [Launch video requirements](rcs-compliance-video.md).
+ **Privacy policy and terms of service** — URLs to your privacy policy and terms of service pages.

## France-specific requirements
<a name="rcs-country-launch-fr-requirements"></a>

**Warning**  
France enforces very strict brand name matching. Your RCS agent display name must **exactly match** your legal company name as registered with French authorities. Even minor differences (such as abbreviations, missing punctuation, or different capitalization) will result in registration denial.

### Brand name matching
<a name="rcs-country-launch-fr-brand-name"></a>

The brand name (display name) in your registration must exactly match your legal company name. The following are examples of common mismatches that result in denial:
+ Using a trading name instead of the legal company name
+ Abbreviating part of the company name (for example, "Corp" instead of "Corporation")
+ Omitting legal suffixes (for example, missing "SAS", "SARL", or "SA")
+ Using different capitalization or punctuation

**Important**  
Before submitting your France registration, verify your exact legal company name and use it as your display name. If your testing agent uses a different brand name, update it for the France launch registration.

### French language requirement
<a name="rcs-country-launch-fr-language"></a>

**Important**  
All end-user communications sent through your RCS agent in France must be in the French language. This includes message content, auto-responses, and keyword responses. Sending messages in other languages may result in your agent being suspended by French carriers.

This requirement applies to:
+ All outbound RCS messages sent to French recipients
+ Auto-response messages configured for keywords
+ Any automated replies or conversational flows

**Note**  
The registration form itself and your communication with AWS can be in English. The French language requirement applies only to messages delivered to end users in France.

## Promotional messaging hours
<a name="rcs-country-launch-fr-promotional"></a>

**Note**  
Some French carriers (Bouygues, SFR) enforce send time windows for promotional messages. Promotional messages sent outside permitted hours may be delayed or rejected. Transactional and OTP messages are not affected.

For general compliance guidance that applies to all countries, see [RCS country launch compliance guide](rcs-country-launch-compliance.md).