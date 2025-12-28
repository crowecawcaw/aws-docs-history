# Replacing your existing S3 File Gateway with a new

instance

You can replace an existing S3 File Gateway with a new instance as your data and
performance needs grow, or if you receive an AWS notification to migrate your gateway. You
might need to do this if you want to move your gateway to a better host platform or newer
Amazon EC2 instances, or to refresh the underlying server hardware.

There are two methods to replace an existing S3 File Gateway. The following table
describes the benefits and drawbacks of each method. Using this information, select the
method best suited for your gateway environment, then refer to the procedure steps in the
corresponding section below.

###### Note

If you need to [log into your new Storage Gateway local console](LocalConsole-login-fgw.md "LocalConsole-login-fgw.md") to complete either method,
the initial username is _admin_, and the temporary password is
_password_.

###### Important

Use these instructions only for migrating gateway appliances running version 1.x. You can't use them to migrate gateway appliances running lower versions.

|                     | **Method 1: Migrate cache disk and Gateway ID<br>to replacement instance\***                                                                                                                        | **Method 2: Replacement instance with empty<br>cache disk and new Gateway ID**                                                                                                                                                                                                                                                                                                                 |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cache disk data** | Data on the cache disk is preserved. This method is useful if your<br>gateway has a large cache disk, or if your applications are sensitive to<br>the delay caused by out-of-cache read operations. | Data in cache is downloaded from the AWS cloud. This method is<br>optimal for write-heavy workloads, if your applications can tolerate the<br>delay caused by out-of-cache reads.                                                                                                                                                                                                              |
| **Down time**       | Your gateway will be offline for 1-2 hours during the migration<br>process.                                                                                                                         | File shares are always available, but clients will experience short<br>cutover downtime when switching from one file share to another during<br>the transition to the new instance.<br>NoteWriting to one Amazon S3 bucket from two file shares simultaneously is<br>_not supported_, so all clients must be<br>remapped from one share to the other simultaneously, rather than<br>gradually. |
| **Gateway ID**      | The new gateway inherits the Gateway ID from the gateway it<br>replaces.                                                                                                                            | The existing gateway and replacement gateway have separate, unique<br>Gateway IDs.                                                                                                                                                                                                                                                                                                             |

###### Note

Migration can only be performed between gateways of the same type. For example, you
cannot migrate settings or data from an FSx File Gateway to an S3 File Gateway.

## Method 1: Migrate cache disk and Gateway ID

to replacement instance

###### To migrate your S3 File Gateway's cache disk and Gateway ID to a

replacement instance:

1. Stop any applications that are writing to the existing S3 File Gateway.
2. Use the following steps to update the gateway to the latest version
   1. Open the Storage Gateway console at
      [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
   2. In the navigation pane, choose **Gateways**, and then choose the old S3 File Gateway that
      you want to migrate.
   3. Click **Update Now** if available. If not, your gateway is already on the latest version.

3. Verify that the `CachePercentDirty` metric on the
   **Monitoring** tab for the existing S3 File Gateway is `0`.
4. Shut down the existing S3 File Gateway by powering off the host virtual
   machine (VM) using its hypervisor controls.

For more information about shutting down an Amazon EC2 instance, see [Stop and
start your instance](../../../AWSEC2/latest/UserGuide/Stop_Start.md "../../../AWSEC2/latest/UserGuide/Stop_Start.md") in the _Amazon EC2 User
Guide_.

For more information about shutting down a KVM, VMware, or Hyper-V VM, see
your hypervisor documentation. 5. Detach all disks, including the root disk and cache disks from the old gateway
VM.

###### Note

Make a note of the root disk's volume ID, as well as the gateway ID
associated with that root disk. You will need to detach this disk from the
new Storage Gateway hypervisor in a later step.

If you are using an Amazon EC2 instance as the VM for your S3 File Gateway, see [Detach an Amazon EBS
volume from a Windows instance](../../../AWSEC2/latest/WindowsGuide/ebs-detaching-volume.md "../../../AWSEC2/latest/WindowsGuide/ebs-detaching-volume.md") or [Detach an Amazon EBS
volume from a Linux instance](../../../AWSEC2/latest/UserGuide/ebs-detaching-volume.md "../../../AWSEC2/latest/UserGuide/ebs-detaching-volume.md") in the _Amazon EC2 User
Guide_.

For information about detaching disks from a KVM, VMware, or Hyper-V VM, see
the documentation for your hypervisor. 6. Create a new AWS Storage Gateway hypervisor VM instance, but don't activate it as a
gateway. In a later step, this new VM will assume the identity of the old
gateway.

For more information about creating a new Storage Gateway hypervisor VM, see
[Choosing a Host Platform and Downloading the VM](create-gateway-file.md#hosting-options-file "create-gateway-file.md#hosting-options-file").

###### Note

Do not add cache disks for the new VM. This VM will use the same cache
disks that were used by the old VM. 7. Configure your new Storage Gateway VM to use the same network settings as the old
VM.

The default network configuration for the gateway is Dynamic Host
Configuration Protocol (DHCP). With DHCP, your gateway is automatically assigned
an IP address.

If you need to manually configure a static IP address for your gateway VM, see
[Configuring
network parameters](appliance-configure-ip.md "appliance-configure-ip.md").

If your gateway VM must use a Socket Secure version 5 (SOCKS5) proxy to
connect to the internet, see [Routing your gateway deployed on EC2 through an HTTP proxy](ec2-local-console-fwg.md#EC2_MaintenanceRoutingProxy-fgw "ec2-local-console-fwg.md#EC2_MaintenanceRoutingProxy-fgw"). 8. Start the new Storage Gateway VM. 9. Attach the disks that you detached from the old gateway VM to the new gateway
VM. Do not detach the existing root disk from the new gateway VM.

###### Note

To migrate successfully, all disks must remain unchanged. Changing the
disk size or other values causes inconsistencies in metadata that prevent
successful migration. 10. Initiate the gateway migration process by either connecting to the new gateway VM’s local console,
or making web requests to the new gateway VM's IP address (described below).

    1. To use the local console, select the option for **Migrate Gateway** and provide
     your existing gateway ID when prompted. You will be provided prompts to copy previously applied
     settings on old gateway to the new gateway. You may choose to apply them or manually configure them later.
     See [Accessing
     the Gateway Local Console](accessing-local-console.md "accessing-local-console.md").
    2. Alternatively, you can initiate the gateway migration process by connecting to the new VM with a URL
     that uses the following format.



    ```
    http://`your-VM-IP-address`/migrate?gatewayId=`your-gateway-ID`
    ```

    You can re-use the same IP address for the new gateway VM as you used for the
     old gateway VM. Your URL should look similar to the example following.



    ```
    http://198.51.100.123/migrate?gatewayId=sgw-12345678
    ```

    Use this URL from a browser, or from the command line using `curl`,
     to initiate the migration process.


    When the gateway migration process is successfully completed, you will see
     a message confirming successful migration.

11. Wait for the gateway status to show as **Running** in the
    AWS Storage Gateway console. Depending on available bandwidth, this can take up to 10
    minutes.
12. Stop the new Storage Gateway VM.
13. Detach the old gateway's root disk, whose volume ID you noted previously, from
    the new gateway.
14. Start the new Storage Gateway VM.
15. If your gateway was joined to an Active Directory domain, re-join the domain.
    For instructions, see
    [Using Active
    Directory to authenticate users](enable-ad-settings.md "enable-ad-settings.md").

###### Note

You must complete this step even if the status of the S3 File Gateway appears as **Joined**. 16. If your gateway was using the SMB Guest Access authentication method, the password will need to be reentered.
For instructions see [Provide guest access to your file share](guest-access.md "guest-access.md"). 17. Confirm that your shares are available at the new gateway VM's IP address,
then delete the old gateway VM.

###### Warning

When a gateway is deleted, there is no way to recover it.

For more information about deleting an Amazon EC2 instance, see [Terminate your
instance](../../../AWSEC2/latest/UserGuide/terminating-instances.md "../../../AWSEC2/latest/UserGuide/terminating-instances.md") in the _Amazon EC2 User Guide_. For more
information about deleting a KVM, VMware, or Hyper-V VM, see the documentation
for your hypervisor.

## Method 2: Replacement instance with

empty cache disk and new Gateway ID

###### To set up a replacement S3 File Gateway instance with empty cache disk and new

Gateway ID:

1.  Stop any applications that are writing to the existing S3 File Gateway. Verify that the `CachePercentDirty` metric
    on the **Monitoring** tab is `0` before you set up
    file shares on the new gateway.
2.  Use the AWS Command Line Interface (AWS CLI) to gather and save the configuration information
    about your existing S3 File Gateway and file shares by doing the
    following:
    1. Save the gateway configuration information for the S3 File Gateway.

    ```
    aws storagegateway describe-gateway-information --gateway-arn "arn:aws:storagegateway:`us-east-2`:`123456789012`:gateway/**sgw-12A3456B**"
    ```

    This command outputs a JSON block that contains metadata about the
    gateway, such as its name, network interfaces, configured time zone, and
    its state (whether the gateway is running). 2. Save the Server Message Block (SMB) settings of the S3 File Gateway.

    ```
    aws storagegateway describe-smb-settings --gateway-arn "arn:aws:storagegateway:`us-east-2`:`123456789012`:gateway/`sgw-12A3456B`"
    ```

    This command outputs a JSON block that contains metadata about the SMB
    file share, such as its domain name, Microsoft Active Directory status,
    whether the guest password is set, and the type of security
    strategy. 3. Save file share information for each SMB and Network File System (NFS)
    file share of the S3 File Gateway:

        * Use the following command for SMB file shares.



        ```
        aws storagegateway describe-smb-file-shares --file-share-arn-list "arn:aws:storagegateway:`us-east-2`:`123456789012`:share/`share-987A654B`"
        ```

        This command outputs a JSON block that contains metadata about
         the SMB file share, such as its name, storage class, status, IAM
         role Amazon Resource Name (ARN), a list of clients that are
         allowed to access the S3 File Gateway, and the path used by the SMB client to
         identify the mount point.
        * Use the following command for NFS file shares.



        ```
        aws storagegateway  describe-nfs-file-shares --file-share-arn-list "arn:aws:storagegateway:`us-east-2`:`123456789012`:share/`share-321A978B`"
        ```

        This command outputs a JSON block that contains metadata about
         the NFS file share, such as its name, storage class, status, IAM
         role ARN, a list of clients that are allowed to access the
         S3 File Gateway, and the path used
         by the NFS client to identify the mount point.

3.  Create a new S3 File Gateway with the same settings and
    configuration as the old gateway. If necessary, refer to the information you
    saved in Step 2.
4.  Create new file shares for the new gateway with the same settings and
    configuration as the file shares that were configured on the old gateway. If
    necessary, refer to the information you saved in Step 2.
5.  Confirm that your new gateway is working correctly, then remap/cut-over your
    clients from the old file shares to the new file shares in the manner that best
    suits your environment.
6.  Confirm that your new gateway is working correctly, then delete the old
    gateway from the Storage Gateway console.

###### Important

Before you delete an S3 File Gateway, make sure that there are no
applications currently writing to that gateway's cache. If you delete a
gateway while it is in use, data loss can occur.

###### Warning

When a gateway is deleted, there is no way to recover it. 7. Delete the old gateway VM or Amazon EC2 instance.
