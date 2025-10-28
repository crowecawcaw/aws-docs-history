# Configuring paravirtualization on a

VMware host

The following procedure describes how to configure the VMware host platform for
your Storage Gateway appliance to use paravirtual Internet Small Computer System Interface
Protocol (iSCSI) controllers. Paravirtual iSCSI controllers are high performance
storage controllers that can result in greater throughput and lower CPU use. These
controllers are best suited for high performance storage environments. When you
configure iSCSI controllers this way, the Storage Gateway virtual machine works with the
host operating system to allow the gateway console to identify the virtual disks
that you add to your virtual machine.

###### Note

You need to complete this step to avoid issues in identifying these disks when
you configure them in the gateway console.

###### To configure your VMware host platform to use paravirtualized

controllers

1. In the VMware vSphere client, right-click on the name of your gateway
   virtual machine in the navigation pane on the left side of the application
   window to open the context menu, and then choose **Edit
   Settings**.
2. In the **Virtual Machine Properties** dialog box, choose
   the **Hardware** tab.
3. On the **Hardware** tab, select **SCSI controller
   0**, and then choose **Change Type**.
4. In the **Change SCSI Controller Type** dialog box, select
   the **VMware Paravirtual** SCSI controller type, and then
   choose **OK** to save the configuration.
