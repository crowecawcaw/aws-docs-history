**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Campaign

delivery metrics

The **Campaign delivery metrics** section contains information about
inbox placement rates for the email that you sent from your domains. However, unlike the
[Domain reputation](channels-email-deliverability-dashboard-domain.md "channels-email-deliverability-dashboard-domain.md")
page, the **Campaign delivery metrics** page contains information about
specific email campaigns, as opposed to information for entire domains.

The Deliverability dashboard's **Campaign delivery metrics** uses
heuristics such as the _from domain_ and _send time_ to group similar messages into categories. We can't
guarantee that this aligns with Amazon Pinpoint campaigns or treatments. When sending an Amazon Pinpoint
campaign with multiple treatments, you can review the campaign analytics page for reporting
of open rate across treatments.

When you choose a domain and a date range, you see a table that contains the following
information:

- **Preview** – A small image that shows the content of the
  email. Hover over the image to see a larger preview.
- **Last send date** – The date and time when the message was
  last sent.
- **Subject** – The subject line of the email.
- **Sender address** – The sender ("From") address for the
  message.
- **ESP** – The email provider (such as Gmail or Yahoo) that
  the metrics apply to.
- **Inbox rate** – The percentage of emails sent from the
  campaign that arrived in recipients' inboxes (as opposed to their junk mail
  folders).
- **Open rate** – The percentage of emails sent from the
  campaign that were opened by their recipients.
  When you choose a campaign in this table, you see a details page for the campaign.
  Campaign details pages contain two sections: **Details** and
  **Sending IP addresses**.

## Details

This section contains the following information about the campaign:

- **Latest sent date** – The date and time when the
  message was last sent.
- **First sent date** – The date and time when the
  message was first sent.
- **Subject** – The subject line of the email.
- **Sender address** – The sender ("From") address for
  the message.
- **Sender domain** – The domain that the message was
  sent from.
- **ESP** – The email provider (such as Gmail or Yahoo)
  that the metrics apply to.
- **Estimated volume** – The approximate number of
  recipients that were sent this campaign.
- **Inbox placement** – The percentage of emails sent
  from the campaign that arrived in recipients' inboxes (as opposed to their junk
  mail folders).
- **Spam placement** – The percentage of emails sent from
  the campaign that arrived in recipients' junk mail folders.
- **Read** – The percentage of emails that were opened by
  their recipients.
- **Read and deleted** – The percentage of emails that
  were opened by their recipients and then deleted.
- **Deleted** – The percentage of emails that were
  deleted by their recipients without being read.

The campaign details page also includes a larger preview of the body of the email.
Amazon Pinpoint automatically removes identifying information from this preview
image.

## Sending IP addresses

This section of the campaign details page lists all the IP addresses that Amazon Pinpoint and
Amazon SES used when sending the selected message to your recipients.
