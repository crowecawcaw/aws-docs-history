# Troubleshooting: hardware

appliance issues

###### Note

End of availability notice: As of May 12, 2025, the AWS Storage Gateway Hardware Appliance
will no longer be offered. Existing customers with the AWS Storage Gateway Hardware
Appliance can continue to use and receive support until May 2028. As an alternative,
you can use the AWS Storage Gateway service to give your applications on-premises and
in-cloud access to virtually unlimited cloud storage.

The following topics discuss issues that you might encounter with the AWS Storage Gateway Hardware Appliance, and
suggestions on troubleshooting these.

###### Topics

- [You can't determine the service IP
  address](#service_ip_address "#service_ip_address")
- [How do you perform a factory reset?](#factory_reset "#factory_reset")
- [How do you perform a remote restart?](#remote-restart "#remote-restart")
- [Where do you obtain Dell iDRAC support?](#iDRAC_support "#iDRAC_support")
- [You can't find the hardware appliance
  serial number](#appliance_serial_number "#appliance_serial_number")
- [Where to obtain hardware appliance
  support](#appliance_support "#appliance_support")

## You can't determine the service IP

address

When attempting to connect to your service, make sure that you are using the
service's IP address and not the host IP address. Configure the service IP
address in the service console, and the host IP address in the hardware console. You
see the hardware console when you start the hardware appliance. To go to the service
console from the hardware console, choose **Open Service
Console**.

## How do you perform a factory reset?

If you need to perform a factory reset on your appliance, contact the AWS Storage Gateway Hardware Appliance
team for support, as described in the Support section following.

## How do you perform a remote restart?

If you need to perform a remote restart of your appliance, you can do so using the
Dell iDRAC management interface. For more information, see [iDRAC9 Virtual Power Cycle: Remotely power cycle Dell EMC PowerEdge
Servers](https://infohub.delltechnologies.com/en-us/p/idrac9-virtual-power-cycle-remotely-power-cycle-dell-emc-poweredge-servers/ "https://infohub.delltechnologies.com/en-us/p/idrac9-virtual-power-cycle-remotely-power-cycle-dell-emc-poweredge-servers/") on the Dell Technologies InfoHub website.

## Where do you obtain Dell iDRAC support?

The Dell PowerEdge server comes with the Dell iDRAC management interface. We
recommend the following:

- If you use the iDRAC management interface, you should change the default
  password. For more information about the iDRAC credentials, see [Dell PowerEdge - What is the default sign-in credentials for
  iDRAC?](https://www.dell.com/support/article/en-us/sln306783/dell-poweredge-what-is-the-default-username-and-password-for-idrac?lang=en "https://www.dell.com/support/article/en-us/sln306783/dell-poweredge-what-is-the-default-username-and-password-for-idrac?lang=en").
- Make sure that the firmware is up-to-date to prevent security
  breaches.
- Moving the iDRAC network interface to a normal (`em`) port can
  cause performance issues or prevent the normal functioning of the
  appliance.

## You can't find the hardware appliance

serial number

You can find the serial number for your AWS Storage Gateway Hardware Appliance using the Storage Gateway
console.

###### To find the hardware appliance serial number:

1. Open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. Choose **Hardware** from the navigation menu on the left
   side of the page.
3. Select your hardware appliance from the list.
4. Locate the **Serial Number** field on the
   **Details** tab for your appliance.

## Where to obtain hardware appliance

support

To contact AWS about technical support for your hardware appliance, see [Support](https://aws.amazon.com/contact-us "https://aws.amazon.com/contact-us").

The Support team might ask you to activate the support channel to troubleshoot your
gateway issues remotely. You don't need this port to be open for the normal
operation of your gateway, but it is required for troubleshooting. You can activate
the support channel from the hardware console as shown in the procedure
following.

###### To open a support channel for AWS

1. Open the hardware console.
2. Choose **Open Support Channel** at the bottom of the main
   page of the hardware console, and then press `Enter`.

The assigned port number should appear within 30 seconds if there are no
network connectivity or firewall issues. For example:

**Status: Open on port 19599** 3. Note the port number and provide it to Support.
