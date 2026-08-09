# Set up WordPress Multisite on Lightsail

###### Did you know?

Lightsail stores seven daily snapshots and automatically replaces the oldest with the newest when you enable
automatic snapshots for your instance. For more information, see
[Configure automatic snapshots for Lightsail instances and disks](amazon-lightsail-configuring-automatic-snapshots.md "amazon-lightsail-configuring-automatic-snapshots.md")
.

Here are a few steps you should take to get started after your WordPress Multisite
instance is up and running on Amazon Lightsail:

Lightsail

###### Step 1: Get the default application password to access the WordPress administration

dashboard

Complete the following procedure to get the default application password required to
access the administration dashboard for your WordPress Multisite website.

1. On your instance management page, under the **Connect** tab,
   choose **Connect using SSH**.

![Connect using SSH in the Lightsail console](images/quick-start-connect-to-your-instance.png) 2. After you're connected, enter the following command to get the default
application password:

```
cat ~/application_credentials
```

You should see a response similar to the following example, which contains the
default application password. Use this password to sign in to the administration
dashboard of your WordPress Multisite website.

![Default application password.](images/lightsail-password-retrieval.png)

###### Step 2: Attach a

static IP address to your instance

The default dynamic public IP address attached to your instance changes every time you
stop and start the instance. You can create a static IP address and attach it to your instance to
keep the public IP address from changing. Later, when you use your domain name with your
instance, you don’t have to update your domain’s DNS records each time you stop and start the
instance. You can attach only one static IP address to each instance.

On the instance management page, under the **Networking** tab,
choose **Create a static IP** or **Attach static
IP** (if you previously created a static IP that you can attach to your
instance), then follow the instructions on the page. For more information, see [Create a static IP and attach it to an
instance](lightsail-create-static-ip.md "lightsail-create-static-ip.md").

![Attach static IP address in the Lightsail console](images/quick-start-static-ip-address.png)

After the new static IP address is attached to your instance, you must complete the
following procedure to make WordPress aware of the new static IP address.

1. Make a note of the new static IP address of your instance. It's listed in the
   header section of your instance management page.

![Public or static IP address of a Lightsail instance](images/quick-start-public-static-ip.png) 2. On the instance management page, under the **Connect** tab,
choose **Connect using SSH**.

![Connect to your instance using SSH](images/quick-start-connect-using-ssh.png) 3. After you're connected, enter the following command. Replace
`<StaticIP>` with the new static IP address
of your instance.

```
sudo /opt/aws/wordpress/update_multisite_domain.sh `<StaticIP>`
```

**Example:**

```
sudo /opt/aws/wordpress/update_multisite_domain.sh `203.0.113.0`
```

The WordPress
website on your instance should now be aware of the new static IP
address.

![Result of the domain configuration tool](images/wp-multisite-lightsail-new-domain.png)

###### Step 3: Sign in to the

administration dashboard of your WordPress Multisite website

Now that you have the default application password, complete the following procedure
to navigate to your WordPress Multisite website's home page, and sign in to the
administration dashboard. After you're signed in, you can start customizing your website
and making administrative changes. For more information about what you can do in
WordPress, see the [Step 6: Read the
WordPress Multisite documentation and continue configuring your website](#amazon-lightsail-read-documentation-wordpress-multisite-lightsail "#amazon-lightsail-read-documentation-wordpress-multisite-lightsail")
section later in this guide.

1. On your instance management page, under the **Connect** tab,
   make note of the public IP address of your instance. The public IP address is
   also displayed in the header section of your instance management page.

![Public IP address of an instance](images/quick-start-public-ip.png) 2. Browse to the public IP address of your instance, for example by going to
`http://203.0.113.0`.

The home page of your WordPress website should appear. 3. On your WordPress website home page, choose the
**Manage** banner.

If the **Manage** banner is not shown, you can reach the sign
in page by browsing to
`http://`<PublicIP>`/wp-login.php`.
Replace `<PublicIP>` with the public
IP address of your instance. 4. Sign in using the default user name (`user`) and the default
password retrieved earlier in this guide.

The WordPress administration dashboard appears.

![The WordPress administration dashboard.](images/amazon-lightsail-wordpress-dashboard.png)

###### Step 4: Route traffic for your registered domain name to your WordPress Multisite

website

To route traffic for your registered domain name, such as `example.com`, to
your WordPress Multisite website, you add a record to the DNS of your domain. DNS
records are typically managed and hosted at the registrar where you registered your
domain. However, we recommend that you transfer management of your domain's DNS records
to Lightsail so that you can administer it using the Lightsail console.

On the Lightsail console home page, under the **Domains &
DNS** tab, choose **Create DNS zone**, then follow the
instructions on the page. For more information, see [Creating a DNS zone to manage your
domain's DNS records in Lightsail](lightsail-how-to-create-dns-entry.md "lightsail-how-to-create-dns-entry.md").

After your domain name is routing traffic to your instance, you must complete the
following procedure to make WordPress aware of the domain name.

1. On the instance management page, under the **Connect** tab,
   choose **Connect using SSH**.

![Connect to your instance using SSH](images/quick-start-connect-using-ssh.png) 2. After you're connected, enter the following command. Replace
`<DomainName>` with the domain name that is
routing traffic to your instance.

```
sudo /opt/aws/wordpress/update_multisite_domain.sh `<DomainName>`
```

**Example:**

```
sudo /opt/aws/wordpress/update_multisite_domain.sh `www.example.com`
```

The WordPress
Multisite software should now be aware of the domain name.

![Result of the domain configuration tool](images/wp-multisite-lightsail-new-domain.png)

If you browse to the domain name that you configured for your instance, you should be
redirected to the main blog of your WordPress Multisite website. Next you must decide
whether you want to add blogs as domains or as subdomains to your WordPress Multisite
website.

###### Step 5: Add blogs as domains or subdomains to your WordPress Multisite

website

WordPress Multisite is designed to host multiple blog websites on one instance of
WordPress. When you add new blog websites to your WordPress Multisite, you can configure
them to use their own domains or a subdomain of your WordPress Multisite's primary
domain.

- To add blog sites as domains, such as `example1.com` and
  `example2.com`, see [Add blogs as domains to your WordPress Multisite instance in
  Lightsail](amazon-lightsail-add-blogs-as-domains-to-your-wordpress-multisite.md "amazon-lightsail-add-blogs-as-domains-to-your-wordpress-multisite.md").
- To add blog sites as subdomains of your WordPress Multisite's primary domain,
  such as `one.example.com` and `two.example.com`, see [Add blogs as subdomains to your WordPress Multisite instance in
  Lightsail](amazon-lightsail-add-blogs-as-subdomains-to-your-wordpress-multisite.md "amazon-lightsail-add-blogs-as-subdomains-to-your-wordpress-multisite.md").

###### Step 6: Read

the WordPress Multisite documentation and continue configuring your website

Read the WordPress Multisite documentation to learn how to administer and customize
your website. For more information, see the [WordPress Multisite Network Administration Documentation](https://developer.wordpress.org/advanced-administration/multisite/ "https://developer.wordpress.org/advanced-administration/multisite/").

###### Step 7: Create

a snapshot of your instance

After you configure your website the way you want it, create
periodic snapshots of your instance to back it up. A snapshot is a copy of the system disk and original configuration of an instance. A
snapshot contains all of the data that is needed to restore your instance (from the moment
when the snapshot was taken).

You can create [snapshots manually](understanding-snapshots-in-amazon-lightsail.md#manual-snapshots "understanding-snapshots-in-amazon-lightsail.md#manual-snapshots"), or
[enable automatic snapshots](understanding-snapshots-in-amazon-lightsail.md#automatic-snapshots "understanding-snapshots-in-amazon-lightsail.md#automatic-snapshots") to have Lightsail create daily snapshots for you. If
something goes wrong with your instance, you can create a new replacement instance using
the snapshot.

You can work with snapshots on your instance's management page on the **Snapshots** tab.
For more information, see [Snapshots in Amazon Lightsail](understanding-snapshots-in-amazon-lightsail.md "understanding-snapshots-in-amazon-lightsail.md").

![Create an instance snapshot in the Lightsail console](images/quick-start-instance-snapshots.png)

Bitnami

###### Step 1: Read the Bitnami documentation

Read the Bitnami documentation to learn how to configure your WordPress Multisite
instance. For more information, see the [WordPress Multisite
Packaged By Bitnami For AWS Cloud](https://docs.bitnami.com/general/apps/wordpress-multisite/ "https://docs.bitnami.com/general/apps/wordpress-multisite/").

###### Step 2: Get the default application password to access the WordPress administration

dashboard

Complete the following procedure to get the default application password required to
access the administration dashboard for your WordPress Multisite website. For more
information, see [Getting the
application user name and password for your Bitnami instance in
Amazon Lightsail](log-in-to-your-bitnami-application-running-on-amazon-lightsail.md "log-in-to-your-bitnami-application-running-on-amazon-lightsail.md").

1. On your instance management page, under the **Connect** tab,
   choose **Connect using SSH**.

![Connect using SSH in the Lightsail console](images/quick-start-connect-to-your-instance.png) 2. After you're connected, enter the following command to get the default
application password:

```
cat $HOME/bitnami_application_password
```

You should see a response similar to the following example, which contains the
default application password. Use this password to sign in to the administration
dashboard of your WordPress Multisite website.

![Bitnami default application password.](images/amazon-lightsail-bitnami-application-password.png)

###### Step 3: Attach a

static IP address to your instance

The default dynamic public IP address attached to your instance changes every time you
stop and start the instance. You can create a static IP address and attach it to your instance to
keep the public IP address from changing. Later, when you use your domain name with your
instance, you don’t have to update your domain’s DNS records each time you stop and start the
instance. You can attach only one static IP address to each instance.

On the instance management page, under the **Networking** tab,
choose **Create a static IP** or **Attach static
IP** (if you previously created a static IP that you can attach to your
instance), then follow the instructions on the page. For more information, see [Create a static IP and attach it to an
instance](lightsail-create-static-ip.md "lightsail-create-static-ip.md").

![Attach static IP address in the Lightsail console](images/quick-start-static-ip-address.png)

After the new static IP address is attached to your instance, you must complete the
following procedure to make WordPress aware of the new static IP address.

1. Make a note of the new static IP address of your instance. It's listed in the
   header section of your instance management page.

![Public or static IP address of a Lightsail instance](images/quick-start-public-static-ip.png) 2. On the instance management page, under the **Connect** tab,
choose **Connect using SSH**.

![Connect to your instance using SSH](images/quick-start-connect-using-ssh.png) 3. After you're connected, enter the following command. Replace
`<StaticIP>` with the new static IP address
of your instance.

```
sudo /opt/bitnami/configure_app_domain --domain `<StaticIP>`
```

**Example:**

```
sudo /opt/bitnami/configure_app_domain --domain `203.0.113.0`
```

You should see a response similar to the following example. The WordPress
website on your instance should now be aware of the new static IP
address.

![Result of the domain configuration tool](images/quick-start-configure-domain-ip.png)

###### Note

If that command fails, you might be using an older version of the WordPress
Multisite instance. Try running the following commands instead. Replace
`<StaticIP>` with the new static IP address
of your instance.

```
cd /opt/bitnami/apps/wordpress
sudo ./bnconfig --machine_hostname `<StaticIP>`
```

After running those commands, enter the following command to keep the bnconfig
tool from automatically running every time the server restarts.

```
sudo mv bnconfig bnconfig.disabled
```

###### Step 4: Sign in to the

administration dashboard of your WordPress Multisite website

Now that you have the default application password, complete the following procedure
to navigate to your WordPress Multisite website's home page, and sign in to the
administration dashboard. After you're signed in, you can start customizing your website
and making administrative changes. For more information about what you can do in
WordPress, see the [Step 7: Read the
WordPress Multisite documentation and continue configuring your website](#amazon-lightsail-read-documentation-wordpress-multisite "#amazon-lightsail-read-documentation-wordpress-multisite")
section later in this guide.

1. On your instance management page, under the **Connect** tab,
   make note of the public IP address of your instance. The public IP address is
   also displayed in the header section of your instance management page.

![Public IP address of an instance](images/quick-start-public-ip.png) 2. Browse to the public IP address of your instance, for example by going to
`http://203.0.113.0`.

The home page of your WordPress website should appear. 3. On your WordPress website home page, choose the
**Manage** banner.

If the **Manage** banner is not shown, you can reach the sign
in page by browsing to
`http://`<PublicIP>`/wp-login.php`.
Replace `<PublicIP>` with the public
IP address of your instance. 4. Sign in using the default user name (`user`) and the default
password retrieved earlier in this guide.

The WordPress administration dashboard appears.

![The WordPress administration dashboard.](images/amazon-lightsail-wordpress-dashboard.png)

###### Step 5: Route traffic for your registered domain name to your WordPress Multisite

website

To route traffic for your registered domain name, such as `example.com`, to
your WordPress Multisite website, you add a record to the DNS of your domain. DNS
records are typically managed and hosted at the registrar where you registered your
domain. However, we recommend that you transfer management of your domain's DNS records
to Lightsail so that you can administer it using the Lightsail console.

On the Lightsail console home page, under the **Domains &
DNS** tab, choose **Create DNS zone**, then follow the
instructions on the page. For more information, see [Creating a DNS zone to manage your
domain's DNS records in Lightsail](lightsail-how-to-create-dns-entry.md "lightsail-how-to-create-dns-entry.md").

After your domain name is routing traffic to your instance, you must complete the
following procedure to make WordPress aware of the domain name.

1. On the instance management page, under the **Connect** tab,
   choose **Connect using SSH**.

![Connect to your instance using SSH](images/quick-start-connect-using-ssh.png) 2. After you're connected, enter the following command. Replace
`<DomainName>` with the domain name that is
routing traffic to your instance.

```
sudo /opt/bitnami/configure_app_domain --domain `<DomainName>`
```

**Example:**

```
sudo /opt/bitnami/configure_app_domain --domain `www.example.com`
```

You should see a response similar to the following example. The WordPress
Multisite software should now be aware of the domain name.

![Result of the domain configuration tool](images/quick-start-configure-domain.png)

###### Note

If that command fails, you might be using an older version of the WordPress
Multisite instance. Try running the following commands instead. Replace
`<DomainName>` with the domain name that is
routing traffic to your instance.

```
cd /opt/bitnami/apps/wordpress
sudo ./bnconfig --machine_hostname `<DomainName>`
```

After running those commands, enter the following command to keep the bnconfig
tool from automatically running every time the server restarts.

```
sudo mv bnconfig bnconfig.disabled
```

If you browse to the domain name that you configured for your instance, you should be
redirected to the main blog of your WordPress Multisite website. Next you must decide
whether you want to add blogs as domains or as subdomains to your WordPress Multisite
website. For more information, continue to the next [Step 6: Add blogs as domains or subdomains to your WordPress Multisite
website](#amazon-lightsail-add-blogs-as-domains-or-subdomains-wordpress-multisite "#amazon-lightsail-add-blogs-as-domains-or-subdomains-wordpress-multisite") section of this guide.

###### Step 6: Add blogs as domains or subdomains to your WordPress Multisite

website

WordPress Multisite is designed to host multiple blog websites on one instance of
WordPress. When you add new blog websites to your WordPress Multisite, you can configure
them to use their own domains or a subdomain of your WordPress Multisite's primary
domain.

- To add blog sites as domains, such as `example1.com` and
  `example2.com`, see [Add blogs as domains to your WordPress Multisite instance in
  Lightsail](amazon-lightsail-add-blogs-as-domains-to-your-wordpress-multisite.md "amazon-lightsail-add-blogs-as-domains-to-your-wordpress-multisite.md").
- To add blog sites as subdomains of your WordPress Multisite's primary domain,
  such as `one.example.com` and `two.example.com`, see [Add blogs as subdomains to your WordPress Multisite instance in
  Lightsail](amazon-lightsail-add-blogs-as-subdomains-to-your-wordpress-multisite.md "amazon-lightsail-add-blogs-as-subdomains-to-your-wordpress-multisite.md").

###### Step 7: Read

the WordPress Multisite documentation and continue configuring your website

Read the WordPress Multisite documentation to learn how to administer and customize
your website. For more information, see the [WordPress Multisite Network Administration Documentation](https://developer.wordpress.org/advanced-administration/multisite/ "https://developer.wordpress.org/advanced-administration/multisite/").

###### Step 8: Create

a snapshot of your instance

After you configure your website the way you want it, create
periodic snapshots of your instance to back it up. A snapshot is a copy of the system disk and original configuration of an instance. A
snapshot contains all of the data that is needed to restore your instance (from the moment
when the snapshot was taken).

You can create [snapshots manually](understanding-snapshots-in-amazon-lightsail.md#manual-snapshots "understanding-snapshots-in-amazon-lightsail.md#manual-snapshots"), or
[enable automatic snapshots](understanding-snapshots-in-amazon-lightsail.md#automatic-snapshots "understanding-snapshots-in-amazon-lightsail.md#automatic-snapshots") to have Lightsail create daily snapshots for you. If
something goes wrong with your instance, you can create a new replacement instance using
the snapshot.

You can work with snapshots on your instance's management page on the **Snapshots** tab.
For more information, see [Snapshots in Amazon Lightsail](understanding-snapshots-in-amazon-lightsail.md "understanding-snapshots-in-amazon-lightsail.md").

![Create an instance snapshot in the Lightsail console](images/quick-start-instance-snapshots.png)
