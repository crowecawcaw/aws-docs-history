

# Adding a custom domain managed by a third-party DNS provider
<a name="to-add-a-custom-domain-managed-by-a-third-party-dns-provider"></a>

If you are not using Amazon Route 53 to manage your domain, you can add a custom domain managed by a third-party DNS provider to your app deployed with Amplify.

If you are using GoDaddy, see [Updating DNS records for a domain managed by GoDaddy](to-add-a-custom-domain-managed-by-godaddy.md) for instructions specific to this provider.

If you are using Cloudflare, see [Updating DNS records for a domain managed by Cloudflare](to-add-a-custom-domain-managed-by-cloudflare.md) for instructions specific to this provider.

**To add a custom domain managed by a third-party DNS provider**

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/).

1. Choose your app that you want to add a custom domain to.

1. In the navigation pane, choose **Hosting**, **Custom domains**.

1. On the **Custom domains** page, choose **Add domain**.

1. Enter the name of your root domain. For example, if the name of your domain is **https://example.com**, enter **example.com**.

1. Amplify detects that you are not using a Route 53 domain and gives you the option to create a hosted zone in Route 53.
   + To create a hosted zone in Route 53

     1. Choose **Create hosted zone on Route 53**.

     1. Choose **Configure domain**.

     1. Hosted zone name servers are displayed in the console. Go to your DNS provider's website and add the name servers to your DNS settings.

     1. Select **I have added the above name servers to my domain registry**.

     1. Proceed to step seven.
   + To continue with manual configuration

     1. Choose **Manual configuration**

     1. Choose **Configure domain**.

     1. Proceed to step seven.

1. By default, Amplify automatically creates two subdomain entries for your domain. For example, if your domain name is **example.com**, you will see the subdomains **https://www.example.com** and **https://example.com** with a redirect set up from the root domain to the **www** subdomain. 

   (Optional) You can modify the default configuration if you want to add subdomains only. To change the default configuration, choose **Rewrites and redirects** from the navigation pane and configure your domain.

1. Choose the SSL/TLS certificate to use. You can either use the default managed certificate that Amplify provisions for you, or a custom third-party certificate that you have imported into AWS Certificate Manager.
   + Use the default Amplify managed certificate.

     1. Choose **Amplify managed certificate**.
   + Use a custom third-party certificate.

     1. Choose **Custom SSL certificate**.

     1. Select the certificate to use from the list.

1. Choose **Add domain**.

1. If you chose **Create hosted zone on Route 53** in step six, proceed to step 15.

   If you chose **Manual configuration**, in step six, you must update your DNS records with your third-party domain provider. 

   On the **Actions** menu, choose **View DNS records**. The following screenshot shows the DNS records displayed in the console.  
![The DNS records displayed in the Amplify console.](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-customdomains-DNSRecords.png)

1. Do one of the following: 
   + If you're using GoDaddy, go to [Updating DNS records for a domain managed by GoDaddy](to-add-a-custom-domain-managed-by-godaddy.md).
   + If you're using Cloudflare, go to [Updating DNS records for a domain managed by Cloudflare](to-add-a-custom-domain-managed-by-cloudflare.md).
   + If you're using a different third-party DNS provider, go to the next step in this procedure. 

1. Go to your DNS provider's website, log in to your account, and locate the DNS management settings for your domain. You will configure two CNAME records.

1. Configure the first CNAME record to point your subdomain to the AWS validation server.

   If the Amplify console displays a DNS record for verifying ownership of your subdomain such as **\_c3e2d7eaf1e656b73f46cd6980fdc0e.example.com**, enter only ** \_c3e2d7eaf1e656b73f46cd6980fdc0e** for the CNAME record subdomain name.

   The following screenshot shows the location of the verification record to use.  
![The DNS records section in the Amplify console with the Hostname verification record circled.](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-customdomains-DNS-verification-1.png)

   If the the Amplify console displays an ACM validation server record such as **\_cjhwou20vhu2exampleuw20vuyb2ovb9.j9s73ucn9vy.acm-validations.aws**, enter **\_cjhwou20vhu2exampleuw20vuyb2ovb9.j9s73ucn9vy.acm-validations.aws** for the CNAME record value.

   The following screenshot shows the location of the ACM verification record to use.  
![The DNS records in the Amplify console, including the ACM verification record.](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-customdomains-DNS-verification2.png)

   Amplify uses this information to verify ownership of your domain and generate an SSL/TLS certificate for your domain. Once Amplify validates ownership of your domain, all traffic will be served using HTTPS/2.
**Note**  
The default Amplify certificate generated by AWS Certificate Manager (ACM) is valid for 13 months and renews automatically as long as your app is hosted with Amplify. Amplify can't renew the certificate if the CNAME verification record has been modified or deleted. You must delete and add the domain again in the Amplify console.
**Important**  
It is important that you perform this step soon after adding your custom domain in the Amplify console. The AWS Certificate Manager (ACM) immediately starts attempting to verify ownership. Over time, the checks become less frequent. If you add or update your CNAME records a few hours after you create your app, this can cause your app to get stuck in the pending verification state.

1. Configure a second CNAME record to point your subdomains to the Amplify domain. For example, if your subdomain is **www.example.com**, enter **www** for the subdomain name.

   If the Amplify console displays the domain for your app as **d111111abcdef8.cloudfront.net**, enter **d111111abcdef8.cloudfront.net** for the Amplify domain.

   If you have production traffic, we recommended you update this CNAME record after your domain status shows as **AVAILABLE** in the Amplify console.

   The following screenshot shows the location of the domain name record to use.  
![The DNS records in the Amplify console, including the domain name record.](http://docs.aws.amazon.com/amplify/latest/userguide/images/amplify-customdomains-DNS-verification3.png)

1. Configure the ANAME/ALIAS record to point to the root domain of your app (for example **https://example.com**). An ANAME record points the root of your domain to a hostname. If you have production traffic, we recommended that you update your ANAME record after your domain status shows as **AVAILABLE** in the console. For DNS providers that don't have ANAME/ALIAS support, we strongly recommend migrating your DNS to Route 53. For more information, see [Configuring Amazon Route 53 as your DNS service](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring.html).

**Note**  
Verification of domain ownership and DNS propagation for third-party domains can take up to 48 hours. For help resolving errors that occur, see [Troubleshooting custom domains](custom-domain-troubleshoot-guide.md). 