# Set up Ruby on Rails on

Lightsail

###### Did you know?

Lightsail stores seven daily snapshots and automatically replaces the oldest with the newest when you enable
automatic snapshots for your instance. For more information, see
[Configure automatic snapshots for Lightsail instances and disks](amazon-lightsail-configuring-automatic-snapshots.md "amazon-lightsail-configuring-automatic-snapshots.md")
.

Here are a few steps you should take to get started after your Ruby on Rails instance is up and
running on Amazon Lightsail:

## Step 1: Attach a static IP address

to your Ruby on Rails instance

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

## Step 2: Visit your Ruby on Rails

instance welcome page

Navigate to the static IP address of your instance to access the application installed on it.

1. On your instance management page, under the **Connect** tab, make
   note of the static IP.
2. Browse to the static IP address, for example `http://192.0.0.1:3000`.

For more information, see [Ruby on Rails Guides](https://guides.rubyonrails.org/ "https://guides.rubyonrails.org/").

## Step 3: Deploy your

application

1. Follow the instructions from [Transfer files securely to Lightsail Linux instances with SFTP](amazon-lightsail-connecting-to-linux-unix-instance-using-sftp.md "amazon-lightsail-connecting-to-linux-unix-instance-using-sftp.md") to copy your application to `/home/ec2-user/my_app`
2. On your instance management page, under the **Connect** tab, choose
   **Connect using SSH**.
3. Run `sudo systemctl restart rails-server`
4. Navigate to your instance's static IP address

## Step 4: Create a snapshot of your

Ruby on Rails instance

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
