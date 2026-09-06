

# Lightsail Setup failed
<a name="amazon-lightsail-troubleshooting-wp-https-lightsail"></a>

Two types of error messages can appear during the WordPress setup workflow in Amazon Lightsail:

## Common errors
<a name="common-errors-lightsail"></a>

These errors appear immediately in a banner at the top of the Lightsail console after you choose **Create certificate** in the final step of the workflow.

![WordPress setup failure message in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/wp-setup-error-message.png)


To begin troubleshooting, match the error that appeared in the message with one of the following errors.
+ [DNS records not found](#dns-not-found-lightsail)
+ [DNS records do not match](#dns-mismatch-error-lightsail)
+ [Unable to connect to your instance](#unable-to-connect-lightsail)
+ [Unsupported WordPress version](#unsupported-wp-version-lightsail)
+ [Instance created prior to January 1, 2023](#instance-create-date-error-lightsail)
+ [Instance firewall ports](#firewall-ports-error-lightsail)

## Setup failures
<a name="setup-failures-lightsail"></a>

These errors appear within a few minutes in the **Set up your WordPress website** section of the instance **Connect** tab. They're caused when the Let's Encrypt HTTPS certificate cannot be configured on your instance.

![WordPress setup failure message in the Lightsail console.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/wp-setup-failure-message.png)


From the failure message, choose the **Download the error log** link to download and view the error logs. Match the error with one of the following:
+ [Some challenges have failed](#certbot-authorization-error-lightsail)
+ [Certbot failed to authenticate some domains](#domain-authentication-failed-lightsail)
+ [Deprecated Debian repository](#deprecated-debian-repo-lightsail)
+ [Deprecated PPA repository](#deprecated-ppa-repo-error-lightsail)
+ [Too many certificates](#too-many-certificates-lightsail)
+ [Too many failed authorizations](#too-many-failed-authorizations-lightsail)

## DNS records not found. Confirm that the domain's DNS records point to the public IP address of your instance, and allow time for DNS changes to propagate.
<a name="dns-not-found-lightsail"></a>

**Reason**  
This error is caused by misconfigured DNS records, or DNS records that have not had sufficient time to propagate throughout the Internet's DNS.

**Fix**  
Confirm that the **A** or **AAAA** DNS records are present in the DNS zone, and that they point to the public IP address of your instance. For more information, see [DNS in Lightsail](understanding-dns-in-amazon-lightsail.md).  
When you add or update DNS records that point traffic from your apex domain (`example.com`) and its `www` subdomains (`www.example.com`), they will need to propagate throughout the Internet's DNS. You can verify that your DNS changes have taken effect by using tools such as [nslookup](https://aws.amazon.com/blogs/messaging-and-targeting/how-to-check-your-domain-verification-settings/), or [DNS Lookup](https://mxtoolbox.com/DnsLookup.aspx) from *MxToolbox*.  
Allow time for any DNS record changes to propagate through the internet's DNS, which may take several hours.

## DNS records do not match. Confirm that the domain's DNS records point to the public IP address of your instance, and allow time for DNS changes to propagate.
<a name="dns-mismatch-error-lightsail"></a>

**Reason**  
The **A** or **AAAA** DNS records do not point to the public IP address of the instance.

**Fix**  
Confirm that the **A** or **AAAA** DNS records are present in the DNS zone, and that they point to the public IP address of your instance. For more information, see [DNS in Lightsail](understanding-dns-in-amazon-lightsail.md).  
Allow time for any DNS record changes to propagate through the internet's DNS, which may take several hours.

## Unable to connect to your instance. Allow a few minutes for the SSH connection to become ready. Then, start setup again.
<a name="unable-to-connect-lightsail"></a>

**Reason**  
The instance was just created or rebooted, and the SSH connection is not ready.

**Fix**  
Allow a few minutes for the SSH connection to become ready. Then, retry the guided workflow. For more information, see [Troubleshooting SSH in Lightsail](amazon-lightsail-troubleshooting-browser-based-ssh-rdp-client-connection.md).

## Unsupported WordPress version. Setup only supports WordPress versions 6, and up.
<a name="unsupported-wp-version-lightsail"></a>

**Reason**  
The version of WordPress that's installed on the instance is older than WordPress version 6. Older WordPress versions contain incompatible software and dependencies that prevent the HTTPS certificate from being generated.

**Fix**  
Create a new WordPress instance from the Lightsail console. Then, migrate the WordPress website from the older instance to the new one. For more information, see [Migrate an existing WordPress blog](migrate-your-wordpress-blog-to-amazon-lightsail.md).  
If you're creating a new instance to replace the existing instance, make sure to update your application dependencies to your new instance.

## Setup only supports WordPress instances that were created on or after January 1, 2023.
<a name="instance-create-date-error-lightsail"></a>

**Reason**  
The instance that is being used with setup, might contain outdated software. Older software will prevent the HTTPS certificate from being generated.

**Fix**  
Create a new WordPress instance from the Lightsail console. Then, migrate the WordPress website from the older instance to the new one. For more information, see [Migrate an existing WordPress blog](migrate-your-wordpress-blog-to-amazon-lightsail.md).  
If you're creating a new instance to replace the existing instance, make sure to update your application dependencies to your new instance.

## Instance firewall ports 22, 80, and 443 must allow a TCP connection from any IP address during the setup workflow. You can change these settings from the instance Networking tab.
<a name="firewall-ports-error-lightsail"></a>

**Reason**  
Instance firewall ports 22, 80, and 443 must allow TCP connections from any IP address while setup is running. This error is generated when one or more of these ports are closed. For more information, see [Instance firewalls](understanding-firewall-and-port-mappings-in-amazon-lightsail.md).

**Fix**  
Add or edit the instance's IPv4 and IPv6 firewall rules to allow TCP connections over ports 22, 80, and 443. For more information, see [Add and edit instance firewall rules](amazon-lightsail-editing-firewall-rules.md). 

## Certbot.errors.AuthorizationError: Some challenges have failed
<a name="certbot-authorization-error-lightsail"></a>

**Reason**  
This error is caused by misconfigured DNS records, or DNS records that have not had sufficient time to propagate throughout the Internet.

**Fix**  
Verify that the **A** or **AAAA** DNS records are present in the DNS zone, and that they point to the public IP address of your instance. For more information, see [DNS in Lightsail](understanding-dns-in-amazon-lightsail.md).  
When you add or update DNS records that point traffic from your apex domain (`example.com`) and its `www` subdomains (`www.example.com`), they will need to propagate throughout the Internet. You can verify that your DNS changes have taken effect by using tools such as [nslookup](https://aws.amazon.com/blogs/messaging-and-targeting/how-to-check-your-domain-verification-settings/), or [DNS Lookup](https://mxtoolbox.com/DnsLookup.aspx) from *MxToolbox*.  
Allow time for any DNS record changes to propagate through the internet's DNS, which may take several hours.

## Certbot failed to authenticate some domains
<a name="domain-authentication-failed-lightsail"></a>

**Reason**  
This error can surface if another process is using port 80 while the HTTPS certificate is being configured on the instance.

**Fix**  
Restart your WordPress instance. Then, run the guided workflow again. Use the following procedure to terminate any running processes on the instance that are running on port 80 if restarting doesn't resolve the issue.

**Procedure**

1. Connect to your instance by using the Lightsail [browser-based SSH client](lightsail-how-to-connect-to-your-instance-virtual-private-server.md), or by using [AWS CloudShell](amazon-lightsail-cloudshell.md). 

1. Stop the Apache service that's running on the instance:

   ```
   $ sudo systemctl stop apache2
   ```

   Verify that the Apache service is stopped:

   ```
   $ sudo systemctl status apache2
   ```

1. Check if there are other processes that are using port 80:

   ```
   $ fuser -n tcp 80
   ```

1. Terminate any processes that are not needed by another application:

   ```
   $ fuser -k -n tcp 80
   ```

1. Restart WordPress setup.

## The repository http://cdn-aws.deb.debian.org/debian buster-backports no longer has a Release file
<a name="deprecated-debian-repo-lightsail"></a>

**Reason**  
There is a deprecated Debian repository on your instance that cannot be updated.

**Fix**  
Use the following procedure to edit the repository URL that's listed in the Debian repository file.

**Procedure**

1. Connect to your instance by using the Lightsail [browser-based SSH client](lightsail-how-to-connect-to-your-instance-virtual-private-server.md), or by using [AWS CloudShell](amazon-lightsail-cloudshell.md). 

1. Navigate to the `/etc/apt/sources.list.d/` directory.

   ```
   $ cd /etc/apt/sources.list.d/
   ```

1. Use a text editor of your choice to open the `buster-backports.list` file. If the file isn't found in this directory, you can also check in `/etc/apt/sources.list`. The preinstalled Vim text editor is used in the example command. For more information, see the [*Vim documentation*](https://www.vim.org/docs.php).

   ```
   $ vim buster-backports.list
   ```

1. Locate any line that contains `cdn-aws.deb.debian.org` or `deb.debian.org`, and replace it with `archive.debian.org`.

1. Save and close the file.

1. Restart WordPress setup.

## The repository http://ppa.launchpad.net/certbot/certbot/ubuntu lunar Release does not have a Release file
<a name="deprecated-ppa-repo-error-lightsail"></a>

**Reason**  
There is a deprecated Certbot Personal Package Archive (PPA) repository on your instance that cannot be updated.

**Fix**  
Use the following procedure to manually remove the deprecated PPA repository from your instance.

**Procedure**

1. Connect to your instance by using the Lightsail [browser-based SSH client](lightsail-how-to-connect-to-your-instance-virtual-private-server.md), or by using [AWS CloudShell](amazon-lightsail-cloudshell.md). 

1. Navigate to the `/etc/apt/sources.list.d/` directory.

   ```
   $ cd /etc/apt/sources.list.d/
   ```

1. Use a text editor of your choice to open the `certbot-ubuntu-certbot-version.list` file. The preinstalled Vim text editor is used in the example command. For more information, see the [*Vim documentation*](https://www.vim.org/docs.php).

   In the command, replace **version** with the version of Ubuntu that the repository is incompatible with; this will be the same version that shows up in the error message. For example, **lunar** or **mantic**.

   ```
   $ vim certbot-ubuntu-certbot-version.list
   ```

1. Remove any line that contains the following text: `http://ppa.launchpad.net/certbot/certbot/ubuntu`.

1. Save and close the file.

1. Restart WordPress setup.

## Too many certificates (5) already issued for this exact set of domains in the last 168 hours
<a name="too-many-certificates-lightsail"></a>

**Reason**  
One or more of your domains or subdomains has already been used to create 5 certificates within the last week. For more information, see [Rate Limits](https://letsencrypt.org/docs/rate-limits/) on the *Let's Encrypt website*.

**Fix**  
Wait one week (168 hours), and then restart the guided workflow for this domain.

## Too many failed authorizations
<a name="too-many-failed-authorizations-lightsail"></a>

**Reason**  
One or more of the domains or subdomains in the request has exceeded the limit of five validations per hour. For more information, see [Rate Limits](https://letsencrypt.org/docs/rate-limits/) on the *Let's Encrypt website*. 

**Fix**  
Wait one hour and run WordPress setup again. Verify that other validation errors have been fixed before you restart setup.