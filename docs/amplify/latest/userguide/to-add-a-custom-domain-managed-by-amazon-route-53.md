# Adding a custom domain

managed by Amazon Route 53

Amazon Route 53 is a highly available and scalable DNS service. For more information, see
[Amazon
Route 53](../../../Route53/latest/DeveloperGuide/Welcome.md "../../../Route53/latest/DeveloperGuide/Welcome.md") in the _Amazon Route 53 Developer Guide_. If you already have a
Route 53 domain, use the following instructions to connect your custom domain to your
Amplify app.

###### To add a custom domain managed by Route 53

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose your app that you want to connect to a custom domain.
3. In the navigation pane, choose **Hosting**, **Custom
   domains**.
4. On the **Custom domains** page, choose **Add
   domain**.
5. Enter the name of your root domain. For example, if the name of your domain is
   **https://example.com**, enter
   `example.com`.

As you start typing, any root domains that you already manage in Route 53 appear in
the list. You can choose the domain you want to use from the list. If you don't
already own the domain and it is available, you can purchase the domain in [Amazon Route 53](../../../Route53/latest/DeveloperGuide/domain-register.md "../../../Route53/latest/DeveloperGuide/domain-register.md"). 6. After you enter your domain name, choose **Configure
domain**. 7. By default, Amplify automatically creates two subdomain entries for your domain.
For example, if your domain name is **example.com**, you
will see the subdomains **https://www.example.com** and
**https://example.com** with a redirect set up from
the root domain to the **www** subdomain.

(Optional) You can modify the default configuration if you want to add subdomains
only. To change the default configuration, choose **Rewrites and
redirects** from the navigation pane, then configure your domain. 8. Choose the SSL/TLS certificate to use. You can either use the default managed
certificate that Amplify provisions for you, or a custom third-party certificate
that you have imported into AWS Certificate Manager.

    * Use the default Amplify managed certificate.


    	1. Choose **Amplify managed certificate**.
    * Use a custom third-party certificate.


    	1. Choose **Custom SSL certificate**.
    	2. Select the certificate to use from the list.

9. Choose **Add domain**.

###### Note

It can take up to 24 hours for the DNS to propagate and to issue the
certificate. For help with resolving errors that occur, see [Troubleshooting custom domains](custom-domain-troubleshoot-guide.md "custom-domain-troubleshoot-guide.md").
