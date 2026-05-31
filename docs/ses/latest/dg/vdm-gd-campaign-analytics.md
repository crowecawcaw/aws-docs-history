# Campaign analytics

Campaign analytics surfaces per-campaign deliverability and engagement metrics based on a
representative sample of emails sent from your monitored domains, across every provider your
domains send through—not just Amazon SES. Use campaign analytics to pinpoint which
campaigns are performing well and where to make improvements.

###### What campaign analytics provides

For each detected campaign, campaign analytics displays the following
information:

- _Subject line_ – The subject line of the campaign.
- _From address_ – The sender address used for the
  campaign.
- _Last send date_ – The most recent date the campaign was
  sent.
- _Messages sent_ – The number of messages sent in the
  campaign.
- _Inbox rate_ – The percentage of messages that reached
  the inbox.
- _Spam rate_ – The percentage of messages that were
  delivered to spam.

## Viewing campaign details

When you select a campaign from the campaigns list, you can view detailed information
including:

- _Campaign details_ – Campaign ID, from address,
  sender address, messages sent, projected volume, first seen date, and last seen
  date.
- _Engagement metrics_ – Inbox rate, spam rate, open
  rate, and delete rate for the campaign.
- _ISP breakdown_ – Per-ISP metrics showing inbox rate,
  spam rate, open rate, and delete rate for each major mailbox provider (Gmail,
  Yahoo, Outlook, and others).

###### To view campaign analytics using the Amazon SES console

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the left navigation pane, choose **Campaign analytics**
   under **Global deliverability** in the **Virtual Deliverability Manager**
   section.
3. The **Campaigns** table displays all detected campaigns for
   your monitored domains.
4. Choose a campaign subject to view its detailed metrics and ISP
   breakdown.
