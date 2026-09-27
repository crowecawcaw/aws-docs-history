

# Configure WordPress with a Lightsail content delivery network
<a name="amazon-lightsail-configure-wordpress-for-distribution"></a>

In this guide, we show you how to configure your WordPress instance to work with a Amazon Lightsail distribution.

All Lightsail distributions have HTTPS enabled by default for their default domain (for example, `123456abcdef.cloudfront.net`). The configuration of your distribution determines whether the connection between your distribution and your instance is encrypted.
+ **Your WordPress website uses HTTP only** – If your website uses HTTP only and is not configured for HTTPS, you can configure your distribution to terminate SSL/TLS. The distribution forwards all content requests to your instance using an unencrypted connection.
+ **Your WordPress website uses HTTPS** – If your website uses HTTPS as the origin, you can configure your distribution to forward all content requests to your instance using an encrypted connection. This configuration is known as end-to-end encryption.

## Create the distribution
<a name="create-distribution-wordpress"></a>

Complete the following steps to configure a Lightsail distribution for your WordPress instance. For more information, see [Create a Lightsail content delivery network distribution](amazon-lightsail-creating-content-delivery-network-distribution.md).

**Prerequisite**  
Create and configure a WordPress instance as described in [Launch and configure a WordPress instance](amazon-lightsail-launch-and-configure-wordpress.md).

**To create a distribution for your WordPress instance**

1. In the left navigation pane, choose **Networking**.

1. Choose **Create distribution**.

1. For **Choose your origin**, choose the Region where you're running your WordPress instance and then choose your WordPress instance. We automatically use the static IP address that you attached to the instance.

1. For **Caching behavior**, choose **Best for WordPress**.

1. (Optional) To configure end-to-end encryption, change the origin protocol policy to **HTTPS only**. For more information, see [Origin protocol policy](amazon-lightsail-changing-distribution-origin.md#changing-distribution-origin-protocol-policy). This requires your WordPress instance to serve HTTPS. For instructions, see [Enable HTTPS on your WordPress instance](amazon-lightsail-enabling-https-on-wordpress.md).

1. Configure the remaining options and then choose **Create distribution**.

1. On the **Custom domains** tab, choose **Create certificate**. Enter a unique name for the certificate, enter the names of your domain and subdomains, and then choose **Create certificate**.

1. Choose **Attach certificate**.

1. For **Update DNS records**, choose **I understand**.

## Update DNS records
<a name="update-dns-records-wordpress"></a>

Complete the following steps to update the DNS records for your Lightsail DNS zone.

**To update the DNS records for your distribution**

1. In the left navigation pane, choose **Domains & DNS**.

1. Under the **DNS zones** section of the page, choose the domain name to which you want to add the record that will direct traffic for your domain to your distribution.

1. Choose the **DNS records** tab. Then, choose **Add record**.

1. Complete one of the following steps depending on the type of domain that you want to point to your distribution:
   + Choose an address (A) record to point an apex domain (e.g., `example.com`) to your distribution.

     If an A record for the apex of your domain is already present in your DNS zone, then you will need to edit that existing record instead of adding another A record.
   + Choose a canonical name (CNAME) to point a sub domain, such as `website.example.com`, to your distribution.

1. If you're adding an A record, then in the **Resolves to** text box choose the name of your distribution. If you're adding a CNAME record, then in the **Maps to** text box enter the default domain name of your distribution.
**Note**  
When you add an A record to your DNS zone, and choose the name of your distribution, you are in fact adding an alias record, which is different than an address record. Lightsail makes it easy for you to add alias records without the additional steps that are typically required at other DNS hosting providers.

1. Choose the save icon to save the record to your DNS zone.

   Repeat these steps to add additional DNS records for domains on your certificate that you are using with your distribution. Allow time for changes to propagate through the Internet's DNS. After a few minutes, you should see if your domain is pointing to your distribution. You should also test your distribution. For more information, see the following [Test your distribution](amazon-lightsail-testing-distribution.md).

## Allow static content to be cached by the distribution
<a name="allow-static-content-caching-wordpress"></a>

Complete the following procedure to edit the `wp-config.php` file in your WordPress instance so that it works with your distribution.

**Note**  
We recommend that you create a snapshot of your WordPress instance before getting started with this procedure. The snapshot can be used as a backup from which you can create another instance in case something goes wrong. For more information, see [Create a snapshot of your Linux or Unix instance](lightsail-how-to-create-a-snapshot-of-your-instance.md).

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose the browser-based SSH client icon that is displayed next to your WordPress instance.

1. After you're connected to your instance, enter the following command to create a backup of the `wp-config.php` file. If something goes wrong, you can restore the file using the backup.

   ```
   sudo cp /var/www/wp-config.php /var/www/wp-config.php.backup
   ```

1. Enter the following command to open the `wp-config.php` file using Vim.

   ```
   sudo vim /var/www/wp-config.php
   ```

1. Press `I` to enter insert mode in Vim.

1. Delete the following lines of code in the file.

   ```
   define('WP_SITEURL', 'http://' . $_SERVER['HTTP_HOST'] . '/');
   define('WP_HOME', 'http://' . $_SERVER['HTTP_HOST'] . '/');
   ```

1. Add the following lines of code to the file where you previously deleted the code:

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
   sudo systemctl restart apache2
   ```

1. Wait a few moments for your the Apache service to restart, then test that your distribution is caching your content. For more information, see [Test your Amazon Lightsail distribution](amazon-lightsail-testing-distribution.md).

1. If something went wrong, re-connect to your instance using the browser-based SSH client. Run the following command to restore the `wp-config.php` file using the backup you created earlier in this guide.

   ```
   sudo cp /var/www/wp-config.php.backup /var/www/wp-config.php
   ```

   After you restore the file, enter the following command to restart the Apache service: 

   ```
   sudo systemctl restart apache2
   ```

## Additional information about distributions
<a name="distribution-wordpress-additional-information"></a>

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