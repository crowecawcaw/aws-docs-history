

# Enable HTTPS on your WordPress instance with a domain registered outside of Lightsail
<a name="amazon-lightsail-enabling-https-on-wordpress-thirdparty"></a>

Lightsail Setup helps you quickly connect your domain to your WordPress instance. Lightsail Setup creates a Let's Encrypt certificate that automatically renews every 60 to 90 days. When the setup is complete, visitors can securely access your website using your custom domain name.

This guide applies when your DNS is managed outside of Lightsail – for example, in a Route 53 hosted zone, Cloudflare, GoDaddy, or another DNS provider. It also applies if you have a domain registered outside of Lightsail and want to use Lightsail to manage your DNS.

If your domain is registered through Lightsail or Route 53 and managed using a Lightsail DNS zone, see [Enable HTTPS on your WordPress instance with a Lightsail managed domain](amazon-lightsail-enabling-https-on-wordpress.md).

## Step 1: Complete the prerequisites
<a name="thirdparty-prerequisites"></a>

Before starting Lightsail Setup, confirm the following:
+ **A running Lightsail WordPress instance.** Your instance must be in a running state. If you don't have one, see [Create an instance](how-to-create-amazon-lightsail-instance-virtual-private-server-vps.md).  
![A WordPress instance in a running state in the Lightsail console.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/instance-running.png)
+ **A domain registered outside of Lightsail.** Your domain is registered with a registrar other than Lightsail – for example, GoDaddy, Namecheap, or Cloudflare. The domain must be verified and active. If your domain is registered through Lightsail or Route 53, use [Enable HTTPS on your WordPress instance with a Lightsail managed domain](amazon-lightsail-enabling-https-on-wordpress.md) instead.
+ **Access to your DNS provider.** You need the ability to create DNS records (A and AAAA) at the service that manages your domain's DNS. This could be a Route 53 hosted zone, Cloudflare, GoDaddy, Google Cloud DNS, or another provider. You can also use a Lightsail DNS zone to manage your DNS records – see [Create a DNS zone to manage domain records](lightsail-how-to-create-dns-entry.md).
+ **Ports 22, 80, and 443 are configured to enable Lightsail Setup.** Port 22 is required for Lightsail Setup to connect to your instance. Port 80 is required for domain ownership validation during certificate installation. Port 443 is required for serving HTTPS traffic after setup. You can verify this on the **Networking** tab of your instance's management page. For more information, see [Instance firewalls](understanding-firewall-and-port-mappings-in-amazon-lightsail.md).  
![Firewall rules showing ports 22, 80, and 443 configured on the Networking tab in the Lightsail console.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/ports-open.png)

## Step 2: Start Lightsail Setup
<a name="thirdparty-start-setup"></a>

1. Open the Lightsail console at [the Lightsail home page](https://lightsail.aws.amazon.com/).

1. Choose your WordPress instance from the instance list.  
![Selecting a WordPress instance from the instance list in the Lightsail console.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/instance-selection.png)

1. Choose the **Connect** tab and choose **Set up your website**.  
![The Set up your website button on the Connect tab in the Lightsail console.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/your-website.png)

## Step 3: Select your domain
<a name="thirdparty-select-domain"></a>

Because your domain is registered outside of Lightsail, choose **Third-party domain** and enter your domain name (for example, `example.com`).

![Entering a domain name in the Third-party domain field of the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/thirdparty-domain-name.png)


Choose **Use this domain** to continue.

## Step 4: Configure DNS
<a name="thirdparty-configure-dns"></a>

A DNS provider manages the records that route traffic from your domain to your instance. Choose how you want to manage these records:
+ **Lightsail DNS zone** – Lightsail manages DNS records for you.
  + **If a Lightsail DNS zone already exists for your domain in the same account where your instance is set up** – Lightsail Setup displays it. Choose **Use this DNS zone**.  
![Choosing an existing DNS zone in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/choose-dns.png)
  + **If a DNS zone does not exist** – Choose **Create DNS zone**. Lightsail Setup creates the DNS zone for your domain.  
![Creating a new DNS zone in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/create-dns.png)
+ **Third-party DNS** – Choose this if you are managing your DNS records with another provider (Route 53 hosted zone, Cloudflare, GoDaddy, and so on).  
![Selecting third-party DNS in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/thirdparty-dns.png)

## Step 5: Update name servers
<a name="thirdparty-update-nameservers"></a>

Complete this step only if you chose **Lightsail DNS zone** in Step 4. If you chose **Third-party DNS**, continue to Step 6.

If you chose to use a Lightsail DNS zone, you need to update your domain's name servers at your registrar to point to the Lightsail name servers displayed in Lightsail Setup.

1. Copy the name servers displayed in the Lightsail Setup page.  
![Name servers displayed in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/update-nameserver.png)

1. Sign in to the website where you registered your domain (your registrar).

1. Find the name server settings for your domain and replace them with the Lightsail name servers you copied from Lightsail Setup.

1. Save your changes.

1. Return to the Lightsail Setup page and choose **Continue**.

### Example: Updating name servers in GoDaddy
<a name="thirdparty-nameserver-example-godaddy"></a>

**Note**  
The following example walks you through how to update your name servers in GoDaddy. For more information, see [GoDaddy: Change my domain nameservers](https://www.godaddy.com/help/edit-my-domain-nameservers-664) on the GoDaddy website.

1. Sign in to your [GoDaddy Domain Portfolio](https://dcc.godaddy.com/control/portfolio).

1. Select your domain to access the Domain Settings page.  
![Selecting a domain in the GoDaddy Domain Portfolio.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/godaddy-domain-selection.png)

1. Select **DNS** and then select **Nameservers**.

1. Select **Change Nameservers**.  
![Changing name servers in GoDaddy.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/godaddy-nameservers.png)

1. Replace the existing name servers with the Lightsail name servers displayed in Lightsail Setup.

1. Select **Save**.

**Note**  
The exact steps for updating name servers vary by registrar. Refer to your registrar's documentation for guidance:  
[Namecheap: Change DNS for a domain](https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-to-change-dns-for-a-domain/) on the Namecheap website.
[Cloudflare: Update nameservers](https://developers.cloudflare.com/dns/nameservers/update-nameservers/) on the Cloudflare website.
Name server changes can take up to 48 hours to propagate. If Lightsail Setup fails after updating name servers, wait and try again.

## Step 6: Configure a static IP
<a name="thirdparty-static-ip"></a>

A static IP address provides a fixed public IP for your instance. Without a static IP, your instance's IP address can change if you stop and restart it, which breaks your domain's connection.

Choose one of the following:
+ **Create a new static IP** – Enter a name for your static IP and choose **Create static IP**.  
![Creating a new static IP in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/create-static-ip.png)
+ **Use an existing static IP** – If you have an unattached static IP in the same AWS Region, select it from the list and choose **Attach static IP**.  
![Attaching an existing static IP in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/attach-static-ip.png)

After this step, Lightsail Setup attaches the static IP to your instance and displays the IP addresses you need for DNS configuration.

## Step 7: Create DNS records
<a name="thirdparty-create-dns-records"></a>

This step appears if you chose **Third-party DNS** in Step 4. If you chose **Lightsail DNS zone**, continue to Step 8.

Lightsail Setup displays the IPv4 and IPv6 addresses that your domain must resolve to. You need to create DNS records at your DNS provider pointing your domain to these addresses.

![IPv4 and IPv6 addresses displayed in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/ipv4-ipv6.png)


Keep the Lightsail Setup page open – you return to it after creating your records.

### If your DNS is managed by another provider (GoDaddy, Cloudflare, and so on)
<a name="thirdparty-dns-provider-example"></a>

1. Sign in to your DNS provider's management console.

1. Navigate to the DNS records section for your domain.

1. Create an **A** record for your root domain (`example.com`) with the value set to the static IPv4 address displayed in Lightsail Setup.

1. Create an **AAAA** record for your root domain (`example.com`) with the value set to the IPv6 address displayed in Lightsail Setup.

1. (Optional) Repeat steps 3–4 for your www subdomain (`www.example.com`).

#### Example: Adding A and AAAA records in GoDaddy
<a name="thirdparty-dns-godaddy-example"></a>

**Note**  
The following example walks you through how to add A and AAAA records in GoDaddy. For more information, see [GoDaddy: Manage DNS records](https://www.godaddy.com/help/manage-dns-records-680) on the GoDaddy website.

1. Sign in to your [GoDaddy Domain Portfolio](https://dcc.godaddy.com/control/portfolio).

1. Select your domain to access the Domain Settings page.

1. Select **DNS** to view your DNS records.

1. Select **Add New Record** and then select **A** from the Type menu.

1. Enter the following:
   + **Name:** `@` (for your root domain)
   + **Value:** The static IPv4 address displayed in Lightsail Setup
   + **TTL:** 1 hour (default)

1. Select **Add another record** and select **AAAA** from the Type menu.

1. Enter the following:
   + **Name:** `@` (for your root domain)
   + **Value:** The IPv6 address displayed in Lightsail Setup
   + **TTL:** 1 hour (default)  
![Adding A and AAAA records in GoDaddy.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/godaddy-records.png)

1. Select **Save**.

1. (Optional) Repeat steps 4–8 for your www subdomain, entering `www` in the Name field.

**Note**  
The exact steps for creating DNS records vary by provider. Refer to your provider's documentation for guidance on adding A and AAAA records:  
[Cloudflare: Manage DNS records](https://developers.cloudflare.com/dns/manage-dns-records/) on the Cloudflare website.
[Namecheap: Set up an A record](https://www.namecheap.com/support/knowledgebase/article.aspx/319/2237/how-can-i-set-up-an-a-address-record-for-my-domain/) on the Namecheap website.

## Step 8: Verify DNS and manage domain assignments
<a name="thirdparty-verify-dns"></a>

### Manage domain assignments
<a name="thirdparty-manage-domain-assignments"></a>

This step appears if you chose **Lightsail DNS zone** in Step 4. If you chose **Third-party DNS**, continue to **Verify your name servers and DNS records**.

Domain assignments are DNS records that direct traffic for your domain to your instance. Lightsail creates these records for you automatically.

1. Choose **Add assignment**.

1. Add your root domain (for example, `example.com`).

1. (Optional) Add your www subdomain (for example, `www.example.com`).

1. Choose **Continue**.

![Managing domain assignments in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/manage-domains.png)


**Tip**  
If you skip the www subdomain, visitors who type `www.example.com` will not reach your site.

### Verify your name servers and DNS records
<a name="thirdparty-verify-dns-records"></a>

This step appears if you chose **Third-party DNS** in Step 4. Before proceeding, confirm the following:

1. **Your domain's name servers point to the correct DNS provider.** They must point to the same provider where you created your A and AAAA records. If they don't match, traffic does not reach your records and Lightsail Setup fails.

   To verify your name servers, use [NS Lookup](https://dnschecker.org/ns-lookup.php) on the *dnschecker.org* website.

   You can also verify from the command line:
   + **macOS and Linux:**

     ```
     $ dig NS {{example.com}} +short
     ```
   + **Windows:**

     ```
     C:\> nslookup -type=NS {{example.com}}
     ```

   For example, if you created records in GoDaddy, the result should show GoDaddy name servers. If you created records in Route 53, the result should show `awsdns-*` name servers. If the result shows a different provider, update your domain's name servers at your registrar before continuing.

1. **Your DNS records resolve to the correct IP addresses.**

   To verify global propagation, check [DNS Checker](https://dnschecker.org) on the *dnschecker.org* website.

   You can also verify from the command line:
   + **macOS and Linux:**

     ```
     $ dig {{example.com}} A +short
     $ dig {{example.com}} AAAA +short
     ```
   + **Windows:**

     ```
     C:\> nslookup -type=A {{example.com}}
     C:\> nslookup -type=AAAA {{example.com}}
     ```

   The A queries should return your instance's static IPv4 address. The AAAA queries should return your instance's IPv6 address. Both should match what Lightsail Setup displayed.

**Important**  
DNS changes can take anywhere from a few minutes to 48 hours to propagate. Do not proceed to certificate creation until all records resolve to the correct addresses. If you proceed before your DNS changes have fully propagated, your SSL/TLS certificate will fail to validate because Lightsail can't confirm that you control the domain. If the commands do not return the expected values, wait and try again.

## Step 9: Create SSL/TLS certificate
<a name="thirdparty-create-certificate"></a>

### Create certificate
<a name="thirdparty-create-cert"></a>

1. Enter the domains and subdomains you want to secure with HTTPS. Because your domain is registered outside of Lightsail, you enter these manually (for example, `example.com` and `www.example.com`). You can secure up to 10 domains and subdomains.

1. Enter your email address. This is used for certificate renewal notifications.

1. Select **I authorize Lightsail to configure a Let's Encrypt certificate on my instance**. This gives Lightsail restricted access to create and configure the certificate on your instance.

1. Choose **Create certificate**.

![Manually entering domain names to create an SSL/TLS certificate in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/create-certificate-thirdparty.png)


Lightsail Setup begins configuring HTTPS on your instance. This process takes up to 15 minutes.

If setup fails, see [Lightsail Setup failed](amazon-lightsail-troubleshooting-wp-https-lightsail.md) for troubleshooting steps.

**Important**  
Do not stop, reboot, or modify your instance while setup is in progress.

## Step 10: Verify your website
<a name="thirdparty-verify-website"></a>

After Lightsail Setup completes:

1. Open your browser and go to `https://{{yourdomain.com}}`.

1. Confirm that your website loads successfully.

1. Test each additional domain and subdomain that you secured in the certificate (for example, `https://www.{{yourdomain.com}}`) to confirm they all load successfully over HTTPS.

1. Test the automatic redirect from HTTP to HTTPS. In your browser, go to `http://{{yourdomain.com}}` and confirm that the address automatically redirects to `https://{{yourdomain.com}}`.

![WordPress website loaded successfully with HTTPS enabled.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/https-verified.png)


Your website is now configured with HTTPS and an **automatic redirect from HTTP to HTTPS**.

**Note**  
Let's Encrypt certificates automatically renew every 60 to 90 days. If renewal fails in the future, see [Certificate did not automatically renew](amazon-lightsail-troubleshooting-wp-cert-renewal-lightsail.md).

## Learn more
<a name="thirdparty-learn-more"></a>
+ [Understanding DNS in Lightsail](understanding-dns-in-amazon-lightsail.md)
+ [Register and manage domains](amazon-lightsail-domain-registration.md)
+ [Create a DNS zone to manage domain records](lightsail-how-to-create-dns-entry.md)
+ [Instance firewalls](understanding-firewall-and-port-mappings-in-amazon-lightsail.md)
+ [Static IP addresses](understanding-static-ip-addresses-in-amazon-lightsail.md)