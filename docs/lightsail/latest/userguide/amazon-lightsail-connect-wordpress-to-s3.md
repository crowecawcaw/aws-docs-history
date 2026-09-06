

# Connect a WordPress website on Lightsail to Amazon S3 with WP Offload Media
<a name="amazon-lightsail-connect-wordpress-to-s3"></a>

This tutorial describes the steps required to connect your WordPress website running on an Amazon Lightsail instance to an Amazon Simple Storage Service (Amazon S3) bucket to store website images and attachments. To do this, you configure a WordPress plugin with a set of Amazon Web Services (AWS) account credentials. The plugin then creates the Amazon S3 bucket for you and configures your website to use the bucket instead of the instance's disk for website images and attachments.

**Topics**
+ [Step 1: Complete the prerequisites](#connect-wordpress-s3-prerequisites)
+ [Step 2: Install the WP Offload Media plugin on your WordPress website](#install-wp-offload-media-wordpress)
+ [Step 3: Create an IAM policy](#create-iam-policy-wordpress-s3)
+ [Step 4: Create an IAM user](#create-iam-user-wordpress-s3)
+ [Step 5: Create an access key for your IAM user](#create-access-key-wordpress-s3)
+ [Step 6: Edit the WordPress configuration file](#edit-wp-config-file-s3)
+ [Step 7: Create the Amazon S3 bucket using the WP Offload Media plugin](#create-s3-bucket-wordpress)
+ [Step 8: Next steps](#connect-wordpress-s3-next-steps)

## Step 1: Complete the prerequisites
<a name="connect-wordpress-s3-prerequisites"></a>

Before you get started, create a WordPress instance in Lightsail, and make sure it's in a running state. For more information, see [Launch and configure a WordPress instance](amazon-lightsail-launch-and-configure-wordpress.md).

## Step 2: Install the WP Offload Media plugin on your WordPress website
<a name="install-wp-offload-media-wordpress"></a>

You must use a plugin to configure your website to use an Amazon S3 bucket. Many plugins are available to configure this; one such plugin is [WP Offload Media Lite](https://wordpress.org/plugins/amazon-s3-and-cloudfront/).

**To install the WP Offload Media plugin on your WordPress website**

1. Sign in to your WordPress dashboard as an administrator.

   For more information, see [Launch and configure a WordPress instance](amazon-lightsail-launch-and-configure-wordpress.md).

1. Hover over **Plugins** in the left navigation menu, and choose **Add New**.

1. Search for **WP Offload Media Lite**.

1. In the search results, choose **Install Now** next to the **WP Offload Media** plugin.

1. Choose **Activate** after the plugin is done installing.

1. In the left navigation menu, choose **Settings**, then choose **Offload Media**.

1. In the **Offload Media** page, choose **Amazon S3** as the storage provider, then choose **Define access keys in wp-config.php**.

   With this option, you must add your AWS account credentials to the `wp-config.php` on the instance. These steps are covered later in this tutorial.

   Leave the **Offload Media** page open; you will return to it later in this tutorial. Continue to the [Step 3: Create an IAM policy](#create-iam-policy-wordpress-s3) section of this tutorial.

## Step 3: Create an IAM policy
<a name="create-iam-policy-wordpress-s3"></a>

**Warning**  
This scenario requires IAM users with programmatic access and long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed. Access keys can be updated if necessary. For more information, see [Update access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id-credentials-access-keys-update.html) in the *IAM User Guide*.

The WP Offload Media plugin requires access to your AWS account to create the Amazon S3 bucket, and to upload your website images and attachments.

**To create a new AWS Identity and Access Management (IAM) policy for the WP Offload Media plugin**

1. Open a new browser tab, and sign in to the [IAM console](https://console.aws.amazon.com/iam/).

1. In the left navigation menu, under **Access management**, choose **Policies**.

1. Choose **Create policy**.

1. On the **Create policy** page, choose **JSON**, then remove all of the content within the policy editor.

1. Specify the following content in the policy editor, replacing the example bucket name of {{amzn-s3-demo-bucket}} with your own:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "s3:*",
               "Resource": [
                   "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*",
                   "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
               ]
           }
       ]
   }
   ```

------

1. Choose **Next**.

1. For **Policy name**, enter a name for the policy.
**Tip**  
Specify a descriptive name, such as **wp\_s3\_user\_policy** or **wp\_offload\_media\_plugin\_user\_policy**, so that you can easily identify it in the future when performing maintenance.

1. Choose **Create policy**.

   Keep the IAM console open for the next step.

## Step 4: Create an IAM user
<a name="create-iam-user-wordpress-s3"></a>

Create a new IAM user and attach the previously created policy to grant the required permissions to use the WP Offload Media plugin.

**To create a new AWS Identity and Access Management (IAM) user for the WP Offload Media plugin**

1. If necessary, open the [IAM console](https://console.aws.amazon.com/iam/).

1. In the left navigation menu, under **Access management**, choose **Users**.

1. Choose **Create user**.

1. For **User name**, enter a name for the new user, then choose **Next**.
**Tip**  
Specify a descriptive name, such as **wp\_s3\_user** or **wp\_offload\_media\_plugin\_user**, so that you can easily identify it in the future when performing maintenance.

1. Choose **Attach policies directly**.

1. Under **Permissions policies**, enter the name of the policy you created previously in the search bar.

1. Select the policy, then choose **Next**.

1. Choose **Create user**.

   Keep the IAM console open for the next step.

## Step 5: Create an access key for your IAM user
<a name="create-access-key-wordpress-s3"></a>

Create an access key for the IAM user which will be used by the WP Offload Media plugin.

**To create an access key for the WP Offload Media plugin IAM user**

1. If necessary, open the [IAM console](https://console.aws.amazon.com/iam/).

1. In the left navigation menu, under **Access management**, choose **Users**.

1. Choose the user name to go to the user details page.

1. On **Security credentials** tab, in the **Access keys** section, choose **Create access key**.

1. Choose **Other**, then choose **Next**.

1. Choose **Create access key**.

1. Make note of the **access key ID** and **secret access key** for the IAM user. You can also choose **Download .csv** to save a copy of these values to your local drive. You will need these in the next few steps when editing the `wp-config.php` file on the WordPress instance.

   You can now close the IAM console and continue on the Lightsail console with the next step.

## Step 6: Edit the WordPress configuration file
<a name="edit-wp-config-file-s3"></a>

The `wp-config.php` file contains your website's base configuration details, such as database connection information.

**To edit the `wp-config.php` file in your WordPress instance**

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. Choose the browser-based SSH client icon for the WordPress instance.
**Note**  
You can also connect to your instance using your own SSH client. For more information, see [Download and set up PuTTY to connect using SSH in Lightsail](lightsail-how-to-set-up-putty-to-connect-using-ssh.md).

1. In the SSH client window that appears, enter the following command to create a backup of the `wp-config.php` file in case something goes wrong:

   ```
   sudo cp /var/www/wp-config.php /var/www/wp-config.php.backup
   ```

1. Enter the following command to open the `wp-config.php` file using `nano`, a text editor:

   ```
   nano /var/www/wp-config.php
   ```

1. Enter the following text above the `/* That's all, stop editing! Happy blogging. */` text.

   Be sure to replace {{AccessKeyID}} with the access key ID and {{SecretAccessKey}} with the secret access key of the IAM user you created earlier in these steps.

   ```
   define( 'AS3CF_SETTINGS', serialize( array(
       'provider' => 'aws',
       'access-key-id' => '{{AccessKeyID}}',
       'secret-access-key' => '{{SecretAccessKey}}',
   ) ) );
   ```

   Example:

   ```
   define( 'AS3CF_SETTINGS', serialize( array(
       'provider' => 'aws',
       'access-key-id' => '{{AKIAIOSFODNN7EXAMPLE}}',
       'secret-access-key' => '{{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}',
   ) ) );
   ```

1. Press **Ctrl\+X** to exit Nano, then press **Y**, and **Enter** to save your edits to the `wp-config.php` file.

1. Enter the following command to restart the services on the instance:

   ```
   sudo systemctl restart apache2
   ```

   Close the SSH window and toggle back to the **Offload Media** page that you left open earlier in this tutorial. You are now ready to [create the Amazon S3 bucket using the WP Offload Media plugin](#create-s3-bucket-wordpress).

## Step 7: Create the Amazon S3 bucket using the WP Offload Media plugin
<a name="create-s3-bucket-wordpress"></a>

Now that the `wp-config.php` file is configured with the AWS credentials, you can return to the **Offload Media** page to complete the process.

**To create the Amazon S3 bucket using the WP Offload Media plugin**

1. Refresh the **Offload Media** page, or choose **Next**.

   You should now see that the Amazon S3 provider is configured.

1. Choose **Create new bucket**.

1. In the **Region** drop-down menu, choose the desired AWS Region. We recommend that you choose the same region in which your WordPress instance is located.

1. In the **Bucket** text box, enter a name for the new S3 bucket.

1. Choose **Create New Bucket**.

   The page refreshes to confirm that a new bucket was created. Review the settings that appear and adjust them accordingly to how you want your WordPress website to behave.

   From now on, images and attachments added to blog posts are automatically uploaded to the Amazon S3 bucket that you created.

## Step 8: Next steps
<a name="connect-wordpress-s3-next-steps"></a>

After you're done connecting your WordPress website to an Amazon S3 bucket, you should create a snapshot of your WordPress instance to back up the changes you made. For more information, see [Create a snapshot of your Linux or Unix instance](lightsail-how-to-create-a-snapshot-of-your-instance.md).