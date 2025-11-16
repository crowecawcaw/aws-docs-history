AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Managing an Amazon EC2 cluster on Snowball Edge with AWS OpsHub

An Amazon EC2 _cluster_ is a group of devices that provision
together as a cluster of devices. To use a cluster, the AWS services
on your device must be running at your default endpoint. You also must choose the
specific device in the cluster that you want to talk to. You use a cluster on a
per-device basis.

###### To create an Amazon EC2 cluster

1. Connect and log in to your Snow device. For instructions on how to log in to your device, see
   [Unlocking a Snowball Edge device with AWS OpsHub](connect-unlock-device.md "connect-unlock-device.md").
2. On the **Choose device** page, choose **Snowball Edge
   cluster**, and then choose **Next**.
3. On the **Connect to your device** page, provide the IP
   address of the device and the IP addresses of other devices in the cluster.
4. Choose **Add another** device to add more devices, and
   then choose **Next**.
5. On the **Provide the keys** page, enter the device client unlock code, upload
   the device manifest, and choose **Unlock device**.

Snowball Edge devices use 256-bit encryption to help ensure both security
and full chain-of-custody for your data. 6. (Optional) Enter a name to create a profile, and then choose **Save profile
name**. You are directed to the dashboard, where you see all
your clusters.

You can now start using AWS services and managing your cluster. You manage
instances in the cluster the same way you manage individual instances. For
instructions, see [Managing AWS services on the Snowball Edge with AWS OpsHub](manage-services.md "manage-services.md").
