# Creating a gateway on your

hardware appliance

###### Note

End of availability notice: As of May 12, 2025, the AWS Storage Gateway Hardware Appliance
will no longer be offered. Existing customers with the AWS Storage Gateway Hardware
Appliance can continue to use and receive support until May 2028. As an alternative,
you can use the AWS Storage Gateway service to give your applications on-premises and
in-cloud access to virtually unlimited cloud storage.

You can create an S3 File Gateway, FSx File Gateway, Tape Gateway, or Volume Gateway on any
AWS Storage Gateway Hardware Appliance in your deployment.

###### To create a gateway on your hardware appliance

1. Sign in to the AWS Management Console and open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Follow the procedures described in [Creating Your
   Gateway](create-file-gateway.md "create-file-gateway.md") to set up, connect, and configure the type of Storage Gateway that
   you want to deploy.
   When you finish creating your gateway in the Storage Gateway console, the Storage Gateway software
   automatically starts installing on the hardware appliance. If you use Dynamic Host
   Configuration Protocol (DHCP), it can take 5 to 10 minutes for a gateway to display as
   online in the console. To assign a static IP address to your installed gateway, see
   [Configuring an IP
   address for the gateway](appliance-configure-ip.md "appliance-configure-ip.md").

To assign a static IP address to your installed gateway, you next configure the
gateway's network interfaces so your applications can use it.

**Next step**

[Configuring a gateway IP address on the
hardware appliance](appliance-configure-ip.md "appliance-configure-ip.md")
