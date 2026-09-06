

# Migrate from WordPress by Bitnami to WordPress by Lightsail
<a name="migrate-your-wordpress-blog-from-bitnami-to-amazon-lightsail"></a>

If you're running on a WordPress blueprint provided by Bitnami and want to move to a WordPress blueprint provided by Lightsail, this tutorial walks you through the migration process.

Lightsail now offers WordPress blueprints that don't rely on Bitnami packaging. Migrating to these WordPress blueprints provides you with simplified updates, Instance Metadata Service Version 2 (IMDSv2) enforced by default, and the same affordable pricing plans starting at $5 USD per month.

Creating a Lightsail WordPress instance only takes a few minutes. Follow this tutorial to back up your existing WordPress blog and import it to a new instance running in Lightsail.

## Prerequisites
<a name="migrate-wordpress-blog-from-bitnami-prerequisites"></a>

Ensure that Bitnami is your blueprint vendor on your instance management page:

![WordPress blueprint vendor on the instance management page](http://docs.aws.amazon.com/lightsail/latest/userguide/images/wordpress/wordpress-blueprint-vendor-bitnami.png)


## Step 1: Back up your existing WordPress blog
<a name="migrate-wordpress-blog-back-up-wordpress-blog"></a>

You can use WordPress to back up your existing blog. You will just need to be able to log into the WordPress admin console and manage your blog.

1. Navigate to your blog, and then choose **Manage**.

   If the **Manage** banner is not shown, you can reach the sign in page by browsing to `http://{{<PublicIP>}}/wp-login.php`. Replace `{{<PublicIP>}}` with the public IP address of your instance.

1. Enter your user name and password to log into the WordPress admin console.

1. On the WordPress **Dashboard**, choose **Tools**, and then choose **Export**.

1. On the **Export** page, choose **All content** to export everything as an XML file.  
![Export your WordPress blog using the export tools](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-wordpress-blog-export-file.png)

1. Choose **Download export file** to download your old blog as an XML file.

   Save the XML file in a location that's easy to find. You will need it in Step 4.

## Step 2: Create a new WordPress instance in Lightsail
<a name="migrate-wordpress-blog-create-new-wordpress-blog-in-lightsail"></a>

You can create a new WordPress instance in Lightsail in just a few minutes. Here's how:

1. Go to the [Lightsail home page](https://lightsail.aws.amazon.com/) and log in.

1. Choose **Create instance**.

1. Select the AWS Region where you'd like to create your blog.

   You can choose the default Availability Zone or change that once you select an AWS Region.

1. Select a **WordPress** blueprint.  
![Pick WordPress as your Lightsail instance image](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-pick-your-instance-image.png)

1. Select **Lightsail** as the **Blueprint provider**.

1. Choose your instance plan (or *bundle*).

   You can upgrade your Lightsail plan later if needed. For more information, see [Create an instance from a snapshot in Lightsail](lightsail-how-to-create-instance-from-snapshot.md).

1. Enter a name for your instance.

   Resource names:
   + Must be unique within each AWS Region in your Lightsail account.
   + Must contain 2–255 characters.
   + Must start and end with an alphanumeric character.
   + Can include alphanumeric characters, periods, dashes, and underscores.

1. (Optional) Choose **Add new tag** to add a tag to your instance. Repeat this step as needed to add additional tags. For more information on tag usage, see [Tags](amazon-lightsail-tags.md).

   1. For **Key**, enter a tag key.  
![A tag with only the tag key specified in the Lightsail create instance workflow.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instance-key-name-only-tags.png)

   1. (Optional) For **Value**, enter a tag value.  
![A tag with the tag key and tag value specified in the Lightsail create instance workflow.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instance-key-name-and-value-tags.png)

1. Choose **Create instance**.

## Step 3: Log into your new Lightsail WordPress blog
<a name="migrate-wordpress-blog-log-into-wordpress-lightsail"></a>

Now that you have a new blog in Lightsail, you will need to access the WordPress Dashboard to import your old blog data. The default password to sign in to the administration dashboard of your WordPress website is stored on the instance. Complete the following steps to get the password.

**To get the default password for the WordPress administrator**

1. Open the instance management page for your WordPress instance.

1. On the **WordPress** panel, choose **Retrieve default password**. This expands **Access default password** at the bottom of the page.  
![Accessing WordPress admin password in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/wordpress/wordpress-lightsail-retrieve-password.png)

1. Choose **Launch CloudShell**. This opens a panel at the bottom of the page.

1. Choose **Copy** and then paste the contents into the CloudShell window. You can either put your cursor at the CloudShell prompt and press Ctrl\+V, or you can right-click to open the menu and then choose **Paste**.

1. Make a note of the password displayed in the CloudShell window. You need this to sign in to the administration dashboard of your WordPress website.  
![Viewing WordPress admin password in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/wordpress/amazon-wordpress-lightsail-viewing-admin-password.png)

Now that you have the password for the administration dashboard of your WordPress website, you can sign in. In the administration dashboard, you can change your user password, install plugins, change the theme of your website, and more.

Complete the following steps to sign in to the administration dashboard of your WordPress website.

**To sign in to the administration dashboard**

1. Open the instance management page for your WordPress instance.

1. On the **WordPress** panel, choose **Access WordPress Admin**.

1. On the **Access your WordPress Admin Dashboard** panel, under **Use public IP address**, choose the link with this format:

   http://{{public-ipv4-address}}./wp-admin

1. For **Username or Email Address**, enter **user**.

1. For **Password**, enter the password obtained in the previous step.

1. Choose **Log in**.  
![Launching and configuring WordPress in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-wordpress-tutorial-07.png)

   You are now signed in to the administration dashboard of your WordPress website where you can perform administrative actions. For more information about administering your WordPress website, see the [WordPress Codex](https://codex.wordpress.org/) in the WordPress documentation.  
![Launching and configuring WordPress in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-wordpress-tutorial-08.png)

## Step 4: Import your XML file into your new Lightsail blog
<a name="migrate-wordpress-blog-in-wordpress"></a>

Once you have successfully logged into the WordPress Dashboard on your new Lightsail instance, follow these steps to import the XML file into your new Lightsail blog.

1. From the WordPress **Dashboard** on your new Lightsail instance, choose **Tools**.

1. Choose **Import**, and then choose **Install Now** to install the WordPress import tool.  
![Install the Import tool in the WordPress Dashboard](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-wordpress-dashboard-install-import-tool.png)

1. Once the tool is done installing, choose **Run Importer** to run the import tool.

1. On the **Import WordPress** page, choose **Browse**.

1. Find the XML file you saved in *Step 1: Back up your existing WordPress blog*, and then choose **Open**.

1. Choose **Upload file and import**.

   Accept the rest of the defaults, and then choose **Submit**.

## Step 5: Attach a static IP address
<a name="migrate-wordpress-blog-static-ip"></a>

The default public IP address attached to your instance changes every time you stop and start the instance. Create a static IP address and attach it to your instance to keep a consistent address for your domain.

For instructions, see [Create a static IP and attach it to an instance](lightsail-create-static-ip.md).

## Step 6: Enable HTTPS on your WordPress instance
<a name="migrate-wordpress-blog-enable-https"></a>

After attaching a static IP and pointing your domain to it, enable HTTPS to secure your WordPress site with an SSL/TLS certificate.

For instructions, see [Enable HTTPS on your WordPress instance](amazon-lightsail-enabling-https-on-wordpress.md).

## Next steps
<a name="migrate-bitnami-wordpress-lightsail-next-steps"></a>

You can verify that everything worked by choosing your blog (next to the Home icon), and then choosing **Visit Site** from the WordPress dashboard. You can also type the IP address into a browser and view the blog.

Here are some next steps:
+  [Configure automatic snapshots for your new Lightsail instance](amazon-lightsail-configuring-automatic-snapshots.md) 
+ Customize your new blog's appearance and/or install some WordPress plugins
+  [Delete the old instance running WordPress by Bitnami](delete-an-amazon-lightsail-instance.md) to save on future charges 
+  [Delete any old snapshots](amazon-lightsail-deleting-snapshots.md) associated with your old instance to save on future charges 