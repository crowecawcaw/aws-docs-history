

# Sender IDs
<a name="nx-features-senders"></a>

A sender ID is an alphanumeric name that identifies the sender of an SMS message. When you send an SMS message using a sender ID, and the recipient is in an area where sender ID authentication is supported, your sender ID appears on the recipient's device instead of a phone number. A sender ID provides SMS recipients with more information about the sender than a phone number or short code provides. For example, a fictitious company Example Corp could use the sender ID `EXAMPLECO`.

Sender IDs are supported in many countries and regions around the world. In some places, if you're a business that sends SMS messages to individual customers, you must use a sender ID that's pre-registered with a regulatory agency or industry group. For the complete list of countries and regions that support or require sender IDs, see the SMS supported countries and regions documentation.

**Advantages**

Sender IDs provide the recipient with more information about the message sender. It's easier to establish your brand identity by using a sender ID than by using a short or long code. There's no additional charge for using a sender ID.

**Disadvantages**

Support and requirements for sender ID authentication aren't consistent across all countries or regions. Several major markets (including Canada, China, and the United States) don't support sender ID. In some areas, you must have your sender IDs pre-approved by a regulatory agency before you can use them.

## Registered and dynamic sender IDs
<a name="nx-features-senders-types"></a>

**Registered sender ID** – A registered sender ID is registered with a regulatory agency or industry group.

**Dynamic sender ID** – A dynamic sender ID does not have to be registered with a regulatory agency or industry group. Registration requirements can change quickly and it is recommended that you complete any optional registration for dynamic sender IDs.

## Considerations for a sender ID
<a name="nx-features-senders-considerations"></a>

When you are creating a sender ID you should consider the following:
+ Choose a sender ID that matches your company branding and SMS service or use case.
+ Numeric-only sender IDs are not supported.
+ AWS End User Messaging sender ID supported characters (some countries might override these): no special characters except dashes (-); no spaces; valid characters a-z, A-Z, 0-9; must contain at least one letter; cannot start or end with a hyphen; minimum of 1 character, maximum of 11 characters (minimum of 3 characters recommended).
+ Some countries have additional character restrictions. For example, France does not support the dash character (-) in sender IDs.
+ If the country you're sending to requires registration you must submit a registration for each AWS Region you plan on sending from.

**Sender ID casing in the console**  
The AWS End User Messaging console displays all sender IDs in uppercase, regardless of the casing used during registration. Sender ID values are case-sensitive at the carrier and aggregator level. Using the wrong casing in API calls can cause delivery failures.  
To verify the registered casing of a sender ID, check the associated registration record in the **Registrations** section of the console, which preserves the original casing submitted during registration. When specifying a sender ID in API calls, use the casing shown in your registration record, not the casing shown in the sender ID list.

**Topics**
+ [Registered and dynamic sender IDs](#nx-features-senders-types)
+ [Considerations for a sender ID](#nx-features-senders-considerations)
+ [Request a sender ID](nx-features-senders-request.md)
+ [Release a sender ID](nx-features-senders-release.md)
+ [Manage tags for a sender ID](nx-features-senders-tags.md)
+ [List shared sender IDs](nx-features-senders-shared.md)