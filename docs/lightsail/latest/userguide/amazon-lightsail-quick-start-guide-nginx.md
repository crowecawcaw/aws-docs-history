

# Deploy and manage an Nginx web server on Lightsail
<a name="amazon-lightsail-quick-start-guide-nginx"></a>

**Did you know?**  
 Lightsail stores seven daily snapshots and automatically replaces the oldest with the newest when you enable automatic snapshots for your instance. For more information, see [ Configure automatic snapshots for Lightsail instances and disks ](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots.html) . 

 Here are a few steps you should take to get started after your Nginx instance is up and running on Amazon Lightsail. Before you get started, identify your blueprint vendor on your instance management page: 

![Nginx blueprint vendor on the instance management page](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/headers/nginx-blueprint-vendor.png)


Select the appropriate guide for your Nginx instance:

------
#### [ Lightsail ]

You need the default application password to access pre-installed applications or services on your instance.

1. On your instance management page, under the **Connect** tab, choose **Connect using SSH**.

1. After you're connected, enter the following command to get the default application password:

   ```
   cat ~/application_credentials
   ```

   You should see a response similar to this, which contains the default application password:  
![Default application password.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-application-password.png)

The default dynamic public IP address attached to your instance changes every time you stop and start the instance. You can create a static IP address and attach it to your instance to keep the public IP address from changing. Later, when you use your domain name with your instance, you don’t have to update your domain’s DNS records each time you stop and start the instance. You can attach only one static IP address to each instance.

On the instance management page, under the **Networking** tab, choose **Create a static IP** or **Attach static IP** (if you previously created a static IP that you can attach to your instance), then follow the instructions on the page. For more information, see [Create a static IP and attach it to an instance](lightsail-create-static-ip.md).

![Attach static IP address in the Lightsail console](http://docs.aws.amazon.com/lightsail/latest/userguide/images/quick-start-static-ip-address.png)


Navigate to the static IP address of your instance to access the application installed on your instance.

1. On your instance management page, copy the static IP address:  
![Copy static IP](http://docs.aws.amazon.com/lightsail/latest/userguide/images/instances/headers/nginx-copy-static-ip.png)

1. Paste the static IP address into your browser address, for example `http://192.0.0.1`.

For more information, see the [Nginx admin guide](https://docs.nginx.com/nginx/admin-guide/).

To map your domain name, such as `example.com`, to your instance, you add a record to the domain name system (DNS) of your domain. DNS records are typically managed and hosted at the registrar where you registered your domain. However, we recommend that you transfer management of your domain's DNS records to Lightsail so that you can administer it using the Lightsail console.

On the Lightsail console home page, under the **Networking** tab, choose **Create DNS zone**, then follow the instructions on the page.

For more information, see [Create a DNS zone to manage your domain’s DNS records](lightsail-how-to-create-dns-entry.md).

For enabling HTTPS, see [Secure your Lightsail Nginx website with Let's Encrypt SSL/TLS](amazon-lightsail-using-lets-encrypt-certificates-with-nginx.md).

1. Follow the instructions from [ Transfer files between Linux instances on Lightsail using scp ](amazon-lightsail-transfer-files-between-linux-instances.md) to copy your application to `/usr/share/nginx/html` 

1. On your instance management page, under the **Connect** tab, choose **Connect using SSH**.

1. Run `sudo systemctl restart nginx`

1. Navigate to your instance's static IP address

After you configure your website the way you want it, create periodic snapshots of your instance to back it up. A snapshot is a copy of the system disk and original configuration of an instance. A snapshot contains all of the data that is needed to restore your instance (from the moment when the snapshot was taken).

You can create [snapshots manually](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-snapshots-in-amazon-lightsail.html#manual-snapshots), or [enable automatic snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-snapshots-in-amazon-lightsail.html#automatic-snapshots) to have Lightsail create daily snapshots for you. If something goes wrong with your instance, you can create a new replacement instance using the snapshot.

You can work with snapshots on your instance's management page on the **Snapshots** tab. For more information, see [Snapshots in Amazon Lightsail](understanding-snapshots-in-amazon-lightsail.md).

![Create an instance snapshot in the Lightsail console](http://docs.aws.amazon.com/lightsail/latest/userguide/images/quick-start-instance-snapshots.png)


------
#### [ Bitnami ]

You need the default application password to access pre-installed applications or services on your instance.

1. On your instance management page, under the **Connect** tab, choose **Connect using SSH**.

1. After you're connected, enter the following command to get the default application password:

   ```
   cat bitnami_application_password
   ```
**Note**  
If you're in a directory other than the user home directory, then enter `cat $HOME/bitnami_application_password`.

   You should see a response similar to this, which contains the default application password:  
![Bitnami default application password.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-bitnami-application-password.png)

For more information, see [Getting the application user name and password for your Bitnami instance in Amazon Lightsail](log-in-to-your-bitnami-application-running-on-amazon-lightsail.md).

The default dynamic public IP address attached to your instance changes every time you stop and start the instance. You can create a static IP address and attach it to your instance to keep the public IP address from changing. Later, when you use your domain name with your instance, you don’t have to update your domain’s DNS records each time you stop and start the instance. You can attach only one static IP address to each instance.

On the instance management page, under the **Networking** tab, choose **Create a static IP** or **Attach static IP** (if you previously created a static IP that you can attach to your instance), then follow the instructions on the page. For more information, see [Create a static IP and attach it to an instance](lightsail-create-static-ip.md).

![Attach static IP address in the Lightsail console](http://docs.aws.amazon.com/lightsail/latest/userguide/images/quick-start-static-ip-address.png)


Navigate to the public IP address of your instance to access the application installed on it, access phpMyAdmin, or access the Bitnami documentation.

1. On your instance management page, under the **Connect** tab, make note of the public IP.

1. Browse to the public IP address, for example by going to `http://192.0.2.3`.

For more information, see [Getting the application user name and password for your Bitnami instance in Amazon Lightsail](log-in-to-your-bitnami-application-running-on-amazon-lightsail.md).

To map your domain name, such as `example.com`, to your instance, you add a record to the domain name system (DNS) of your domain. DNS records are typically managed and hosted at the registrar where you registered your domain. However, we recommend that you transfer management of your domain's DNS records to Lightsail so that you can administer it using the Lightsail console.

On the Lightsail console home page, under the **Networking** tab, choose **Create DNS zone**, then follow the instructions on the page.

For more information, see [Create a DNS zone to manage your domain’s DNS records](lightsail-how-to-create-dns-entry.md).

Read the Bitnami documentation to learn how to deploy your Nginx application, enable HTTPS support with SSL certificates, upload files to the server with SFTP, and more.

For more information, see the [Bitnami Nginx for AWS Cloud](https://docs.bitnami.com/general/infrastructure/nginx/).

After you configure your website the way you want it, create periodic snapshots of your instance to back it up. A snapshot is a copy of the system disk and original configuration of an instance. A snapshot contains all of the data that is needed to restore your instance (from the moment when the snapshot was taken).

You can create [snapshots manually](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-snapshots-in-amazon-lightsail.html#manual-snapshots), or [enable automatic snapshots](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-snapshots-in-amazon-lightsail.html#automatic-snapshots) to have Lightsail create daily snapshots for you. If something goes wrong with your instance, you can create a new replacement instance using the snapshot.

You can work with snapshots on your instance's management page on the **Snapshots** tab. For more information, see [Snapshots in Amazon Lightsail](understanding-snapshots-in-amazon-lightsail.md).

![Create an instance snapshot in the Lightsail console](http://docs.aws.amazon.com/lightsail/latest/userguide/images/quick-start-instance-snapshots.png)


------