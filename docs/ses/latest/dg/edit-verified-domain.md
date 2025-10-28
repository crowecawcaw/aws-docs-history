# Edit an identity using the SES console

You can use the Amazon SES console to edit a domain or email address identity in your account
in the selected AWS Region.

###### To edit a domain or email address identity

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the console, use the Region selector to choose the AWS Region from which you
   want to edit one or more identities.
3. In the navigation pane, under **Configuration**, choose
   **Verified identities**.

The **Loaded identities** table displays a list of both domain
and email address identities. 4. In the **Identity** column, select the identity that you want to
edit (by clicking directly on the identity name as opposed to selecting its
checkbox). 5. On the identity's detail page, select the tab containing the categories you'd like
to edit. 6. In any of the selected tab's categorical containers, choose the
**Edit** button of the attribute you wish to edit, make your
changes, then choose **Save changes**.

    1. If you wish to edit attributes under the
     **Authentication** tab and your domain identity is
     hosted in Amazon Route 53, and you haven't already published its DNS records,
     there will be a **Publish DNS records to Route53** button
     (next to the **Edit** button) in either or both of the
     **DomainKeys Identified Mail (DKIM)** or
     **Custom MAIL FROM domain** containers.


    ###### Note

    The **Authentication** tab is only present when your
     account has a verified domain or an email address that uses a verified
     domain in your account.
    2. You can publish the DNS records directly from the **Publish DNS
     records to Route53** button - just click it, a confirmation
     banner will be displayed, and the **Publish DNS records to
     Route53** button will no longer be visible for the respective
     container.

7. Repeat steps 5 & 6 for each attribute of the identity you'd like to
   edit.
