Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Configuring hardware appliance network

parameters

###### Note

End of availability notice: As of May 12, 2025, the AWS Storage Gateway Hardware Appliance
will no longer be offered. Existing customers with the AWS Storage Gateway Hardware
Appliance can continue to use and receive support until May 2028. As an alternative,
you can use the AWS Storage Gateway service to give your applications on-premises and
in-cloud access to virtually unlimited cloud storage.

After the hardware appliance boots up and you set your admin user password in the
hardware console as described in [Accessing the hardware appliance
console](access-hardware-appliance-console.md "access-hardware-appliance-console.md"), use the following procedure to
configure network parameters so your hardware appliance can connect to AWS.

###### To set a network address

1. From the **Home** page, choose **Configure
   Network** and then press `Enter`. The
   **Configure Network** page appears. The **Configure
   Network** page shows IP and DNS information for each of the 4
   network interfaces on the hardware appliance, and includes menu options to
   configure **DHCP** or **Static** addresses for
   each.
2. For the **em1** interface, do one of the following:
   - Choose **DHCP** and press `Enter` to use
     the IPv4 address assigned by your Dynamic Host Configuration Protocol
     (DHCP) server to your physical network port.

   Note this address for later use in the activation step.
   - Choose **Static** and press `Enter` to
     configure a static IPv4 address.

   Enter a valid **IP Address**, **Subnet
   Mask**, **Gateway**, and
   **DNS** server address for the
   **em1** network interface.

   When finished, choose **Save** and then press
   `Enter` to save the configuration.

###### Note

You can use this procedure to configure other network interfaces in
addition to **em1**. If you configure other interfaces,
they must provide the same always-on connection to the AWS endpoints
listed in the requirements.

Network bonding and Link Aggregation Control Protocol (LACP) are not
supported by the hardware appliance or by Storage Gateway.

We do not recommend configuring multiple network interfaces on the same
subnet as this can sometimes cause routing issues.

###### To log out of the hardware console

1. Choose **Back** and press `Enter` to return to the
   **Home** page.
2. Choose **Logout** and press `Enter` to return to
   the **Welcome** page.
   **Next step**

[Activating your AWS Storage Gateway Hardware Appliance](appliance-activation.md "appliance-activation.md")
