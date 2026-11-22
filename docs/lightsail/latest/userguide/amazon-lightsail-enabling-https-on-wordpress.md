

# Enable HTTPS on your WordPress instance with a Lightsail managed domain

Lightsail Setup helps you quickly connect your domain to your WordPress instance. Lightsail Setup creates a Let's Encrypt certificate that automatically renews every 60 to 90 days. When the setup is complete, visitors can securely access your website using your custom domain name.

This guide applies to domains that are:
+ Registered through Lightsail or Route 53
+ Managed using a Lightsail DNS zone

If your domain is registered with a third-party registrar (such as GoDaddy, Namecheap, or Cloudflare), or your DNS is not managed using a Lightsail DNS zone, see [Enable HTTPS on your WordPress instance with a domain registered outside of Lightsail](amazon-lightsail-enabling-https-on-wordpress-thirdparty.md).

## Step 1: Complete the prerequisites
<a name="before-you-begin-https"></a>

Before starting Lightsail Setup, confirm the following:
+ **A running Lightsail WordPress instance.** Create a WordPress instance in Lightsail. Your instance must be in a running state. To learn more, see [Create an instance](how-to-create-amazon-lightsail-instance-virtual-private-server-vps.md).  
![A WordPress instance in a running state in the Lightsail console.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/instance-running.png)
+ **A domain registered through Lightsail or Route 53.** Register a domain name through Lightsail or Route 53. For more information, see [Register a domain in Lightsail](amazon-lightsail-register-new-domain.md). Also ensure the domain is verified, active, and in the same account that you are using for Lightsail Setup. See [Verify the domain contact information](amazon-lightsail-register-new-domain.md#reg-new-domain-verify-info).
+ **Your instance firewall allows Lightsail Setup.** Ensure that your instance's firewall allows the following traffic, so that Lightsail Setup can configure HTTPS:
  + **SSH** (TCP 22) – Must allow **Lightsail Setup**. Lightsail Setup uses this port to connect to your instance.
  + **HTTP** (TCP 80) – Must allow any IPv4 and IPv6 address. Let's Encrypt uses this port to validate domain ownership.
  + **HTTPS** (TCP 443) – Must allow any IPv4 and IPv6 address. Your website uses this port to serve HTTPS traffic.

  To check, open the **Networking** tab of your instance. If the **SSH** rule doesn't allow **Lightsail Setup**, edit the rule and select **Lightsail Setup access**. To learn more, see [Instance firewalls](understanding-firewall-and-port-mappings-in-amazon-lightsail.md).  
![Firewall rules on the Networking tab in the Lightsail console showing HTTP (80) and HTTPS (443) open to any IPv4 or IPv6 address, and SSH (22) allowing Lightsail browser SSH and Lightsail Setup.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/ports-open.png)

**Note**  
If your domain is registered with a third-party registrar, or your DNS is not managed using a Lightsail DNS zone, see [Enable HTTPS on your WordPress instance with a domain registered outside of Lightsail](amazon-lightsail-enabling-https-on-wordpress-thirdparty.md).

## Step 2: Start Lightsail Setup
<a name="setup-wizard-start-lightsail"></a>

1. Open the Lightsail console at [https://lightsail.aws.amazon.com/](https://lightsail.aws.amazon.com/).

1. Choose your WordPress instance from the instance list.  
![Selecting a WordPress instance from the instance list in the Lightsail console.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/instance-selection.png)

1. In the **Getting started** tab, choose **Start Lightsail Setup**.  
![The "Start Lightsail Setup" button on the "Getting started" tab in the Lightsail console.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/your-website.png)

## Step 3: Select your domain
<a name="setup-wizard-domain-lightsail"></a>

1. Choose **Lightsail managed domain**.

1. Select your domain from the dropdown list.

Your domain appears in this list if it is registered through Lightsail or Route 53 in the same account that you are using for Lightsail Setup.

**Note**  
Your domain must be in **Registered** status for Lightsail Setup to work.

![Selecting a domain name in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/domain-name.png)


## Step 4: Configure DNS
<a name="setup-wizard-dns-lightsail"></a>

A DNS zone manages the DNS records that direct traffic for your domain to your instance. Lightsail Setup requires a Lightsail DNS zone to automatically create and manage these records for you.

1. Choose **Lightsail DNS zone**.

1. Lightsail Setup checks if a Lightsail DNS zone already exists for your domain:
   + **If a DNS zone exists** – Lightsail Setup displays it. Choose **Use this DNS zone**.  
![Choosing an existing DNS zone in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/choose-dns.png)
   + **If a DNS zone does not exist** – Choose **Create DNS zone**. Lightsail Setup creates the DNS zone for your domain.  
![Creating a new DNS zone in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/create-dns.png)

**Important**  
To route traffic to your instance, your domain's name servers must point to your Lightsail DNS zone. If they don't match, update your name servers before continuing with Lightsail Setup. For instructions, see [Change the name servers at your domain registrar](lightsail-how-to-create-dns-entry.md#lightail-change-the-name-servers).

To verify your name servers are pointing correctly and have propagated globally, check [DNS Checker](https://dnschecker.org) on the *dnschecker.org* website.

You can also verify from the command line:
+ **macOS and Linux:**

  ```
  $ dig NS {{yourdomain.com}} +short
  ```
+ **Windows:**

  ```
  C:\> nslookup -type=NS {{yourdomain.com}}
  ```

The result should show your Lightsail DNS zone's name servers (for example, `ns-123.awsdns-01.com`). You can find your DNS zone's name servers on the **Domains & DNS** > **DNS zones** page in the Lightsail console.

**Note**  
Name server changes can take up to 48 hours to propagate. If Lightsail Setup fails after updating name servers, wait and try again.

## Step 5: Configure a static IP
<a name="setup-wizard-static-ip-lightsail"></a>

A static IP address provides a fixed public IP for your instance. Without a static IP, your instance's IP address can change if you stop and restart it, which breaks your domain's connection.

Choose one of the following:
+ **Create a new static IP** – Enter a name for your static IP and choose **Create static IP**.  
![Creating a new static IP in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/create-static-ip.png)
+ **Use an existing static IP** – If you have an unattached static IP in the same AWS Region, select it from the list and choose **Attach static IP**.  
![Attaching an existing static IP in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/attach-static-ip.png)

After this step, Lightsail Setup attaches the static IP to your instance.

## Step 6: Add domain assignments
<a name="setup-wizard-domain-assignments-lightsail"></a>

Domain assignments are DNS records that direct traffic for your domain to your instance.

1. Choose **Add assignment**.

1. Add your apex domain (for example, `exampletest.com`).

1. (Optional) To also secure your www subdomain, choose **Add assignment** again and add your www subdomain (for example, `www.exampletest.com`).

![Managing domain assignments in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/manage-domains.png)


**Tip**  
If you skip the www subdomain, visitors who type `www.exampletest.com` will not reach your site. Add it if you want both addresses to work.

## Step 7: Create SSL/TLS certificate
<a name="setup-wizard-certificate-lightsail"></a>

1. Select the domains and subdomains you want to secure with HTTPS. You can choose up to 10 domains and subdomains.

1. Enter your email address. This is used for certificate renewal notifications.

1. Select **I authorize Lightsail to configure a Let's Encrypt certificate on my instance**. This gives Lightsail restricted access to create and configure the certificate on your instance.

1. Choose **Create certificate**.

![Creating an SSL/TLS certificate in the Lightsail Setup workflow.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/create-certificate.png)


Lightsail Setup begins configuring HTTPS on your instance. This process takes up to 15 minutes.

If setup fails, see [Lightsail Setup failed](amazon-lightsail-troubleshooting-wp-https-lightsail.md) for troubleshooting steps.

**Important**  
Do not stop, reboot, or modify your instance while setup is in progress.

## Step 8: Verify your website
<a name="setup-wizard-verify-lightsail"></a>

After Lightsail Setup completes:

1. Open your browser and go to `https://{{yourdomain.com}}`.

1. Confirm that your website loads successfully.

1. (Optional) Test `https://www.{{yourdomain.com}}` to confirm both addresses work.

To confirm that your website uses the certificate that Lightsail Setup created, view the certificate in your browser. For example, in Google Chrome:

1. In the address bar, choose the site information icon to the left of the URL, and then choose **Connection is secure**.  
![The "Connection is secure" option in the Google Chrome site information menu.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/https-verified.png)

1. Choose **Certificate details**.  
![The "Certificate details" option in the Google Chrome Security panel.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/https-certificate-details.png)

1. Confirm that the certificate is issued to your domain. Under **Issued By**, confirm that **Organization (O)** is Let's Encrypt.  
![Certificate details in Google Chrome showing Let's Encrypt as the issuing organization.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/lightsail-setup/https-certificate-issuer.png)

Your website is now configured with HTTPS and an **automatic redirect from HTTP to HTTPS**.

**Note**  
Let's Encrypt certificates will automatically renew every 60 to 90 days. If renewal fails in the future, see [Certificate did not automatically renew](amazon-lightsail-troubleshooting-wp-cert-renewal-lightsail.md).

## Learn more
<a name="lightsail-setup-learn-more"></a>
+ [Understanding DNS in Lightsail](understanding-dns-in-amazon-lightsail.md)
+ [Register and manage domains](amazon-lightsail-domain-registration.md)
+ [Create a DNS zone to manage domain records](lightsail-how-to-create-dns-entry.md)
+ [Instance firewalls](understanding-firewall-and-port-mappings-in-amazon-lightsail.md)
+ [Static IP addresses](understanding-static-ip-addresses-in-amazon-lightsail.md)