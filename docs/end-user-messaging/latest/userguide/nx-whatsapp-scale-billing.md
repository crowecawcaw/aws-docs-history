

# Billing and cost
<a name="nx-whatsapp-scale-billing"></a>

WhatsApp pricing is conversation-based rather than per-message. Meta charges for a conversation, which is a session that groups the messages exchanged with a recipient over a period of time, and AWS End User Messaging passes that charge through on your bill. Understanding how conversations are metered helps you forecast and control cost as volume grows. If you only want to view your monthly charges, use the AWS Billing and Cost Management console, which provides an estimate of your bill for the current month and your final charges for previous months.

**Topics**
+ [How conversations are metered](#nx-whatsapp-scale-billing-conversations)
+ [Read your usage reports](#nx-whatsapp-scale-billing-usage)

## How conversations are metered
<a name="nx-whatsapp-scale-billing-conversations"></a>

A conversation starts when the first message in a session is delivered, and it groups the messages exchanged with that recipient for the duration of the session. The price of a conversation depends on its category, which reflects the purpose of the conversation, and on the recipient's country. Because billing is conversation-based, sending several messages to a recipient within the same open session does not multiply the cost the way per-message billing would. For current conversation rates by category and country, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/).

**Note**  
The exact WhatsApp conversation categories, the session duration that defines a conversation, and the per-category and per-country pricing are defined by Meta [needs SME confirmation]. Confirm the current categories and metering rules against Meta's WhatsApp Business Platform pricing and the AWS End User Messaging pricing page before publishing specific values.

## Read your usage reports
<a name="nx-whatsapp-scale-billing-usage"></a>

The WhatsApp channel generates usage on your bill for the conversations that AWS End User Messaging passes through. To view your charges, use the AWS Billing and Cost Management console for a current-month estimate and final charges for previous months.

**Note**  
The exact WhatsApp usage type string format on the bill and the set of usage types generated per conversation [needs SME confirmation]. Confirm the usage type details against the AWS Billing and Cost Management usage report before publishing specific examples.

You can use tags for organizing your bill to reflect your own cost structure. For example, you can tag resources with a campaign name and then organize your billing information to see the total cost of that campaign across several services. For more information, see [Cost allocation and tagging](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*.