# Configuring a gateway IP address on the

hardware appliance

###### Note

End of availability notice: As of May 12, 2025, the AWS Storage Gateway Hardware Appliance
will no longer be offered. Existing customers with the AWS Storage Gateway Hardware
Appliance can continue to use and receive support until May 2028. As an alternative,
you can use the AWS Storage Gateway service to give your applications on-premises and
in-cloud access to virtually unlimited cloud storage.

Before you activated your hardware appliance, you assigned an IP address to its
physical network interface. Now that you have activated the appliance and launched your
Storage Gateway on it, you need to assign another IP address to the Storage Gateway virtual machine that
runs on the hardware appliance. To assign a static IP address to a gateway installed on
your hardware appliance, configure the IP address from the gateway local console for that
gateway. Your applications (such as your NFS or SMB client) connect to this IP address.
You can access the gateway local console from the hardware appliance console using the
**Open Service Console** option.

###### To configure an IP address on your appliance to work with applications

1. On the hardware console, choose **Open Service Console** and
   then press `Enter` to open the login page for the gateway local
   console.
2. The AWS Storage Gateway local console login page prompts you to login to change your
   network configuration and other settings.

The default account is `admin` and the default password is
`password`.

###### Note

We recommend changing the default password by entering the corresponding
numeral for **Gateway Console** from the **AWS
Appliance Activation - Configuration** main menu, then running
the `passwd` command. For information about how to run the
command, see [Running Storage Gateway commands on the
local console](MaintenanceGatewayConsole-fgw.md "MaintenanceGatewayConsole-fgw.md"). You can also set the
password from the Storage Gateway console. For more information, see [Setting the local console password from the Storage Gateway console](LocalConsole-login-fgw.md#set-password "LocalConsole-login-fgw.md#set-password") . 3. The **AWS Appliance Activation - Configuration** page
includes the following menu options:

    * HTTP/SOCKS Proxy Configuration
    * Network Configuration
    * Test Network Connectivity
    * View System Resource Check
    * System Time Management
    * License Information
    * Command Prompt

###### Note

Some options appear only for specific gateway types or host
platforms.

Enter the corresponding numeral to navigate to the **Network
Configuration** page. 4. Do one of the following to configure the gateway IP address:

    * To use the IP address assigned by your Dynamic Host Configuration
     Protocol (DHCP) server, enter the corresponding numeral for
     **Configure DHCP**, and then enter valid DHCP
     configuration information on the following page.
    * To assign a static IP address, enter the corresponding numeral for
     **Configure Static IP**, and then enter valid IP
     address and DNS information on the following page.


    ###### Note

    The IP address you specify here must be on the same subnet as the
     IP address used during hardware appliance activation.

###### To exit the gateway local console

- Press the `Crtl+]` (close bracket) keystroke. The hardware console
  appears.

###### Note

The keystroke preceding is the only way to exit the gateway local
console.
After your hardware appliance has been activated and configured, your appliance appears in
the console. Now you can continue the setup and configuration procedure for your gateway
in the Storage Gateway console. For instructions, see [Configure your Amazon S3 File Gateway](create-gateway-file.md#configure-gateway-s3-file "create-gateway-file.md#configure-gateway-s3-file").
