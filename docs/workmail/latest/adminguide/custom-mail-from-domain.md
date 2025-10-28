# Configuring a custom MAIL FROM domain

By default, Amazon WorkMail uses a subdomain of amazonses.com as the `MAIL
 FROM` domain for your outgoing email. This can cause delivery failure if the
DMARC policy on your domain is only set up for SPF. To resolve this, configure your own
domain as the `MAIL FROM` domain. To learn how to set up your email domain as
the `MAIL FROM` domain, see [Setting up a custom MAIL FROM
domain](../../../ses/latest/DeveloperGuide/mail-from.md "../../../ses/latest/DeveloperGuide/mail-from.md") in the _Amazon Simple Email Service Developer Guide_.

###### Important

A custom MAIL FROM domain is required when you enable AutoDiscover for iOS
devices.

For more information about custom `MAIL FROM` domains, see
[Amazon SES now supports custom MAIL FROM domains](https://aws.amazon.com/blogs/messaging-and-targeting/amazon-ses-now-supports-custom-mail-from-domains/ "https://aws.amazon.com/blogs/messaging-and-targeting/amazon-ses-now-supports-custom-mail-from-domains/").
