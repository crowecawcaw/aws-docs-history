

# Configuring CHAP Authentication for Your iSCSI Targets
<a name="ConfiguringiSCSIClientInitiatorCHAP"></a>

Storage Gateway supports authentication between your gateway and iSCSI initiators by using Challenge-Handshake Authentication Protocol (CHAP). CHAP provides protection against playback attacks by periodically verifying the identity of an iSCSI initiator as authenticated to access a volume and VTL device target. 

**Note**  
CHAP configuration is optional but highly recommended.

To set up CHAP, you must configure it both on the Storage Gateway console and in the iSCSI initiator software that you use to connect to the target. Storage Gateway uses mutual CHAP, which is when the initiator authenticates the target and the target authenticates the initiator.

**To set up mutual CHAP for your targets**

1. Configure CHAP on the Storage Gateway console, as discussed in [To configure CHAP for a VTL device target on the Storage Gateway console](#ConfiguringiSCSIClientInitiatorCHAPConsole-tgw).

1. In your client initiator software, complete the CHAP configuration:
   + To configure mutual CHAP on a Windows client, see [To configure mutual CHAP on a Windows client](#ConfiguringiSCSIClientInitiatorCHAPWindows).
   + To configure mutual CHAP on a Red Hat Linux client, see [To configure mutual CHAP on a Red Hat Linux client](#ConfiguringiSCSIClientInitiatorCHAPLinux).<a name="ConfiguringiSCSIClientInitiatorCHAPConsole-tgw"></a>

**To configure CHAP for a VTL device target on the Storage Gateway console**

In this procedure, you specify two secret keys that are used to read and write to a virtual tape. These same keys are used in the procedure to configure the client initiator.

1. In the navigation pane, choose **Gateways**.

1. Choose your gateway, and then choose the **VTL Devices** tab to display all your VTL devices.

1. Choose the device that you want to configure CHAP for.

1. Provide the requested information in the **Configure CHAP Authentication** dialog box.

   1. For **Initiator Name**, enter the name of your iSCSI initiator. This name is an Amazon iSCSI qualified name (IQN) that is prepended by `iqn.1997-05.com.amazon:` followed by the target name. The following is an example.

      `iqn.1997-05.com.amazon:{{your-tape-device-name}}`

      You can find the initiator name by using your iSCSI initiator software. For example, for Windows clients, the name is the value on the **Configuration** tab of the iSCSI initiator. For more information, see [To configure mutual CHAP on a Windows client](#ConfiguringiSCSIClientInitiatorCHAPWindows).
**Note**  
To change an initiator name, you must first deactivate CHAP, change the initiator name in your iSCSI initiator software, and then activate CHAP with the new name.

   1. For **Secret used to Authenticate Initiator**, enter the secret requested.

      This secret must be a minimum of 12 characters and a maximum of 16 characters long. This value is the secret key that the initiator (that is, the Windows client) must know to participate in CHAP with the target.

   1. For **Secret used to Authenticate Target (Mutual CHAP)**, enter the secret requested.

      This secret must be a minimum of 12 characters and a maximum of 16 characters long. This value is the secret key that the target must know to participate in CHAP with the initiator.
**Note**  
The secret used to authenticate the target must be different than the secret to authenticate the initiator.

   1. Choose **Save**.

1. On the **VTL Devices** tab, confirm that the iSCSI CHAP authentication field is set to **true**.<a name="ConfiguringiSCSIClientInitiatorCHAPWindows"></a>

**To configure mutual CHAP on a Windows client**

In this procedure, you configure CHAP in the Microsoft iSCSI initiator using the same keys that you used to configure CHAP for the volume on the console.

1. If the iSCSI initiator is not already started, on the **Start** menu of your Windows client computer, choose **Run**, enter **iscsicpl.exe**, and then choose **OK** to run the program.

1. Configure mutual CHAP configuration for the initiator (that is, the Windows client):

   1. Choose the **Configuration** tab.

       
**Note**  
The **Initiator Name** value is unique to your initiator and company. The name shown preceding is the value that you used in the **Configure CHAP Authentication** dialog box of the Storage Gateway console.  
The name shown in the example image is for demonstration purposes only.

   1. Choose **CHAP**.

   1. In the **iSCSI Initiator Mutual Chap Secret** dialog box, enter the mutual CHAP secret value.

      In this dialog box, you enter the secret that the initiator (the Windows client) uses to authenticate the target (the storage volume). This secret allows the target to read and write to the initiator. This secret is the same as the secret entered into the **Secret used to Authenticate Target (Mutual CHAP)** box in the **Configure CHAP Authentication** dialog box. For more information, see [Configuring CHAP Authentication for Your iSCSI Targets](#ConfiguringiSCSIClientInitiatorCHAP).

   1. If the key that you entered is fewer than 12 characters or more than 16 characters long, an **Initiator CHAP secret** error dialog box appears.

      Choose **OK**, and then enter the key again.

1. Configure the target with the initiator's secret to complete the mutual CHAP configuration.

   1. Choose the **Targets** tab.

   1. If the target that you want to configure for CHAP is currently connected, disconnect the target by selecting it and choosing **Disconnect**.

   1. Select the target that you want to configure for CHAP, and then choose **Connect**.

   1. In the **Connect to Target** dialog box, choose **Advanced**.

   1. In the **Advanced Settings** dialog box, configure CHAP.

       

      1. Select **Activate CHAP log on**.

      1. Enter the secret that is required to authenticate the initiator. This secret is the same as the secret entered into the **Secret used to Authenticate Initiator** box in the **Configure CHAP Authentication** dialog box. For more information, see [Configuring CHAP Authentication for Your iSCSI Targets](#ConfiguringiSCSIClientInitiatorCHAP).

      1. Select **Perform mutual authentication**.

      1. To apply the changes, choose **OK**.

   1. In the **Connect to Target** dialog box, choose **OK**. 

1. If you provided the correct secret key, the target shows a status of **Connected**.<a name="ConfiguringiSCSIClientInitiatorCHAPLinux"></a>

**To configure mutual CHAP on a Red Hat Linux client**

In this procedure, you configure CHAP in the Linux iSCSI initiator using the same keys that you used to configure CHAP for the volume on the Storage Gateway console.

1. Ensure that the iSCSI daemon is running and that you have already connected to a target. If you have not completed these two tasks, see [Connecting to a Linux Client](https://docs.aws.amazon.com/storagegateway/latest/tgw/GettingStarted-create-tape-gateway.html#iscsi-vtl-linux).

1. Disconnect and remove any existing configuration for the target for which you are about to configure CHAP.

   1. To find the target name and ensure it is a defined configuration, list the saved configurations using the following command.

      ```
      sudo /sbin/iscsiadm --mode node
      ```

   1. Disconnect from the target.

      The following command disconnects from the target named **myvolume** that is defined in the Amazon iSCSI qualified name (IQN). Change the target name and IQN as required for your situation.

      ```
      sudo /sbin/iscsiadm --mode node --logout {{GATEWAY_IP}}:3260,1 iqn.1997-05.com.amazon:myvolume
      ```

   1. Remove the configuration for the target.

      The following command removes the configuration for the **myvolume** target.

      ```
      sudo /sbin/iscsiadm --mode node --op delete --targetname iqn.1997-05.com.amazon:myvolume
      ```

1. Edit the iSCSI configuration file to activate CHAP.

   1. Get the name of the initiator (that is, the client you are using).

      The following command gets the initiator name from the `/etc/iscsi/initiatorname.iscsi` file.

      ```
      sudo cat /etc/iscsi/initiatorname.iscsi
      ```

      The output from this command looks like this:

      `InitiatorName=iqn.1994-05.com.redhat:8e89b27b5b8`

   1. Open the `/etc/iscsi/iscsid.conf` file.

   1. Uncomment the following lines in the file and specify the correct values for {{username}}, {{password}}, {{username\_in}}, and {{password\_in}}.

      ```
      node.session.auth.authmethod = CHAP
      node.session.auth.username = {{username}}
      node.session.auth.password = {{password}}
      node.session.auth.username_in = {{username_in}}
      node.session.auth.password_in = {{password_in}}
      ```

      For guidance on what values to specify, see the following table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/tgw/ConfiguringiSCSIClientInitiatorCHAP.html)

   1. Save the changes in the configuration file, and then close the file.

1. Discover and log in to the target. To do so, follow the steps in [Connecting to a Linux Client](https://docs.aws.amazon.com/storagegateway/latest/tgw/GettingStarted-create-tape-gateway.html#iscsi-vtl-linux).