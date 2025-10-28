**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Verifying email identities

In Amazon Pinpoint, an _identity_ is an email address or domain that you use to
send email. Before you can send email by using Amazon Pinpoint, you must verify each identity that you
plan to use as a _From_, _Source_, _Sender_, or _Return path_ address to prove that you own it. If your account
is still in the Amazon Pinpoint sandbox, you also must verify the identities that you plan to send
email to.

Before you verify an identity, you have to create a project and enable the email channel
for the project. For more information, see [Creating an Amazon Pinpoint project with email
support](channels-email-setup-create.md "channels-email-setup-create.md").

###### Topics in this section

- [Verifying an email
  address](#channels-email-manage-verify-email-address "#channels-email-manage-verify-email-address")
- [Verifying a domain](#channels-email-manage-verify-domain "#channels-email-manage-verify-domain")

## Verifying an email

address

If you've already created a project for sending email, you probably already verified
an email address. You can verify a different email address by using the Amazon Pinpoint
console.

###### To verify an email address

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. In the navigation pane, under **Email**, choose
   **Email identities**.
3. Choose **Verify email identity**.
4. Under **Identity type**, choose **Email
   address**.
5. For **Verify a new email address**, enter the email address
   that you want to verify.
6. Choose **Verify email address**.
7. Check the inbox of the address that you entered and look for an email from
   *no-reply-aws@amazon.com*. Open the email and select the
   link in the email to complete the verification process for the email
   address.

###### Note

You should receive the verification email within five minutes. If you
don't receive the email, do the following:

    * Make sure you typed the address correctly.
    * Make sure the email address that you're attempting to verify can
     receive email. You can test this by using another email address to
     send a test email to the address that you want to verify.
    * Check your junk mail folder.The link in the verification email expires after 24 hours. To resend the

verification email, choose **Send verification email
again**.

When you verify an email address, consider the following:

- Amazon Pinpoint has endpoints in multiple AWS Regions and the verification status of
  an email address is separate for each Region. If you want to send email from the
  same identity in more than one Region, you must verify that identity in each
  Region. You can verify as many as 10,000 identities (email addresses and
  domains, in any combination) in each AWS Region.
- The _local part_ of the email address, which is the part
  that precedes the at sign (@), is case sensitive. For example, if you verify
  *user@example.com*, you can't send email from
  *USER@example.com* unless you verify that address
  too.
- Domain names are case insensitive. For example, if you verify
  *user@example.com*, you can also send emails from
  *user@EXAMPLE.com*.
- You can apply labels to verified email addresses by adding a plus sign (+)
  followed by a string of text after the local part of the address and before the
  at sign (@). For example, to apply _label1_ to the address
  *user@example.com*, use
  *user+label1@example.com*. You can use as many labels as
  you want for each verified address. You can also use labels in the _From_ and _Return
  path_ fields to implement Variable Envelope Return Path (VERP).

###### Note

When you verify an unlabeled address, you're verifying all addresses that
could be formed by adding a label to the address. However, if you verify a
labeled address, you can't use other labels with that address.

## Verifying a domain

When you verify a domain, you verify all the email addresses that are associated with
that domain. Therefore, you don't need to verify individual email addresses from the
domain. For example, if you verify the _example.com_ domain, you can
send email from *carlos@example.com*,
*jane@example.com*, and any other address from the
_example.com_ domain.

Before you can use Amazon Pinpoint to send email from a domain, you have to verify the domain to
confirm that you own it and to prevent others from using it.

###### Note

To complete the verification process, you must be able to modify the DNS settings
for the domain. The procedures for modifying the DNS settings for a domain vary
depending on the DNS or web hosting provider. For information about changing the DNS
settings for your domain, see the documentation for your provider.

###### To verify a domain

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. In the navigation pane, under **Email**, choose
   **Email identities**.
3. Choose **Verify email identity**.
4. Under **Identity type**, choose **Domain**,
   and then choose **Verify a new domain**.
5. For **Domain**, enter the domain that you want to
   verify.
6. Choose **Verify domain**.
7. Under **Record set**, copy the three CNAME records and save
   them to a location on your computer. Or, to download and save the values in a
   .csv file, choose **Download record set**.
8. Log in to the management console for your DNS or web hosting provider, and
   then create three new CNAME records that contain the values that you saved in
   the previous step. See the next section for links to the documentation for
   several common providers.
9. When Amazon Pinpoint detects all three of these CNAME records in the DNS configuration
   of your domain, the verification process is complete. You can check the
   verification status by returning to the **Email identities**
   page. In the **All identities** table, locate the domain that
   you attempted to verify. If the value in the **Status** column
   for that domain is _Active_, the verification process is
   complete.

###### Note

In some cases, it can take 72 hours or more for DNS changes to propagate
across the internet. You can't send email from a domain until the
verification process is complete.

When you verify a domain, consider the following:

- You can send email from any subdomain of the verified domain, without
  verifying the subdomain specifically. For example, if you verify
  _example.com_, you don't need to verify
  _a.example.com_ or _a.b.example.com_.
- As specified in [RFC
  1034](https://datatracker.ietf.org/doc/html/rfc1034 "https://datatracker.ietf.org/doc/html/rfc1034"), each DNS label can have up to 63 characters. In addition, the
  whole domain name must not exceed a total length of 255 characters.
- Amazon Pinpoint is available in multiple AWS Regions, and the verification status of a
  domain is separate for each Region. If you want to send email from the same
  identity in more than one Region, you must verify that identity in each Region.
  You can verify as many as 10,000 identities (domains and email addresses, in any
  combination) in each AWS Region.

### Instructions for configuring DNS records for various providers

The procedures for updating the DNS records for a domain vary depending on which
DNS or web hosting provider you use. The following table lists links to the
documentation for several common providers. This list isn't exhaustive and inclusion
in this list isn't an endorsement or recommendation of any company's products or
services. If your provider isn't listed in the table, you can probably use the
domain with Amazon Pinpoint.

| DNS/hosting provider | Documentation link                                                                                                                                                                                                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Route 53      | [Working with records](../../../Route53/latest/DeveloperGuide/rrsets-working-with.md "../../../Route53/latest/DeveloperGuide/rrsets-working-with.md")                                                                                                                                                                           |
| GoDaddy              | [Add a CNAME record](https://www.godaddy.com/help/add-a-cname-record-19236 "https://www.godaddy.com/help/add-a-cname-record-19236") (external link)                                                                                                                                                                             |
| Dreamhost            | [How do I add custom DNS records?](https://help.dreamhost.com/hc/en-us/articles/360035516812-Adding-custom-DNS-records "https://help.dreamhost.com/hc/en-us/articles/360035516812-Adding-custom-DNS-records") (external link)                                                                                                   |
| Cloudflare           | [Managing DNS records in cloudflare](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records "https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records") (external link)                                                                                                   |
| HostGator            | [Manage DNS records with HostGator/eNom](https://www.hostgator.com/help/article/manage-dns-records-with-hostgatorenom "https://www.hostgator.com/help/article/manage-dns-records-with-hostgatorenom") (external link)                                                                                                           |
| Namecheap            | [How do I add TXT/SPF/DKIM/DMARC records for my domain?](https://www.namecheap.com/support/knowledgebase/article.aspx/317/2237/how-do-i-add-txtspfdkimdmarc-records-for-my-domain/ "https://www.namecheap.com/support/knowledgebase/article.aspx/317/2237/how-do-i-add-txtspfdkimdmarc-records-for-my-domain/") (external link) |
| Names.co.uk          | [Changing your domains DNS settings](https://www.names.co.uk/support/articles/changing-your-domains-dns-settings/ "https://www.names.co.uk/support/articles/changing-your-domains-dns-settings/") (external link)                                                                                                               |
| Wix                  | [Adding or Updating CNAME Records in Your Wix Account](https://support.wix.com/en/article/adding-or-updating-cname-records-in-your-wix-account "https://support.wix.com/en/article/adding-or-updating-cname-records-in-your-wix-account")                                                                                       | ### Domain verification tips and troubleshooting If you completed the preceding steps but your domain isn't verified after 72 hours, check the following: <br>• Make sure that you entered the values for the DNS records in the correct fields. Some providers refer to the **Name/host** field as _Host_ or _Hostname_. In addition, some providers refer to the **Record value** field as _Points to_ or _Result_. <br>• Make sure that your provider didn't automatically append your domain name to the **Name/host** value that you entered in the DNS record. Some providers append the domain name without indicating that they've done so. If your provider appended your domain name to the **Name/host** value, remove the domain name from the end of the value. You can also try adding a period to the end of the value in the DNS record. This period indicates to the provider that the domain name is fully qualified. <br>• The underscore character (\_) is required in the **Name/host** value of each DNS record. If your provider doesn't allow underscores in DNS record names, contact the provider's customer support department for additional assistance. <br>• The validation records that you have to add to the DNS configuration for your domain are different for each AWS Region. If you want to use a domain to send email from multiple AWS Regions, you have to verify the domain in each of those Regions. |
