

# Configure WordPress with a Lightsail content delivery network
<a name="amazon-lightsail-configure-wordpress-for-distribution-bitnami"></a>

**This blueprint packaged by Bitnami is being deprecated**  
Blueprints packaged by Bitnami will no longer receive updates after May 19, 2026. Starting November 19, 2026, you will no longer be able to create new instances with this blueprint. When creating new instances, we recommend using the equivalent Lightsail blueprint if available. Existing instances using blueprints packaged by Bitnami will continue to run without any disruption. [Learn more](amazon-lightsail-faq-bitnami-blueprints.md)  
If you have an existing instance that uses a blueprint packaged by Bitnami and want to migrate to a Lightsail-packaged blueprint, see [Migrate to Lightsail blueprints](migrate-from-bitnami-to-lightsail-blueprints.md).

**This tutorial applies to instances that use WordPress packaged by Bitnami only**  
If your instance uses the WordPress blueprint packaged by Lightsail, see [WordPress](amazon-lightsail-wordpress.md) instead.

In this guide, we show you how to configure your WordPress instance to work with an Amazon Lightsail distribution.

All Lightsail distributions have HTTPS enabled by default for their default domain (for example, `123456abcdef.cloudfront.net`). The configuration of your distribution determines whether the connection between your distribution and your instance is encrypted.
+ **Your WordPress website uses HTTP only** – If your website uses HTTP only as the origin of your distribution, and it is not configured to use HTTPS, you can configure your distribution to terminate SSL/TLS and forward all content requests to your instance using an unencrypted connection.
+ **Your WordPress website uses HTTPS** – If your website uses HTTPS as the origin of your distribution, you can configure your distribution to forward all content requests to your instance using an encrypted connection. This configuration is known as end-to-end encryption.

## Step 1: Complete the prerequisites
<a name="configure-distribution-wordpress-prerequisites-bitnami"></a>

Before you get started, make sure your WordPress instance is in a running state. For more information, see [Start, stop, or restart your instance](lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md).

## Step 2: Create the distribution
<a name="create-distribution-wordpress-bitnami"></a>

Complete the following steps to configure a Lightsail distribution for your WordPress instance. For more information, see [Create a Lightsail content delivery network distribution](amazon-lightsail-creating-content-delivery-network-distribution.md).

**To create a distribution for your WordPress instance**

1. In the left navigation pane, choose **Networking**.

1. Choose **Create distribution**.

1. For **Choose your origin**, choose the Region where you're running your WordPress instance and then choose your WordPress instance. We automatically use the static IP address that you attached to the instance.

1. For **Caching behavior**, choose **Best for WordPress**.

1. (Optional) To configure end-to-end encryption, change the origin protocol policy to **HTTPS only**. For more information, see [Origin protocol policy](amazon-lightsail-changing-distribution-origin.md#changing-distribution-origin-protocol-policy).

1. Configure the remaining options and then choose **Create distribution**.

1. On the **Custom domains** tab, choose **Create certificate**. Enter a unique name for the certificate, enter the names of your domain and subdomains, and then choose **Create certificate**.

1. Choose **Attach certificate**.

1. For **Update DNS records**, choose **I understand**.

## Step 3: Update DNS records
<a name="update-dns-records-wordpress-bitnami"></a>

Complete the following steps to update the DNS records for your Lightsail DNS zone.

**To update the DNS records for your distribution**

1. In the left navigation pane, choose **Domains & DNS**.

1. Choose your DNS zone and then choose the **DNS records** tab.

1. Delete the A and AAAA records for the domain that you specified in your certificate.

1. Choose **Add record** and create a CNAME record that resolves your domain to the domain for your distribution (for example, d2vbec9EXAMPLE.cloudfront.net).

1. Choose **Save**.

## Step 4: Allow static content to be cached by the distribution
<a name="allow-static-content-caching-wordpress-bitnami"></a>

Complete the following procedure to edit the `wp-config.php` file in your WordPress instance so that it works with your distribution.

**Note**  
We recommend that you create a snapshot of your WordPress instance before getting started with this procedure. The snapshot can be used as a backup from which you can create another instance in case something goes wrong. For more information, see [Create a snapshot of your Linux or Unix instance](lightsail-how-to-create-a-snapshot-of-your-instance.md).

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose the browser-based SSH client icon that is displayed next to your WordPress instance.

1. After you're connected to your instance, enter the following command to create a backup of the `wp-config.php` file. If something goes wrong, you can restore the file using the backup.

   ```
   sudo cp /opt/bitnami/wordpress/wp-config.php /opt/bitnami/wordpress/wp-config.php.backup
   ```

1. Enter the following command to open the `wp-config.php` file using Vim.

   ```
   sudo vim /opt/bitnami/wordpress/wp-config.php
   ```

1. Press `I` to enter insert mode in Vim.

1. Delete the following lines of code in the file.

   ```
   define('WP_SITEURL', 'http://' . $_SERVER['HTTP_HOST'] . '/');
   define('WP_HOME', 'http://' . $_SERVER['HTTP_HOST'] . '/');
   ```

1. Add one of the following lines of code to the file depending on the version of WordPress that you're using:
   + If you're using version 3.3 or lower, add the following lines of code where you previously deleted the code.

     ```
     define('WP_SITEURL', 'https://' . $_SERVER['HTTP_HOST'] . '/');
     define('WP_HOME', 'https://' . $_SERVER['HTTP_HOST'] . '/');
     if (isset($_SERVER['HTTP_CLOUDFRONT_FORWARDED_PROTO'])
     && $_SERVER['HTTP_CLOUDFRONT_FORWARDED_PROTO'] === 'https') {
     $_SERVER['HTTPS'] = 'on';
     }
     ```
   + If you're using version 3.3.1-5 or higher, add the following lines of code where you previously deleted the code.

     ```
     define('WP_SITEURL', 'http://DOMAIN/');
     define('WP_HOME', 'http://DOMAIN/');
     if (isset($_SERVER['HTTP_CLOUDFRONT_FORWARDED_PROTO'])
     && $_SERVER['HTTP_CLOUDFRONT_FORWARDED_PROTO'] === 'https') {
     $_SERVER['HTTPS'] = 'on';
     }
     ```

1. Press the **Esc** key to exit insert mode in Vim, then type `:wq!` and press **Enter** to save your edits (write) and quit Vim.

1. Enter the following command to restart the Apache service on your instance.

   ```
   sudo /opt/bitnami/ctlscript.sh restart apache
   ```

1. Wait a few moments for your the Apache service to restart, then test that your distribution is caching your content. For more information, see [Test your Amazon Lightsail distribution](amazon-lightsail-testing-distribution.md).

1. If something went wrong, re-connect to your instance using the browser-based SSH client. Run the following command to restore the `wp-config.php` file using the backup you created earlier in this guide.

   ```
   sudo cp /opt/bitnami/wordpress/wp-config.php.backup /opt/bitnami/wordpress/wp-config.php
   ```

   After you restore the file, enter the following command to restart the Apache service: 

   ```
   sudo /opt/bitnami/ctlscript.sh restart apache
   ```

## Additional information about distributions
<a name="distribution-wordpress-bitnami-additional-information"></a>

Here are some articles to help you manage distributions in Lightsail:
+ [Content delivery network distributions](amazon-lightsail-content-delivery-network-distributions.md)
+ [Creating distributions](amazon-lightsail-creating-content-delivery-network-distribution.md)
+ [Understand request and response behaviors of a distribution](amazon-lightsail-distribution-request-and-response.md)
+ [Test your distribution](amazon-lightsail-testing-distribution.md)
+ [Change the origin of your distribution](amazon-lightsail-changing-distribution-origin.md)
+ [Change the caching behavior of your distribution](amazon-lightsail-changing-default-cache-behavior.md)
+ [Reset the cache of your distribution](amazon-lightsail-resetting-distribution-cache.md)
+ [Change the plan of your distribution](amazon-lighstail-changing-distribution-plan.md)
+ [Enable custom domains for your distribution](amazon-lightsail-enabling-distribution-custom-domains.md)
+ [Point your domains to your distribution](amazon-lightsail-point-domain-to-distribution.md)
+ [Change custom domains for your distribution](amazon-lightsail-changing-distribution-custom-domains.md)
+ [Disable custom domains for your distributions](amazon-lightsail-disabling-distribution-custom-domains.md)
+ [View distribution metrics](amazon-lightsail-viewing-distribution-health-metrics.md)
+ [Delete your distribution](amazon-lightsail-deleting-distribution.md)