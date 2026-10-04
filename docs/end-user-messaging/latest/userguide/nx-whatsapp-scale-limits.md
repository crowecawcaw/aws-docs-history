

# Limits and quotas
<a name="nx-whatsapp-scale-limits"></a>

WhatsApp messaging is subject to two kinds of limits: the per-account service quotas that AWS End User Messaging applies, and the messaging limits and quality rules that Meta applies to your WhatsApp Business Account (WABA). Both affect how much you can send, so plan for both when you scale.

**Topics**
+ [AWS End User Messaging service quotas](#nx-whatsapp-scale-limits-service)
+ [WhatsApp messaging limits and quality tiers](#nx-whatsapp-scale-limits-meta)
+ [Template limits](#nx-whatsapp-scale-limits-template)

## AWS End User Messaging service quotas
<a name="nx-whatsapp-scale-limits-service"></a>

AWS End User Messaging applies per-account quotas to the resources and send rates that support WhatsApp messaging. For the account-level quotas that apply across channels, and how to request an increase, see [Quotas](nx-features-quotas.md).

## WhatsApp messaging limits and quality tiers
<a name="nx-whatsapp-scale-limits-meta"></a>

Meta applies a messaging limit to your WhatsApp Business Account that caps how many unique recipients you can start conversations with in a rolling period. Meta also assigns a quality rating to each of your phone numbers based on how recipients respond to your messages, such as blocking or reporting them. Your messaging limit can increase as you send high-quality messages to engaged recipients, and it can decrease, or your number can be restricted, if your quality rating falls. These limits and ratings are managed by Meta, not by AWS End User Messaging, so follow the practices in [Best practices](nx-whatsapp-scale-best-practices.md) to protect them.

**Note**  
The exact WhatsApp messaging-limit tiers, the thresholds at which they increase or decrease, and the quality-rating levels are defined and changed by Meta [needs SME confirmation]. Confirm the current values against Meta's WhatsApp Business Platform documentation before publishing specific numbers.

## Template limits
<a name="nx-whatsapp-scale-limits-template"></a>

WhatsApp business messaging is template-first: you open a conversation with an approved template, and Meta reviews each template before you can use it. Meta applies limits to the number of templates on a WABA and to how templates are categorized and reviewed. For how to create and manage templates, see [WhatsApp Message Templates](nx-features-whatsapp-templates.md).

**Note**  
The exact template count limits per WABA and the per-category review rules are defined by Meta [needs SME confirmation].