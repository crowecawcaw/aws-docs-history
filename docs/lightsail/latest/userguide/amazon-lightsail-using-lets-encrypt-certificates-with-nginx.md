

# Enable HTTPS on your Nginx instance with Let's Encrypt and Certbot
<a name="amazon-lightsail-using-lets-encrypt-certificates-with-nginx"></a>

Amazon Lightsail makes it easy to secure your websites and applications with SSL/TLS using Lightsail load balancers. However, using a Lightsail load balancer might not generally be the right choice. Perhaps your site doesn't need the scalability or fault tolerance load balancers provide, or maybe you're optimizing for cost.

In the latter case, you might consider using Let's Encrypt to obtain a free SSL certificate. If so, that's no problem. You can integrate those certificates with Lightsail instances. This tutorial shows you how to request a Let's Encrypt wildcard certificate using Certbot, and integrate it with your Nginx instance.

 **Contents** 
+  [ Step 1: Complete the prerequisites ](#complete-the-prerequisites) 
+  [ Step 2: Install Certbot on your Lightsail instance ](#install-certbot-on-your-instance) 
+  [ Step 3: Request a Let’s Encrypt SSL wildcard certificate ](#request-a-lets-encrypt-certificate) 
+  [ Step 4: Add TXT records to your domain’s DNS zone ](#add-a-text-record-to-your-domains-dns-zone-lets-encrypt) 
+  [ Step 5: Confirm that the TXT records have propagated ](#confirm-the-text-records-have-propagated-lets-encrypt) 
+  [ Step 6: Complete the Let’s Encrypt SSL certificate request ](#complete-the-lets-encrypt-certificate-request) 
+  [ Step 7: Update SSL configuration in Nginx and redirect traffic from HTTP to HTTPS ](#update-ssl-configuration) 
+  [ Step 8: Renew the Let’s Encrypt certificates every 90 days ](#renew-a-lets-encrypt-certificate) 

## Step 1: Complete the prerequisites
<a name="complete-the-prerequisites"></a>

Complete the following prerequisites if you haven't already done so:
+  Create a Nginx instance in Lightsail. To learn more, see [ Create an instance ](how-to-create-amazon-lightsail-instance-virtual-private-server-vps.md). 
+  Register a domain name, and get administrative access to edit its DNS records. To learn more, see [DNS](understanding-dns-in-amazon-lightsail.md). 
**Note**  
 We recommend that you manage your domain's DNS records using a Lightsail DNS zone. To learn more, see [ Create a DNS zone to manage your domain's DNS records ](lightsail-how-to-create-dns-entry.md) . 
+  Use the browser-based SSH terminal in the Lightsail console to perform the steps in this tutorial. However, you can also use your own SSH client, such as PuTTY. To learn more about configuring PuTTY, see [ Download and set up PuTTY to connect using SSH in Amazon Lightsail ](lightsail-how-to-set-up-putty-to-connect-using-ssh.md). 

## Step 2: Install Certbot on your Lightsail instance
<a name="install-certbot-on-your-instance"></a>

Certbot is a client used to request a certificate from Let's Encrypt and deploy it to a web server. Let's Encrypt uses the ACME protocol to issue certificates, and Certbot is an ACME-enabled client that interacts with Let's Encrypt.

**To install Certbot on your Lightsail instance**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. On the Instances tab of the Lightsail home page, choose the SSH quick connect icon for the instance that you want to connect to.  
![SSH quick connect on the Lightsail home page.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/resource_cards/ssh-quick-connect.png)

1. After your Lightsail browser-based SSH session is connected, enter the following command to update the packages on your instance:

   ```
   sudo apt-get update
   ```

1. Enter the following command to install the software properties package. Certbot's developers use a Personal Package Archive (PPA) to distribute Certbot. The software properties package makes it more efficient to work with PPAs.

   ```
   sudo apt-get install software-properties-common -y
   ```
**Note**  
If you encounter a `Could not get lock` error when running the `sudo apt-get install` command, wait approximately 15 minutes and try again. This error might be caused by a cron job that is using the Apt package management tool to install unattended upgrades.

1. Enter the following command to update apt to include the new repository:

   ```
   sudo apt-get update -y
   ```

1. Enter the following command to install Certbot:

   ```
   sudo apt-get install certbot -y
   ```

   Certbot is now installed on your Lightsail instance.

## Step 3: Request a Let’s Encrypt SSL wildcard certificate
<a name="request-a-lets-encrypt-certificate"></a>

Begin the process of requesting a certificate from Let's Encrypt. Using Certbot, request a wildcard certificate, which lets you use a single certificate for a domain and its subdomains. For example, a single wildcard certificate works for the `example.com` top-level domain, and the `blog.example.com`, and `stuff.example.com` subdomains.

**To request a Let's Encrypt SSL wildcard certificate**

1. In the same browser-based SSH terminal window used in the previous step of this tutorial, enter the following commands to set an environment variable for your domain. Be sure to replace {{domain}} with the name of your registered domain name.

   ```
   DOMAIN={{domain}}
   WILDCARD=*.$DOMAIN
   ```

   Example:

   ```
   DOMAIN=example.com
   WILDCARD=*.$DOMAIN
   ```

1. Enter the following command to confirm the variables return the correct values:

   ```
   echo $DOMAIN && echo $WILDCARD
   ```

   You should see a result similar to the following:  
![Confirm the domain environment variables.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/confirm-domain-and-wildcard-variables.png)

1. Enter the following command to start Certbot in interactive mode. This command tells Certbot to use a manual authorization method with DNS challenges to verify domain ownership. It requests a wildcard certificate for your top-level domain, as well as its subdomains.

   ```
   sudo certbot -d $DOMAIN -d $WILDCARD --manual --preferred-challenges dns certonly
   ```

1. Enter your email address when prompted, because it's used for renewal and security notices.

1. Read the Let's Encrypt terms of service. When done, press Y if you agree. If you disagree, you cannot obtain a Let's Encrypt certificate.

1. Respond accordingly to the prompt to share your email address and to the warning about your IP address being logged.

1. Let's Encrypt now prompts you to verify that you own the domain specified. You do this by adding TXT records to the DNS records for your domain. A set of TXT record values are provided as shown in the following example:
**Note**  
Let's Encrypt may provide a single or multiple TXT records that you must use for verification. In this example, we were provided with two TXT records to use for verification.  
![TXT records for Let's Encrypt certificates.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/get-TXT-records.png)

## Step 4: Add TXT records to your domain’s DNS zone
<a name="add-a-text-record-to-your-domains-dns-zone-lets-encrypt"></a>

 Adding a TXT record to your domain’s DNS zone verifies that you own the domain. For demonstration purposes, we use the Lightsail DNS zone. However, the steps might be similar for other DNS zones typically hosted by domain registrars. 

**Note**  
 To learn more about how to create a Lightsail DNS zone for your domain, see [ Creating a DNS zone to manage your domain’s DNS records in Lightsail ](lightsail-how-to-create-dns-entry.md) . 

**To add TXT records to your domain’s DNS zone in Lightsail**

1. In the left navigation pane, choose the **Domains & DNS**.

1.  Under the **DNS zones** section of the page, choose the DNS Zone for the domain that you specified in the Certbot certificate request. 

1. In the DNS zone editor, choose **DNS records**.

1. Choose **Add record**.

1.  In the **Record type** drop-down menu, choose **TXT record**. 

1.  Enter the values specified by the Let’s Encrypt certificate request into the **Record name** and **Responds with** fields. 
**Note**  
 The Lightsail console pre-populates the apex portion of your domain. For example, if you want to add the `{{_acme-challenge.example.com}}` subdomain, then you only have to enter `{{_acme-challenge}}` into the text box, and Lightsail adds the `.example.com` portion for you when you save the record. 

1. Choose **Save**.

1.  Repeat steps 4 through 7 to add the second set of TXT records specified by the Let’s Encrypt certificate request. 

1.  Keep the Lightsail console browser window open—you return to it later in this tutorial. Continue to the [ next section ](#confirm-the-text-records-have-propagated-lets-encrypt) of this tutorial. 

## Step 5: Confirm that the TXT records have propagated
<a name="confirm-the-text-records-have-propagated-lets-encrypt"></a>

 Use the MxToolbox utility to confirm that the TXT records have propagated to the Internet’s DNS. DNS record propagation might take a while depending on your DNS hosting provider, and the configured time to live (TTL) for your DNS records. It is important that you complete this step, and confirm that your TXT records have propagated, before continuing your Certbot certificate request. Otherwise, your certificate request fails. 

**To confirm the TXT records have propagated to the Internet’s DNS**

1.  Open a new browser window and go to [https://mxtoolbox.com/TXTLookup.aspx](https://mxtoolbox.com/TXTLookup.aspx) . 

1.  Enter the following text into the text box. Be sure to replace `{{domain}}` with your domain. 

   ```
   _acme-challenge.{{domain}}
   ```

   Example:

   ```
   _acme-challenge.{{example.com}}
   ```  
![MxToolbox TXT record lookup.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/mxtoolbox-text-record-lookup.png)

1. Choose **TXT Lookup** to run the check.

1. One of the following responses occurs:
   +  If your TXT records have propagated to the Internet’s DNS, you see a response similar to the one shown in the following screenshot. Close the browser window and continue to the [next section](#complete-the-lets-encrypt-certificate-request) of this tutorial.   
![Confirmation that TXT records propagated.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/mxtoolbox-propagated-text-record-lookup.png)
   +  If your TXT records have not propagated to the Internet’s DNS, you see a **DNS Record not found** response. Confirm that you added the correct DNS records to your domains’ DNS zone. If you added the correct records, wait a while longer to let your domain’s DNS records propagate, and run the TXT lookup again. 

## Step 6: Complete the Let’s Encrypt SSL certificate request
<a name="complete-the-lets-encrypt-certificate-request"></a>

 Go back to the Lightsail browser-based SSH session for your instance and complete the Let’s Encrypt certificate request. Certbot saves your SSL certificate, chain, and key files to a specific directory on your instance.

**To complete the Let’s Encrypt SSL certificate request**

1.  In the Lightsail browser-based SSH session for your instance, press **Enter** to continue your Let’s Encrypt SSL certificate request. If successful, a response similar to the one shown in the following screenshot appears:   
![Successful Let’s Encrypt certificate request.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/certificate-request-success.png)

    The message confirms that your certificate, chain, and key files are stored in the `/etc/letsencrypt/live/{{domain}}/` directory. Make sure to replace `{{domain}}` with your domain, such as `/etc/letsencrypt/live/{{example.com}}/`. 

1.  Make note of the expiration date specified in the message. You use it to renew your certificate by that date.   
![Let’s Encrypt certificate renewal date.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/certificate-renewal-date.png)

## Step 7: Update SSL configuration in Nginx and redirect traffic from HTTP to HTTPS
<a name="update-ssl-configuration"></a>

**To update the SSL configuration in Nginx's default.conf**

1.  In the SSH session for your Nginx instance, enter the following command to stop the underlying services: 

   ```
   sudo systemctl stop nginx
   sudo systemctl stop mariadb
   sudo systemctl stop php8.2-fpm
   ```

   You should see a response similar to the following:  
![Nginx instance services stopped.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/nginx-stop-services.png)

1.  Enter the following command to set an environment variable for your domain. You can more efficiently copy and paste commands to link the certificate files. Be sure to replace `{{domain}}` with the name of your registered domain. 

   ```
   DOMAIN={{domain}}
   ```

   Example:

   ```
   DOMAIN={{example.com}}
   ```

1. Enter the following command to confirm the variables return the correct values:

   ```
   echo $DOMAIN
   ```

   You should see a result similar to the following:  
![Confirm the domain environment variable.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/confirm-domain-variable.png)

1. Run the command below to change the SSL configuration:
**Note**  
If you closed your browser-based SSH terminal window since setting the `DOMAIN` variable in Step 3, run `DOMAIN={{example.com}}` again, replacing {{example.com}} with your domain.

   ```
   sudo sed \
   -i -e "s|ssl_certificate /etc/ssl/certs/ssl-cert-snakeoil.pem|ssl_certificate /etc/letsencrypt/live/$DOMAIN/fullchain.pem|g" \
   -i -e "s|ssl_certificate_key /etc/ssl/private/ssl-cert-snakeoil.key|ssl_certificate_key /etc/letsencrypt/live/$DOMAIN/privkey.pem|g" \
   /etc/nginx/conf.d/default.conf
   ```

1.  After overwriting the `default.conf` file, run the commands below to check the configuration and restart Nginx

   ```
   sudo nginx -t
   sudo systemctl restart nginx
   sudo systemctl restart mariadb
   sudo systemctl restart php8.2-fpm
   ```

   You should see a result similar to the following:  
![Nginx instance services started.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/lets-encrypt/nginx-start-services.png)

    Your Nginx instance is now configured to use SSL encryption and traffic is redirected from HTTP to HTTPS 

## Step 8: Renew the Let’s Encrypt certificates every 90 days
<a name="renew-a-lets-encrypt-certificate"></a>

 Let’s Encrypt certificates are valid for 90 days. Certificates can be renewed 30 days before they expire. To renew the Let’s Encrypt certificate, repeat [ Step 3: Request a Let’s Encrypt SSL wildcard certificate ](#request-a-lets-encrypt-certificate) . 