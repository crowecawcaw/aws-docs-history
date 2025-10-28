# Locking a domain to prevent unauthorized transfer to

another registrar

The domain registries for all generic TLDs and many geographic TLDs let you lock a
domain to prevent someone from transferring the domain to another registrar without your
permission. To determine whether the registry for your domain lets you lock the domain,
see [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md"). If locking
is supported and you want to lock your domain, perform the following procedure. You can
also use the procedure to disable the lock if you want to transfer a domain to another
registrar.

###### To lock a domain to prevent unauthorized

transfer to another registrar

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Registered Domains**.
3. Choose the name of the domain that you want to update.
4. On the **Details** section, in the
   **Actions** dropdown, choose **Turn on transfer
   lock** or **Turn off transfer lock**, depending on
   whether you want to turn the transfer lock on or off.

You can navigate to the **Requests** page to see the progress
of your request. 5. If you encounter issues while locking a domain, you can contact AWS Support
for free. For more information, see [Contacting AWS Support about domain registration issues](domain-contact-support.md "domain-contact-support.md").
In WHOIS search, this status shows up as: `clientTransferProhibited`. Some
TLDs might have these statuses in addition:

- `clientUpdateProhibited`
- `clientDeleteProhibited`
