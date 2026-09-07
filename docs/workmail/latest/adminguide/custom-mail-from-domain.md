

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Configuring a custom MAIL FROM domain
<a name="custom-mail-from-domain"></a>

By default, Amazon WorkMail uses a subdomain of amazonses.com as the `MAIL FROM` domain for your outgoing email. This can cause delivery failure if the DMARC policy on your domain is only set up for SPF. To resolve this, configure your own domain as the `MAIL FROM` domain. To learn how to set up your email domain as the `MAIL FROM` domain, see [Setting up a custom MAIL FROM domain](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from.html) in the *Amazon Simple Email Service Developer Guide*.

**Important**  
A custom MAIL FROM domain is required when you enable AutoDiscover for iOS devices.

For more information about custom `MAIL FROM` domains, see [ Amazon SES now supports custom MAIL FROM domains](https://aws.amazon.com/blogs/messaging-and-targeting/amazon-ses-now-supports-custom-mail-from-domains/).