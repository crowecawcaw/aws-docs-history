# Managing network type

When you create an FSx for ONTAP file system, you must specify a network type, which
must be one of the following options:

- `IPv4` allows your file system to communicate using only
  Internet Protocol version 4 (IPv4).
- `Dual-stack` allows your file system to communicate using
  both Internet Protocol version 6 (IPv6) and IPv4.
  You can change the network type of an existing FSx for ONTAP file system at any time
  using the Amazon FSx Management Console, AWS CLI, AWS API, or one of the AWS SDKs. For example,
  if your subnets support both IPv4 and IPv6 addressing, you can update your existing file
  system from IPv4-only to dual-stack mode, You can also update your dual-stack file system
  to IPv4-only.

## Using dual-stack mode

You should use dual-stack mode if you need to access and manage your Amazon FSx file systems
natively from IPv6 clients. By configuring your Amazon FSx file system to use dual-stack addressing,
you can access your file data from IPv6 clients, as well as IPv4 clients, in the same Amazon VPC, in
another AWS account's VPC, or in your on-premises network. For example, with an Amazon FSx file system
configured to use dual-stack, you can have existing IPv4 clients and new IPv6 clients accessing
your file data stored on your file system.

By default, Amazon FSx and Amazon VPC use the IPv4 addressing protocol. So as a prerequisite to using IPv6,
you must first assign an Amazon-provided IPv6 Classless Inter-Domain Range (CIDR) block to your VPC
and subnets before you can use IPv6 with your Amazon FSx file systems. For information on enabling IPv6
for your VPC, see [Add IPv6 support for your VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md "../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md") in the
_Amazon Virtual Private Cloud User Guide_.

When creating FSx for ONTAP file systems set to dual-stack mode, you can specify the IPv6 address
range, in addition to the existing IPv4 address range, in which the endpoints to access your file system
will be created. By default, Amazon FSx chooses a block of 1024 IP addresses from one of the VPC's IPv6 CIDR
ranges to use as the endpoint IPv6 address range for the file system.

## Changing network type

You can modify a file system's network type using the Amazon FSx console, the
AWS Command Line Interface (AWS CLI), or the Amazon FSx API.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Navigate to **File systems**, and choose the FSx for ONTAP file system that you
   want to change the network type for.
3. For **Actions**, choose **Update network type**. Or, in the
   **Network & security** panel, choose **Manage** next to the file
   system's **Network type**.

The **Update network type** window appears. 4. For **Desired network type**, choose either **IPv4**
or **Dual-stack**.

    * If you choose `IPv4`, no further configuration is required.
    * If you choose `Dual-stack`, specify the IPv6 address range that your
     file system endpoints will use:




    	+ **Unallocated IPv6 address range from your VPC** – Amazon FSx
    	 chooses an available /118 IP address range from one of the VPC's IPv6 CIDR ranges to
    	 use as the endpoint IPv6 address range for the file system.
    	+ **Enter an IPv6 address range** – You can provide
    	 an IPv6 CIDR range of your own choosing. The IP address range that you choose can
    	 either be inside or outside the VPC’s IP address range, as long as it doesn't
    	 overlap with any subnet.

5. Choose **Update**.

- To modify a file system's network type, use the [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md") CLI command (or the equivalent
  [UpdateFileSystem](../APIReference/API_UpdateFileSystem.md "../APIReference/API_UpdateFileSystem.md") API operation), as shown in the
  following example.

```
`aws fsx update-file-system \
 --file-system-id fs-0123456789abcdef0 \
 --network-type DUAL`
```
