

# Limits and quotas
<a name="nx-rcs-scale-limits"></a>

RCS messaging is subject to limits on the content you can send and on how quickly you can send it. There are limits on the length of the message text, the size and number of rich cards and carousel cards, the number of suggested actions, and how long a message remains valid for delivery. There are also throughput limits that control your send rate. When you design your RCS program in AWS End User Messaging, consider these limits and follow the guidance in [Best practices](nx-rcs-scale-bestpractices.md). For the per-account service quotas that apply across channels, and how to request an increase, see [Quotas](nx-features-quotas.md).

**Topics**
+ [RCS content limits](#nx-rcs-scale-limits-content)
+ [Throughput limits](#nx-rcs-scale-limits-throughput)
+ [Monthly spending quota](#nx-rcs-scale-limits-spend)

## RCS content limits
<a name="nx-rcs-scale-limits-content"></a>

The following limits apply to the content of a single RCS message.


| Content element | Limit | 
| --- | --- | 
| Text message body | Up to 3,072 characters. | 
| Rich card title | Up to 200 characters. | 
| Rich card description | Up to 2,000 characters. | 
| Cards in a carousel | 2 to 10 cards. | 
| Message-level suggested actions | Up to 11 suggestions per message. | 
| Card-level suggested actions | Up to 4 suggestions per card. | 
| Suggested action display text | Up to 25 characters. | 
| Time to live | 1 to 172,800 seconds (48 hours). If the message is not delivered within this duration, it expires. When you set a fallback, the fallback is triggered when the time to live expires without a delivery confirmation. | 

## Throughput limits
<a name="nx-rcs-scale-limits-throughput"></a>

Throughput in AWS End User Messaging, also referred to as throttling, controls how quickly you can send. Each RCS message is sent as a single unit and is not broken into multiple message parts the way an SMS message is, so each RCS message counts as one unit against your send rate. The send rate that applies to your messaging varies by country. For the per-country throughput values and the account-level throughput quotas, see [Quotas](nx-features-quotas.md).

## Monthly spending quota
<a name="nx-rcs-scale-limits-spend"></a>

AWS End User Messaging applies a monthly spending quota that caps how much you can spend on RCS messages each month. When your account reaches the RCS monthly spending quota, further RCS sends are rejected until the next month or until you raise the quota. You can set your own lower limit, and you can request an increase up to the maximum that AWS allows. For how to set a limit and track your spending, see [Spending and cost](nx-rcs-scale-spending.md). For the account-level quotas and how to request an increase, see [Quotas](nx-features-quotas.md).