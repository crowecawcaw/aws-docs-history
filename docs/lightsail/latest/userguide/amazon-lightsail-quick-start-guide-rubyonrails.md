

# Set up Ruby on Rails on Lightsail
<a name="amazon-lightsail-quick-start-guide-rubyonrails"></a>

**Did you know?**  
 Lightsail stores seven daily snapshots and automatically replaces the oldest with the newest when you enable automatic snapshots for your instance. For more information, see [ Configure automatic snapshots for Lightsail instances and disks ](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots.html) . 

Here are a few steps you should take to get started after your Ruby on Rails instance is up and running on Amazon Lightsail:

## Step 1: Attach a static IP address to your Ruby on Rails instance
<a name="amazon-lightsail-ruby-on-rails-attach-static-ip"></a>

The default dynamic public IP address attached to your instance changes every time you stop and start the instance. You can create a static IP address and attach it to your instance to keep the public IP address from changing. Later, when you use your domain name with your instance, you don’t have to update your domain’s DNS records each time you stop and start the instance. You can attach only one static IP address to each instance.

On the instance management page, under the **Networking** tab, choose **Create a static IP** or **Attach static IP** (if you previously created a static IP that you can attach to your instance), then follow the instructions on the page. For more information, see [Create a static IP and attach it to an instance](lightsail-create-static-ip.md).

![Attach static IP address in the Lightsail console](http://docs.aws.amazon.com/lightsail/latest/userguide/images/quick-start-static-ip-address.png)


## Step 2: Visit your Ruby on Rails instance welcome page
<a name="amazon-lightsail-ruby-on-rails-visit-welcome-page"></a>

Navigate to the static IP address of your instance to access the application installed on it.

1. On your instance management page, under the **Connect** tab, make note of the static IP.

1. Browse to the static IP address, for example `http://192.0.0.1:3000`.

For more information, see [Ruby on Rails Guides](https://guides.rubyonrails.org/).

## Step 3: Deploy your application
<a name="amazon-lightsail-ruby-on-rails-deploy-application"></a>

1. Follow the instructions from [Transfer files securely to Lightsail Linux instances with SFTP](amazon-lightsail-connecting-to-linux-unix-instance-using-sftp.md) to copy your application to `/home/ec2-user/my_app`

1. On your instance management page, under the **Connect** tab, choose **Connect using SSH**.

1. Run `sudo systemctl restart rails-server`

1. Navigate to your instance's static IP address

## Step 4: Create a snapshot of your Ruby on Rails instance
<a name="amazon-lightsail-ruby-on-rails-create-snapshot"></a>

After you configure your website the way you want it, create periodic snapshots of your instance to back it up. A snapshot is a copy of the system disk and original configuration of an instance. A snapshot contains all of the data that is needed to restore your instance (from the moment when the snapshot was taken).

You can create [snapshots manually](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-snapshots-in-amazon-lightsail.html#manual-snapshots), or [enable automatic snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-snapshots-in-amazon-lightsail.html#automatic-snapshots) to have Lightsail create daily snapshots for you. If something goes wrong with your instance, you can create a new replacement instance using the snapshot.

You can work with snapshots on your instance's management page on the **Snapshots** tab. For more information, see [Snapshots in Amazon Lightsail](understanding-snapshots-in-amazon-lightsail.md).

![Create an instance snapshot in the Lightsail console](http://docs.aws.amazon.com/lightsail/latest/userguide/images/quick-start-instance-snapshots.png)
