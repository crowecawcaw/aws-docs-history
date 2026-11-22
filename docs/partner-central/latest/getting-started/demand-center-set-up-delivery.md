

# Setting up delivery with Demand Center

When you launch with Demand Center, set the sender, the recipients, and the social accounts that the campaign posts from.

The **Sender email** sends every email message in the campaign. It must be an address on your alliance lead's email domain in AWS Partner Central, not a subdomain of it.

The audience source is who receives the email messages. A lead list is a comma-separated values (CSV) file of recipients that you upload for this campaign. Lead groups are saved groups of leads that AWS Partner Central curates. Lead groups can't be saved with a campaign yet, so use a lead list to send email messages.

Your lead list must meet the following requirements:
+ A CSV file up to 5 MB, saved as UTF-8, with its columns separated by commas.
+ A header row with an email column named Email, E-mail, Email Address, or E-mail Address. Other columns are ignored.
+ Up to 10,000 recipients. A list with more than 10,000 recipients isn't accepted.

1. On the **Set up delivery** step, choose **Launch with Demand Center**.

1. For **Sender email**, enter an address on your alliance lead's email domain in AWS Partner Central, not a subdomain of it.

1. For the audience source, choose **Upload a lead list**, and then upload your CSV file.

1. Under **Social accounts**, choose the connected account that each platform posts from.

1. Choose **Save and next**.

For more information about connecting a social media account, see [Connecting social media accounts to Demand Center](demand-center-social-connections.md).