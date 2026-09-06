

# Campaign analytics
<a name="vdm-gd-campaign-analytics"></a>

Campaign analytics surfaces per-campaign deliverability and engagement metrics based on a representative sample of emails sent from your monitored domains, across every provider your domains send through—not just Amazon SES. Use campaign analytics to pinpoint which campaigns are performing well and where to make improvements.

**What campaign analytics provides**  
For each detected campaign, campaign analytics displays the following information:
+ *Subject line* – The subject line of the campaign.
+ *From address* – The sender address used for the campaign.
+ *Last send date* – The most recent date the campaign was sent.
+ *Messages sent* – The number of messages sent in the campaign.
+ *Inbox rate* – The percentage of messages that reached the inbox.
+ *Spam rate* – The percentage of messages that were delivered to spam.

## Viewing campaign details
<a name="vdm-gd-campaign-analytics-detail"></a>

When you select a campaign from the campaigns list, you can view detailed information including:
+ *Campaign details* – Campaign ID, from address, sender address, messages sent, projected volume, first seen date, and last seen date.
+ *Engagement metrics* – Inbox rate, spam rate, open rate, and delete rate for the campaign.
+ *ISP breakdown* – Per-ISP metrics showing inbox rate, spam rate, open rate, and delete rate for each major mailbox provider (Gmail, Yahoo, Outlook, and others).

**To view campaign analytics using the Amazon SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation pane, choose **Campaign analytics** under **Global deliverability** in the **Virtual Deliverability Manager** section.

1. The **Campaigns** table displays all detected campaigns for your monitored domains.

1. Choose a campaign subject to view its detailed metrics and ISP breakdown.