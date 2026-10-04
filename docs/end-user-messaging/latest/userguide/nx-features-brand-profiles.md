

# Brand profiles
<a name="nx-features-brand-profiles"></a>

A brand profile stores your business identity — company details, contact information, addresses, compliance documents, and logos — in one place so you can reuse it across your SMS and RCS registrations instead of re-entering the same information each time. You store the information once as a set of flexible attributes, and AWS End User Messaging maps those attributes onto registration form fields when you register a sender.

A brand profile has a status of `ACTIVE`, `BLOCKED`, `PAUSED`, `CANCELLED`, or `FAILED`. You can protect a profile from accidental deletion by enabling deletion protection.

Brand profiles work in three steps: add your brand data as attributes, match those attributes to registration forms (optionally with AI-powered smart match), then submit and reuse the same profile across registration types.

## Data handling for brand profiles
<a name="nx-features-brand-profiles-data-handling"></a>

A brand profile stores the business identity information that you provide, including your company details, contact information, addresses, compliance documents, and logos. AWS End User Messaging stores this information in the AWS Region that you selected for AWS End User Messaging, and uses it to populate the registration form fields for the senders that you register.

Your brand profile information is encrypted at rest within the AWS boundary and encrypted in transit when it is transmitted across Amazon's secure network. When you reuse a brand profile across registrations, AWS End User Messaging maps the stored attributes onto each registration form rather than storing a separate copy for each registration. When you register a sender, the applicable registration information is shared with the regulatory body or carrier that reviews the registration for that country and number type. You can enable deletion protection on a brand profile to prevent accidental deletion.

Smart match is an optional feature that uses an AI model to map fields between your brand profile and a registration form semantically, so that the information lines up even when the profile attributes and the form fields are not named the same way.

When you use smart match, the feature may use AI models to process your request, depending on the model. When it does, AWS End User Messaging securely routes the inference request to compute resources within the geographic area where the request originated, so your data stays within your Region. For example, a request that originates in the European Union is processed within the European Union, a request from the United States within the United States, a request from Australia within Australia, and a request from Japan within Japan. If a request originates in a geographic area that is not listed, AWS End User Messaging processes it using the regional endpoint for the AWS Region that you selected for AWS End User Messaging. Your data is encrypted while it is transmitted across Amazon's secure network, and this processing does not change where your brand profile information is stored.

**Topics**
+ [Data handling for brand profiles](#nx-features-brand-profiles-data-handling)
+ [Managing brand profiles](nx-features-brand-profiles-manage.md)
+ [Managing brand profile attributes](nx-features-brand-profiles-attributes.md)
+ [Syncing brand profiles with registrations](nx-features-brand-profiles-sync.md)