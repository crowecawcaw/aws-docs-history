# Activating your AWS Storage Gateway Hardware Appliance

###### Note

End of availability notice: As of May 12, 2025, the AWS Storage Gateway Hardware Appliance
will no longer be offered. Existing customers with the AWS Storage Gateway Hardware
Appliance can continue to use and receive support until May 2028. As an alternative,
you can use the AWS Storage Gateway service to give your applications on-premises and
in-cloud access to virtually unlimited cloud storage.

After configuring your IP address, you enter this IP address on the
**Hardware** page of the AWS Storage Gateway console to activate your
hardware appliance. The activation process registers the appliance to your AWS
account.

You can choose to activate your hardware appliance in any of the supported AWS Regions.
For a list of supported AWS Regions, see [Storage Gateway Hardware Appliance
Regions](../../../general/latest/gr/sg.md#sg-hardware-appliance "../../../general/latest/gr/sg.md#sg-hardware-appliance") in the _AWS General Reference_.

###### To activate your AWS Storage Gateway Hardware Appliance

1. Open the [AWS Storage Gateway
   Management Console](https://console.aws.amazon.com/storagegateway/home "https://console.aws.amazon.com/storagegateway/home") and sign in with the account credentials you want
   to use to activate your hardware.

###### Note

For activation only, the following must be true:

    * Your browser must be on the same network as your hardware
     appliance.
    * Your firewall must allow HTTP access on port 8080 to the appliance
     for inbound traffic.

2. Choose **Hardware** from the navigation menu on the left side
   of the page.
3. Choose **Activate appliance**.
4. For **IP Address**, enter the IP address that you configured
   for your hardware appliance, then choose **Connect**.

For more information about configuring the IP address, see [Configuring
network parameters](appliance-configure-network.md "appliance-configure-network.md"). 5. For **Name**, enter a name for your hardware appliance. Names can
be up to 255 characters long and can't include a slash character. 6. For **Hardware appliance time zone**, enter the local time
zone from which most of the workload for the gateway will be generated., then
choose **Next**.

The time zone controls when hardware updates take place, with 2 a.m. used as
the default scheduled time to perform updates. Ideally, if the time zone is set
properly, updates will take place outside of the local working day window by
default. 7. Review the activation parameters in the Hardware appliance detail section. You
can choose **Previous** to go back and make changes if
necessary. Otherwise, choose **Activate** to finish the
activation.
A banner appears on the **Hardware appliance overview** page,
indicating that the hardware appliance has been successfully activated.

At this point, the appliance is associated with your account. The next step is to
configure and launch an S3 File Gateway, FSx File Gateway, Tape Gateway, or Volume Gateway on the
new appliance.

**Next step**

[Creating a gateway on your
hardware appliance](appliance-launch-gateway.md "appliance-launch-gateway.md")
