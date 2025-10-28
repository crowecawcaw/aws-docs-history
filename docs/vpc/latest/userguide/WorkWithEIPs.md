# Start using Elastic IP addresses

The following sections describe how you can get started using Elastic IP addresses.

###### Tasks

- [1. Allocate an Elastic IP address](#allocate-eip "#allocate-eip")
- [2. Associate an Elastic IP address](#associate-eip "#associate-eip")
- [3. Disassociate an Elastic IP address](#disassociate-eip "#disassociate-eip")
- [4. Transfer Elastic IP addresses](#transfer-EIPs-intro "#transfer-EIPs-intro")
- [5. Release an Elastic IP address](#release-eip "#release-eip")
- [6. Recover an Elastic IP address](#recover-eip "#recover-eip")
- [Command line overview](#eip-api-cli "#eip-api-cli")

## 1. Allocate an Elastic IP address

Before you use an Elastic IP, you must allocate one for use in your VPC.

###### To allocate an Elastic IP address

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Elastic IPs**.
3. Choose **Allocate Elastic IP
   address**.
4. (Optional) When you allocate an Elastic IP address (EIP), you choose the
   **Network border group** in which to allocate the EIP.
   A network border group is a collection of Availability Zones (AZs), Local
   Zones, or Wavelength Zones from which AWS advertises a public IP address.
   Local Zones and Wavelength Zones may have different network border groups
   than the AZs in a Region to ensure minimum latency or physical distance
   between the AWS network and the customers accessing the resources in these
   Zones.

###### Important

You must allocate an EIP in the same network border group as the AWS resource that will be associated with the EIP. An EIP in one network border group can only be advertised in zones in that network border group and not in any other zones represented by other network border groups.

If you have Local Zones or Wavelength Zones enabled (for more information,
see [Enable a Local Zone](../../../local-zones/latest/ug/getting-started.md#getting-started-find-local-zone "../../../local-zones/latest/ug/getting-started.md#getting-started-find-local-zone") or [Enable Wavelength Zones](../../../wavelength/latest/developerguide/get-started-wavelength.md#enable-zone-group "../../../wavelength/latest/developerguide/get-started-wavelength.md#enable-zone-group")), you can choose a network border group
for AZs, Local Zones, or Wavelength Zones. Choose the network border group
carefully as the EIP and the AWS resource it is associated with must reside
in the same network border group. You can use the EC2 console to view the
network border group that your Availability Zones, Local Zones, or
Wavelength Zones are in (see [Local Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-local-zones "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-local-zones")). Typically, all Availability Zones in a Region
belong to the same network border group, whereas Local Zones or Wavelength
Zones belong to their own separate network border groups.

If you don't have Local Zones or Wavelength Zones enabled, when you allocate an EIP, the network border group that represents all of the AZs for the Region (such as `us-west-2`) is predefined for you and you cannot change it. This means that the EIP that you allocate to this network border group will be advertised in all AZs in the Region you're in. 5. For **Public IPv4 address pool** choose one of the
following:

    * **Amazon's pool of IP addresses**—If you want
     an IPv4 address to be allocated from Amazon's pool of IP
     addresses.
    * **My pool of public IPv4
     addresses**—If you want to allocate an
     IPv4 address from an IP address pool that you have
     brought to your AWS account. This option is disabled
     if you do not have any IP address pools.
    * **Customer owned pool of IPv4
     addresses**—If you want to allocate
     an IPv4 address from a pool created from your
     on-premises network for use with an Outpost. This option
     is only available if you have an Outpost.

6. (Optional) Add or remove a tag.

[Add a tag] Choose **Add new tag** and do the
following:

    * For **Key**, enter the key
     name.
    * For **Value**, enter the key
     value.

[Remove a tag] Choose **Remove** to the right
of the tag’s Key and Value. 7. Choose **Allocate**.

## 2. Associate an Elastic IP address

You can associate an Elastic IP with a running instance or network interface in
your VPC.

After you associate the Elastic IP address with your instance,
the instance receives a public DNS hostname if DNS hostnames are enabled. For more
information, see [DNS attributes for your VPC](vpc-dns.md "vpc-dns.md").

###### To associate an Elastic IP address with an instance or network interface

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Elastic
   IPs**.
3. Select an Elastic IP address that's allocated for use with a
   VPC (the **Scope** column has a value of
   `vpc`), and then choose
   **Actions**, **Associate Elastic IP
   address**.
4. Choose **Instance** or **Network
   interface**, and then select either the instance or
   network interface ID. Select the private IP address with which
   to associate the Elastic IP address. Choose
   **Associate**.

## 3. Disassociate an Elastic IP address

To change the resource that the Elastic IP address is associated with, you must
first disassociate it from the currently associated resource.

###### To disassociate an Elastic IP address

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Elastic
   IPs**.
3. Select the Elastic IP address, and then choose
   **Actions**, **Disassociate Elastic
   IP address**.
4. When prompted, choose
   **Disassociate**.

## 4. Transfer Elastic IP addresses

This section describes how to transfer Elastic IP addresses from one AWS account
to another. Transferring Elastic IP addresses can be helpful in the following
situations:

- Organizational restructuring – Use Elastic IP address
  transfers to quickly move workloads from one AWS account to another. You
  don't have to wait for new Elastic IP addresses to be allowlisted in your
  security groups and NACLs.
- Centralized security administration – Use a centralized AWS security
  account to track and transfer Elastic IP addresses that have been vetted for
  security compliance.
- Disaster recovery – Use Elastic IP address transfers to quickly remap IPs
  for public-facing internet workloads during emergency events.

There is no charge for transferring Elastic IP addresses.

###### Tasks

- [Enable Elastic IP address transfer](#using-instance-addressing-eips-transfer-enable "#using-instance-addressing-eips-transfer-enable")
- [Disable Elastic IP address transfer](#using-instance-addressing-eips-transfer-disable "#using-instance-addressing-eips-transfer-disable")
- [Accept a transferred Elastic IP address](#using-instance-addressing-eips-transfer-accept "#using-instance-addressing-eips-transfer-accept")

### Enable Elastic IP address transfer

This section describes how to accept a transferred Elastic IP address. Note
the following limitations related to enabling Elastic IP addresses for
transfer:

- You can transfer Elastic IP addresses from any AWS account (source
  account) to any other AWS account in the same AWS Region (transfer
  account).
- When you transfer an Elastic IP address, there is a two-step handshake
  between the AWS accounts. When the source account starts the transfer,
  the transfer accounts have seven days to accept the Elastic IP address
  transfer. During those seven days, the source account can view the
  pending transfer (for example in the AWS console or by using the
  [describe-address-transfers](../../../cli/latest/reference/ec2/describe-address-transfers.md "../../../cli/latest/reference/ec2/describe-address-transfers.md") AWS CLI command). After seven days, the
  transfer expires and ownership of the Elastic IP
  address returns to the source
  account.
- Accepted transfers are visible to the source account (for example in
  the AWS console or by using the [describe-address-transfers](../../../cli/latest/reference/ec2/describe-address-transfers.md "../../../cli/latest/reference/ec2/describe-address-transfers.md") AWS CLI command) for 14 days
  after the transfers have been accepted.
- AWS does not notify transfer accounts about pending Elastic IP
  address transfer requests. The owner of the source account must notify
  the owner of the transfer account that there is an Elastic IP address
  transfer request that they must accept.
- Any tags that are associated with an Elastic IP address being
  transferred are reset when the transfer is complete.
- You cannot transfer Elastic IP addresses allocated from public IPv4
  address pools that you bring to your AWS account – commonly
  referred to as Bring Your Own IP (BYOIP) address pools.
- If you attempt to transfer an Elastic IP address that has a reverse
  DNS record associated with it, you can begin the transfer process, but
  the transfer account will not be able to accept the transfer until the
  associated DNS record is removed.
- If you have enabled and configured AWS Outposts, you might have allocated
  Elastic IP addresses from a customer-owned IP address pool
  (CoIP). You cannot transfer Elastic IP addresses allocated from a CoIP.
  However, you can use AWS RAM to share a CoIP with another account.
  For more information, see [Customer-owned IP addresses](../../../outposts/latest/userguide/routing.md#ip-addressing "../../../outposts/latest/userguide/routing.md#ip-addressing") in the _AWS Outposts User Guide_.
- You can use Amazon VPC IPAM to track the transfer of Elastic IP
  addresses to accounts in an organization from AWS Organizations. For more
  information, see [View IP address
  history](../ipam/view-history-cidr-ipam.md "../ipam/view-history-cidr-ipam.md"). If an Elastic IP address is transferred to an AWS account
  outside of the organization, the IPAM audit history of the Elastic IP
  address is lost.

These steps must be completed by the source account.

###### To enable Elastic IP address transfer

1. Ensure that you're using the source AWS account.
2. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
3. In the navigation pane, choose **Elastic IPs**.
4. Select one or more Elastic IP address to enable for transfer and choose **Actions**,
   **Enable transfer**.
5. If you are transferring multiple Elastic IP addresses, you’ll see the **Transfer
   type** option. Choose one of the following options:
   - Choose **Single account** if you are transferring the Elastic IP addresses to
     a single AWS account.
   - Choose **Multiple accounts** if you are transferring the Elastic IP addresses
     to multiple AWS accounts.

6. Under **Transfer account ID**, enter the IDs of the
   AWS accounts that you want to transfer the Elastic IP addresses
   to.
7. Confirm the transfer by entering `enable` in the
   text box.
8. Choose **Submit**.
9. To accept the transfer, see [Accept a transferred Elastic IP address](#using-instance-addressing-eips-transfer-accept "#using-instance-addressing-eips-transfer-accept"). To
   disable the transfer, see [Disable Elastic IP address transfer](#using-instance-addressing-eips-transfer-disable "#using-instance-addressing-eips-transfer-disable").

### Disable Elastic IP address transfer

This section describes how to disable an Elastic IP transfer after the
transfer has been enabled.

These steps must be completed by the source account that enabled the
transfer.

###### To disable an Elastic IP address transfer

1. Ensure that you're using the source AWS account.
2. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
3. In the navigation pane, choose **Elastic IPs**.
4. In the resource list of Elastic IPs, ensure that you have the property enabled that shows the column **Transfer status**.
5. Select one or more Elastic IP address that have a **Transfer
   status** of **Pending**, and choose
   **Actions**, **Disable
   transfer**.
6. Confirm by entering `disable` in the text
   box.
7. Choose **Submit**.

### Accept a transferred Elastic IP address

This section describes how to accept a transferred Elastic IP address.

When you transfer an Elastic IP address, there is a two-step handshake
between the AWS accounts. When the source account starts the transfer,
the transfer accounts have seven days to accept the Elastic IP address
transfer. During those seven days, the source account can view the
pending transfer (for example in the AWS console or by using the
[describe-address-transfers](../../../cli/latest/reference/ec2/describe-address-transfers.md "../../../cli/latest/reference/ec2/describe-address-transfers.md") AWS CLI command). After seven days, the
transfer expires and ownership of the Elastic IP
address returns to the source
account.

When accepting transfers, note the following exceptions that might occur and
how to resolve them:

- **AddressLimitExceeded**: If your
  transfer account has exceeded the Elastic IP address quota, the source
  account can enable Elastic IP address transfer, but this exception
  occurs when the transfer account tries to accept the transfer. By
  default, all AWS accounts are limited to 5 Elastic IP addresses per
  Region. See [Elastic IP address limit](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-limit "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-limit") in the
  _Amazon EC2 User Guide_ for instructions on increasing
  the limit.
- **InvalidTransfer.AddressCustomPtrSet**:
  If you or someone in your organization has configured the Elastic IP
  address that you are attempting to transfer to use reverse DNS lookup,
  the source account can enable transfer for the Elastic IP address, but
  this exception occurs when the transfer account tries to accept the
  transfer. To resolve this issue, the source account must remove the DNS
  record for the Elastic IP address. For more information, see [Remove a reverse DNS record](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#Using_Elastic_Addressing_Reverse_DNS "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#Using_Elastic_Addressing_Reverse_DNS") in the
  _Amazon EC2 User Guide_.
- **InvalidTransfer.AddressAssociated**: If
  an Elastic IP address is associated with an ENI or EC2 instance, the
  source account can enable transfer for the Elastic IP address, but this
  exception occurs when the transfer account tries to accept the transfer.
  To resolve this issue, the source account must disassociate the Elastic
  IP address. For more information, see [Disassociate an Elastic IP address](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-eips-associating-different "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md#using-instance-addressing-eips-associating-different") in the
  _Amazon EC2 User Guide_.

For any other exceptions, [contact
Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

These steps must be completed by the transfer account.

###### To accept an Elastic IP address transfer

1. Ensure that you're using the transfer account.
2. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
3. In the navigation pane, choose **Elastic IPs**.
4. Choose **Actions**,
   **Accept transfer**.
5. No tags that are associated with the Elastic IP address being
   transferred are transferred with the Elastic IP address when you accept
   the transfer. If you want to define a **Name** tag for
   the Elastic IP address that you are accepting, select **Create a
   tag with a key of 'Name' and a value that you
   specify**.
6. Enter the Elastic IP address that you want to transfer.
7. If you are accepting multiple transferred Elastic IP addresses, choose
   **Add address** to enter an additional Elastic IP
   address.
8. Choose **Submit**.

## 5. Release an Elastic IP address

If you no longer need an Elastic IP address, we recommend that you release it. You
incur charges for any Elastic IP address that's allocated for use with a VPC even if
it's not associated with an instance. The Elastic IP address must not be associated
with an instance or network interface.

###### To release an Elastic IP address

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Elastic
   IPs**.
3. Select the Elastic IP address, and then choose
   **Actions**, **Release Elastic IP
   addresses**.
4. When prompted, choose **Release**.

## 6. Recover an Elastic IP address

If you release an Elastic IP address but change your mind, you might be able to
recover it. You cannot recover the Elastic IP address if it has been allocated to
another AWS account, or if recovering it results in you exceeding your Elastic IP
address quota.

You can recover an Elastic IP address by using the Amazon EC2 API or a command line
tool.

###### To recover an Elastic IP address using the AWS CLI

Use the [allocate-address](../../../cli/latest/reference/ec2/allocate-address.md "../../../cli/latest/reference/ec2/allocate-address.md") command
and specify the IP address using the `--address` parameter.

```
aws ec2 allocate-address --domain vpc --address `203.0.113.3`
```

## Command line overview

You can perform the tasks described in this section using the command line or an
API. For more information about the command line interfaces and a list of available
API actions, see [Working with Amazon VPC](what-is-amazon-vpc.md#VPCInterfaces "what-is-amazon-vpc.md#VPCInterfaces").

###### Accept Elastic IP address transfer

- [accept-address-transfer](../../../cli/latest/reference/ec2/accept-address-transfer.md "../../../cli/latest/reference/ec2/accept-address-transfer.md") (AWS CLI)
- [Approve-EC2AddressTransfer](../../../powershell/latest/reference/items/Approve-EC2AddressTransfer.md "../../../powershell/latest/reference/items/Approve-EC2AddressTransfer.md")
  (AWS Tools for Windows PowerShell)

###### Allocate an Elastic IP address

- [allocate-address](../../../cli/latest/reference/ec2/allocate-address.md "../../../cli/latest/reference/ec2/allocate-address.md")
  (AWS CLI)
- [New-EC2Address](../../../powershell/latest/reference/items/New-EC2Address.md "../../../powershell/latest/reference/items/New-EC2Address.md")
  (AWS Tools for Windows PowerShell)

###### Associate an Elastic IP address with an instance or network interface

- [associate-address](../../../cli/latest/reference/ec2/associate-address.md "../../../cli/latest/reference/ec2/associate-address.md") (AWS CLI)
- [Register-EC2Address](../../../powershell/latest/reference/items/Register-EC2Address.md "../../../powershell/latest/reference/items/Register-EC2Address.md") (AWS Tools for Windows PowerShell)

###### Describe Elastic IP address transfers

- [describe-address-transfers](../../../cli/latest/reference/ec2/describe-address-transfers.md "../../../cli/latest/reference/ec2/describe-address-transfers.md") (AWS CLI)
- [Get-EC2AddressTransfer](../../../powershell/latest/reference/items/Get-EC2AddressTransfer.md "../../../powershell/latest/reference/items/Get-EC2AddressTransfer.md") (AWS Tools for Windows PowerShell)

###### Disable Elastic IP address transfer

- [disable-address-transfer](../../../cli/latest/reference/ec2/disable-address-transfer.md "../../../cli/latest/reference/ec2/disable-address-transfer.md") (AWS CLI)
- [Disable-EC2AddressTransfer](../../../powershell/latest/reference/items/Disable-EC2AddressTransfer.md "../../../powershell/latest/reference/items/Disable-EC2AddressTransfer.md") (AWS Tools for Windows PowerShell)

###### Disassociate an Elastic IP address

- [disassociate-address](../../../cli/latest/reference/ec2/disassociate-address.md "../../../cli/latest/reference/ec2/disassociate-address.md") (AWS CLI)
- [Unregister-EC2Address](../../../powershell/latest/reference/items/Unregister-EC2Address.md "../../../powershell/latest/reference/items/Unregister-EC2Address.md") (AWS Tools for Windows PowerShell)

###### Enable Elastic IP address transfer

- [enable-address-transfer](../../../cli/latest/reference/ec2/enable-address-transfer.md "../../../cli/latest/reference/ec2/enable-address-transfer.md") (AWS CLI)
- [Enable-EC2AddressTransfer](../../../powershell/latest/reference/items/Enable-EC2AddressTransfer.md "../../../powershell/latest/reference/items/Enable-EC2AddressTransfer.md") (AWS Tools for Windows PowerShell)

###### Release an Elastic IP address

- [release-address](../../../cli/latest/reference/ec2/release-address.md "../../../cli/latest/reference/ec2/release-address.md") (AWS CLI)
- [Remove-EC2Address](../../../powershell/latest/reference/items/Remove-EC2Address.md "../../../powershell/latest/reference/items/Remove-EC2Address.md") (AWS Tools for Windows PowerShell)

###### Tag an Elastic IP address

- [create-tags](../../../cli/latest/reference/ec2/create-tags.md "../../../cli/latest/reference/ec2/create-tags.md") (AWS CLI)
- [New-EC2Tag](../../../powershell/latest/reference/items/New-EC2Tag.md "../../../powershell/latest/reference/items/New-EC2Tag.md") (AWS Tools for Windows PowerShell)

###### View your Elastic IP addresses

- [describe-addresses](../../../cli/latest/reference/ec2/describe-addresses.md "../../../cli/latest/reference/ec2/describe-addresses.md") (AWS CLI)
- [Get-EC2Address](../../../powershell/latest/reference/items/Get-EC2Address.md "../../../powershell/latest/reference/items/Get-EC2Address.md") (AWS Tools for Windows PowerShell)
