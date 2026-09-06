

# Launch and configure a Windows Server 2016 instance on Lightsail
<a name="amazon-lightsail-tutorial-launching-and-configuring-windows-server-2016"></a>

Amazon Lightsail is the easiest way to get started with Amazon Web Services (AWS) if you just need virtual private servers. Lightsail includes everything you need to launch your project quickly – a virtual machine, SSD-based storage, data transfer, DNS management, and a static IP – for a low, predictable price.

This tutorial shows you how to launch and configure a Windows Server 2016 instance on Lightsail. It includes steps to connect to your instance via RDP, create a static IP and attach it to your instance, and create a DNS zone and map your domain. When you’re done with this tutorial, you have the fundamentals to get your instance up and running on Lightsail.

**Contents**
+ [Step 1: Sign up for AWS](#tutorial-launching-and-configuring-windows-server-2016-sign-up-for-aws)
+ [Step 2: Create a Windows Server 2016 instance](#create-a-windows-server-instance)
+ [Step 3: Connect to your Windows Server 2016 instance with RDP](#connecting-to-your-instance-via-rdp)
+ [Step 4: Create a static IP address and attach it to your Windows Server 2016 instance](#tutorial-launching-and-configuring-windows-server-2016-creating-a-lightsail-static-ip)
+ [Step 5: Create a DNS zone and map a domain to your Windows Server 2016 instance](#tutorial-launching-and-configuring-windows-server-2016-creating-a-lightsail-static-ip)
+ [Next steps](#tutorial-launching-and-configuring-windows-server-2016-next-steps)

## Step 1: Sign up for AWS
<a name="tutorial-launching-and-configuring-windows-server-2016-sign-up-for-aws"></a>

This tutorial requires an AWS account. [Sign up for AWS](https://console.aws.amazon.com/console/home), or [sign in to AWS](https://console.aws.amazon.com/console/home) if you already have an account.

## Step 2: Create a Windows Server 2016 instance in Lightsail
<a name="create-a-windows-server-instance"></a>

Get your Windows Server 2016 instance up and running in Lightsail. For more information, see [Get started with Windows Server-based instances](get-started-with-windows-based-instances-in-lightsail.md).

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. On the **Instances** section of the Lightsail home page, choose **Create instance**.  
![Launching and configuring a Windows Server 2016 instance in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lamp-tutorial-01.png)

1. Choose the AWS Region and Availability Zone for your instance.  
![Launching and configuring a Windows Server 2016 instance in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/create-instance-select-region-az.png)

1. Choose your instance image.

   1. Choose **Microsoft Windows** as the platform.

   1. Choose **OS Only**, then choose **Windows Server 2016** as the blueprint.  
![Launching and configuring a Windows Server 2016 instance in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-ws-tutorial-03.png)

1. Choose an instance plan.

   A plan includes a low, predictable cost, machine configuration (RAM, SSD, vCPU), and data transfer allowance. You can try the $9.50 USD Lightsail plan without charge for one month (up to 750 hours). AWS credits one free month to your account.
**Note**  
As part of the AWS Free Tier, you can get started with Amazon Lightsail for free. For more information, see the [AWS Free Tier FAQs](https://aws.amazon.com/free/free-tier-faqs/).

1. Enter a name for your instance.

   Resource names:
   + Must be unique within each AWS Region in your Lightsail account.
   + Must contain 2 to 255 characters.
   + Must start and end with an alphanumeric character or number.
   + Can include alphanumeric characters, numbers, periods, dashes, and underscores.  
![Launching and configuring a Windows Server 2016 instance in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-ws-tutorial-04.png)

1. (Optional) Choose **Add new tag** to add a tag to your instance. Repeat this step as needed to add additional tags. For more information on tag usage, see [Tags](amazon-lightsail-tags.md).

   1. For **Key**, enter a tag key.  
![A tag with only the tag key specified in the Lightsail create instance workflow.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instance-key-name-only-tags.png)

   1. (Optional) For **Value**, enter a tag value.  
![A tag with the tag key and tag value specified in the Lightsail create instance workflow.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-instance-key-name-and-value-tags.png)

1. Choose **Create instance**.

## Step 3: Connect to your Windows Server 2016 instance with RDP
<a name="connecting-to-your-instance-via-rdp"></a>

Connect to your Windows Server 2016 instance using the browser-based RDP client in the Lightsail console. For more information, see [Connect to your Windows instance](connect-to-your-windows-based-instance-using-amazon-lightsail.md).

1. On the **Instances** section of the Lightsail home page, choose the RDP quick-connect icon for your Windows Server 2016 instance.  
![Launching and configuring a Windows Server 2016 instance in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-ws-tutorial-05.png)

1. After the browser-based RDP client window opens, you can begin configuring your Windows Server 2016 instance:  
![Launching and configuring a Windows Server 2016 instance in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-ws-tutorial-06.png)

## Step 4: Create a static IP address and attach it to your Windows Server 2016 instance
<a name="tutorial-launching-and-configuring-windows-server-2016-creating-a-lightsail-static-ip"></a>

The default public IP for your Windows Server 2016 instance changes if you stop and start the instance. A static IP address, attached to an instance, stays the same even if you stop and start your instance.

Create a static IP address and attach it to your Windows Server 2016 instance. For more information, see [Create a static IP and attach it to an instance](lightsail-create-static-ip.md) in the Lightsail documentation.

1. On the **Instances** section of the Lightsail home page, choose your running Windows Server 2016 instance.  
![Launching and configuring a Windows Server 2016 instance in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-ws-tutorial-09.png)

1. Choose the **Networking** tab, then choose **Create static IP**.  
![Launching and configuring a Windows Server 2016 instance in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-wordpress-tutorial-10.png)

1. The static IP location, and attached instance are pre-selected based on the instance that you chose earlier in this tutorial.  
![Launching and configuring a Windows Server 2016 instance in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-ws-tutorial-11.png)

1. Enter a name for your static IP.

   Resource names:
   + Must be unique within each AWS Region in your Lightsail account.
   + Must contain 2 to 255 characters.
   + Must start and end with an alphanumeric character or number.
   + Can include alphanumeric characters, numbers, periods, dashes, and underscores.

1. Choose **Create**.  
![Launching and configuring a Windows Server 2016 instance in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-wordpress-tutorial-12.png)

## Step 5: Create a DNS zone and map a domain to your Windows Server 2016 instance
<a name="tutorial-launching-and-configuring-windows-server-2016-creating-a-dns-zone"></a>

Transfer management of your domain's DNS records to Lightsail. This allows you to more easily map a domain to your Windows Server 2016 instance, and manage all of your website’s resources using the Lightsail console. For more information, see [Create a DNS zone to manage your domain’s DNS records](lightsail-how-to-create-dns-entry.md) in the Lightsail documentation.

1. On the **Domains & DNS** section of the Lightsail home page, choose **Create DNS zone**.

1. Enter your domain, then choose **Create DNS zone**.

1. Make note of the name server addresses listed on the page.

   You add these name server addresses to your domain name’s registrar to transfer management of your domain’s DNS records to Lightsail.  
![Launching and configuring a LAMP instance in Lightsail.](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-wordpress-tutorial-15.png)

1. After management of your domain’s DNS records are transferred to Lightsail, add an A record to point the apex of your domain to your LAMP instance, as follows:

   1. In the **Assignments** tab of the DNS zone, choose **Add assignment**.

   1. In the **Select a domain** field, choose the domain or subdomain.

   1. In the **Select a resource** drop down, select the LAMP instance you created earlier in this tutorial.

   1. Choose the **Assign**.

   Allow time for the change to propagate through the internet's DNS before your domain begins routing traffic to your LAMP instance.

## Next steps
<a name="tutorial-launching-and-configuring-windows-server-2016-next-steps"></a>

Here are a few additional steps you can perform after launching a Windows Server 2016 instance in Amazon Lightsail:
+ [Creating a snapshot of your Windows Server instance](prepare-windows-based-instance-and-create-snapshot.md)
+ [Best practices for securing Windows Server-based Lightsail instances](best-practices-for-securing-windows-based-lightsail-instances.md)
+ [Creating and attaching a block storage disk to your Windows Server instance](create-and-attach-additional-block-storage-disks-windows.md)
+ [Extending the storage space of your Windows Server instance](extending-windows-server-storage-space-in-amazon-lightsail.md)