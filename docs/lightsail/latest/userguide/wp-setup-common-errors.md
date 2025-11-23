# Resolve WordPress setup errors on

Lightsail

An error message will appear at the top of the Lightsail console if there's an issue
with the information that was submitted during the workflow.

The first line of the message informs you that setup has encountered an error:

**`Could not complete setup on your instance
 `InstanceName`in the
`InstanceRegion` Region`**.

The second line contains the error that setup encountered:

**`An error occurred and we were unable to connect or stay connected to your
 instance`**

![WordPress setup failure message in the Lightsail console.](images/wp-setup-error-message.png)
To begin troubleshooting, match the error that appeared in the message with one of the
following errors.

###### Errors

- [DNS records not found. Confirm that the domain's DNS
  records point to the public IP address of your instance, and allow time for DNS
  changes to propagate.](#dns-not-found "#dns-not-found")
- [DNS records do not match. Confirm that the
  domain's DNS records point to the public IP address of your instance, and allow
  time for DNS changes to propagate.](#dns-mismatch-error "#dns-mismatch-error")
- [Unable to connect to your instance. Allow a few
  minutes for the SSH connection to become ready. Then, start setup again.](#unable-to-connect "#unable-to-connect")
- [Unsupported WordPress version. Setup only
  supports WordPress versions 6, and up.](#unsupported-wp-version "#unsupported-wp-version")
- [Setup only supports WordPress instances
  that were created on or after January 1, 2023.](#instance-create-date-error "#instance-create-date-error")
- [Instance firewall ports 22, 80, and 443 must
  allow a TCP connection from any IP address during the setup workflow. You can
  change these settings from the instance Networking tab.](#firewall-ports-error "#firewall-ports-error")

## DNS records not found. Confirm that the domain's DNS

records point to the public IP address of your instance, and allow time for DNS
changes to propagate.

**Reason**

This error is caused by misconfigured DNS records, or DNS records that
have not had sufficient time to propagate throughout the Internet's
DNS.

**Fix**

Confirm that the **A** or **AAAA**
DNS records are present in the DNS zone, and that they point to the
public IP address of your instance. For more information, see [DNS in
Lightsail](understanding-dns-in-amazon-lightsail.md "understanding-dns-in-amazon-lightsail.md").

When you add or update DNS records that point traffic from your apex
domain (`example.com`) and its `www` subdomains
(`www.example.com`), they will need to propagate
throughout the Internet's DNS. You can verify that your DNS changes have
taken effect by using tools such as [nslookup](https://aws.amazon.com/blogs//messaging-and-targeting/how-to-check-your-domain-verification-settings/ "https://aws.amazon.com/blogs//messaging-and-targeting/how-to-check-your-domain-verification-settings/"), or [DNS Lookup](https://mxtoolbox.com/DnsLookup.aspx "https://mxtoolbox.com/DnsLookup.aspx") from
_MxToolbox_.

###### Note

Allow time for any DNS record changes to propagate through the
internet's DNS, which may take several hours.

## DNS records do not match. Confirm that the

domain's DNS records point to the public IP address of your instance, and allow
time for DNS changes to propagate.

**Reason**

The **A** or **AAAA** DNS records do
not point to the public IP address of the instance.

**Fix**

Confirm that the **A** or **AAAA**
DNS records are present in the DNS zone, and that they point to the
public IP address of your instance. For more information, see [DNS in
Lightsail](understanding-dns-in-amazon-lightsail.md "understanding-dns-in-amazon-lightsail.md").

###### Note

Allow time for any DNS record changes to propagate through the
internet's DNS, which may take several hours.

## Unable to connect to your instance. Allow a few

minutes for the SSH connection to become ready. Then, start setup again.

**Reason**

The instance was just created or rebooted, and the SSH connection is
not ready.

**Fix**

Allow a few minutes for the SSH connection to become ready. Then,
retry the guided workflow. For more information, see [Troubleshooting SSH in Lightsail](amazon-lightsail-troubleshooting-browser-based-ssh-rdp-client-connection.md "amazon-lightsail-troubleshooting-browser-based-ssh-rdp-client-connection.md").

## Unsupported WordPress version. Setup only

supports WordPress versions 6, and up.

**Reason**

The version of WordPress that’s installed on the instance is older
than WordPress version 6. Older WordPress versions contain incompatible
software and dependencies that prevent the HTTPS certificate from being
generated.

**Fix**

Create a new WordPress instance from the Lightsail console. Then,
migrate the WordPress website from the older instance to the new one.
For more information, see [Migrate an
existing WordPress blog](migrate-your-wordpress-blog-to-amazon-lightsail.md "migrate-your-wordpress-blog-to-amazon-lightsail.md").

If you’re creating a new instance to replace the existing instance,
make sure to update your application dependencies to your new
instance.

## Setup only supports WordPress instances

that were created on or after January 1, 2023.

**Reason**

The instance that is being used with setup, might contain outdated
software. Older software will prevent the HTTPS certificate from being
generated.

**Fix**

Create a new WordPress instance from the Lightsail console. Then,
migrate the WordPress website from the older instance to the new one.
For more information, see [Migrate an
existing WordPress blog](migrate-your-wordpress-blog-to-amazon-lightsail.md "migrate-your-wordpress-blog-to-amazon-lightsail.md").

If you’re creating a new instance to replace the existing instance,
make sure to update your application dependencies to your new
instance.

## Instance firewall ports 22, 80, and 443 must

allow a TCP connection from any IP address during the setup workflow. You can
change these settings from the instance Networking tab.

**Reason**

Instance firewall ports 22, 80, and 443 must allow TCP connections
from any IP address while setup is running. This error is generated when
one or more of these ports are closed. For more information, see [Instance firewalls](understanding-firewall-and-port-mappings-in-amazon-lightsail.md "understanding-firewall-and-port-mappings-in-amazon-lightsail.md").

**Fix**

Add or edit the instance’s IPv4 and IPv6 firewall rules to allow TCP
connections over ports 22, 80, and 443. For more information, see [Add and edit
instance firewall rules](amazon-lightsail-editing-firewall-rules.md "amazon-lightsail-editing-firewall-rules.md").
