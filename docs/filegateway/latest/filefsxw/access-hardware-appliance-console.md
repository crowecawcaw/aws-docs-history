Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Accessing the hardware appliance

console

###### Note

End of availability notice: As of May 12, 2025, the AWS Storage Gateway Hardware Appliance
will no longer be offered. Existing customers with the AWS Storage Gateway Hardware
Appliance can continue to use and receive support until May 2028. As an alternative,
you can use the AWS Storage Gateway service to give your applications on-premises and
in-cloud access to virtually unlimited cloud storage.

When you power on your hardware appliance, the hardware appliance console appears on the monitor.
The hardware appliance console presents a user interface specific to AWS that you can use to
set an administrator password, configure initial network parameters, and open a support
channel to AWS.

To work with the hardware appliance console, enter text from the keyboard and use the
`Up`, `Down`, `Right`, and `Left Arrow`
keys to move about the screen in the indicated direction. Use the `Tab` key
to move forward in order through items on-screen. On some setups, you can use the
`Shift+Tab` keystroke to move sequentially backward. Use the
`Enter` key to save selections, or to choose a button on the
screen.

The first time the hardware appliance console appears, the **Welcome** page
is displayed, and you are prompted to set a password for the _admin_
user account before you can access the console.

###### To set an admin password

- At the **Please set your login password** prompt, do the
  following:

      1. For **Set Password**, enter a password, and then
       press `Down arrow`.
      2. For **Confirm**, re-enter your password, and then
       choose **Save Password**.

  After you set your password, the hardware console **Home** page
  appears. The **Home** page displays network information for the
  **em1**, **em2**, **em3**, and
  **em4** network interfaces, and has the following menu
  options:

- Configure Network
- Open Service Console
- Change Password
- Logout
- Open Support Console
  **Next step**

[Configuring hardware appliance network
parameters](appliance-configure-network.md "appliance-configure-network.md")
