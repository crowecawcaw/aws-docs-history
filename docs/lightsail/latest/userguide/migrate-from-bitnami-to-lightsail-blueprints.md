

# Migrating from Bitnami blueprints to Lightsail blueprints
<a name="migrate-from-bitnami-to-lightsail-blueprints"></a>

Amazon Lightsail offers blueprints packaged by Lightsail for several popular application stacks. Lightsail blueprints offer default security settings, including IMDSv2 enforced by default and port 22 restricted on launch. This guide walks you through migrating an existing Lightsail instance running a Bitnami blueprint to a new Lightsail instance running the equivalent Lightsail blueprint.

Your application version on your instance may become outdated over time as newer updates are released with security patches, performance improvements, and new features. There are two ways to keep your application up to date: update the application already running on your existing instance, or migrate to a new instance with a new version of the blueprint that includes the latest updates.

## Supported Lightsail blueprints
<a name="migrate-bitnami-supported-blueprints"></a>

Lightsail-packaged blueprints are currently available for the following applications:
+ [WordPress](migrate-your-wordpress-blog-from-bitnami-to-amazon-lightsail.md)
+ WordPress Multisite
+ LAMP
+ Nginx
+ Node.js

If your existing instance runs a Bitnami blueprint that does *not* have a Lightsail equivalent — including **Joomla, Magento, MEAN, Drupal, GitLab, Redmine, Ghost, Django, and PrestaShop** — a direct blueprint migration path is not available. You have two options:
+ **Use an alternative managed offering**: Consider an equivalent [AWS Marketplace](https://aws.amazon.com/marketplace) AMI deployed on Amazon Elastic Compute Cloud.
+ **Start from scratch on Lightsail**: Create a new Lightsail instance using a base OS blueprint (e.g., Amazon Linux 2023 or Ubuntu), manually install the required dependencies, and then copy over your application configuration and data.

## Prerequisites
<a name="migrate-bitnami-prerequisites"></a>

Before you begin, confirm the following:
+ Your existing Lightsail instance is running a **Bitnami blueprint** (verify this on the instance management page in the Lightsail console).
+ You have **admin access** to your application (e.g. the application's admin dashboard or SSH access to the instance).
+ You have identified the **equivalent Lightsail blueprint** for your application stack (see the [list of supported blueprints](#migrate-bitnami-supported-blueprints) above).

## Step 1: Back up your application data
<a name="migrate-bitnami-step1-backup"></a>

Export or back up all application content, configuration, and data from your existing Bitnami instance. The method varies by application:
+ **CMS applications (e.g., [WordPress](migrate-your-wordpress-blog-from-bitnami-to-amazon-lightsail.html#migrate-wordpress-blog-back-up-wordpress-blog))**: Use the application's built-in export tool (e.g., Tools → Export in WordPress) to download a full content export file. Save the file in an easy-to-find location — you will need it in Step 4.
+ **Database-backed applications**: Export your database (e.g., using `mysqldump` for MySQL/MariaDB or `pg_dump` for PostgreSQL) and save the dump file.
+ **File-based assets**: Copy any uploaded media, static files, or custom configuration files from the instance (e.g., via SFTP or the Lightsail browser-based SSH client).
+ **Application configuration**: Note any custom settings, environment variables, or configuration file changes specific to your deployment.

**Tip**  
Consider taking a manual snapshot of your existing Lightsail instance as an additional safety net before proceeding.

## Step 2: Create a new Lightsail instance with the Lightsail blueprint
<a name="migrate-bitnami-step2-create-instance"></a>

1. Go to the [Lightsail home page](https://lightsail.aws.amazon.com/) and sign in.

1. Choose **Create instance**.

1. Select the **AWS Region** (and optionally the Availability Zone) where you want to create the new instance.

1. Under **Select a blueprint**, choose your application stack and ensure the blueprint provider is **Lightsail** — not Bitnami.

1. Select an **instance plan** (bundle). You can upgrade later by creating an instance from a snapshot if needed.

1. Enter a name for your instance.

   Resource names:
   + Must be unique within the AWS Region in your Lightsail account.
   + Must contain 2–255 characters.
   + Must start and end with an alphanumeric character.
   + Can include alphanumeric characters, periods, dashes, and underscores.

1. Optionally, add tags to help organize your resources.

1. Choose **Create instance** and wait for the instance to reach a running state.

## Step 3: Configure your new instance
<a name="migrate-bitnami-step3-access-instance"></a>

Once the instance is running, follow these steps to access and configure it:

**Retrieve the default application password**

You need the default application password to access pre-installed applications or services on your new instance.

1. On your instance management page, under the **Connect** tab, choose **Connect using SSH**.

1. After you're connected, enter the following command to get the default application password:

   ```
   cat ~/application_credentials
   ```

**Attach a static IP address**

The default dynamic public IP address attached to your instance changes every time you stop and start the instance. Create a static IP address and attach it to your instance so you don't have to update your DNS records each time.

1. On the instance management page, under the **Networking** tab, choose **Create a static IP** or **Attach static IP**, then follow the instructions on the page.

1. For more information, see [Create a static IP and attach it to an instance](lightsail-create-static-ip.md).

**Visit your application's welcome page**

1. On your instance management page, copy the static IP address.

1. Paste the static IP address into your browser address bar (e.g., `http://192.0.2.1`).

1. Verify that the default application page loads successfully.

## Step 4: Restore your application data
<a name="migrate-bitnami-step4-restore-data"></a>

Import or restore the data you backed up in Step 1. The method varies by application:
+ **CMS applications (e.g., [WordPress](migrate-your-wordpress-blog-from-bitnami-to-amazon-lightsail.html#migrate-wordpress-blog-in-wordpress))**: Use the application's built-in import tool (e.g., Tools → Import in WordPress) to upload and run the content export file from Step 1.
+ **Database-backed applications**: Import your database dump into the new instance's database server using the appropriate tool (e.g., `mysql` CLI or `psql`).
+ **File-based assets**: Transfer your media files, static assets, and custom configuration files to the appropriate directories on the new instance.
+ **Application configuration**: Re-apply any custom settings or environment variables to match your previous deployment.

## Step 5: Verify the migration
<a name="migrate-bitnami-step5-verify"></a>

After restoring your data, verify that the application is working correctly:

1. Open a browser and navigate to the public IP address of your new instance.

1. Confirm that your content, configuration, and functionality are behaving as expected.

1. Test key application workflows (e.g. user login, content display, form submissions).

1. Check application and server logs for any errors.

## Step 6: Transfer the static IP address (if applicable)
<a name="migrate-bitnami-step6-static-ip"></a>

If your application uses a custom domain with a static IP already attached to your old instance, you can preserve your existing DNS setup by moving the static IP to the new instance:

1. **Detach the static IP** from your old Bitnami instance in the Lightsail console.

1. **Attach the static IP** to your new Lightsail instance. Since your DNS records already point to this IP, no DNS changes are needed and there will be no propagation delay.

**Note**  
If your application uses a custom domain but you did not previously have a static IP attached, attach a new static IP to your new instance first, then update your DNS records to point your domain to the new static IP address. Allow time for DNS propagation before decommissioning the old instance.

## Step 7: Regenerate SSL/TLS certificates (if applicable)
<a name="migrate-bitnami-step7-ssl-tls"></a>

The SSL/TLS certificates from your old instance cannot be transferred to the new instance. You must regenerate them on the new instance. For WordPress, refer to [Enable HTTPS with guided workflow](amazon-lightsail-enabling-https-on-wordpress.md).

## Step 8: Delete the old instance
<a name="migrate-bitnami-step8-decommission"></a>

Once you have verified the migration is successful and DNS has fully propagated:

1. Take a final [snapshot of the old instance](lightsail-how-to-create-a-snapshot-of-your-instance.md) for backup.

1. Delete the old instance to stop incurring charges.