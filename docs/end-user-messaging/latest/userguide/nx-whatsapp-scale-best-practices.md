

# Best practices
<a name="nx-whatsapp-scale-best-practices"></a>

WhatsApp messaging is governed by Meta's quality and policy rules, and your messaging limit rises or falls with how recipients respond to your messages. The following practices protect your quality rating and messaging limits and help your program scale.

**Topics**
+ [Send only to opted-in recipients](#nx-whatsapp-scale-bp-optin)
+ [Use approved templates and the right category](#nx-whatsapp-scale-bp-templates)
+ [Respect the conversation window](#nx-whatsapp-scale-bp-window)
+ [Monitor your quality rating and messaging limit](#nx-whatsapp-scale-bp-quality)

## Send only to opted-in recipients
<a name="nx-whatsapp-scale-bp-optin"></a>

Send WhatsApp messages only to recipients who have opted in to hear from you on WhatsApp. Opt-in is both a Meta requirement and the single biggest factor in your quality rating: messaging people who did not ask to hear from you leads to blocks and reports, which lower your quality rating and can reduce your messaging limit or restrict your number. Record how and when each recipient opted in.

## Use approved templates and the right category
<a name="nx-whatsapp-scale-bp-templates"></a>

You open a conversation with a template that Meta has approved, so create templates that clearly reflect their purpose and submit them in the correct category. A template whose content does not match its category, or that reads as unsolicited marketing, can be rejected in review or can hurt your quality rating after it is sent. Keep templates concise and relevant. For how to create, categorize, and manage templates, see [WhatsApp Message Templates](nx-features-whatsapp-templates.md).

## Respect the conversation window
<a name="nx-whatsapp-scale-bp-window"></a>

After a recipient messages you, you can exchange free-form messages with them for the duration of the open conversation session. Outside that window, you must use an approved template to message them again. Design your flows around this window: respond while the conversation is open, and use templates deliberately rather than as a way to push unsolicited messages, which recipients are likely to block or report.

## Monitor your quality rating and messaging limit
<a name="nx-whatsapp-scale-bp-quality"></a>

Watch your quality rating and messaging limit so you can react before Meta restricts your number. A falling quality rating is an early signal that your content or targeting needs to change. Reduce send volume to unengaged recipients, review your templates, and confirm your opt-in source when your rating drops. For how to monitor WhatsApp events and build operational alarms, see [Monitoring](nx-whatsapp-scale-monitoring.md).