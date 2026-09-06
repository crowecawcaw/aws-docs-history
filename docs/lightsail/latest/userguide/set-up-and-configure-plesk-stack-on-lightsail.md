

# Deploy a Plesk hosting stack on Lightsail
<a name="set-up-and-configure-plesk-stack-on-lightsail"></a>

**Did you know?**  
 Lightsail stores seven daily snapshots and automatically replaces the oldest with the newest when you enable automatic snapshots for your instance. For more information, see [ Configure automatic snapshots for Lightsail instances and disks ](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots.html) . 

Learn how to create a Plesk instance in Amazon Lightsail, and how to sign in to the Plesk User Interface for the first time by creating a username and password. You will also learn how to connect to and configure your Plesk instance after it is up and running.

**Important**  
Instances launched with the **Plesk Hosting Stack on Ubuntu (BYOL)** blueprint have a 30-day trial license. After 30 days, you must purchase and install a license from Plesk to continue using the Plesk application. For more information, see [Step 8: Purchase a Plesk license](#purchase-plesk-license).

With Plesk hosting stacks in Lightsail, you can accomplish tasks such as:
+ Automate WordPress site management using WP Toolkit's graphical interface
+ Secure your site with free SSL certificates and configure HTTPS traffic using Let's Encrypt
+ Transfer files to and from your instance using FTP
+ Monitor and secure your server using web-based tools, including Plesk Firewall, Logs, and ModSecurity
+ Route inbound traffic from specific domains to designated container ports using Docker Proxy Rules

## Considerations for deploying a Plesk hosting stack
<a name="considerations-for-deploying-plesk"></a>

Before you begin deploying your Plesk instance, determine if you need to register a domain for your website and how you want to manage it. You need a registered domain to access your website by a logical name (such as `http://example.com`) rather than by IP address. You also need a DNS name created within your domain to secure connections to your website with a certificate (required for HTTPS traffic).

Review the following options for domain configuration and management:
+ If you already have a registered domain in Lightsail that you want to use, you can begin the steps in this tutorial.
+ If you have a domain with a different registrar that you prefer to manage your DNS records with, you can begin the steps in this tutorial. Otherwise, you can [transfer management of your domain's DNS records](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-create-dns-entry.html#lightail-change-the-name-servers). This can help you to more efficiently manage all of your compute and DNS resources within Lightsail.
+ If you don't have a domain that you want to use, you can find and register one for your website. For more information on registering a domain with Lightsail, see [Register and manage domains for your website in Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-domain-registration.html).

## Step 1: Create a Plesk instance
<a name="create-plesk-instance"></a>

Complete the following steps to create a Plesk instance on Lightsail.

1. Sign in to the Lightsail console at [https://lightsail.aws.amazon.com/](https://lightsail.aws.amazon.com/).

1. On the **Instances** home page, choose **Create instance**.

1. Select a location for your instance (an AWS Region and Availability Zone).

   Choose **Change AWS Region and Availability Zone** to create your instance in another location.

1. Optionally, you can change the Availability Zone.

   Choose **Change your Availability Zone**.

1. Under **Apps \+ OS**, choose **Plesk Hosting Stack on Ubuntu (BYOL)**.

1. Choose an available instance plan.
**Tip**  
For optimal website performance, select an instance plan that can accommodate the resource demands of the plugins and extensions that you plan to install. If you later require more compute power, you can [upsize your instance from a snapshot](https://docs.aws.amazon.com/lightsail/latest/userguide/how-to-create-larger-instance-from-snapshot-using-console.html). For more information about the requirements for plugins and extensions, consult the respective vendor's documentation.

1. Enter a name for your instance.

   Resource names:
   + Must be unique within each AWS Region in your Lightsail account.
   + Must contain 2 to 255 characters.
   + Must start and end with an alphanumeric character or number.
   + Can include alphanumeric characters, numbers, periods, dashes, and underscores.

1. (Optional) Choose **Add new tag** to add a tag to your instance. Repeat this step as needed to add additional tags. For more information on tag usage, such as for billing and resource organization, see [Tags](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags.html).
   + For **Key**, enter a tag key.
   + (Optional) For **Value**, enter a tag value.

1. Choose **Create instance**.

Your instance takes a few minutes to provision and become available after you create it.

**Tip**  
To streamline the initial setup process for Plesk, don't assign a static IP to your instance for now—you'll do this in a later step. If you attach a static IP to your Plesk instance now, you might get a one-time login URL that uses an outdated public IP address. This can occur because your instance might use the public IP address that was assigned initially rather than the static IP address.

## Step 2: Sign in to the Plesk user interface for the first time
<a name="sign-in-to-plesk-ui"></a>

**Tip**  
Keep your Lightsail console and Plesk user interface browser tabs open until you complete this tutorial as you'll be working through multiple steps in each.

Use the following procedure to obtain a one-time login URL to access the Plesk user interface as an administrator. This interface is where you'll create and manage your websites.

**To obtain a one-time login URL**

1. In the left navigation pane, choose Instances.

1. Choose the name of the Plesk instance that you created.

1. On your instance management page, under the **Connect** tab, choose **Connect using SSH**.
**Note**  
If you attempt to connect too quickly after launching the instance, you might experience a connection or SSH key error. If you see these issues while connecting, wait a few minutes and try again.

1. After you're connected, enter the following command to get the one-time login URL.

   ```
   sudo plesk login | grep plesk.page
   ```

   You should see a response similar to the following example, which contains the one-time login URL.

   ```
   https://heuristic-bassi.192-0-2-0.plesk.page/login?secret=ce-EXAMPLE298fc1c149afbf4c8996fb92427
   ```
**Note**  
If your public IP address has changed (for example, you assigned a static IP since it was launched), you'll need to modify the returned URL to match your new address to access the login page.

1. Select the one-time login URL in the browser-based connection window and copy it.

1. Paste the URL in your web browser to access the Plesk login page.

1. Follow the instructions on the page to create your sign in credentials for Plesk. You should see an option to add your domain to Plesk when you sign in for the first time.

## Step 3: Attach a static IP address to your Plesk instance
<a name="attach-static-ip"></a>

The default dynamic public IP address attached to your instance changes every time you stop and start the instance. To keep the public IP address from changing, create a static IP address and attach it to your instance. In a later step, you'll map your static IP address to your domain name. With this mapping configured, you don't have to update your domain's DNS records each time you stop and start the instance.

**Note**  
You can only attach one static IP to a Lightsail instance. Static IP addresses are only free when they are attached to an instance.

**To attach a static IP and update your public IP address in Plesk**

1. Sign in to the Lightsail console at [https://lightsail.aws.amazon.com/](https://lightsail.aws.amazon.com/).

1. On the **Instances** home page of the Lightsail console, choose the name of your Plesk instance.

1. Under the **Networking** tab, choose **Attach static IP**.

1. Create and attach a static IP address.
   + To create and attach a static IP when none exists in the Region:

     1. Enter a name to identify the static IP.

     1. Choose **Create and attach**.

     1. Choose **Continue**.
   + To create and attach a new static IP when you already have one in the Region:

     1. Choose the **Select a static IP** menu to display the available options.

     1. Choose **Create a new static IP** in the dropdown menu.

     1. Enter a name to identify the static IP.

     1. Choose **Create and attach**.

     1. Choose **Continue**.
   + To use an existing static IP in the Region:

     1. Choose the **Select a static IP** menu to display the available options.

     1. Choose an already available static IP in the dropdown menu.

     1. Choose **Attach**.

With the public IP address changed, you access the Plesk user interface using a URL that resembles `https://StaticIPAddress:8443`. Replace `StaticIPAddress` with the static IP address attached to your instance. For example, `https://192.0.2.0:8443`. On the login page, enter the username and password that you created previously to sign in to the Plesk user interface.

**Note**  
When you connect with an IP address in the URL, you might see a browser warning that your connection is not private, not secure, or that there's a security risk. This happens because your Plesk instance's SSL/TLS certificate applied to it doesn't match the new public IP being used. In the browser window, choose **Advanced**, **Details**, or **More information** to view the options that are available. Then choose to proceed to the website even if it's not private or secure.

## Step 4: Update your public IP address in Plesk
<a name="update-public-ip"></a>

Now that you have the static IP address assigned to your instance, update the public IP address used by Plesk. This ensures that Plesk uses your updated public IP address rather than the dynamic address which is no longer associated with your instance. If you don't perform this step, the Plesk user interface might present warnings about the mismatch.

**To update your public IP address in Plesk**

1. Access the Plesk user interface using the new public IP address that is assigned. For example, `https://192.0.2.0:8443`.

1. Authenticate using the sign in credentials that you created previously in [Step 2: Sign in to the Plesk user interface for the first time](#sign-in-to-plesk-ui).

1. In the Plesk user interface, choose **Change View**, then choose **Switch to Power User view**.

1. In the left navigation pane of the Plesk user interface, choose **Tools & Settings**.

1. Under **Tools & Resources**, choose **IP Addresses**.

1. Choose **Update public IPs**.

In the **Public IP Address** column, you should now see the value match with the static IP attached to your instance.

## Step 5: Add a website to your Plesk instance
<a name="add-website"></a>

You can map one or more domain names (websites) within the Plesk user interface. Adding a domain in your Plesk instance enables you to [upload content](https://docs.plesk.com/en-US/obsidian/reseller-guide/website-management/quick-start-with-plesk/set-up-your-first-website/1-create-your-site/uploading-content.70312/), use [Presence Builder](https://www.plesk.com/extensions/offer-web-presence-builder/), and to install a [content management system](https://www.plesk.com/blog/various/top-10-php-cms-platforms-for-developers-in-2024/) (CMS).

**To add a new domain in Plesk**

1. In the left navigation pane of the Plesk user interface, choose **Websites & Domains**.

1. Choose **Add Domain**.

1. Select an option for how you want to create your website.

1. Enter a domain name and fill out any additional required information fields.

1. Choose **Add Domain**.

For more information, see [Adding and Removing Domains](https://docs.plesk.com/en-US/obsidian/administrator-guide/website-management/websites-and-domains/domains-and-dns/adding-and-removing-domains.65150/) in the *Plesk Administrator's Guide*.

## Step 6: Map your domain name to your Plesk instance
<a name="map-domain-name"></a>

You can map a domain to your Plesk instance to access your Plesk user interface using the domain name that you create. You can also map multiple domains within the Plesk user interface, which you can use to manage websites. For more information about mapping multiple domains within the Plesk user interface, see [Adding a Domain in Plesk](https://docs.plesk.com/en-US/obsidian/quick-start-guide/plesk-tutorial/step-6-change-your-password-and-log-out.74376/#adding-a-domain-in-plesk) in the *Plesk Documentation and Help Portal*.

To map your domain name, such as `example.com`, to your instance, you add an A record to the domain name system (DNS) of your domain. DNS records are typically managed and hosted at the registrar where you registered your domain. However, we recommend that you transfer management of your domain's DNS records to Lightsail so that you can administer them using the Lightsail console. For more information, see [Transfer DNS management for your Lightsail domain](amazon-lightsail-domain-register-other-dns-service-procedure.md).

**To map your domain name to your Plesk instance in Lightsail**

1. Open the Amazon Lightsail console at [https://console.aws.amazon.com/lightsail/](https://console.aws.amazon.com/lightsail/).

1. In the left-navigation pane of the Plesk user interface, choose **Domains & DNS**.

1. Choose the name of your DNS zone.

1. Choose the **DNS records** tab.

1. Choose **Add record**.

1. For **Record name**, enter a value, such as `www`.

1. For **Resolves to**, enter the static IP address attached to your Plesk instance.

1. Choose **Save**.

You should now be able to access your Plesk website using the domain name that you configured.

## Step 7: Read the Plesk documentation
<a name="read-plesk-documentation"></a>

Read the Plesk documentation to learn how to administer websites, customize the Plesk user interface, and more.

For more information, see the [Getting Started with Managing Websites in Plesk](https://docs.plesk.com/en-US/obsidian/quick-start-guide/read-me-first.74371/) in the *Plesk Documentation and Help Portal*.

## Step 8: Purchase a Plesk license
<a name="purchase-plesk-license"></a>

Your Plesk instance includes a 30-day trial license. After 30 days, you must purchase a license from Plesk to continue using it. For more information, see [Pricing](https://www.plesk.com/pricing/) on the *Plesk* website.

You must install the license after you purchase it from Plesk. To install your Plesk license, see [How to install the Plesk license](https://support.plesk.com/hc/en-us/articles/12378028764951-How-to-install-the-Plesk-license) on the *Plesk support* website.

## Step 9: Create a snapshot of your Plesk instance
<a name="amazon-lightsail-plesk-create-a-snapshot"></a>

After you configure your website the way you want it, create periodic snapshots of your instance to back it up. A snapshot is a copy of the system disk and original configuration of an instance. A snapshot contains all of the data that is needed to restore your instance (from the moment when the snapshot was taken).

You can create [snapshots manually](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-snapshots-in-amazon-lightsail.html#manual-snapshots), or [enable automatic snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-snapshots-in-amazon-lightsail.html#automatic-snapshots) to have Lightsail create daily snapshots for you. If something goes wrong with your instance, you can create a new replacement instance using the snapshot.

You can work with snapshots on your instance's management page on the **Snapshots** tab. For more information, see [Snapshots in Amazon Lightsail](understanding-snapshots-in-amazon-lightsail.md).

![Create an instance snapshot in the Lightsail console](http://docs.aws.amazon.com/lightsail/latest/userguide/images/quick-start-instance-snapshots.png)
