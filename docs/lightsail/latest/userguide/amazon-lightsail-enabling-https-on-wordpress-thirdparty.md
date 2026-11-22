

# Enabling HTTPS on a WordPress instance with a domain outside Lightsail

Lightsail Setup helps you quickly connect your domain to your WordPress instance. With Lightsail Setup, you get a Let's Encrypt certificate that automatically renews every 60–90 days. When the setup is complete, visitors can securely access your website using your custom domain name.

Follow these instructions if:
+ Your Domain Name System (DNS) is managed outside of Lightsail, such as in a Route 53 hosted zone, Cloudflare, GoDaddy, or another DNS provider
+ You have a domain registered outside of Lightsail and want to use Lightsail to manage your DNS.

For instructions on enabling HTTPS when your domain is registered through Lightsail or Route 53 and managed using a Lightsail DNS zone, see [Enable HTTPS on your WordPress instance with a Lightsail managed domain](amazon-lightsail-enabling-https-on-wordpress.md).

## Prerequisites
<a name="thirdparty-prerequisites"></a>

Before starting Lightsail Setup, confirm the following:
+ **A running Lightsail WordPress instance** – Your instance must be in a running state. If you don't have one, see [Create a Lightsail instance](how-to-create-amazon-lightsail-instance-virtual-private-server-vps.md).
+ **A domain registered outside of Lightsail** – Your domain is registered with a registrar other than Lightsail – for example, GoDaddy, Namecheap, or Cloudflare. The domain must be verified and active. If your domain is registered through Lightsail or Route 53, use [Enable HTTPS on your WordPress instance with a Lightsail managed domain](amazon-lightsail-enabling-https-on-wordpress.md) instead.
+ **Access to your DNS provider** – You need the ability to create DNS records (A and AAAA) at the service that manages your domain's DNS. This could be a Route 53 hosted zone, Cloudflare, GoDaddy, Google Cloud DNS, or another provider. You can also use a Lightsail DNS zone to manage your DNS records – see [Create a DNS zone to manage domain records for Lightsail instances](lightsail-how-to-create-dns-entry.md).
+ **Your instance firewall allows Lightsail Setup** – Ensure that your instance's firewall allows the following traffic, so that Lightsail Setup can configure HTTPS:
  + **SSH** (TCP 22) – Must allow **Lightsail Setup**. Lightsail Setup uses this port to connect to your instance.
  + **HTTP** (TCP 80) – Must allow any IPv4 and IPv6 address. Let's Encrypt uses this port to validate domain ownership.
  + **HTTPS** (TCP 443) – Must allow any IPv4 and IPv6 address. Your website uses this port to serve HTTPS traffic.

  To check, open the **Networking** tab of your instance. If the **SSH** rule doesn't allow **Lightsail Setup**, edit the rule and select **Lightsail Setup access**. For more information, see [Control instance traffic with firewalls in Lightsail](understanding-firewall-and-port-mappings-in-amazon-lightsail.md).

## Step 1: Selecting your domain
<a name="thirdparty-start-setup"></a>

**To select your domain**

1. Open the Lightsail console at [the Lightsail home page](https://lightsail.aws.amazon.com/).

1. Choose your WordPress instance from the instance list.

1. In the **Getting started** tab, choose **Start Lightsail Setup**.

1. Because your domain is registered outside of Lightsail, select **Third-party domain**, and then enter your domain name (for example, `example.com`).

1. Choose **Use this domain** to continue.

## Step 2: Configuring DNS
<a name="thirdparty-configure-dns"></a>

A DNS provider manages the records that route traffic from your domain to your instance.

**To configure DNS**

1. Choose how you want to manage these records:
   + **Lightsail DNS zone** – Lightsail manages DNS records for you.
     + If a Lightsail DNS zone already exists for your domain in the same account where your instance is set up, Lightsail Setup displays it. Choose **Use this DNS zone**.
     + If a DNS zone does not exist, choose **Create DNS zone**. Lightsail Setup creates the DNS zone for your domain.
   + **Third-party DNS** – Choose this if you are managing your DNS records with another provider, such as Route 53 hosted zone, Cloudflare, or GoDaddy.

1. If you chose **Lightsail DNS zone**, continue to [Step 3: Updating name servers](#thirdparty-update-nameservers).

   If you chose **Third-party DNS**, skip to [Step 4: Configuring a static IP](#thirdparty-static-ip).

## Step 3: Updating name servers
<a name="thirdparty-update-nameservers"></a>

Complete this step only if you chose **Lightsail DNS zone** in [Step 2: Configuring DNS](#thirdparty-configure-dns). You need to update your domain's name servers at your registrar to point to the Lightsail name servers displayed in Lightsail Setup.

The exact steps for updating name servers vary by registrar. Refer to your registrar's documentation for guidance:
+ [GoDaddy: Change my domain nameservers](https://www.godaddy.com/help/edit-my-domain-nameservers-664) on the GoDaddy website
+ [Namecheap: Change DNS for a domain](https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-to-change-dns-for-a-domain/) on the Namecheap website
+ [Cloudflare: Update nameservers](https://developers.cloudflare.com/dns/nameservers/update-nameservers/) on the Cloudflare website

**To update your name servers**

1. Under **Update name server**, enable **Display all name servers into a single, comma separated list**, and then copy the name servers.

1. Sign in to the website where you registered your domain (your registrar).

1. Find the name server settings for your domain and replace them with the Lightsail name servers you copied from Lightsail Setup.

1. Save your changes.

1. Return to the Lightsail Setup page and choose **Continue**.

**Note**  
Name server changes can take up to 48 hours to propagate. If Lightsail Setup fails after updating name servers, wait and try again.

### Example: Updating name servers in GoDaddy
<a name="thirdparty-nameserver-example-godaddy"></a>

The following example walks you through how to update your name servers in GoDaddy. For more information, see [GoDaddy: Change my domain nameservers](https://www.godaddy.com/help/edit-my-domain-nameservers-664) on the GoDaddy website.

**To update name servers in GoDaddy**

1. Sign in to your [GoDaddy Domain Portfolio](https://dcc.godaddy.com/control/portfolio).

1. Select your domain to access the Domain Settings page.

1. Select **DNS** and then select **Nameservers**.

1. Select **Change Nameservers**.

1. Replace the existing name servers with the Lightsail name servers displayed in Lightsail Setup.

1. Select **Save**.

## Step 4: Configuring a static IP
<a name="thirdparty-static-ip"></a>

A static IP address provides a fixed public IP for your instance. Without a static IP, your instance's IP address can change if you stop and restart it, which breaks your domain's connection.

**To configure a static IP**

1. Choose one of the following:
   + **Create a new static IP** – Enter a name for your static IP and choose **Create static IP**.
   + **Use an existing static IP** – If you have an unattached static IP in the same AWS Region, select it from the list, and then choose **Attach static IP**.

1. If you chose **Third-party DNS** in [Step 2: Configuring DNS](#thirdparty-configure-dns), continue to [Step 5: Creating DNS records](#thirdparty-create-dns-records).

   If you chose **Lightsail DNS zone** in [Step 2: Configuring DNS](#thirdparty-configure-dns), skip to [Step 6: Verifying DNS and managing domain assignments](#thirdparty-verify-dns).

After this step, you have a static IP attached to your instance and can see the IP addresses you need for DNS configuration.

## Step 5: Creating DNS records
<a name="thirdparty-create-dns-records"></a>

Complete this step only if you chose **Third-party DNS** in [Step 2: Configuring DNS](#thirdparty-configure-dns). In Lightsail Setup, you can see the IPv4 and IPv6 addresses that your domain must resolve to. You need to create DNS records at your DNS provider that point your domain to these addresses.
+ **A record** (required) – Points your domain to the IPv4 address of your instance.
+ **AAAA record** (optional) – Points your domain to the IPv6 address of your instance.

**Note**  
An AAAA record isn't required. If your domain has an AAAA record, it must point to your instance's IPv6 address, else Lightsail Setup fails.

The exact steps for creating DNS records vary by provider. Refer to your provider's documentation for guidance on adding A and AAAA records:
+ [GoDaddy: Manage DNS records](https://www.godaddy.com/help/manage-dns-records-680) on the GoDaddy website
+ [Cloudflare: Manage DNS records](https://developers.cloudflare.com/dns/manage-dns-records/) on the Cloudflare website
+ [Namecheap: Set up an A record](https://www.namecheap.com/support/knowledgebase/article.aspx/319/2237/how-can-i-set-up-an-a-address-record-for-my-domain/) on the Namecheap website

**Note**  
Keep the Lightsail Setup page open. You return to it after creating your DNS records.

**To create your DNS records with another provider**

1. Sign in to your DNS provider's management console.

1. Navigate to the DNS records section for your domain.

1. Create an **A** record for your root domain (`example.com`) with the value set to the static IPv4 address displayed in Lightsail Setup.

1. (Optional) Create an **AAAA** record for your root domain (`example.com`) with the value set to the IPv6 address displayed in Lightsail Setup.

1. (Optional) Repeat steps 3–4 for your www subdomain (`www.example.com`).

### Example: Adding A and AAAA records in GoDaddy
<a name="thirdparty-dns-godaddy-example"></a>

The following example walks you through how to add A and AAAA records in GoDaddy. For more information, see [GoDaddy: Manage DNS records](https://www.godaddy.com/help/manage-dns-records-680) on the GoDaddy website.

**To add A and AAAA records in GoDaddy**

1. Sign in to your [GoDaddy Domain Portfolio](https://dcc.godaddy.com/control/portfolio).

1. Select your domain to access the Domain Settings page.

1. Select **DNS** to view your DNS records.

1. Select **Add New Record**, and then select **A** from the **Type** menu.

1. Enter the following:
   + **Name**: `@` (for your root domain)
   + **Value**: The static IPv4 address displayed in Lightsail Setup
   + **TTL**: 1 hour (default)

1. Select **Add another record**, and select **AAAA** from the **Type** menu.

1. Enter the following:
   + **Name**: `@` (for your root domain)
   + **Value**: The IPv6 address displayed in Lightsail Setup
   + **TTL**: 1 hour (default)

1. Select **Save**.

1. (Optional) Repeat steps 4–8 for your www subdomain, entering `www` in the **Name** field.

## Step 6: Verifying DNS and managing domain assignments
<a name="thirdparty-verify-dns"></a>

### Managing domain assignments
<a name="thirdparty-manage-domain-assignments"></a>

Complete these instructions if you chose **Lightsail DNS zone** in [Step 2: Configuring DNS](#thirdparty-configure-dns). If you chose **Third-party DNS**, skip to [Verifying your name servers and DNS records](#thirdparty-verify-dns-records). *Domain assignments* are DNS records that direct traffic for your domain to your instance. Lightsail creates these records for you automatically.

**To add a domain assignment**

1. Choose **Add assignment**.

1. Add your root domain (for example, `example.com`).

1. (Optional) Add your www subdomain (for example, `www.example.com`).

1. Choose **Continue**.

1. Continue to [Step 7: Creating an SSL/TLS certificate](#thirdparty-create-certificate).

**Tip**  
If you skip the www subdomain, visitors who type `www.example.com` do not reach your site.

### Verifying your name servers and DNS records
<a name="thirdparty-verify-dns-records"></a>

Complete these instructions if you chose **Third-party DNS** in [Step 2: Configuring DNS](#thirdparty-configure-dns). If you chose **Lightsail DNS zone**, skip to [Step 7: Creating an SSL/TLS certificate](#thirdparty-create-certificate).

Your domain's name servers point to the correct DNS provider. They must point to the same provider where you created your A and AAAA records. If they don't match, traffic does not reach your records, and Lightsail Setup fails.

**To verify your name servers**

1. Use [NS Lookup](https://dnschecker.org/ns-lookup.php) on the *dnschecker.org* website. You can also verify from the command line:
   + For macOS and Linux, run the following command:

     ```bash
     $ dig NS {{example.com}} +short
     ```
   + For Windows, run the following command:

     ```
     C:\> nslookup -type=NS {{example.com}}
     ```

1. Confirm that the result shows the correct provider. For example, if you created records in GoDaddy, the result should show GoDaddy name servers. If you created records in Route 53, the result should show `awsdns-*` name servers. If the result shows a different provider, update your domain's name servers at your registrar before continuing.

**To verify your DNS records**

1. Check [DNS Checker](https://dnschecker.org) on the *dnschecker.org* website. You can also verify from the command line:
   + For macOS and Linux, run the following command:

     ```bash
     $ dig {{example.com}} A +short
     $ dig {{example.com}} AAAA +short
     ```
   + For Windows, run the following command:

     ```
     C:\> nslookup -type=A {{example.com}}
     C:\> nslookup -type=AAAA {{example.com}}
     ```

1. Confirm the results. The **A** queries should return your instance's static IPv4 address. If you created an **AAAA** record, the **AAAA** queries should return your instance's IPv6 address. The results should match what Lightsail Setup displayed.

**Important**  
DNS changes can take anywhere from a few minutes to 48 hours to propagate. Do not proceed to certificate creation until all records resolve to the correct addresses. If you proceed before your DNS changes have fully propagated, your SSL/TLS certificate fails to validate because Lightsail can't confirm that you control the domain. If the commands do not return the expected values, wait and try again.

## Step 7: Creating an SSL/TLS certificate
<a name="thirdparty-create-certificate"></a>

**To create a certificate**

1. Select the domains and subdomains you want to secure with HTTPS (for example, `example.com` and `www.example.com`). You can secure up to 10 domains and subdomains.

1. Enter your email address. This is used for certificate renewal notifications.

1. Select **I authorize Lightsail to configure a Let's Encrypt certificate on my instance**. This gives Lightsail restricted access to create and configure the certificate on your instance.

1. Choose **Create certificate**.

Lightsail Setup configures HTTPS on your instance. This process takes up to 15 minutes.

If setup fails, see [Lightsail Setup failed](amazon-lightsail-troubleshooting-wp-https-lightsail.md) for troubleshooting steps.

**Important**  
Do not stop, reboot, or modify your instance while setup is in progress.

## Step 8: Verifying your website
<a name="thirdparty-verify-website"></a>

**To verify your website**

1. Open your browser and go to `https://{{example.com}}`.

1. Confirm that your website loads successfully.

1. Test each additional domain and subdomain that you secured in the certificate (for example, `https://www.{{example.com}}`) to confirm they all load successfully over HTTPS.

1. To confirm that your website uses the certificate that Lightsail Setup created, view the certificate in your browser. For example, in Google Chrome:

   1. In the address bar, choose the site information icon to the left of the URL, and then choose **Connection is secure**.

   1. Choose **Certificate details**.

   1. Confirm that the certificate is issued to your domain. Under **Issued By**, confirm that **Organization (O)** is Let's Encrypt.

Your website is now configured with HTTPS and an automatic redirect from HTTP to HTTPS.

**Note**  
Let's Encrypt certificates automatically renew every 60–90 days. If renewal fails in the future, see [Certificate did not automatically renew](amazon-lightsail-troubleshooting-wp-cert-renewal-lightsail.md).

## Learn more
<a name="thirdparty-learn-more"></a>
+ [Understanding DNS in Lightsail](understanding-dns-in-amazon-lightsail.md)
+ [Register and manage domains](amazon-lightsail-domain-registration.md)
+ [Create a DNS zone to manage domain records](lightsail-how-to-create-dns-entry.md)
+ [Instance firewalls](understanding-firewall-and-port-mappings-in-amazon-lightsail.md)
+ [Static IP addresses](understanding-static-ip-addresses-in-amazon-lightsail.md)