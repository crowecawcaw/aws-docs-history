Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Replacing your existing FSx File Gateway with a new

instance

You can replace an existing FSx File Gateway with a new instance as your data and
performance needs grow, or if you receive an AWS notification to migrate your gateway. You
might need to do this if you want to move your gateway to a better host platform or newer
Amazon EC2 instances, or to refresh the underlying server hardware.

###### Important

Use these instructions only for migrating gateway appliances running version 1.x. You can't use them to migrate gateway appliances running lower versions.

###### Note

Migration can only be performed between gateways of the same type. For example, you
cannot migrate settings or data from an FSx File Gateway to an S3 File Gateway.

###### To replace your FSx File Gateway gateway with a new

instance with an empty cache disk and a new Gateway ID:

1. Stop any applications that are writing to the existing FSx File Gateway. Verify that
   the `CachePercentDirty` metric on the **Monitoring** tab
   is `0` before you set up file system associations on the new
   gateway.
2. Use the AWS Command Line Interface (AWS CLI) to gather and save the configuration information about
   your existing FSx File Gateway and associated file systems by doing
   the following:
   1. Save the gateway configuration information for the FSx File Gateway.

   ```
   aws storagegateway describe-gateway-information --gateway-arn "arn:aws:storagegateway:`us-east-2`:`123456789012`:gateway/**sgw-12A3456B**"
   ```

   This command outputs a JSON block that contains metadata about the
   gateway, such as its name, network interfaces, configured time zone, and its
   state (whether the gateway is running). 2. Save the Server Message Block (SMB) settings of the FSx File Gateway.

   ```
   aws storagegateway describe-smb-settings --gateway-arn "arn:aws:storagegateway:`us-east-2`:`123456789012`:gateway/`sgw-12A3456B`"
   ```

   This command outputs a JSON block that contains the domain name of the
   Microsoft Active Directory that the gateway is joined to. 3. Save file share information for each file system associated with the
   FSx File Gateway:

   Use the following command for each associated file system.

   ```
   aws storagegateway describe-file-system-associations --file-system-association-arn-list "arn:aws:storagegateway:`us-east-2`:`123456789012`:fs-association/`fsa-987A654B`"

   ```

   This command outputs a JSON block that contains metadata about the file
   system, such as its location ARN, audit log destination, cache refresh
   attributes, configured IP addresses, and tags.

3. Create a new FSx File Gateway with the same settings and
   configuration as the old gateway. If necessary, refer to the information you saved
   in Step 2.
4. Create new file system associations for the new gateway with the same settings and
   configuration as the file systems that were configured on the old gateway. If
   necessary, refer to the information you saved in Step 2.
5. Confirm that your new gateway is working correctly, then remap/cut-over your
   clients from the old file systems to the new file systems in the manner that best
   suits your environment.
6. Confirm that your new gateway is working correctly, then delete the old gateway
   from the Storage Gateway console.

###### Important

Before you delete an FSx File Gateway, make sure that there are no
applications currently writing to that gateway's cache. If you delete a
gateway while it is in use, data loss can occur.

###### Warning

When a gateway is deleted, there is no way to recover it. 7. Delete the old gateway VM or Amazon EC2 instance.
