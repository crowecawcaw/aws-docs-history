# Add alternate domains

and subdomains to your Lightsail SSL/TLS certificate

When you create your SSL/TLS certificate for your Lightsail load balancer, you can add
alternate domains and subdomains to it. These alternate names help ensure that all traffic to
your load balancer is encrypted.

When you specify a primary domain, you can use a fully qualified domain name such as
`www.example.com` or an apex domain name such as `example.com`.

The total number of domains and subdomains must not exceed 10, so you can add up to 9
alternate domains and subdomains to your certificate. You might want to add entries similar to
the following list.

- example.com
- example.net
- blog.example.com
- myexamples.com

## To create a

certificate with alternate domains and subdomains

1. If you don't have one yet, [Create a load balancer](create-lightsail-load-balancer-and-attach-lightsail-instances.md "create-lightsail-load-balancer-and-attach-lightsail-instances.md").
2. In the left navigation pane, choose **Networking**.
3. Choose your Lightsail load balancer.
4. Choose the **Custom domains** tab.
5. Choose **Create certificate**.
6. Enter a name for your certificate or accept the default name.

Resource names:

    * Must be unique within each AWS Region in your Lightsail account.
    * Must contain 2 to 255 characters.
    * Must start and end with an alphanumeric character or number.
    * Can include alphanumeric characters, numbers, periods, dashes, and
     underscores.

7. Enter your primary domain (`www.example.com`), and up to 9 alternate
   domains or subdomains.
8. Choose **Create certificate**.

Once created, you have 72 hours to verify that you own your domain.

## Next steps

- [Verify
  domain ownership using DNS](verify-tls-ssl-certificate-using-dns-cname-https.md "verify-tls-ssl-certificate-using-dns-cname-https.md")

Once verified, you can select your validated certificate to associate it with your
Lightsail load balancer.

- [Enable session persistence](update-settings-for-lightsail-load-balancer-health-check-path-https-session-stickiness-persistence-cookie-duration.md "update-settings-for-lightsail-load-balancer-health-check-path-https-session-stickiness-persistence-cookie-duration.md")
