Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Synchronize VM time with VMware host

time

To successfully activate your gateway, you must ensure that your VM time is synchronized
to the host time, and that the host time is correctly set. In this section, you first
synchronize the time on the VM to the host time. Then you check the host time and, if
needed, set the host time and configure the host to synchronize its time automatically to a
Network Time Protocol (NTP) server.

###### Important

Synchronizing the VM time with the host time is required for successful gateway
activation.

###### To synchronize VM time with host time

1. Configure your VM time.
   1. In the vSphere client, right-click on the name of your gateway VM in panel
      on the left side of the application window to open the context menu for the
      VM, and then choose **Edit Settings**.

   The **Virtual Machine Properties** dialog box
   opens. 2. Choose the **Options** tab, and then choose
   **VMware Tools** from the options list. 3. Check the **Synchronize guest time with host** option in
   the **Advanced** section on the right side of the
   **Virtual Machine Properties** dialog box, and then
   choose **OK**.

   The VM synchronizes its time with the host.

2. Configure the host time.

It is important to make sure that your host clock is set to the correct time. If
you have not configured your host clock, perform the following steps to set and
synchronize it with an NTP server.

    1. In the VMware vSphere client, select the vSphere host node in the left
     panel, and then choose the **Configuration** tab.
    2. Select **Time Configuration** in the
     **Software** panel, and then choose the
     **Properties** link.


    The **Time Configuration** dialog box appears.
    3. Under **Date and Time**, set the date and time for your
     vSphere host.
    4. Configure the host to synchronize its time automatically to an NTP
     server.


    	1. Choose **Options** in the **Time
    	 Configuration** dialog box, and then in the
    	 **NTP Daemon (ntpd) Options** dialog box,
    	 choose **NTP Settings** in the left panel.
    	2. Choose **Add** to add a new NTP server.
    	3. In the **Add NTP Server** dialog box, type the IP
    	 address or the fully qualified domain name of an NTP server, and
    	 then choose **OK**.


    	You can use `pool.ntp.org` as the domain
    	 name.
    	4. In the **NTP Daemon (ntpd) Options** dialog box,
    	 choose **General** in the left panel.
    	5. Under **Service Commands**, choose
    	 **Start** to start the service.


    	Note that if you change this NTP server reference or add another
    	 later, you will need to restart the service to use the new
    	 server.
    5. Choose **OK** to close the **NTP Daemon (ntpd)
     Options** dialog box.
    6. Choose **OK** to close the **Time
     Configuration** dialog box.
