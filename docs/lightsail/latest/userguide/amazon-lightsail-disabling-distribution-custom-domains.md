# Disable custom domains

for Lightsail distributions

Disable custom domains for your Amazon Lightsail distribution to stop using your registered
domain names with your distribution. After you disable custom domains, your distribution accepts
traffic only for the default domain that is associated with your distribution when you first
create it (e.g., `123456abcdef.cloudfront.net`), and traffic for the previously
associated custom domains will see a 403 error.

For more information about distributions, see [Content delivery network
distributions](amazon-lightsail-content-delivery-network-distributions.md "amazon-lightsail-content-delivery-network-distributions.md").

## Disable custom domains for your

distribution

Complete the following procedure to disable custom domains for your distribution.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/ "https://lightsail.aws.amazon.com/").
2. In the left navigation pane, choose **Networking**.
3. Choose the name of the distribution for which want to disable custom domains.
4. Choose the **Custom domains** tab on your distribution's management
   page.

The **Custom domains** page displays the SSL/TLS certificates
currently attached to your distribution, if any. 5. Choose one of the following options:

    1. Choose **Configure distribution domains** to either deselect
     domains that were previously selected, or to select more domains that are associated
     to the distribution.
    2. Choose **Detach** to detach the certificate from the
     distribution, and remove all of its associated domains.

6. Your request to disable custom domains is submitted, and the status of your
   distribution is changed to **In progress**. After a while, the status of
   your distribution changes to **Enabled**.

After you disable custom domains, your distribution accepts traffic only for the default
domain that is associated with your distribution when you first create it (e.g.,
`123456abcdef.cloudfront.net`), and traffic for the previously associated custom
domains will see a 403 error. You should update the DNS records of the domains so that traffic
for those domains is directed to another resource.
