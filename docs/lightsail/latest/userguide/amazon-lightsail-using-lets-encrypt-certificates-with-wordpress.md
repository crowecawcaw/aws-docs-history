

# Secure your Lightsail WordPress instance with free Let's Encrypt SSL certificates and certbot
<a name="amazon-lightsail-using-lets-encrypt-certificates-with-wordpress"></a>

**This blueprint packaged by Bitnami is being deprecated**  
Blueprints packaged by Bitnami will no longer receive updates after May 19, 2026. Starting November 19, 2026, you will no longer be able to create new instances with this blueprint. When creating new instances, we recommend using the equivalent Lightsail blueprint if available. Existing instances using blueprints packaged by Bitnami will continue to run without any disruption. [Learn more](amazon-lightsail-faq-bitnami-blueprints.md)  
If you have an existing instance that uses a blueprint packaged by Bitnami and want to migrate to a Lightsail-packaged blueprint, see [Migrate to Lightsail blueprints](migrate-from-bitnami-to-lightsail-blueprints.md).

**This tutorial applies to instances that use WordPress packaged by Bitnami only**  
If your instance uses the WordPress blueprint packaged by Lightsail, see [WordPress](amazon-lightsail-wordpress.md) instead.

**Tip**  
Amazon Lightsail offers a guided workflow that automates the installation, configuration, and renewal of a Let's Encrypt certificate on your WordPress instance. We highly recommend that you use the workflow instead of following the manual steps in this tutorial. For more information, see [Launch and configure a WordPress instance](amazon-lightsail-launch-and-configure-wordpress.md).

Lightsail makes it easy to secure your websites and applications with SSL/TLS using Lightsail load balancers. However, using a Lightsail load balancer might not generally be the right choice. Perhaps your site doesn't need the scalability or fault tolerance that load balancers provide, or maybe you're optimizing for cost. In the latter case, you might consider using Let's Encrypt to obtain a free SSL certificate. If so, that's no problem. You can integrate those certificates with Lightsail instances.

With this guide, you will learn how to request a Let’s Encrypt wildcard certificate using Certbot, and integrate it with your WordPress instance using the Really Simple SSL plugin.
+ The Linux distribution used by Bitnami instances changed from Ubuntu to Debian in July, 2020. Because of this change, some of the steps in this tutorial will differ depending on the Linux distribution of your instance. All Bitnami blueprint instances created after the change use the Debian Linux distribution. Instances created before the change will continue to use the Ubuntu Linux distribution. To check the distribution of your instance, run the `uname -a `command. The response will show either Ubuntu or Debian as your instance's Linux distribution.
+ Bitnami has modified the file structure for many of their stacks. The file paths in this tutorial may change depending on whether your Bitnami stack uses native Linux system packages (Approach A), or if it is a self-contained installation (Approach B). To identify your Bitnami installation type and which approach to follow, run the following command:

  `test ! -f "/opt/bitnami/common/bin/openssl" && echo "Approach A: Using system packages." || echo "Approach B: Self-contained installation."`

**Contents**
+ [Before getting started](#lets-encrypt-certificates-wordpress-before-getting-started)
+ [Step 1: Complete the prerequisites](#complete-the-prerequisites-lets-encrypt-wordpress)
+ [Step 2: Install Certbot on your Lightsail instance](#install-certbot-on-your-instance-wordpress)
+ [Step 3: Request a Let’s Encrypt SSL wildcard certificate](#request-a-lets-encrypt-certificate-wordpress)
+ [Step 4: Add TXT records to your domain’s DNS zone](#add-a-text-record-to-your-domains-dns-zone-lets-encrypt-wordpress)
+ [Step 5: Confirm that the TXT records have propagated](#confirm-the-text-records-have-propagated-lets-encrypt-wordpress)
+ [Step 6: Complete the Let’s Encrypt SSL certificate request](#complete-the-lets-encrypt-certificate-request-wordpress)
+ [Step 7: Create links to the Let’s Encrypt certificate files in the Apache server directory](#link-the-lets-encrypt-certificate-files-in-the-apache-directory-wordpress)
+ [Step 8: Integrate the SSL certificate with your WordPress site using the Really Simple SSL plug-in](#integrate-certificates-with-wordpress-using-really-simple-ssl-plugin)
+ [Step 9: Renew the Let's Encrypt certificates every 90 days](#renew-a-lets-encrypt-certificate-wordpress)

## Before getting started
<a name="lets-encrypt-certificates-wordpress-before-getting-started"></a>

You should consider the following before getting started with this tutorial:

**Use the Bitnami HTTPS configuration (`bncert`) tool instead**

The steps outlined in this tutorial show you how to implement an SSL/TLS certificate using a manual process. However, Bitnami offers a more automated process that uses the Bitnami HTTPS configuration (`bncert`) tool that is typically pre-installed on WordPress instances in Lightsail. We highly recommend that you use that tool instead of following the manual steps in this tutorial. This tutorial was written before the `bncert` tool became available. For more information about using the `bncert` tool, see [Secure your WordPress site with HTTPS on Lightsail with bncert](amazon-lightsail-enabling-https-on-wordpress-with-bncert.md).

**Identify the Linux distribution of your WordPress instance**

The Linux distribution used by Bitnami instances changed from Ubuntu to Debian in July, 2020. All Bitnami blueprint instances created after the change use the Debian Linux distribution. Instances created before the change will continue to use the Ubuntu Linux distribution. Because of this change, some of the steps in this tutorial will differ depending on the Linux distribution of your instance. You must identify the Linux distribution of your instance so that you know which steps in this tutorial to use. To identify the Linux distribution of your instance, run the `uname -a `command. The response will show either Ubuntu or Debian as your instance's Linux distribution.

**Identify the tutorial approach that applies to your instance**

Bitnami is in the process of modifying the file structure for many of their stacks. The file paths in this tutorial may change depending on whether your Bitnami stack uses native Linux system packages (Approach A), or if it is a self-contained installation (Approach B). To identify your Bitnami installation type and which approach to follow, run the following command:

`test ! -f "/opt/bitnami/common/bin/openssl" && echo "Approach A: Using system packages." || echo "Approach B: Self-contained installation."`

## Step 1: Complete the prerequisites
<a name="complete-the-prerequisites-lets-encrypt-wordpress"></a>

Complete the following prerequisites if you haven’t already done so:
+ Make sure your WordPress instance is in a running state. For more information, see [Start, stop, or restart your instance](lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md).
+ Register a domain name, and get administrative access to edit its DNS records. To learn more, see [DNS](understanding-dns-in-amazon-lightsail.md).

  We recommend that you manage your domain’s DNS records using a Lightsail DNS zone. To learn more, see [Create a DNS zone to manage your domain’s DNS records](lightsail-how-to-create-dns-entry.md).
+ Use the browser-based SSH terminal in the Lightsail console to perform the steps in this tutorial. However, you can also use your own SSH client, such as PuTTY. To learn more about configuring PuTTY, see [Download and set up PuTTY to connect using SSH in Amazon Lightsail](lightsail-how-to-set-up-putty-to-connect-using-ssh.md).

After you've completed the prerequisites, continue to the [next section](#install-certbot-on-your-instance-wordpress) of this tutorial.

## Step 2: Install Certbot on your Lightsail instance
<a name="install-certbot-on-your-instance-wordpress"></a>

Certbot is a client used to request a certificate from Let’s Encrypt and deploy it to a web server. Let's Encrypt uses the ACME protocol to issue certificates, and Certbot is an ACME-enabled client that interacts with Let's Encrypt.

**To install Certbot on your Lightsail instance**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. On the Instances home page, choose the SSH quick connect icon for the instance that you want to connect to. For example, with a WordPress instance named *Example*:  
![SSH quick connect on the Lightsail home page.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/resource_cards/ssh-quick-connect.png)

1. After your Lightsail browser-based SSH session is connected, enter the following command to update the packages on your instance:

   ```
   sudo apt-get update
   ```  
![Update the packages on your instance.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-wordpress-ssh-lets-encrypt-update-packages.png)

1. Enter the following command to install the software properties package. Certbot's developers use a Personal Package Archive (PPA) to distribute Certbot. The software properties package makes it more efficient to work with PPAs.

   ```
   sudo apt-get install software-properties-common
   ```
**Note**  
If you encounter a `Could not get lock` error when running the `sudo apt-get install` command, please wait approximately 15 minutes and try again. This error may be caused by a cron job that is using the Apt package management tool to install [unattended-upgrades](https://wiki.debian.org/PeriodicUpdates).

1. Enter the following commands to install the GPG package, and add Certbot to the local apt repository:
**Note**  
Step 5 applies only to instances that use the Ubuntu Linux distribution. Skip this step if your instance uses the Debian Linux distribution.

   ```
   sudo apt-get install gpg -y
   ```

   ```
   sudo apt-add-repository ppa:certbot/certbot -y
   ```

1. Enter the following command to update apt to include the new repository:

   ```
   sudo apt-get update -y
   ```

1. Enter the following command to install Certbot:

   ```
   sudo apt-get install certbot -y
   ```

   Certbot is now installed on your Lightsail instance.

1. Keep the browser-based SSH terminal window open—you return to it later in this tutorial. Continue to the [next section](#request-a-lets-encrypt-certificate-wordpress) of this tutorial.

## Step 3: Request a Let’s Encrypt SSL wildcard certificate
<a name="request-a-lets-encrypt-certificate-wordpress"></a>

Begin the process of requesting a certificate from Let’s Encrypt. Using Certbot, request a wildcard certificate, which lets you use a single certificate for a domain and its subdomains. For example, a single wildcard certificate works for the `example.com` top-level domain, and the `blog.example.com`, and `stuff.example.com` subdomains.

**To request a Let’s Encrypt SSL wildcard certificate**

1. In the same browser-based SSH terminal window used in [step 2](#install-certbot-on-your-instance-wordpress) of this tutorial, enter the following commands to set an environment variable for your domain. You can now more efficiently copy and paste commands to obtain the certificate. Be sure to replace `{{domain}}` with the name of your registered domain.

   ```
   DOMAIN={{domain}}
   ```

   ```
   WILDCARD=*.$DOMAIN
   ```

   Example:

   ```
   DOMAIN={{example.com}}
   ```

   ```
   WILDCARD=*.$DOMAIN
   ```

1. Enter the following command to confirm the variables return the correct values:

   ```
   echo $DOMAIN && echo $WILDCARD
   ```

   You should see a result similar to the following:  
![Confirm the domain environment variables.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/bitnami-confirm-variables.png)

1. Enter the following command to start Certbot in interactive mode. This command tells Certbot to use a manual authorization method with DNS challenges to verify domain ownership. It requests a wildcard certificate for your top-level domain, as well as its subdomains.

   ```
   sudo certbot -d $DOMAIN -d $WILDCARD --manual --preferred-challenges dns certonly
   ```

1. Enter your email address when prompted, because it’s used for renewal and security notices.

1. Read the Let’s Encrypt terms of service. When done, press Y if you agree. If you disagree, you cannot obtain a Let’s Encrypt certificate.

1. Respond accordingly to the prompt to share your email address and to the warning about your IP address being logged.

1. Let’s Encrypt now prompts you to verify that you own the domain specified. You do this by adding TXT records to the DNS records for your domain. A set of TXT record values are provided as shown in the following example:
**Note**  
Let's Encrypt may provide a single or multiple TXT records that you must use for verification. In this example, we were provided with two TXT records to use for verification.  
![TXT records for Let's Encrypt certificates.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/get-TXT-records.png)

1. Keep the Lightsail browser-based SSH session open—you return to it later in this tutorial. Continue to the [next section](#add-a-text-record-to-your-domains-dns-zone-lets-encrypt-wordpress) of this tutorial.

## Step 4: Add TXT records to your domain’s DNS zone
<a name="add-a-text-record-to-your-domains-dns-zone-lets-encrypt-wordpress"></a>

Adding a TXT record to your domain’s DNS zone verifies that you own the domain. For demonstration purposes, we use the Lightsail DNS zone. However, the steps might be similar for other DNS zones typically hosted by domain registrars.

**Note**  
To learn more about how to create a Lightsail DNS zone for your domain, see [Creating a DNS zone to manage your domain’s DNS records in Lightsail](lightsail-how-to-create-dns-entry.md).

**To add TXT records to your domain’s DNS zone in Lightsail**

1. In the left navigation pane, choose **Domains & DNS**.

1. Under the **DNS zones** section of the page, choose the DNS Zone for the domain that you specified in the Certbot certificate request.

1. In the DNS zone editor, choose **DNS records**.

1. Choose **Add record**.

1. In the **Record type** drop-down menu, choose **TXT record**.

1. Enter the values specified by the Let’s Encrypt certificate request into the **Record name** and **Responds with** fields.
**Note**  
The Lightsail console pre-populates the apex portion of your domain. For example, if you want to add the `{{_acme-challenge.example.com}}` subdomain, then you only have to enter `{{_acme-challenge}}` into the text box, and Lightsail adds the `.example.com` portion for you when you save the record.

1. Choose **Save**.

1. Repeat steps 4 through 7 to add the second set of TXT records specified by the Let’s Encrypt certificate request.

1. Keep the Lightsail console browser window open—you return to it later in this tutorial. Continue to the [next section](amazon-lightsail-using-lets-encrypt-certificates-with-lamp.md#confirm-the-text-records-have-propagated-lets-encrypt-lamp) of this tutorial.

## Step 5: Confirm that the TXT records have propagated
<a name="confirm-the-text-records-have-propagated-lets-encrypt-wordpress"></a>

Use the MxToolbox utility to confirm that the TXT records have propagated to the internet's DNS. DNS record propagation might take a while depending on your DNS hosting provider, and the configured time to live (TTL) for your DNS records. It is important that you complete this step, and confirm that your TXT records have propagated, before continuing your Certbot certificate request. Otherwise, your certificate request fails.

**To confirm the TXT records have propagated to the internet's DNS**

1. Open a new browser window and go to [https://mxtoolbox.com/TXTLookup.aspx](https://mxtoolbox.com/TXTLookup.aspx).

1. Enter the following text into the text box. Be sure to replace {{domain}} with your domain.

   ```
   _acme-challenge.{{domain}}
   ```

   Example:

   ```
   _acme-challenge.example.com
   ```  
![MXToolbox TXT record lookup.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/mxtoolbox-text-record-lookup.png)

1. Choose **TXT Lookup** to run the check.

1. One of the following responses occurs:
   + If your TXT records have propagated to the internet's DNS, you see a response similar to the one shown in the following screenshot. Close the browser window and continue to the next section of this tutorial.  
![Confirmation that TXT records propagated.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/mxtoolbox-propagated-text-record-lookup.png)
   + If your TXT records have not propagated to the internet's DNS, you see a **DNS Record not found** response. Confirm that you added the correct DNS records to your domains' DNS zone. If you added the correct records, wait a while longer to let your domain's DNS records propagate, and run the TXT lookup again.

## Step 6: Complete the Let’s Encrypt SSL certificate request
<a name="complete-the-lets-encrypt-certificate-request-wordpress"></a>

Go back to the Lightsail browser-based SSH session for your WordPress instance and complete the Let’s Encrypt certificate request. Certbot saves your SSL certificate, chain, and key files to a specific directory on your WordPress instance.

**To complete the Let’s Encrypt SSL certificate request**

1. In the Lightsail browser-based SSH session for your WordPress instance, press **Enter** to continue your Let’s Encrypt SSL certificate request. If successful, a response similar to the one shown in the following screenshot appears:  
![Successful Let's Encrypt certificate request.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/bitnami-certificate-request-success.png)

   The message confirms that your certificate, chain, and key files are stored in the `/etc/letsencrypt/live/{{domain}}/` directory. Make sure to replace `{{domain}}` with your domain, such as `/etc/letsencrypt/live/{{example.com}}/`.

1. Make note of the expiration date specified in the message. You use it to renew your certificate by that date.  
![Let's Encrypt certificate renewal date.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/certificate-renewal-date.png)

1. Now that you have the Let’s Encrypt SSL certificate, continue to the [next section](#link-the-lets-encrypt-certificate-files-in-the-apache-directory-wordpress) of this tutorial.

## Step 7: Create links to the Let’s Encrypt certificate files in the Apache server directory
<a name="link-the-lets-encrypt-certificate-files-in-the-apache-directory-wordpress"></a>

Create links to the Let’s Encrypt SSL certificate files in the Apache server directory on your WordPress instance. Also, back up your existing certificates, in case you need them later.

**To create links to the Let’s Encrypt certificate files in the Apache server directory**

1. In the Lightsail browser-based SSH session for your WordPress instance, enter the following command to stop the underlying services:

   ```
   sudo /opt/bitnami/ctlscript.sh stop
   ```

   You should see a response similar to the following:  
![Instance services stopped.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-ssh-stop-services.png)

1. Enter the following commands individually to rename your existing certificate files as backups. Refer to the **Important** block at the beginning of this tutorial for information about the different distributions and file structures.
   + For Debian Linux distributions

     Approach A (Bitnami installations using system packages):

     ```
     sudo mv /opt/bitnami/apache2/conf/bitnami/certs/server.crt /opt/bitnami/apache2/conf/bitnami/certs/server.crt.old
     ```

     ```
     sudo mv /opt/bitnami/apache2/conf/bitnami/certs/server.key /opt/bitnami/apache2/conf/bitnami/certs/server.key.old
     ```

     Approach B (Self-contained Bitnami installations):

     ```
     sudo mv /opt/bitnami/apache2/conf/server.crt /opt/bitnami/apache2/conf/server.crt.old
     ```

     ```
     sudo mv /opt/bitnami/apache2/conf/server.key /opt/bitnami/apache2/conf/server.key.old
     ```
   + For older instances that use the Ubuntu Linux distribution:

     ```
     sudo mv /opt/bitnami/apache/conf/bitnami/certs/server.crt /opt/bitnami/apache/conf/bitnami/certs/server.crt.old
     ```

     ```
     sudo mv /opt/bitnami/apache/conf/bitnami/certs/server.key /opt/bitnami/apache/conf/bitnami/certs/server.key.old
     ```

     ```
     sudo mv /opt/bitnami/apache/conf/bitnami/certs/server.csr /opt/bitnami/apache/conf/bitnami/certs/server.csr.old
     ```

1. Enter the following commands individually to create links to your Let’s Encrypt certificate files in the Apache directory. Refer to the **Important** block at the beginning of this tutorial for information about the different distributions and file structures.
**Note**  
If you closed your browser-based SSH terminal window since setting the `DOMAIN` variable in Step 3, run `DOMAIN={{example.com}}` again, replacing {{example.com}} with your domain.
   + For Debian Linux distributions

     Approach A (Bitnami installations using system packages):

     ```
     sudo ln -sf /etc/letsencrypt/live/$DOMAIN/privkey.pem /opt/bitnami/apache2/conf/bitnami/certs/server.key
     ```

     ```
     sudo ln -sf /etc/letsencrypt/live/$DOMAIN/fullchain.pem /opt/bitnami/apache2/conf/bitnami/certs/server.crt
     ```

     Approach B (Self-contained Bitnami installations):

     ```
     sudo ln -sf /etc/letsencrypt/live/$DOMAIN/privkey.pem /opt/bitnami/apache2/conf/server.key
     ```

     ```
     sudo ln -sf /etc/letsencrypt/live/$DOMAIN/fullchain.pem /opt/bitnami/apache2/conf/server.crt
     ```
   + For older instances that use the Ubuntu Linux distribution:

     ```
     sudo ln -s /etc/letsencrypt/live/$DOMAIN/privkey.pem /opt/bitnami/apache/conf/bitnami/certs/server.key
     ```

     ```
     sudo ln -s /etc/letsencrypt/live/$DOMAIN/fullchain.pem /opt/bitnami/apache/conf/bitnami/certs/server.crt
     ```

1. Enter the following command to start the underlying services that you had stopped earlier:

   ```
   sudo /opt/bitnami/ctlscript.sh start
   ```

   You should see a result similar to the following:  
![Instance services started.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-ssh-start-services.png)

   The SSL certificate files for your WordPress instance are now in the correct directory.

1. Continue to the [next section](#integrate-certificates-with-wordpress-using-really-simple-ssl-plugin) of this tutorial.

## Step 8: Integrate the SSL certificate with your WordPress site using the Really Simple SSL plug-in
<a name="integrate-certificates-with-wordpress-using-really-simple-ssl-plugin"></a>

Install the Really Simple SSL plug-in to your WordPress site, and use it to integrate the SSL certificate. Really Simple SSL also configures HTTP to HTTPS redirection to ensure that users who visit your site are always on the HTTPS connection.

**To integrate the SSL certificate with your WordPress site using the Really Simple SSL plug-in**

1. In the Lightsail browser-based SSH session for your WordPress instance, enter the following command to set your `wp-config.php` and `htaccess.conf` files to be writeable. The Really Simple SSL plug-in will write to the wp-config.php file to configure your certificates.
   + For newer instances that use the Debian Linux distribution:

     ```
     sudo chmod 666 /opt/bitnami/wordpress/wp-config.php && sudo chmod 666 /opt/bitnami/apache/conf/vhosts/htaccess/wordpress-htaccess.conf
     ```
   + For older instances that use the Ubuntu Linux distribution:

     ```
     sudo chmod 666 /opt/bitnami/apps/wordpress/htdocs/wp-config.php && sudo chmod 666 /opt/bitnami/apps/wordpress/conf/htaccess.conf
     ```

1. Open a new browser window and sign in to the administration dashboard of your WordPress instance.
**Note**  
For more information, see [Getting the application user name and password for your Bitnami instance in Amazon Lightsail](log-in-to-your-bitnami-application-running-on-amazon-lightsail.md).

1. Choose **Plugins** from the left navigation pane.

1. Choose **Add New** from the top of the Plugins page.  
![Add a new plug-in in WordPress.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/amazon-lightsail-wordpress-add-new-plugin.png)

1. Search for **Really Simple SSL**.

1. Choose **Install Now** next to the Really Simple SSL plug-in in the search results.  
![The Really Simple SSL plug-in for WordPress.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/amazon-lightsail-wordpress-really-simple-ssl-plugin.png)

1. After it’s done installing, choose **Activate**.

1. In the prompt that appears, choose **Go ahead, activate SSL\!** You may be redirected to the sign in page for the administration dashboard of your WordPress instance.

   Your WordPress instance is now configured to use SSL encryption. Additionally, your WordPress instance is now configured to automatically redirect connections from HTTP to HTTPS. When a visitor goes to `http://example.com`, they are automatically redirected to the encrypted HTTPS connection (i.e., `https://example.com`).

1. Go back to the Lightsail browser-based SSH session for your WordPress instance and enter the following command to restore restrictive permissions on your configuration files. These files contain database credentials and security keys that should not be left world-readable.
   + For newer instances that use the Debian Linux distribution:

     ```
     sudo chmod 640 /opt/bitnami/wordpress/wp-config.php && sudo chmod 640 /opt/bitnami/apache/conf/vhosts/htaccess/wordpress-htaccess.conf
     ```
   + For older instances that use the Ubuntu Linux distribution:

     ```
     sudo chmod 640 /opt/bitnami/apps/wordpress/htdocs/wp-config.php && sudo chmod 640 /opt/bitnami/apps/wordpress/conf/htaccess.conf
     ```

## Step 9: Renew the Let's Encrypt certificates every 90 days
<a name="renew-a-lets-encrypt-certificate-wordpress"></a>

Let’s Encrypt certificates are valid for 90 days. Certificates can be renewed 30 days before they expire. To renew the Let's Encrypt certificates, run the original command used to obtain them. Repeat the steps in the [Request a Let’s Encrypt SSL wildcard certificate](#request-a-lets-encrypt-certificate-wordpress) section of this tutorial.

**Note**  
The Amazon Lightsail guided workflow handles certificate renewal automatically. To avoid renewing certificates manually, switch to the guided workflow. For more information, see [Launch and configure a WordPress instance](amazon-lightsail-launch-and-configure-wordpress.md).