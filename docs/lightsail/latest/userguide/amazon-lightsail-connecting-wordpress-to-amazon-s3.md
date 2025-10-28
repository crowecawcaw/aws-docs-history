# Connect a WordPress website

on Lightsail to Amazon S3 with WP Offload Media

This tutorial describes the steps required to connect your WordPress website running on an
Amazon Lightsail instance to an Amazon Simple Storage Service (Amazon S3) bucket to store website images and attachments.
To do this, you configure a WordPress plugin with a set of Amazon Web Services (AWS) account
credentials. The plugin then creates the Amazon S3 bucket for you and configures your website to use
the bucket instead of the instance’s disk for website images and attachments.

###### Topics

- [Step 1: Complete the
  prerequisites](#connect-wordpress-to-s3-prerequisites "#connect-wordpress-to-s3-prerequisites")
- [Step 2: Install the WP Offload Media
  plugin on your WordPress website](#install-wp-offload-media-on-wordpress "#install-wp-offload-media-on-wordpress")
- [Step 3: Create an IAM
  policy](#create-iam-policy-for-wordpress "#create-iam-policy-for-wordpress")
- [Step 4: Create an IAM
  user](#create-iam-user-for-wordpress "#create-iam-user-for-wordpress")
- [Step 5: Create an access key for your IAM
  user](#create-access-key-for-wordpress "#create-access-key-for-wordpress")
- [Step 6: Edit the WordPress
  configuration file](#edit-the-wp-config-file-for-s3-bucket "#edit-the-wp-config-file-for-s3-bucket")
- [Step 7: Create the Amazon S3 bucket using the WP
  Offload Media plugin](#create-the-amazon-s3-bucket "#create-the-amazon-s3-bucket")
- [Step 8: Next steps](#connect-wordpress-to-s3-prerequisites-next-steps "#connect-wordpress-to-s3-prerequisites-next-steps")

## Step 1: Complete the

prerequisites

Before you get started, create a WordPress instance in Lightsail, and make sure it’s in
a running state. For more information, see [Tutorial: Launch and
configure a WordPress instance](amazon-lightsail-tutorial-launching-and-configuring-wordpress.md "amazon-lightsail-tutorial-launching-and-configuring-wordpress.md").

## Step 2: Install the WP Offload Media

plugin on your WordPress website

You must use a plugin to configure your website to use an Amazon S3 bucket. Many plugins are
available to configure this; one such plugin is [WP Offload Media
Lite](https://wordpress.org/plugins/amazon-s3-and-cloudfront/ "https://wordpress.org/plugins/amazon-s3-and-cloudfront/").

###### To install the WP Offload Media plugin on your WordPress

website

1. Sign in to your WordPress dashboard as an administrator.

For more information, see [Getting the
application user name and password for your Bitnami instance in
Amazon Lightsail](log-in-to-your-bitnami-application-running-on-amazon-lightsail.md "log-in-to-your-bitnami-application-running-on-amazon-lightsail.md"). 2. Hover over **Plugins** in the left navigation menu, and choose
**Add New**.

![Add new plugin menu item in the WordPress dashboard.](images/amazon-lightsail-wordpress-add-new-plugin-menu.png) 3. Search for **WP Offload Media Lite**. 4. In the search results, choose **Install Now** next to the
**WP Offload Media** plugin.

![WP Offload Media Lite plugin for WordPress.](images/amazon-lightsail-wp-offload-media-plugin.png) 5. Choose **Activate** after the plugin is done installing. 6. In the left navigation menu, choose **Settings**, then choose
**Offload Media**.

![Wordpress dashboard settings.](images/amazon-lightsail-offload-media-menu.png) 7. In the **Offload Media** page, choose **Amazon S3** as
the storage provider, then choose **Define access keys in
wp-config.php**.

With this option, you must add your AWS account credentials to the
`wp-config.php` on the instance. These steps are covered later in
this tutorial.

![WP Offload Media page.](images/amazon-lightsail-offload-media-configuration.png)

Leave the **Offload Media** page open; you will return to it later in
this tutorial. Continue to the [Step 3: Create an IAM
policy](#create-iam-policy-for-wordpress "#create-iam-policy-for-wordpress") section of this tutorial.

## Step 3: Create an IAM

policy

###### Warning

This scenario requires IAM users with programmatic access and long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed. Access keys can be updated if necessary. For more information, see [Update access keys](../../../IAM/latest/UserGuide/id-credentials-access-keys-update.md "../../../IAM/latest/UserGuide/id-credentials-access-keys-update.md") in the _IAM User Guide_.

The WP Offload Media plugin requires access to your AWS account to create the Amazon S3
bucket, and to upload your website images and attachments.

###### To create a new AWS Identity and Access Management (IAM) policy for the WP Offload

Media plugin

1. Open a new browser tab, and sign in to the [IAM
   console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation menu, under **Access management**, choose
   **Policies**.
3. Choose **Create policy**.
4. On the **Create policy** page, choose **JSON**, then
   remove all of the content within the policy editor.
5. Specify the following content in the policy editor, replacing the example bucket name
   of `amzn-s3-demo-bucket` with your own:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
 "arn:aws:s3:::`amzn-s3-demo-bucket`"
 ]
 }
 ]
}`

```

6. Choose **Next**.
7. For **Policy name**, enter a name for the policy.

###### Tip

Specify a descriptive name, such as `wp_s3_user_policy` or
`wp_offload_media_plugin_user_policy`, so that you can easily
identify it in the future when performing maintenance. 8. Choose **Create policy**.

Keep the IAM console open for the next step.

## Step 4: Create an IAM

user

Create a new IAM user and attach the previously created policy to grant the required permissions to use the WP Offload Media plugin.

###### To create a new AWS Identity and Access Management (IAM) user for the WP

Offload Media plugin

1. If necessary, open the [IAM
   console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation menu, under **Access management**, choose
   **Users**.
3. Choose **Create user**.
4. For **User name**, enter a name for the new user, then choose
   **Next**.

###### Tip

Specify a descriptive name, such as `wp_s3_user` or
`wp_offload_media_plugin_user`, so that you can easily identify
it in the future when performing maintenance. 5. Choose **Attach policies directly**. 6. Under **Permissions policies**, enter the name of the policy you
created previously in the search bar. 7. Select the policy, then choose **Next**. 8. Choose **Create user**.

Keep the IAM console open for the next step.

## Step 5: Create an access key for your IAM

user

Create an access key for the IAM user which will be used by the WP
Offload Media plugin.

###### To create a new AWS Identity and Access Management (IAM) user for the WP

Offload Media plugin

1. If necessary, open the [IAM
   console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation menu, under **Access management**, choose
   **Users**.
3. Choose the user name to go to the user details page.
4. On **Security credentials** tab, in the **Access
   keys** section, choose **Create access key**.
5. Choose **Other**, then choose **Next**.
6. Choose **Create access key**.
7. Make note of the **access key ID** and **secret access
   key** for the IAM user. You can also choose **Download
   .csv** to save a copy of these values to your local drive. You will need these
   in the next few steps when editing the `wp-config.php` file on the
   WordPress instance.

You can now close the IAM console and continue on the Lightsail console with the
next step.

## Step 6: Edit the WordPress

configuration file

The `wp-config.php` file contains your website’s base configuration
details, such as database connection information.

###### To edit the `wp-config.php`

file in your WordPress instance

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/ "https://lightsail.aws.amazon.com/").
2. Choose the browser-based SSH client icon for the WordPress instance.

![The browser-based SSH client icon in the Lightsail console.](images/amazon-lightsail-wordpress-browser-based-ssh-client.png)

###### Note

You can also connect to your instance using your own SSH client. For more
information, see [Download and set up PuTTY to connect using SSH in Lightsail](lightsail-how-to-set-up-putty-to-connect-using-ssh.md "lightsail-how-to-set-up-putty-to-connect-using-ssh.md"). 3. In the SSH client window that appears, enter the following command to create a backup
of the `wp-config.php` file in case something goes wrong:

```
sudo cp /opt/bitnami/wordpress/wp-config.php /opt/bitnami/wordpress/wp-config.php.backup
```

4. Enter the following command to open the `wp-config.php` file using
   `nano`, a text editor:

```
nano /opt/bitnami/wordpress/wp-config.php
```

5. Enter the following text above the `/* That's all, stop editing! Happy blogging.
*/` text.

Be sure to replace `AccessKeyID` with the access key ID and
`SecretAccessKey` with the secret access key of the IAM user
you created earlier in these steps.

```
define( 'AS3CF_SETTINGS', serialize( array(
    'provider' => 'aws',
    'access-key-id' => '`AccessKeyID`',
    'secret-access-key' => '`SecretAccessKey`',
) ) );
```

Example:

```
define( 'AS3CF_SETTINGS', serialize( array(
    'provider' => 'aws',
    'access-key-id' => '`AKIAIOSFODNN7EXAMPLE`',
    'secret-access-key' => '`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`',
) ) );
```

The result should look like the following example:

![AWS account credentials in the wp-config.php file.](images/amazon-lightsail-ssh-wp-config-s3-bucket.png) 6. Press `Ctrl+X` to exit Nano, then press `Y`,
and `Enter` to save your edits to the
`wp-config.php` file. 7. Enter the following command to restart the services on the instance:

```
sudo /opt/bitnami/ctlscript.sh restart
```

You will see a result similar to the following when the services have
restarted:

![Restarting the services on the instance.](images/amazon-lightsail-ssh-restart-services-bitnami.png)

Close the SSH window and toggle back to the **Offload Media** page
that you left open earlier in this tutorial. You are now ready to [create the Amazon S3 bucket using the WP
Offload Media plugin](#create-the-amazon-s3-bucket "#create-the-amazon-s3-bucket").

## Step 7: Create the Amazon S3 bucket using the WP

Offload Media plugin

Now that the `wp-config.php` file is configured with the AWS
credentials, you can return to the **Offload Media** page to complete the
process.

###### To create the Amazon S3 bucket using the WP Offload Media

plugin

1. Refresh the **Offload Media** page, or choose
   **Next**.

You should now see that the Amazon S3 provider is configured. 2. Choose **Create new bucket**.

![Creating a new Amazon S3 bucket using the WP Offload Media plugin.](images/amazon-lightsail-offload-media-create-new-bucket.png) 3. In the **Region** drop-down menu, choose the desired AWS Region. We
recommend that you choose the same region in which your WordPress instance is
located. 4. In the **Bucket** text box, enter a name for the new S3
bucket.

![Configuring the new Amazon S3 bucket using the WP Offload Media plugin.](images/amazon-lightsail-offload-media-bucket-configuration.png) 5. Choose **Create New Bucket**.

The page refreshes to confirm that a new bucket was created. Review the settings that
appear and adjust them accordingly to how you want your WordPress website to
behave.

![WP Offload Media plugin settings.](images/amazon-lightsail-offload-media-settings-saved.png)

From now on, images and attachments added to blog posts are automatically uploaded to
the Amazon S3 bucket that you created.

## Step 8: Next steps

After you’re done connecting your WordPress website to an Amazon S3 bucket, you should create a
snapshot of your WordPress instance to back up the changes you made. For more information, see
[Create a snapshot of
your Linux or Unix instance](lightsail-how-to-create-a-snapshot-of-your-instance.md "lightsail-how-to-create-a-snapshot-of-your-instance.md").
